<script setup lang="ts">
import { use } from 'echarts/core'
import { CanvasRenderer } from 'echarts/renderers'
import { PieChart } from 'echarts/charts'
import { TitleComponent, TooltipComponent, LegendComponent } from 'echarts/components'
import VChart, { THEME_KEY } from 'vue-echarts'
import { ref, provide, computed } from 'vue'
import { type Record } from 'neo4j-driver'

const props = defineProps<{ papers: Record[] }>()
const gather = computed(() => {
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
  return ccf_gather
})
const ccf_data = computed(() => {
  const ccf_gather = gather.value
  return [
    { value: ccf_gather.A.length, name: 'CCF A' },
    { value: ccf_gather.B.length, name: 'CCF B' },
    { value: ccf_gather.C.length, name: 'CCF C' },
    { value: ccf_gather.N.length, name: 'Others' }
  ]
})
const journal_data = computed(() => {
  const ccf_gather = gather.value
  function count(gather: any[]) {
    const dict: { [id: string]: number } = {}
    gather.map((j) => {
      if (!j || !j.properties || !j.properties.dblp_name) dict['Others']++
      else {
        if (j.properties.dblp_name in dict) {
          dict[j.properties.dblp_name]++
        } else {
          dict[j.properties.dblp_name] = 1
        }
      }
    })
    let d: { value: number; name: string }[] = []
    for (let k in dict) d.push({ value: dict[k], name: k })
    return d.sort((a, b) => a.value - b.value)
  }
  return count(ccf_gather.A)
    .concat(count(ccf_gather.B))
    .concat(count(ccf_gather.C))
    .concat(count(ccf_gather.N))
})

use([CanvasRenderer, PieChart, TitleComponent, TooltipComponent, LegendComponent])

provide(THEME_KEY, 'dark')

const ccf_option = ref({
  tooltip: {
    trigger: 'item',
    formatter: '{b} : {c} ({d}%)'
  },
  series: [
    {
      name: 'Traffic Sources',
      type: 'pie',
      radius: '50%',
      center: ['50%', '50%'],
      data: ccf_data,
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

const journal_option = ref({
  tooltip: {
    trigger: 'item',
    formatter: '{b} : {c} ({d}%)'
  },
  series: [
    {
      name: 'Traffic Sources',
      type: 'pie',
      radius: '50%',
      center: ['50%', '50%'],
      data: journal_data,
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
  <div class="wrapper">
    <v-chart class="chart" :option="ccf_option" />
    <v-chart class="chart" :option="journal_option" />
  </div>
</template>

<style scoped>
.wrapper {
  height: 300px;
  width: 100%;
  display: flex;
}
.chart {
  height: 100%;
  width: 50%;
  display: flex;
}
</style>
