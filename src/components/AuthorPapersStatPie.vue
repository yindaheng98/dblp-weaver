<script setup lang="ts">
import { computed } from 'vue'
import { type ECElementEvent } from 'echarts/core'
import { type Record } from 'neo4j-driver'
import PieSimple from './echarts/PieSimple.vue'
import { statePaperList } from './state'

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
    { value: ccf_gather.N.length, name: 'No CCF' }
  ]
})
function ccf_click(e: ECElementEvent) {
  statePaperList.show(undefined, undefined, undefined, ["A", "B", "C", "N"][e.dataIndex])
}
const journal_data = computed(() => {
  const ccf_gather = gather.value
  function count(gather: any[]) {
    const dict: { [id: string]: number } = {}
    gather.map((j) => {
      if (!j || !j.properties || !j.properties.dblp_name) {
        if (dict['Null']) dict['Null']++
        else dict['Null'] = 1
      } else {
        if (j.properties.dblp_name in dict) {
          dict[j.properties.dblp_name]++
        } else {
          dict[j.properties.dblp_name] = 1
        }
      }
    })
    let d: { value: number; name: string }[] = []
    for (let k in dict) d.push({ value: dict[k], name: k })
    return d.sort((a, b) => b.value - a.value)
  }
  return count(ccf_gather.A)
    .concat(count(ccf_gather.B))
    .concat(count(ccf_gather.C))
    .concat(count(ccf_gather.N))
})
function journal_click(e: ECElementEvent) {
  statePaperList.show(undefined, undefined, journal_data.value[e.dataIndex].name)
}
</script>

<template>
  <div class="wrapper">
    <PieSimple :data="ccf_data" name="CCF Count" @click="ccf_click" />
    <PieSimple :data="journal_data" name="Journal count" @click="journal_click" />
  </div>
</template>

<style scoped>
.wrapper {
  height: 300px;
  width: 100%;
  display: flex;
}
</style>
