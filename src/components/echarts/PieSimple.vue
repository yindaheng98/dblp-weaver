<script setup lang="ts">
import { use } from 'echarts/core'
import { CanvasRenderer } from 'echarts/renderers'
import { PieChart } from 'echarts/charts'
import { TitleComponent, TooltipComponent, LegendComponent } from 'echarts/components'
import VChart, { THEME_KEY } from 'vue-echarts'
import { computed, provide } from 'vue'

const props = defineProps<{ data: { value: number; name: string }[]; name: string }>()

use([CanvasRenderer, PieChart, TitleComponent, TooltipComponent, LegendComponent])

provide(THEME_KEY, 'dark')

const option = computed(() => {
  return {
    tooltip: {
      trigger: 'item',
      formatter: '{b} : {c} ({d}%)'
    },
    series: [
      {
        name: props.name,
        type: 'pie',
        radius: '50%',
        center: ['50%', '50%'],
        data: props.data,
        emphasis: {
          itemStyle: {
            shadowBlur: 10,
            shadowOffsetX: 0,
            shadowColor: 'rgba(0, 0, 0, 0.5)'
          }
        }
      }
    ]
  }
})
</script>

<template>
  <v-chart class="chart" :option="option" />
</template>

<style scoped>
.chart {
  height: 100%;
  width: 50%;
  display: flex;
}
</style>
