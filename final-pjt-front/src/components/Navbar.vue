<template>
  <nav class="navbar navbar-expand-lg bg-white">
    <div class="container-fluid">
      <div class="d-flex flex-row">
        <img src="@/assets/img/logo.png" width="70px" height="100%" class="mx-4 cursor-pointer" @click="goHome" />
        <MiniProfile />
      </div>
      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarScroll"
        aria-controls="navbarScroll"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarScroll">
        <ul class="navbar-nav me-auto my-2 my-lg-0 navbar-nav-scroll" style="--bs-scroll-height: 100px">
          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
              회원게시판
            </a>
            <ul class="dropdown-menu">
              <li>
                <RouterLink :to="{ name: 'board', query: { board_type: 0 } }" class="dropdown-item">
                  전체 글 목록
                </RouterLink>
              </li>
              <li>
                <RouterLink :to="{ name: 'board', query: { board_type: 1 } }" class="dropdown-item">
                  자유 게시판
                </RouterLink>
              </li>
              <li>
                <RouterLink :to="{ name: 'board', query: { board_type: 2 } }" class="dropdown-item">
                  질문 게시판
                </RouterLink>
              </li>
              <li>
                <hr class="dropdown-divider" />
              </li>
              <li>
                <RouterLink to="" class="dropdown-item">인기 순위</RouterLink>
              </li>
            </ul>
          </li>
          <li class="nav-item">
            <RouterLink :to="{ name: 'banksearch' }" class="nav-link">주변은행 검색</RouterLink>
          </li>
          <li class="nav-item">
            <RouterLink :to="{ name: 'exchangecalc' }" class="nav-link">오늘의 환율</RouterLink>
          </li>
          <li class="nav-item">
            <RouterLink :to="{ name: 'productlist' }" class="nav-link">금융상품</RouterLink>
          </li>
          <li class="nav-item">
            <RouterLink :to="{ name: 'productrecommend' }" class="nav-link">추천상품</RouterLink>
          </li>
        </ul>
        <ul class="navbar-nav ml-auto">
          <li class="nav-item">
            <button class="btn btn-primary rounded-pill" @click="openOffcanvas">물어보세요</button>
          </li>
        </ul>
      </div>
    </div>
  </nav>

  <div
    class="offcanvas offcanvas-end"
    tabindex="-1"
    id="offcanvasRight"
    ref="offcanvasRight"
    aria-labelledby="offcanvasRightLabel"
  >
    <div class="offcanvas-header">
      <h5 id="offcanvasRightLabel">물어보세요</h5>
      <button type="button" class="btn-close" data-bs-dismiss="offcanvas" aria-label="Close"></button>
    </div>
    <div class="offcanvas-body">
      <div class="offcanvas-menu">
        <ChatbotUI />
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import MiniProfile from "./MiniProfile.vue";
import { Offcanvas } from "bootstrap";
import { RouterView, RouterLink, useRouter } from "vue-router";
import { useAccountStore } from "@/stores/account";
import BoardView from "@/views/Board/BoardView.vue";
import ChatbotUI from "@/components/chatbot/ChatbotUI.vue";
const store = useAccountStore();
const accountStore = useAccountStore();
const offcanvasRight = ref(null);

const openOffcanvas = () => {
  const offcanvas = new Offcanvas(offcanvasRight.value);
  offcanvas.show();
};

const router = useRouter();
const goHome = () => {
  router.push({ name: "Home" });
};
</script>

<style scoped>
.navbar {
  background-color: #ffffff;
}

.navbar .nav-link {
  color: #000000;
}

.navbar .nav-link.active {
  font-weight: bold;
}

.navbar .site-name {
  font-size: 1.5rem;
  color: #007bff;
}

.navbar .btn-primary {
  background-color: #007bff;
  border-color: #007bff;
  color: #ffffff;
}

.offcanvas-end {
  background-color: #f8f9fa;
  /* background-image: url("@/assets/img/offcanvas.webp"); */
  background-size: cover;
}

.offcanvas-header {
  background-color: rgba(0, 123, 255, 0.1);
}

.offcanvas-menu .offcanvas-link {
  display: block;
  padding: 10px 15px;
  margin-bottom: 10px;
  background-color: rgba(255, 255, 255, 0.8);
  border-radius: 5px;
  color: #007bff;
  text-decoration: none;
  transition: background-color 0.3s ease;
}

.offcanvas-menu .offcanvas-link:hover {
  background-color: rgba(0, 123, 255, 0.1);
}

#offcanvasRightLabel {
  color: rgb(0, 0, 0);
}

.cursor-pointer {
  cursor: pointer;
}
</style>
