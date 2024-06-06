<template>
  <div class="create-post">
    <h1 class="mt-5">게시글 생성 페이지</h1>

    <form class="border p-3" style="margin: 10px 0px" @submit.prevent="postEvent" ref="articleformitem">
      <label for="category-select">카테고리 선택</label>
      <select class="form-select" id="category-select" name="article_type">
        <option :value="0">--선택해 주세요!--</option>
        <option :value="1">자유 게시판</option>
        <option :value="2">질문 게시판</option>
      </select>

      <div class="mt-3">
        <label for="title">제목</label>
        <input type="text" name="title" id="title" class="form-control" required />
      </div>

      <div class="mt-3">
        <label for="content">내용</label>
        <textarea name="content" id="content" class="form-control" required></textarea>
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
import { useRouter } from "vue-router";
import { onMounted, ref } from "vue";
const accountStore = useAccountStore();
const articleStore = useArticleStore();
const router = useRouter();
const articleformitem = ref(null);
onMounted(() => {
  if (!accountStore.isLogin) {
    window.alert("로그인을 먼저 해 주세요!");
    router.push({ name: "account" });
  }
});

const postEvent = function (event) {
  const articleForm = new FormData(event.target);
  const info = {};
  articleForm.forEach((value, key) => {
    info[key] = value;
  });
  if (info.article_type != 1 && info.article_type != 2) {
    window.alert("게시판 종류를 꼭 골라주세요!");
  } else {
    articleformitem.value.reset();
    articleStore.postArticles(info).then((res) => {
      if (res !== false) {
        // console.log(res);
        router.push({ name: "boardDetail", params: { article_id: res.id } });
      } else {
        window.alert("에러! 다시 한번 시도해 주세요");
      }
    });
  }
};
</script>

<style scoped>
.create-post {
  margin: 10px 20%;
}
</style>
