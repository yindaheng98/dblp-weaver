<script setup lang="ts">
import { ref, onMounted } from 'vue'
import NeoVis from 'neovis.js'
import { type NumberOrInteger } from 'neovis.js'
import * as Neo4jTypes from 'neo4j-driver'
import { content_show } from '../state'
import { serverUrl, serverUser, serverPassword } from '../connection'

const props = defineProps({
  cypher: { type: String, required: true }
})
const viz = ref()

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
        shape: 'dot',
        chosen: {
          node: function (values, id, selected, hovering) {
            content_show.author(id)
          },
          label: false
        }
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
