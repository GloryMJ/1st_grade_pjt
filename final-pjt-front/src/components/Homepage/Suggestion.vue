<template>
  <div>
    <section class="board-section mx-5 row d-none d-md-block">
      <div class="row row-cols-1 row-cols-lg-2">
        <div class="col mb-4 mb-lg-0">
          <div class="board-list animate-left">
            <h2>실시간 인기 게시글</h2>
            <nav>
              <ul class="nav nav-tabs">
                <li class="nav-item">
                  <a class="nav-link" :class="{ active: boardType === 1 }" @click="setBoardType(1)">자유 게시판</a>
                </li>
                <li class="nav-item">
                  <a class="nav-link" :class="{ active: boardType === 2 }" @click="setBoardType(2)">질문 게시판</a>
                </li>
                <li class="nav-item">
                  <a class="nav-link" :class="{ active: boardType === 3 }" @click="setBoardType(3)">인기순위</a>
                </li>
              </ul>
            </nav>
            <ul>
              <li v-for="(post, index) in filteredPosts" :key="index">
                <a :href="`/detail-article/${post.pk}`" class="post-link">
                  {{ post.title }}
                </a>
                - {{ getBoardName(post.article_type) }} (조회수 {{ post.views }})
              </li>
            </ul>
            <div class="text-end more-link">
              <a @click="navigateTo('/board?board_type=0')" class="more-link-btn">더보기</a>
            </div>
          </div>
        </div>
        <div class="col">
          <div class="recommend-section animate-right">
            <h2>사람들이 가장 많이 찾는 상품!</h2>
            <img src="@/assets/img/recommend.webp" alt="추천상품 이미지" class="recommend-image" />
            <button @click="navigateTo('/product-recommend')" class="recommend-button">오늘의 추천상품 바로가기</button>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from "vue";
import { useRouter } from "vue-router";
import axios from "axios";

const posts = ref([]);
const boardType = ref(0);

const router = useRouter();

onMounted(async () => {
  try {
    const response = await axios.get("http://localhost:8000/articles/list/");
    posts.value = response.data;
  } catch (error) {
    console.error("게시판 데이터를 불러오는 데 실패했습니다.", error);
  }
});

const setBoardType = (type) => {
  boardType.value = type;
};

const filteredPosts = computed(() => {
  if (boardType.value === 0) {
    return posts.value;
  } else if (boardType.value === 3) {
    return posts.value
      .slice()
      .sort((a, b) => b.views - a.views)
      .slice(0, 5);
  } else {
    return posts.value.filter((post) => post.article_type === boardType.value);
  }
});

const getBoardName = (articleType) => {
  if (articleType === 1) return "자유 게시판";
  if (articleType === 2) return "질문 게시판";
  return "기타 게시판";
};

function navigateTo(path) {
  router.push(path);
}
</script>

<style scoped>
.board-section {
  display: flex;
  flex-flow: row wrap;
  align-items: stretch;
  justify-content: space-center;
  gap: 20px;
  background-color: #f5f7fa;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.board-list {
  border: 1px solid #e0e0e0;
  background-color: #ffffff;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  height: 100%;
}

.board-list h2 {
  font-size: 1.5rem;
  color: #333333;
  border-bottom: 2px solid #e0e0e0;
  padding-bottom: 10px;
  margin-bottom: 20px;
}

.nav-tabs {
  border-bottom: 1px solid #e0e0e0;
}

.nav-item .nav-link {
  color: #007bff;
  font-weight: bold;
  padding: 10px 15px;
  transition: color 0.3s;
}

.nav-item .nav-link.active {
  color: #0056b3;
  border-color: #0056b3;
}

.nav-item .nav-link:hover {
  color: #0056b3;
}

ul {
  list-style: none;
  padding: 0;
}

li {
  padding: 10px 0;
  border-bottom: 1px solid #e0e0e0;
}

li:last-child {
  border-bottom: none;
}

.post-link {
  color: #333333;
  font-weight: bold;
  text-decoration: none;
  transition: color 0.3s;
}

.post-link:hover {
  color: #007bff;
}

.more-link {
  margin-top: 20px;
}

.more-link-btn {
  color: #007bff;
  font-weight: bold;
  text-decoration: none;
  cursor: pointer;
  transition: color 0.3s;
}

.more-link-btn:hover {
  color: #0056b3;
}

.recommend-section {
  background-color: #ffffff;
  border: 1px solid #e0e0e0;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  text-align: center;
  height: 100%;
}

.recommend-section h2 {
  font-size: 1.5rem;
  color: #333333;
  border-bottom: 2px solid #e0e0e0;
  padding-bottom: 10px;
  margin-bottom: 20px;
}

.recommend-image {
  max-width: 100%;
  height: auto;
  object-fit: contain;
  display: block;
  margin: 0 auto 20px;
}

.recommend-button {
  background-color: #007bff;
  color: #ffffff;
  border: none;
  padding: 10px 20px;
  border-radius: 5px;
  font-size: 1rem;
  font-weight: bold;
  cursor: pointer;
  transition: background-color 0.3s;
}

.recommend-button:hover {
  background-color: #0056b3;
}

/* 애니메이션 */
@keyframes slideInFromLeft {
  0% {
    transform: translateX(-100%);
    opacity: 0;
  }
  100% {
    transform: translateX(0);
    opacity: 1;
  }
}

@keyframes slideInFromRight {
  0% {
    transform: translateX(100%);
    opacity: 0;
  }
  100% {
    transform: translateX(0);
    opacity: 1;
  }
}

.animate-left {
  animation: 1s ease-out 0s 1 slideInFromLeft;
}

.animate-right {
  animation: 1s ease-out 0s 1 slideInFromRight;
}
</style>
