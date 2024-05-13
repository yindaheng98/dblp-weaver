<script setup lang="ts">
import { computed } from 'vue'
import PapersGraph from './neovis/PapersGraph.vue'
import { type IdType } from 'vis-network'
import { stateAuthorPapersStat, statePaperList } from './state'

const props = defineProps<{ id: IdType, limit: number }>()

const cyphers = computed(() => {
  const Cyphers: string[] = []
  Cyphers.push(`MATCH (p:Publication) WHERE id(p) = ${props.id} RETURN p`) // The first node
  const GET_CR = `MATCH (pp:Publication)-[c:CITE]-(p:Publication) WHERE id(p) = ${props.id}` // pp is citations or references
  const GET_CR_CIT = `${GET_CR} OPTIONAL MATCH (cc:Publication)-[:CITE]->(pp)` // citations' or references' citations
  Cyphers.push(`${GET_CR_CIT} WITH COUNT(cc) AS cc, p, c, pp ORDER BY cc LIMIT ${props.limit} RETURN p, c, pp`) // Those citation or reference nodes
  const GET_CR_LIM = `${GET_CR_CIT} WITH COUNT(cc) AS cc, pp ORDER BY cc LIMIT ${props.limit} WITH pp AS p` // citation or reference nodes limited by citation count
  const GET_CR_CR = `${GET_CR_LIM} MATCH (p)-[c:CITE]-(pp:Publication)-[:CITE]-(p0:Publication) WHERE id(p0) = ${props.id} WITH p, c, pp` // pp is other citation or reference nodes
  const GET_CR_CR_CIT = `${GET_CR_CR} OPTIONAL MATCH (cc:Publication)-[:CITE]->(pp)` // other citations' or references' citations
  Cyphers.push(`${GET_CR_CR_CIT} WITH COUNT(cc) AS cc, p, c, pp ORDER BY cc LIMIT ${props.limit} RETURN p, c, pp`) // Those citation or reference nodes
  return Cyphers
})
</script>

<template>
  <PapersGraph :cyphers="cyphers" @selectPaper="console.log" />
</template>
