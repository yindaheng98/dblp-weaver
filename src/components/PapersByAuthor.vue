<script setup lang="ts">
import { ref } from 'vue'
import neo4j from 'neo4j-driver'
import { type Record } from 'neo4j-driver'
import { type IdType } from 'vis-network'
import { serverUrl, serverUser, serverPassword } from './connection'
import CCFPie from './CCFPie.vue'

const props = defineProps<{ id: IdType }>()
const driver = neo4j.driver(serverUrl, neo4j.auth.basic(serverUser, serverPassword))
const papers = ref<Record[]>([])
const error = ref(null)
driver
  .session({ database: 'neo4j' })
  .run(
    `MATCH (a:Person) WHERE id(a)=$id
  MATCH (a)-[:WRITE]->(p:Publication)
  MATCH (j:Journal)<-[:PUBLISH]-(p)
  RETURN p,j`,
    { id: props.id }
  )
  .then((result) => {
    papers.value = result.records
  })
  .catch((err) => {
    error.value = err
  })
</script>

<template>
  <div v-if="error">Oops! Error encountered: {{ error }}</div>
  <CCFPie v-else-if="papers" :papers="papers" />
</template>

<style scoped>
.chart {
  height: 400px;
}
</style>
