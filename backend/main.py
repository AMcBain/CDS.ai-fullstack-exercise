from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder
from sqlalchemy import text
from sqlalchemy.orm import Session
from data.db import get_db
import pandas as pd
import os


# FastAPI application from example on their website
# https://fastapi.tiangolo.com/#example
app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/census")
def read_item(sex = None, db: Session = Depends(get_db)):
    query = "select * from census"

    if sex:
        query += " where sex = :sex_filter"

    result = db.execute(text(query), {'sex_filter': sex}).mappings().all()

    # return to frontend
    return jsonable_encoder(result)

@app.get("/summary-stats")
def get_summary_stats(sex = None, db: Session = Depends(get_db)):
    sex_filter = "1 = 1"

    if sex:
        sex_filter = " sex = :sex_filter"

    total = db.execute(
        text(f"select count(id) from census where {sex_filter}"),
        {"sex_filter": sex}
    ).scalar()
    ages = db.execute(
        text(f"select age from census where {sex_filter}"),
        {"sex_filter": sex}
    ).scalars().all()

    age_f = pd.DataFrame({"age": ages})
    q_25 = age_f["age"].quantile(.25)
    q_50 = age_f["age"].quantile(.50)
    q_75 = age_f["age"].quantile(.75)
    inter_range = q_75 - q_25
    outlier_low = q_25 - 1.5 * inter_range
    outlier_high = q_75 + 1.5 * inter_range

    output = {
        "age": {
           "25%": q_25,
           "50%": q_50,
           "75%": q_75,
           "count": total,
            "max": age_f.max()["age"].item(),
            "mean": age_f.mean()["age"].item(),
            "min": age_f.min()["age"].item(),
            "std": age_f.std()["age"].item(),
            "outliers": list(filter(lambda age: age < outlier_low or age > outlier_high, age_f["age"].unique().tolist())),
        }
    }

    # Pandas docs are inscruitable. SQL I can do.
    # I suppose it might be faster to fetch it all at once and do Pandas stuff but that'd require it be less inscruitable, so...
    for key in ["education_level", "race", "sex"]:
        # Yeah yeah absolutely not best practice, but I can't bind column names the way I can parameters.
        stats = db.execute(
            text(f"select {key}, (count(over_50k) * 1.0 / (select count(id) from census as c2 where {key} = c1.{key})) as over_50k from census as c1 where over_50k = 1 and {sex_filter} group by {key}"),
            {"sex_filter": sex}
        ).all()
        output[key] = [{ key: row[0], "over_50k": row[1] } for row in stats]

    return output
