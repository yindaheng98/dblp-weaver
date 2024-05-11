<script setup lang="ts">
import { computed } from 'vue'
import AuthorNeoVis from './AuthorNeoVis.vue'

const props = defineProps({
  limit: { type: Number, required: true }
})

const cypher = computed(() => {
  return `MATCH (a1:Person)-[:WRITE]->(p:Publication)<-[:WRITE]-(a2:Person) WHERE elementId(a1)<elementId(a2) RETURN a1,apoc.create.vRelationship(a1,'COORPERATE',{weight:count(p)},a2),a2 LIMIT ${props.limit}`
})
</script>

<template>
  <AuthorNeoVis :cypher="cypher" />
</template>
