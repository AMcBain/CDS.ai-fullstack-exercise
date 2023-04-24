<!-- using  script setup (composition api) -->
<!-- https://vuejs.org/api/sfc-script-setup.html -->
<script setup>
import { onMounted, ref } from 'vue'
import filterPanel from "@/components/filterPanel.vue"

// creating a reactive variable
// https://vuejs.org/api/reactivity-core.html#ref
let censusData = ref([])

// using the mounted lifecycle hook to fetch our data
// https://vuejs.org/api/composition-api-lifecycle.html
onMounted(async () => {
  censusData.value = await fetch('http://localhost:8000/census').then(census => census.json())
})
</script>

<template>
  <div class="container">
    <div v-if="censusData.length">
      <filterPanel />
      {{ censusData }}
    </div>
    <div v-else class="spinner-border" role="status">
      <span class="visually-hidden">Loading...</span>
    </div>
    
  </div>
</template>