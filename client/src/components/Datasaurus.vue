<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { useConfig } from '../stores/vaConfig';


const buttonList = [
  { name: 'us' },
  { name: 'artists' },
];
const selectedButton = ref<string>('us');
function onSelectButton(button: any) {
  selectedButton.value = button.name;
  button.get();
}
</script>

<template>
  <div class="datasaurus">
    <div class="button-group">
      <a-button
          class="button"
          v-for="button in buttonList"
          :key="button.name"
          :type="button.name === selectedButton ? 'primary' : ''"
          @click="onSelectButton(button)"
      >
        {{ ` ${button.name}` }}
      </a-button>
    </div>
    <img src="../assets/keyword.png">
  </div>
</template>

<style scoped>
.datasaurus {
  height: calc(100% - 2px);
  width: 100%;
  display: flex;
  flex-direction: column;
  border: 1px solid black;
  padding :10px;
  box-sizing:border-box;
}

.button-group {
  padding: 5px;
  display: flex;
  flex: 0 1 auto;
  flex-flow: row wrap;
}

.button {
  flex: auto;
}

img{
  height:100%;
}


#datasaurus-svg {
  flex: 1 0 auto;
  /* border: 1px solid black; */
}

.datapoint-move,
.datapoint-enter-active,
.datapoint-leave-active {
  transition: all 0.5s ease;
}
.datapoint-enter-from,
.datapoint-leave-to {
  opacity: 0;
  transform: translateX(30px);
}

.noselect {
  user-select: none;
}
</style>
