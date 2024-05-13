<script setup lang="ts">
import { computed, ref, watch } from 'vue'
import neo4j from 'neo4j-driver'
import { type Record } from 'neo4j-driver'
import { type IdType } from 'vis-network'
import { serverUrl, serverUser, serverPassword } from './connection'
import { statePaperList } from './state'

const props = defineProps<{ id: IdType, filter: { year?: number, journal?: string, ccf?: string } }>()
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
type PaperContent = {
  title?: string,
  year?: number,
  journal?: string,
  ccf?: string
}
const content = computed(() => {
  let texts: PaperContent[] = []
  for (let paper of papers.value) {
    const data: PaperContent = {}
    const p = paper.get('p')
    if (p && p.properties) {
      if (p.properties.title) data.title = p.properties.title
      if (p.properties.year) data.year = Math.max(p.properties.year.low, p.properties.year.high)
    }
    const j = paper.get('j')
    if (j && j.properties) {
      if (j.properties.dblp_name) data.journal = j.properties.dblp_name
      if (j.properties.ccf) data.ccf = j.properties.ccf
    }
    if (statePaperList.filter.ccf) {
      if (statePaperList.filter.ccf == data.ccf) texts.push(data)
      else if (statePaperList.filter.ccf == "N" && !data.ccf) texts.push(data)
    } else texts.push(data)
  }
  return texts.sort((a, b) => {
    if (!a.year) return 1
    if (!b.year) return -1
    return b.year - a.year
  })
})
</script>

<template>
  <div v-if="error">Oops! Error encountered: {{ error }}</div>
  <div v-else-if="papers">
    <div v-for="(item, index) in content" :key="index">{{ item.title }},
      <span v-if="item.journal">{{ item.journal }}</span>
      <span v-else>unknown journal</span>, {{ item.year }}
      <span v-if="item.ccf">, CCF {{ item.ccf }}</span>
    </div>
  </div>
</template>

<style scoped>
.chart {
  height: 400px;
}
</style>
