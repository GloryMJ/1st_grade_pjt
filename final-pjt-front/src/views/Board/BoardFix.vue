<template>
  <div class="create-post" v-if="article">
    <h1 class="mt-5">게시글 생성 페이지</h1>

    <form class="border p-3" style="margin: 10px 0px" @submit.prevent="fixPostEvet" :ref="ref_value">
      <label for="category-select">카테고리 선택</label>
      <select class="form-select" id="category-select" name="article_type">
        <option :value="0">--선택해 주세요!--</option>
        <option :value="1" :selected="article.article_type == 1">자유 게시판</option>
        <option :value="2" :selected="article.article_type == 2">질문 게시판</option>
      </select>

      <div class="mt-3">
        <label for="title">제목</label>
        <input type="text" name="title" id="title" class="form-control" :value="article.title" required />
      </div>

      <div class="mt-3">
        <label for="content">내용</label>
        <textarea name="content" id="content" class="form-control" required>{{ article.content }}</textarea>
      </div>

      <div class="d-grid gap-2 mt-4">
        <input class="btn btn-primary" type="submit" value="제출" />
      </div>
    </form>
  </div>
</template>

<script setup>
import { useAccountStore } from "@/stores/account";
import { useArticleStore } from "@/stores/article";
import { useRouter, useRoute } from "vue-router";
import { onMounted, ref } from "vue";
const accountStore = useAccountStore();
const articleStore = useArticleStore();
const router = useRouter();
const route = useRoute();
const ref_value = ref(null);
const article = ref(null);
onMounted(() => {
  if (!accountStore.isLogin) {
    window.alert("로그인을 먼저 해 주세요!");
    router.push({ name: "account" });
  }
  console.log(route.params);
  articleStore
    .getDetailArticles(route.params.article_id)
    .then((res) => {
      article.value = res.data;
      if (accountStore.userInfo.id != article.value.user) {
        window.alert("작성자 본인만 접근 가능합니다.");
        console.log(accountStore.userInfo.id, article.value);
        router.go(-1);
      }
    })
    .catch((e) => {
      window.alert("에러! 잘못된 접근");
      router.push(-1);
    });
});

const fixPostEvet = function (event) {
  let form_data = {};
  new FormData(event.target).forEach((value, key) => (form_data[key] = value));
  articleStore.fixArticles(route.params.article_id, form_data);
};
</script>

<style scoped>
.create-post {
  margin: 10px 20%;
}
</style>
