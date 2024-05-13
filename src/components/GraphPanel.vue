<script setup lang="ts">
import { stateGraphPanel, ShowNeoVisType } from './state'
import PaperAuthorsGraph from './PaperAuthorsGraph.vue'
import PaperCitesGraph from './PaperCitesGraph.vue'

const props = defineProps<{ limit: number }>()
</script>

<template>
  <div v-if="stateGraphPanel.type == ShowNeoVisType.None">Please select a starting point</div>
  <PaperAuthorsGraph v-else-if="stateGraphPanel.type == ShowNeoVisType.PaperAuthorsGraph" :id="stateGraphPanel.id" />
  <PaperCitesGraph v-else-if="stateGraphPanel.type == ShowNeoVisType.PaperCitesGraph" :id="stateGraphPanel.id" :limit="props.limit" />
</template>
