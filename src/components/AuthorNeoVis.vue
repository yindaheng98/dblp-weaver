<script setup lang="ts">
import { ref, onMounted } from 'vue'
import NeoVis from 'neovis.js'
import { type NumberOrInteger } from 'neovis.js'
import * as Neo4jTypes from 'neo4j-driver'

const props = defineProps({
  cypher: { type: String, required: true }
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
      },
      width: '100%',
      height: '100%'
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
            value:
              'MATCH (a:Person) WHERE id(a) = $id MATCH (a)-[:WRITE]->(p:Publication) RETURN COUNT(p)'
          }
        }
      }
    },
    relationships: {
      COORPERATE: {
        value: 'weight',
        title: 'weight'
      }
    },
    initialCypher: props.cypher
  })
  neoviz.render()
})
</script>

<template>
  <div ref="viz" id="viz" class="viz">Loading...</div>
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

.viz {
  display: flex;
  width: 100%;
  height: 99%;
  align-items: center;
  text-align: center;
}
</style>
