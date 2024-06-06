<template>
  <div>
    <img v-if="loaded" :src="imgSrc" alt="Empty" class="img-fluid img-thumbnail" @error="onAlt" />
    <img v-else src="@/assets/img/default.png" alt="Empty" />
  </div>
</template>

<script setup>
import { ref, onMounted, defineProps } from "vue";
import axios from "axios";

const props = defineProps({
  product: {
    type: String,
    required: true,
  },
});

const imgSrc = ref(null);
const loaded = ref(true);
const onAlt = () => {
  loaded.value = false;
};

onMounted(() => {
  axios({
    method: "get",
    url: "/api/v1/search/image.json",
    params: {
      query: props.product,
      display: 1,
      sort: "sim",
    },
    headers: {
      "X-Naver-Client-Id": import.meta.env.VITE_APP_NAVER_CLIENT_ID,
      "X-Naver-Client-Secret": import.meta.env.VITE_APP_NAVER_CLIENT_SECRET,
    },
  })
    .then((response) => {
      imgSrc.value = response.data.items[0].link;
    })
    .catch((error) => {
      console.log(error);
    });
});
</script>

<style scoped></style>
