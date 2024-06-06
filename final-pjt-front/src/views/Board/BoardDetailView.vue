<template>
  <div class="container mt-4">
    <template v-if="article">
      <h1>상세 내용</h1>
      <div class="card">
        <div class="card-body letter">
          <h2 class="card-title">게시글 상세 정보</h2>
          <p>{{ name_article_type(article.article_type) }}</p>
          <p>{{ article.id }}번 글</p>
          <h4 class="card-title">{{ article.title }}</h4>
          <hr />
          <p>작성일 : {{ article.created_at }}</p>
          <p>
            작성자 :
            <b>{{ article.nickname }}</b>
          </p>
          <hr />
          <h4>내용</h4>
          <p>{{ article.content }}</p>
          <br />

          <!-- 작성자만 뜨는 수정 및 삭제 버튼 -->
          <section v-if="accountStore.isLogin && article.user == accountStore.userInfo.id">
            <button type="button" class="btn btn-primary" @click="fixButtonEvent(article.id)">수정</button>
            &emsp;
            <button type="button" class="btn btn-danger" @click="articleStore.deleteArticles(article.id)">삭제</button>
          </section>
          <hr />
          <!-- 덧글 생성 -->

          <template v-if="accountStore.isLogin">
            <form @submit.prevent="commentPostEvent">
              <div class="input-group mb-3">
                <span class="input-group-text" id="inputGroup-sizing-default">댓글 :</span>
                <input
                  type="text"
                  class="form-control"
                  aria-label="Sizing example input"
                  aria-describedby="inputGroup-sizing-default"
                  name="comment"
                />
                <input class="btn btn-outline-secondary" type="submit" id="submitButton" value="덧글작성" />
              </div>
            </form>
          </template>
          <!-- 덧글 내용 -->
          <section v-if="article && article.comments" class="d-flex flex-column">
            <div v-for="comment in article.comments" :key="comment.id">
              <div class="d-flex justify-content-between mb-3 align-content-between align-items-center">
                <p>작성자 : {{ comment.nickname }} -> {{ comment.content }}</p>
                <div v-if="comment.user == accountStore.userInfo.id">
                  <button
                    type="button"
                    class="btn btn-danger"
                    style="--bs-btn-padding-y: 0.25rem; --bs-btn-padding-x: 0.5rem; --bs-btn-font-size: 0.75rem"
                    @click="deleteCommentEvent($event, comment.id)"
                  >
                    덧글삭제
                  </button>
                  <!-- 덧글수정
                  <button
                    type="button"
                    class="btn btn-primary"
                    style="--bs-btn-padding-y: 0.25rem; --bs-btn-padding-x: 0.5rem; --bs-btn-font-size: 0.75rem"
                    @click=""
                  >
                    덧글수정
                  </button> -->
                </div>
              </div>
              <!-- 덧글 수정 폼
              <form class="letter" :id="`${comment.id}form`">
                <div class="input-group mb-3">
                  <input
                    type="text"
                    class="form-control"
                    aria-label="Recipient's username"
                    aria-describedby="button-addon2"
                  />
                  <button class="btn btn-outline-secondary" type="button" id="button-addon2">Button</button>
                </div>
              </form> -->
            </div>
            <hr />
          </section>
        </div>
      </div>
    </template>
  </div>
</template>

<script setup>
import { useArticleStore } from "@/stores/article";
import { onMounted, ref, computed } from "vue";
import { useRoute, useRouter } from "vue-router";
import { useAccountStore } from "@/stores/account";
import axios from "axios";
const router = useRouter();
const route = useRoute();
const accountStore = useAccountStore();
const articleStore = useArticleStore();
const article = ref(null);

const name_article_type = function (article_type) {
  if (article_type == 1) return "자유 게시판";
  else return "질문 게시판";
};

onMounted(() => {
  articleStore.getDetailArticles(route.params.article_id).then((res) => {
    if (res == false) {
      window.alert("에러가 발생했어요");
      router.push({ name: "Home" });
    } else {
      // console.log(res);
      article.value = res.data;
      articleStore.updateArticleViewsCount(route.params.article_id);
      article.value.views++;
    }
  });
});

const commentPostEvent = function (event) {
  const comment = event.currentTarget.comment.value;
  axios({
    method: "post",
    url: `${articleStore.article_URL}/${route.params.article_id}/comments/`,
    data: {
      content: comment,
    },
    headers: {
      Authorization: `Token ${accountStore.key}`,
    },
  })
    .then((res) => {
      article.value.comments.push(res.data);
    })
    .catch((e) => {
      window.alert("error!");
    });
};

const fixButtonEvent = function (id) {
  // console.log(id);
  router.push({ name: "fix-board", params: { article_id: id } });
};

const deleteCommentEvent = async function (event, comment_id) {
  articleStore
    .deleteComment(article.value.id, comment_id)
    .then((res) => {
      article.value.comments = article.value.comments.filter((element) => {
        return element.id != comment_id;
      });
    })
    .catch((e) => {
      console.log(e);
    });
};
</script>

<style scoped>
div {
  overflow: hidden;
}

@keyframes reveal {
  0% {
    transform: translateY(100%);
  }
  100% {
    transform: translateY(0);
  }
}

.letter {
  display: inline-block;
  animation: reveal 1s cubic-bezier(0.77, 0, 0.175, 1) forwards;
}
</style>
