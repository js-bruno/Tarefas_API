<template>
  <div id="app">
<!--     
    <div class="jumbotron jumbotron-fluid">
      <div class="container">
        <h1 class="display-4">API COM VUE``</h1>
      </div>
    </div> -->

    <div class="container">
      <br><br>
      <TarefasLista />

    </div>

  </div>
</template>

<script>

import TarefasLista from './components/TarefasLista.vue'

export default {
    components: {
        TarefasLista
    }
}
</script>