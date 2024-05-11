<script setup lang="ts">
import { use } from 'echarts/core'
import { CanvasRenderer } from 'echarts/renderers'
import { PieChart } from 'echarts/charts'
import { TitleComponent, TooltipComponent, LegendComponent } from 'echarts/components'
import VChart, { THEME_KEY } from 'vue-echarts'
import { ref, provide, computed } from 'vue'
import { type Record } from 'neo4j-driver'

const props = defineProps<{ papers: Record[] }>()
const data = computed(() => {
  const d = [
    { value: 0, name: 'CCF A' },
    { value: 0, name: 'CCF B' },
    { value: 0, name: 'CCF C' },
    { value: 0, name: 'Others' }
  ]
  for (let paper of props.papers) {
    const j = paper.get('j')
    if (!j || !j.properties || !j.properties.ccf) d[3].value++
    else {
      switch (j.properties.ccf) {
        case 'A':
          d[0].value++
          break
        case 'B':
          d[1].value++
          break
        case 'C':
          d[2].value++
          break
        default:
          d[3].value++
      }
    }
  }
  return d
})

use([CanvasRenderer, PieChart, TitleComponent, TooltipComponent, LegendComponent])

provide(THEME_KEY, 'dark')

const option = ref({
  tooltip: {
    trigger: 'item',
    formatter: '{b} : {c} ({d}%)'
  },
  series: [
    {
      name: 'Traffic Sources',
      type: 'pie',
      radius: '55%',
      center: ['50%', '60%'],
      data: data,
      emphasis: {
        itemStyle: {
          shadowBlur: 10,
          shadowOffsetX: 0,
          shadowColor: 'rgba(0, 0, 0, 0.5)'
        }
      }
    }
  ]
})
</script>

<template>
  <v-chart class="chart" :option="option" />
</template>

<style scoped>
.chart {
  height: 400px;
}
</style>
