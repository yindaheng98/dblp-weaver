<script setup lang="ts">
import * as echarts from 'echarts/core'
import {
  TooltipComponent,
  type TooltipComponentOption,
  GridComponent,
  type GridComponentOption,
  LegendComponent,
  type LegendComponentOption
} from 'echarts/components'
import { BarChart, type BarSeriesOption } from 'echarts/charts'
import { CanvasRenderer } from 'echarts/renderers'
import VChart from 'vue-echarts'

echarts.use([TooltipComponent, GridComponent, LegendComponent, BarChart, CanvasRenderer])

type EChartsOption = echarts.ComposeOption<
  TooltipComponentOption | GridComponentOption | LegendComponentOption | BarSeriesOption
>

var option: EChartsOption

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

option = {
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
  series: [
    {
      name: 'CCF A',
      type: 'bar',
      barGap: 0,
      label: labelOption,
      emphasis: {
        focus: 'series'
      },
      data: [320, 332, 301, 334, 390]
    },
    {
      name: 'CCF B',
      type: 'bar',
      label: labelOption,
      emphasis: {
        focus: 'series'
      },
      data: [220, 182, 191, 234, 290]
    },
    {
      name: 'CCF C',
      type: 'bar',
      label: labelOption,
      emphasis: {
        focus: 'series'
      },
      data: [150, 232, 201, 154, 190]
    },
    {
      name: 'No CCF',
      type: 'bar',
      label: labelOption,
      emphasis: {
        focus: 'series'
      },
      data: [98, 77, 101, 99, 40]
    }
  ]
}
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
