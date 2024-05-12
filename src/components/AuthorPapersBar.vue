<script setup lang="ts">
import { computed } from 'vue'
import { type Record } from 'neo4j-driver'
import BarLabelRotation from './echarts/BarLabelRotation.vue'

const props = defineProps<{ papers: Record[] }>()
const year_data = [
  {
    name: 'CCF A',
    data: [320, 332, 301, 334, 390]
  },
  {
    name: 'CCF B',
    data: [220, 182, 191, 234, 290]
  },
  {
    name: 'CCF C',
    data: [150, 232, 201, 154, 190]
  },
  {
    name: 'No CCF',
    data: [98, 77, 101, 99, 40]
  }
]
</script>

<template>
  <div class="wrapper">
    <BarLabelRotation :data="year_data" />
  </div>
</template>

<style scoped>
.wrapper {
  height: 300px;
  width: 100%;
  display: flex;
}
</style>
