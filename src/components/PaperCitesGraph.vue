<script setup lang="ts">
import { computed } from 'vue'
import PapersGraph from './neovis/PapersGraph.vue'
import { type IdType } from 'vis-network'
import { stateAuthorPapersStat, statePaperList } from './state'

const props = defineProps<{ id: IdType }>()

const cypher = computed(() => {
  return `
  MATCH (p1:Publication) WHERE id(p1) = ${props.id}
  MATCH (p2:Publication)-[r1:CITE]->(p1)
  MATCH (p3:Publication)<-[r2:CITE]-(p1)
  RETURN p1,r1,p2,r2,p3`
})
</script>

<template>
  <PapersGraph :cypher="cypher" @selectPaper="console.log" />
</template>
