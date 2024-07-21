<script setup>
import { ref, onMounted, onBeforeUpdate } from 'vue'
import { Chart } from 'chart.js/auto'
import { useI18n } from 'vue-i18n'

const { t } = useI18n({
  useScope: 'global'
})

// defining a prop on the component
// this allows us to get the censusData object transmitted down
// from our parent, App.vue
// https://vuejs.org/guide/components/props.html
const props = defineProps({
  censusData: {
    required: true,
    type: Array
  },
  category: {
    required: true,
    type: String
  },
  order: {
    type: Array,
  },
  colors: {
    type: Array
  }
})

// using a template ref instead of the DOM element
// https://vuejs.org/guide/essentials/template-refs.html
const chartCanvas = ref(null)
let chart = null

function update() {
  // get the categories from the data
  const categories = props.censusData.reduce((acc, datum) => {
    if (!acc.includes(datum[props.category])) {
      acc.push(datum[props.category])
    }
    return acc
  }, [])

  if (props.order) {
    categories.sort((a, b) => props.order.indexOf(a) - props.order.indexOf(b))
  }

  // generate a dataset for the categories
  // using a chartjs bar chart
  // dataset definition here
  // https://www.chartjs.org/docs/latest/charts/bar.html
  const dataset = {
    label: t(props.category),
    backgroundColor: props.colors.map(color => color.replace(',1)', ',.65')),
    borderColor: props.colors,
    data: categories.map((category) => {
      return props.censusData.filter((datum) => datum[props.category] === category).length
    })
  }

  if (chart) {
    chart.data.labels = categories
    chart.data.datasets = [dataset]
    chart.update()
  } else {
    // draw bar chart
    // https://www.chartjs.org/docs/latest/charts/bar.html
    chart = new Chart(chartCanvas.value, {
      type: 'bar',
      data: {
        labels: categories,
        datasets: [dataset]
      },
      options: {
        indexAxis: 'y'
      }
    })
  }
}

// using the onMounted lifecycle hook
// this way we don't try and build the chart until the DOM has rendered
// https://vuejs.org/guide/essentials/lifecycle.html#lifecycle-diagram
onMounted(update)
onBeforeUpdate(update)
</script>
<template>
  <div>
    <h5 class="display-7 text-center">Census Data By {{ $t(props.category) }}</h5>
    <canvas id="barChartHolder" ref="chartCanvas"></canvas>
  </div>
</template>
