<script setup lang="ts">
import { computed } from 'vue'
import PapersGraph from './neovis/PapersGraph.vue'
import { type IdType } from 'vis-network'
import { stateAuthorPapersStat, statePaperList } from './state'

const props = defineProps<{ id: IdType, limit: number }>()

const cyphers = computed(() => {
  const GET_CIT = `MATCH (pc:Publication)-[c:CITE]->(p:Publication) WHERE id(p) = ${props.id}` // pc is citations
  const GET_REF = `MATCH (pr:Publication)<-[r:CITE]-(p:Publication) WHERE id(p) = ${props.id}` // pr is references
  const GET_CIT_CIT = `${GET_CIT} OPTIONAL MATCH (cc:Publication)-[:CITE]->(pc)` // citations' citations
  const GET_REF_CIT = `${GET_REF} OPTIONAL MATCH (cc:Publication)-[:CITE]->(pr)` // references' citations
  return [`MATCH (p:Publication) WHERE id(p) = ${props.id} RETURN p`, // The first node
  `${GET_CIT_CIT}
  WITH COUNT(cc) AS pcc, p, c, pc ORDER BY pcc LIMIT ${props.limit}
  RETURN p, c, pc`, // citations
  `${GET_REF_CIT}
  WITH COUNT(cc) AS prc, p, r, pr ORDER BY prc LIMIT ${props.limit}
  RETURN p, r, pr`, // references
  ]
})
</script>

<template>
  <PapersGraph :cyphers="cyphers" @selectPaper="console.log" />
</template>
