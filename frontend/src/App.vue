<!-- using  script setup (composition api) -->
<!-- https://vuejs.org/api/sfc-script-setup.html -->
<script setup>
import { onMounted, ref } from 'vue'
import barChart from '@/components/barChart.vue'
import boxPlot from '@/components/boxPlot.vue'
import percentBarChart from './components/percentBarChart.vue'

// creating a reactive variable
// https://vuejs.org/api/reactivity-core.html#ref
let censusData = ref([])
let summStats = ref({})
let loading = ref(false)

const order = [
  'Did not complete high school',
  'High school',
  'Some college',
  'Associates',
  'Bachelors',
  'Masters',
  'Doctorate',
  'Professional school',
]

const colors = [
  'rgba(228,26,28,1)',
  'rgba(55,126,184,1)',
  'rgba(77,175,74,1)',
  'rgba(152,78,163,1)',
  'rgba(255,127,0,1)',
  'rgba(255,255,51,1)',
  'rgba(166,86,40,1)',
  'rgba(247,129,191,1)'
]

async function fetchData(sex) {
  let query = ''

  if (sex) {
    query = '?sex=' + sex
  }

  loading.value = true
  censusData.value = await fetch(`http://localhost:8000/census${query}`).then((census) => census.json())
  summStats.value = await fetch(`http://localhost:8000/summary-stats${query}`).then((summ) =>
    summ.json()
  )
  loading.value = false
}

// using the mounted lifecycle hook to fetch our data
// https://vuejs.org/api/composition-api-lifecycle.html
onMounted(fetchData)
</script>

<template>
  <!-- As a heading -->
  <div>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
      <div class="container-md">
        <a class="navbar-brand" href="#">CDS.ai Full Stack Exercise</a>
      </div>
    </nav>
    <div class="container">
      <p class="lead text-center">
        <small>Census data text</small>
      </p>
      <div v-if="censusData.length">
        <div class="row">
          <div class="col-3 mb-2">
            <label for="sex_filter" class="d-block mb-1">Filter by Sex</label>
            <select id="sex" @change="fetchData($event.target.value)">
              <option value="" selected></option>
              <option>Male</option>
              <option>Female</option>
            </select>
          </div>
          <div class="col-3">
            <div v-if="loading" class="spinner-border" role="status">
              <span class="visually-hidden">Loading...</span>
            </div>
          </div>
        </div>
        <div class="row">
          <div class="col-6">
            <barChart :censusData="censusData" :category="'education_level'" :order="order" :colors="colors" />
          </div>
          <div class="col-6">
            <barChart :censusData="censusData" :category="'race'" :colors="colors" />
          </div>
        </div>
      </div>
      <div v-else class="spinner-border" role="status">
        <span class="visually-hidden">Loading...</span>
      </div>
      <div v-if="summStats.age">
        <p class="lead text-center">
          <small>Summary Statistics</small>
        </p>
        <div class="row">
          <div class="col-6">
            <boxPlot :summStats="summStats.age" />
          </div>
          <div class="col-6">
            <percentBarChart :summStats="summStats" :category="'sex'" :colors="colors" />
          </div>
        </div>
        <div class="row">
          <div class="col-6">
            <percentBarChart :summStats="summStats" :category="'education_level'" :order="order" :colors="colors" />
          </div>
          <div class="col-6">
            <percentBarChart :summStats="summStats" :category="'race'" :colors="colors" />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<style scoped>
.navbar {
  margin-bottom: 1rem;
}
</style>
