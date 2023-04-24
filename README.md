# CDS.ai Full-Stack Developer Exercise

## About this repository
This repository includes a barebones full-stack web application built with the following technologies:

* Backend
    * Python
    * [FastAPI](https://fastapi.tiangolo.com/)
    * [Pandas](https://pandas.pydata.org/)
* Frontend
    * Javascript
    * [Vue.js](https://vuejs.org/)
    * chart lib?

This application mimics a standard data visualization application at CDS.ai - a Python-based backend reads data, manipulates it, and returns it. A Javascript-based frontend retrieves this data from the backend and visualizes it.

In this exercise, you will clone this repository and make changes from the list of tasks below. 
***
## Developer Setup
This repository includes containerization using Docker. CDS.ai frequently uses Docker to containerize our applications so that they are more portable and infrastructure-agnostic. Using Docker to set up this application locally is fully optional, and may ease your speed of development as you don't have to install and debug environments for both Python and Javascript. If you would like to set up the Python and Javascript applications natively, see the "native" section below.

### Docker
Install [Docker Desktop](https://www.docker.com/products/docker-desktop/).

From the root directory of this repository, run `docker-compose up`. This will build the Docker images for the frontend and backend and run both containers.

### Native
Alternatively, you can set up both the frontend and backend natively.

#### Backend (Python)
Install [Python 3.9 or later](https://www.python.org/downloads/). From the `backend` directory of this repository, use a Python dependency management strategy of your choosing and install the required packages with `pip install -r requirements.txt`. Then run `uvicorn main:app --reload` to run the development server.

#### Frontend (Javascript)
Install [Node.js 18 or later](https://nodejs.org/en/download). From the `frontend` directory of this repository, run `npm install` to install dependencies, and `npm run dev` to run the development server.

### Usage
Once installed and running, the backend will be available at `http://localhost:8000` and the frontend will be available at `http://localhost:5173`.

## Tasks
What follows is a list of tasks you can perform in this repository. These are roughly separated into four buckets: frontend, backend, orchestration, and engineering. Please spend no more than 4 hours total on this exercise, and be prepared to talk about your process in your upcoming interview.

### Frontend
* placeholder task
### Backend
* placeholder task
### Orchestration
* placeholder task
### Engineering
* placeholder task