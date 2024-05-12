<script setup lang="ts">
import { computed } from 'vue'
import AuthorNeoVis from './neovis/AuthorNeoVis.vue'
import { type IdType } from 'vis-network'
import { contentShow } from './state'

const props = defineProps<{ limit: number; id: IdType }>()

const cypher = computed(() => {
  return `
  MATCH (a1:Person)-[:WRITE]->(p1:Publication) WHERE id(p1) = ${props.id}
  MATCH (a1:Person)-[:WRITE]->(p2:Publication)<-[:WRITE]-(a2:Person) WHERE elementId(a1)<elementId(a2)
  RETURN a1,apoc.create.vRelationship(a1,'COORPERATE',{weight:count(p2)},a2),a2 LIMIT ${props.limit}`
})
</script>

<template>
  <AuthorNeoVis :cypher="cypher" @selectAuthor="(id) => contentShow.author(id)" />
</template>
