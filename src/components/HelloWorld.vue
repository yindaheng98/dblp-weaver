<script setup lang="ts">
import { ref, onMounted } from 'vue'
import NeoVis from 'neovis.js'
import { type NumberOrInteger } from 'neovis.js'
import * as Neo4jTypes from 'neo4j-driver'

const props = defineProps({
  limit: { type: Number, required: true }
})
const viz = ref()
const serverUrl = import.meta.env.VITE_NEO4J_SERVER_URL
const serverUser = import.meta.env.VITE_NEO4J_SERVER_USER
const serverPassword = import.meta.env.VITE_NEO4J_SERVER_PASSWORD

onMounted(() => {
  let neoviz = new NeoVis({
    containerId: viz.value.id,
    neo4j: {
      serverUrl: serverUrl,
      serverUser: serverUser,
      serverPassword: serverPassword
    },
    visConfig: {
      nodes: {
        shape: 'dot'
      }
    },
    labels: {
      Person: {
        label: 'name',
        [NeoVis.NEOVIS_ADVANCED_CONFIG]: {
          function: {
            title: (node: Neo4jTypes.Node<NumberOrInteger>) =>
              NeoVis.objectToTitleHtml(node, ['name'])
          },
          cypher: {
            value: 'MATCH (a:Person{id:$id})-[:WRITE]->(p:Publication) RETURN COUNT(p)'
          }
        }
      }
    },
    relationships: {
      COORPERATE: {
        value: 'weight'
      }
    },
    initialCypher: `MATCH (a1:Person)-[:WRITE]->(p:Publication)<-[:WRITE]-(a2:Person) WHERE elementId(a1)<elementId(a2) RETURN a1,apoc.create.vRelationship(a1,'COORPERATE',{weight:count(p)},a2),a2 LIMIT ${props.limit}`
  })
  neoviz.render()
})
</script>

<template>
  <div class="greetings">
    <div ref="viz" id="viz">Loading...</div>
  </div>
</template>

<style scoped>
h1 {
  font-weight: 500;
  font-size: 2.6rem;
  position: relative;
  top: -10px;
}

h3 {
  font-size: 1.2rem;
}

.greetings h1,
.greetings h3 {
  text-align: center;
}

@media (min-width: 1024px) {
  .greetings h1,
  .greetings h3 {
    text-align: left;
  }
}
</style>
