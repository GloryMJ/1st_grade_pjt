<template>
  <div>
    <h1>게시판</h1>
    <button @click="gotoCreateBoard" class="btn btn-info btn-effect mb-3">게시글 만들기!</button>
    <!-- 게시판 선택 Nav -->
    <nav>
      <ul class="nav nav-tabs">
        <li class="nav-item">
          <RouterLink
            :to="{ name: 'board', query: { board_type: 0 } }"
            class="nav-link"
            :class="{ active: BoardType == 0 }"
          >
            전체 게시판
          </RouterLink>
        </li>
        <li class="nav-item">
          <RouterLink
            :to="{ name: 'board', query: { board_type: 1 } }"
            class="nav-link"
            :class="{ active: BoardType == 1 }"
          >
            자유 게시판
          </RouterLink>
        </li>
        <li class="nav-item">
          <RouterLink
            :to="{ name: 'board', query: { board_type: 2 } }"
            class="nav-link"
            :class="{ active: BoardType == 2 }"
          >
            질문 게시판
          </RouterLink>
        </li>
      </ul>
      <div class="tab-content"></div>
    </nav>

    <section class="container letter content-hide" v-if="articleStore.articles">
      <div v-for="article in articleStore.articles">
        <div @click="moveDetailArticle(article.pk)" v-if="filtering(article.article_type)">
          <div class="articleItem">
            <p>{{ name_article_type(article.article_type) }}</p>
            <div class="d-flex justify-content-between">
              <span class="boldp hoverEvent">#{{ article.pk }} | 제목 : {{ article.title }}</span>
              <div>
                <span class="text-end">닉네임 : {{ article.nickname }}</span>
                <span>|</span>
                <span class="text-end">조회수 : {{ article.views }}</span>
              </div>
            </div>
          </div>
        </div>
        <hr />
      </div>
    </section>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, watch } from "vue";
import { useRoute, useRouter } from "vue-router";
const route = useRoute();
const BoardType = ref(0);
import { useArticleStore } from "@/stores/article";
const articleStore = useArticleStore();
const router = useRouter();
// console.log(useArticleStore);
onMounted(() => {
  const { board_type } = route.query;
  if (!board_type || !Number.isInteger(board_type) || board_type < 0 || board_type > 2) {
    BoardType.value = 0;
  } else {
    BoardType.value = Number(board_type);
  }
  articleStore.getArticles();
});

watch(
  () => route.query.board_type,
  () => {
    BoardType.value = route.query.board_type;
  }
);

const name_article_type = function (article_type) {
  if (article_type == 1) return "자유 게시판";
  else return "질문 게시판";
};

const moveDetailArticle = function (article_id) {
  router.push({ name: "boardDetail", params: { article_id: article_id } });
};

const filtering = function (id) {
  if (BoardType.value == 1 || BoardType.value == 2) return id == BoardType.value;
  else return true;
};

const gotoCreateBoard = () => {
  router.push({ name: "createBoard" });
};
</script>

<style scoped>
.nav-tabs .nav-link.active {
  background-color: #007bff;
  color: white;
}
.tab-content {
  margin-top: 20px;
}

.boldp {
  font-size: 20px;
  font-weight: bold;
}

.articleItem {
  padding: 5px;
  border-radius: 8px;
}

.articleItem:hover {
  cursor: pointer;
}

.articleItem:hover {
  transform: scale(1.01);
  /* animation-duration: 0.4s; */
  box-shadow: 0 19px 38px rgba(0, 0, 0, 0.3), 0 15px 12px rgba(0, 0, 0, 0.22);
}

.articleItem:active {
  transform: scale(0.99);
  /* animation-duration: 0.1s; */
}

.btn-effect:hover {
  transform: scale(1.01);
}
.btn-effect:active {
  transform: scale(0.99);
}
</style>
