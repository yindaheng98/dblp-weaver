<script setup lang="ts">
import { ref, watch } from 'vue'
import neo4j from 'neo4j-driver'
import { type Record } from 'neo4j-driver'
import { type IdType } from 'vis-network'
import { serverUrl, serverUser, serverPassword } from './connection'
import AuthorPapersPie from './AuthorPapersPie.vue'
import AuthorPapersBar from './AuthorPapersBar.vue'

const props = defineProps<{ id: IdType }>()
const driver = neo4j.driver(serverUrl, neo4j.auth.basic(serverUser, serverPassword))
const papers = ref<Record[]>([])
const error = ref<any>(null)
const today = new Date()
watch(
  () => props.id,
  async (id) => {
    try {
      const result = await driver.session({ database: 'neo4j' }).run(
        `MATCH (a:Person) WHERE id(a)=$id
  MATCH (a)-[:WRITE]->(p:Publication) WHERE p.year>$year
  OPTIONAL MATCH (j:Journal)<-[:PUBLISH]-(p)
  RETURN p,j`,
        { id: id, year: today.getFullYear() - 5 }
      )
      papers.value = result.records
    } catch (e) {
      error.value = e
    }
  },
  { immediate: true }
)
</script>

<template>
  <div v-if="error">Oops! Error encountered: {{ error }}</div>
  <div v-else-if="papers">
    <AuthorPapersPie :papers="papers" />
    <AuthorPapersBar :papers="papers" :maxyear="today.getFullYear()" :minyear="today.getFullYear() - 5" />
  </div>
</template>

<style scoped>
.chart {
  height: 400px;
}
</style>
