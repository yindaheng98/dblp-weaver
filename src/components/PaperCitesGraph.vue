<script setup lang="ts">
import { computed } from 'vue'
import PapersGraph from './neovis/PapersGraph.vue'
import { type IdType } from 'vis-network'
import { stateAuthorPapersStat, statePaperList } from './state'

const props = defineProps<{ id: IdType, limit: number }>()

const cyphers = computed(() => {
  return [`
  MATCH (p:Publication) WHERE id(p) = ${props.id} RETURN p
  `, `
  MATCH (pc:Publication)-[c:CITE]->(p:Publication) WHERE id(p) = ${props.id}
  OPTIONAL MATCH (cc:Publication)-[:CITE]->(pc)
  WITH COUNT(cc) AS pcc, p, c, pc ORDER BY pcc LIMIT ${props.limit}
  RETURN p, c, pc
  `, `
  MATCH (pr:Publication)<-[r:CITE]-(p:Publication) WHERE id(p) = ${props.id}
  OPTIONAL MATCH (cc:Publication)-[:CITE]->(pr)
  WITH COUNT(cc) AS prc, p, r, pr ORDER BY prc LIMIT ${props.limit}
  RETURN p, r, pr
  `]
})
</script>

<template>
  <PapersGraph :cyphers="cyphers" @selectPaper="console.log" />
</template>
