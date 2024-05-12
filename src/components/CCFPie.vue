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
  const ccf_gather: { [id: string]: any[] } = { A: [], B: [], C: [], N: [] }
  for (let paper of props.papers) {
    const j = paper.get('j')
    if (!j || !j.properties || !j.properties.ccf) ccf_gather.N.push(j)
    else {
      switch (j.properties.ccf) {
        case 'A':
          ccf_gather.A.push(j)
          break
        case 'B':
          ccf_gather.B.push(j)
          break
        case 'C':
          ccf_gather.C.push(j)
          break
        default:
          ccf_gather.N.push(j)
      }
    }
  }
  const ccf = [
    { value: ccf_gather.A.length, name: 'CCF A' },
    { value: ccf_gather.B.length, name: 'CCF B' },
    { value: ccf_gather.C.length, name: 'CCF C' },
    { value: ccf_gather.N.length, name: 'Others' }
  ]
  return { ccf: ccf }
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
      data: data.value.ccf,
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
