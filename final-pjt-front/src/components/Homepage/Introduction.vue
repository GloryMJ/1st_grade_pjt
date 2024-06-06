<template>
  <section class="introduction-section mx-5 animate-fade-in">
    <h1 class="text-center">Finance Navigator에 오신 것을 환영합니다!</h1>
    <div class="text-center">
      <img src="@/assets/img/logo.png" alt="logo" width="" />
    </div>
    <div class="d-flex flex-row justify-content-between">
      <article class="mx-5 introduce text-center mt-3">
        고객님의 최적의 금융 여정을 위한 안내서, Finance Navigator입니다.
        <br />
        다양한 금융 상품을 비교하고 추천받아 당신에게 맞는 최적의 상품을 찾아보세요!
        <hr />
        <section>
          <!-- 기능 안내 섹션 -->
          <div class="row text-center">
            <div
              class="col feature d-lg-block d-none"
              v-for="(feature, index) in features"
              :key="index"
              @click="navigateTo(feature.path)"
              style="cursor: pointer"
            >
              <img :src="feature.icon" :alt="feature.title" class="img-fluid mb-2" />
              <h5>{{ feature.title }}</h5>
            </div>
          </div>
        </section>
      </article>
    </div>
  </section>
</template>

<script setup>
import { ref, onMounted, computed } from "vue";
import { useRouter } from "vue-router";
import axios from "axios";
import { useAccountStore } from "@/stores/account";

// vite의 import.meta.glob을 사용하여 디렉토리 내의 이미지 파일들 한번에 불러오기
const featureIcons = import.meta.glob("@/assets/img/*.png", { eager: true });

const features = ref([
  { title: "예금금리", icon: featureIcons["/src/assets/img/deposit.png"].default, path: "/productlist" },
  { title: "적금금리", icon: featureIcons["/src/assets/img/saving.png"].default, path: "/productlist" },
  { title: "환율비교", icon: featureIcons["/src/assets/img/exchange.png"].default, path: "/exchangecalc" },
  { title: "상품추천", icon: featureIcons["/src/assets/img/recommend.png"].default, path: "/product-recommend" },
  { title: "은행검색", icon: featureIcons["/src/assets/img/bank-search.png"].default, path: "/banksearch" },
]);

const router = useRouter();

function navigateTo(path) {
  router.push(path);
}
</script>

<style scoped>
.introduction-section {
  overflow: hidden;
  background-color: #f5f7fa;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  animation: fadeIn 1s ease-in;
}

.introduction-section h1 {
  font-size: 2rem;
  color: #007bff;
  margin-bottom: 20px;
}

.introduce {
  font-size: 1.25rem;
  color: #333;
}

.introduce hr {
  border: 0;
  border-top: 1px solid #e0e0e0;
  margin: 20px 0;
}

.feature {
  overflow: hidden;
  display: inline-block;
  margin: 10px;
  padding: 20px;
  background-color: #fff;
  border: 1px solid #e0e0e0;
  border-radius: 10px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s, box-shadow 0.3s;
}

.feature:hover {
  transform: translateY(-5px);
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

.feature img {
  max-width: 100%;
  height: auto;
  border-radius: 5px;
}

.feature h5 {
  margin-top: 10px;
  font-size: 1rem;
  color: #007bff;
}

@keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}
</style>
