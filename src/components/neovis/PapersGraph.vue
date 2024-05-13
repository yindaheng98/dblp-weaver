<script setup lang="ts">
import { ref, onMounted } from 'vue'
import NeoVis from 'neovis.js'
import { type NumberOrInteger } from 'neovis.js'
import * as Neo4jTypes from 'neo4j-driver'
import { type IdType } from 'vis-network'
import { serverUrl, serverUser, serverPassword } from '../connection'
import { counters } from './state'

const props = defineProps<{ cyphers: string[] }>()
const emit = defineEmits<{
  (e: 'selectPaper', id: IdType): void
}>()
const viz = ref()

onMounted(() => {
  viz.value.id = `papers-graph-${counters.PapersGraph++}`
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
            emit('selectPaper', id)
          },
          label: false
        }
      },
      width: '100%',
      height: '100%'
    },
    labels: {
      Publication: {
        [NeoVis.NEOVIS_ADVANCED_CONFIG]: {
          function: {
            title: (node: Neo4jTypes.Node<NumberOrInteger>) =>
              NeoVis.objectToTitleHtml(node, ['year'])
          },
          cypher: {
            value:
              'MATCH (p:Publication)<-[:CITE]-(a:Publication) WHERE id(p) = $id RETURN COUNT(a)',
            label:
              `
              MATCH (p:Publication) WHERE id(p) = $id
              OPTIONAL MATCH (a:Person)-[:WRITE]->(p)
              OPTIONAL MATCH (a)-[:WRITE]->(pp:Publication) WITH p, a, COUNT(pp) AS c ORDER BY c LIMIT 1
              RETURN a.name + ", " + p.year`,
          }
        }
      }
    },
    relationships: {
      CITE: {
        value: 'weight',
        title: 'weight'
      }
    },
    initialCypher: props.cyphers[0]
  })
  neoviz.render()
  if (props.cyphers.length > 1)
    for (let cypher of props.cyphers.slice(1))
      neoviz.updateWithCypher(cypher)
})
</script>

<template>
  <div ref="viz" class="viz">Loading...</div>
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
