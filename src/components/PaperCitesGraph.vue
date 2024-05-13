<script setup lang="ts">
import { computed } from 'vue'
import PapersGraph from './neovis/PapersGraph.vue'
import { type IdType } from 'vis-network'
import { stateAuthorPapersStat, statePaperList } from './state'

const props = defineProps<{ id: IdType }>()

const cypher = computed(() => {
  return `
  MATCH (p:Publication) WHERE id(p) = ${props.id}
  OPTIONAL MATCH cit=(pc:Publication)-[:CITE]->(p)
  OPTIONAL MATCH ref=(pr:Publication)<-[:CITE]-(p)
  OPTIONAL MATCH cr=(pc)-[:CITE]->(pr)
  OPTIONAL MATCH rc=(pr)-[:CITE]->(pc)
  RETURN p, cit, ref, cr, rc`
})
</script>

<template>
  <PapersGraph :cypher="cypher" @selectPaper="console.log" />
</template>
