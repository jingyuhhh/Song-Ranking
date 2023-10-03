<script setup lang="ts">
import { ref, onMounted } from 'vue';
import axios from "axios";

const imgURL = ref<string>("/src/assets/trend a_x forecast.png");
onMounted(async () => {
  const res = await axios.post("http://localhost:5000/predict", )
  if (res.data.status == "success"){
    console.log(res.data.data)
  }
  else{
    console.log("error")
  }
})



</script>

<template>
  <div class="datasaurus">
    <h3>Predict the Trend of Streams of "Shape of You"</h3>
    <img :src="imgURL">
  </div>
</template>

<style scoped>
.datasaurus {
  height: calc(100% - 0px);
  width: 100%;
  display: flex;
  flex-direction: column;
  border: 1px solid black;
  padding :10px;
  box-sizing:border-box;
}
h3{
  margin: 0;
}

img{
  height:77%;
}

</style>
