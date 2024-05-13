<script setup lang="ts">
import { computed } from 'vue'
import { type ECElementEvent } from 'echarts/core'
import { type Record } from 'neo4j-driver'
import BarLabelRotation from './echarts/BarLabelRotation.vue'
import { statePaperList } from './state'

const props = defineProps<{ papers: Record[], maxyear: number, minyear: number }>()

const year_data = computed(() => {
  const year_gather = [
    {
      name: 'CCF A',
      data: Array.from({ length: (props.maxyear - props.minyear) }, () => 0)
    },
    {
      name: 'CCF B',
      data: Array.from({ length: (props.maxyear - props.minyear) }, () => 0)
    },
    {
      name: 'CCF C',
      data: Array.from({ length: (props.maxyear - props.minyear) }, () => 0)
    },
    {
      name: 'No CCF',
      data: Array.from({ length: (props.maxyear - props.minyear) }, () => 0)
    }
  ]
  for (let paper of props.papers) {
    const j = paper.get('j')
    const p = paper.get('p')
    if (!p || !p.properties || !p.properties.year || p.properties.year - props.minyear - 1 < 0) continue
    const year = p.properties.year
    if (!j || !j.properties || !j.properties.ccf) year_gather[3].data[year - props.minyear - 1] += 1
    else {
      switch (j.properties.ccf) {
        case 'A':
          year_gather[0].data[year - props.minyear - 1] += 1
          break
        case 'B':
          year_gather[1].data[year - props.minyear - 1] += 1
          break
        case 'C':
          year_gather[2].data[year - props.minyear - 1] += 1
          break
        default:
          year_gather[3].data[year - props.minyear - 1] += 1
      }
    }
  }
  return year_gather
})
function year_click(e: ECElementEvent) {
  console.log(e.dataIndex + props.minyear + 1)
  console.log(["A", "B", "C", "N"][e.componentIndex])
  statePaperList.show(undefined, e.dataIndex + props.minyear + 1, undefined, ["A", "B", "C", "N"][e.componentIndex])
}
</script>

<template>
  <div class="wrapper">
    <BarLabelRotation :data="year_data"
      :xAxis="Array.from({ length: (props.maxyear - props.minyear) }, (v, k) => k + props.minyear + 1)"
      @click="year_click" />
  </div>
</template>

<style scoped>
.wrapper {
  height: 300px;
  width: 100%;
  display: flex;
}
</style>
