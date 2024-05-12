<script setup lang="ts">
import GraphPanel from './components/GraphPanel.vue'
import ContentPanel from './components/ContentPanel.vue'
import { neovisShow } from './components/state'
neovisShow.authorsbypaper(88) // Only for test
</script>

<template>
  <header>
    <div class="wrapper">
      <GraphPanel :limit="64" />
    </div>
  </header>

  <main>
    <ContentPanel />
  </main>
</template>

<style scoped>
header {
  line-height: 1.5;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    height: 99vh;
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: center;
    flex-wrap: wrap;
    height: 100%;
  }
  main {
    overflow-x: hidden;
    overflow-y: scroll;
    height: 99vh;
  }
}
</style>
