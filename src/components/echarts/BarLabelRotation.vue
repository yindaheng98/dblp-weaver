<script setup lang="ts">
import * as echarts from 'echarts/core'
import { TooltipComponent, GridComponent, LegendComponent } from 'echarts/components'
import { BarChart, type BarSeriesOption } from 'echarts/charts'
import { CanvasRenderer } from 'echarts/renderers'
import { computed } from 'vue'
import VChart from 'vue-echarts'

const props = defineProps<{ data: { data: number[]; name: string }[] }>()

echarts.use([TooltipComponent, GridComponent, LegendComponent, BarChart, CanvasRenderer])

const labelOption: NonNullable<BarSeriesOption['label']> = {
  show: true,
  position: 'insideBottom',
  distance: 15,
  align: 'left',
  verticalAlign: 'middle',
  rotate: 90,
  formatter: '{c}  {name|{a}}',
  fontSize: 16,
  rich: {
    name: {}
  }
}

const option = computed(() => {
  return {
    tooltip: {
      trigger: 'axis',
      axisPointer: {
        type: 'shadow'
      }
    },
    xAxis: [
      {
        type: 'category',
        axisTick: { show: false },
        data: ['2012', '2013', '2014', '2015', '2016']
      }
    ],
    yAxis: [
      {
        type: 'value'
      }
    ],
    series: props.data.map((item) => {
      return {
        name: item.name,
        type: 'bar',
        barGap: 0,
        label: labelOption,
        emphasis: {
          focus: 'series'
        },
        data: item.data
      }
    })
  }
})
</script>

<template>
  <v-chart class="chart" :option="option" />
</template>

<style scoped>
.chart {
  height: 300px;
  width: 100%;
  display: flex;
}
</style>
