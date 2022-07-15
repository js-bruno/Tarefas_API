<template>
  <div>
    <div class="row">
      <div class="col-sm-10">
        <h1 class="font-weight-light">Lista de Tarefas {{versao}} </h1>
      </div>
      <div class="col-sm-2">
        <button class="btn btn-primary float-right" @click="exibirFormularioCriarTarefa">
          <i class="fa fa-plus mr-2">Criar</i>
        </button>
      </div>
    </div>

    <ul class="list-group" v-if="tarefas.length > 0">
      <TarefasListaIten
        v-for="tarefa in tarefas"
        :key="tarefa.id"
        :tarefa="tarefa"
        @editar="selecionarTarefaParaEdicao"
        @deletar="deletarTarefa"
        @concluir="editarTarefa"
      />
    </ul>

    <p v-else>Nenhuma tarefa criada.</p>

    <TarefaSalvar
      v-if="exibirFormulario"
      :tarefa="tarefaSelecionada"
      @criar="criarTarefa"
      @editar="editarTarefa"
    />
  </div>
</template>

<script>
/* eslint-disable */
import axios from "axios";

import TarefaSalvar from "./TarefaSalvar.vue";
import TarefasListaIten from "./TarefasListaIten.vue";
// console.log("jorginho", process.env.VUE_APP_URLAPI);
export default {
  components: {
    TarefaSalvar,
    TarefasListaIten
  },

  data() {
    return {
      tarefas: [],
      exibirFormulario: false,
      tarefaSelecionada: undefined,
      versao: '1.0.1'
    };
  },
  created() {
    axios.get('http://localhost:8000/api/tarefas/').then(response => {
      this.tarefas = response.data;
    });
  },
  methods: {
    criarTarefa(tarefa) {
      axios.post("http://localhost:8000/api/tarefas/", tarefa).then(response => {
        this.tarefas.push(response.data);
        this.resetar();
      });
    },
    deletarTarefa(tarefa) {
      const confirmar = window.confirm(`Realmente deseja deletar?`);
      if (confirmar) {
        axios
          .delete("http://localhost:8000/api/tarefas/" + `${tarefa.id}` + "/")
          .then(response => {
            const indice = this.tarefas.findIndex(t => t.id === tarefa.id);
            this.tarefas.splice(indice, 1);
          });
      }
    },
    selecionarTarefaParaEdicao(tarefa) {
      this.tarefaSelecionada = tarefa;
      this.exibirFormulario = true;
    },
    editarTarefa(tarefa) {
      axios
        .put("http://localhost:8000/api/tarefas/" + `${tarefa.id}` + "/", tarefa)
        .then(response => {
          const indice = this.tarefas.findIndex(t => t.id === tarefa.id);
          this.tarefas.splice(indice, 1, tarefa);
          this.resetar();
        });
    },
    
    resetar() {
      this.tarefaSelecionada = undefined;
      this.exibirFormulario = false;
    },
    exibirFormularioCriarTarefa(){
        if(this.tarefaSelecionada){
            this.tarefaSelecionada = undefined
            return 
        }
        this.exibirFormulario = !this.exibirFormulario
    }
  }
};
</script>
