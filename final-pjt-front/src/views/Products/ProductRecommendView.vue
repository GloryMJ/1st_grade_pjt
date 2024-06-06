<template>
  <div>
    <div>
      <article class="container">
        <div class="flexbox">
          <img src="@/assets/img/recommend_product.png" alt="" />
          <h1 class="text-center my-4">Finance Navigator가 추천하는 금융상품!</h1>
        </div>
        <hr />
        <section class="mx-2 mb-4">
          <h2 class="text-center mb-4">가장 사랑받는 상품들을 추천합니다!</h2>
          <!-- 캐러셀 -->
          <div id="popularCarousel" class="carousel slide" data-bs-ride="carousel">
            <div class="carousel-indicators">
              <button
                type="button"
                data-bs-target="#popularCarou-sel"
                data-bs-slide-to="0"
                class="active"
                aria-current="true"
                aria-label="Slide 1"
              ></button>
              <button
                type="button"
                data-bs-target="#popularCarousel"
                data-bs-slide-to="1"
                aria-label="Slide 2"
              ></button>
            </div>
            <div class="carousel-inner">
              <div class="carousel-item active">
                <div class="row d-flex justify-content-center">
                  <!-- 캐러셀 상품 목록들 -->
                  <div v-for="(p, index) in most_like_products.slice(0, 3)" :key="index" class="col-md-3 mx-2">
                    <div class="card card-event" @click="Carousel_product_ClickEvent(p.product_pk)">
                      <h5 class="card-header">{{ p.bank.kor_co_nm }}</h5>
                      <div class="card-body">
                        <h5 class="card-title">{{ p.fin_prdt_nm }}</h5>
                        <p class="card-text">가입방법 : {{ p.join_way }}</p>
                        <p class="card-text">가입자 수 : {{ p.likes_count }}</p>
                      </div>
                    </div>
                  </div>
                  <!-- ------ -->
                </div>
              </div>
              <div class="carousel-item">
                <div class="row d-flex justify-content-center">
                  <div v-for="(p, index) in most_like_products.slice(3, 6)" :key="index" class="col-md-3 mx-2">
                    <!-- 캐러셀 상품 목록들 -->
                    <div class="card card-event" @click="Carousel_product_ClickEvent(p.product_pk)">
                      <h5 class="card-header">{{ p.bank.kor_co_nm }}</h5>
                      <div class="card-body">
                        <h5 class="card-title">{{ p.fin_prdt_nm }}</h5>
                        <p class="card-text">가입방법 : {{ p.join_way }}</p>
                        <p class="card-text">가입자 수 : {{ p.likes_count }}</p>
                      </div>
                    </div>
                  </div>
                </div>
                <!-- ------ -->
              </div>
            </div>
            <button
              class="carousel-control-prev"
              type="button"
              data-bs-target="#popularCarousel"
              data-bs-slide="prev"
              style="z-index: 2; position: absolute"
            >
              <span class="carousel-control-prev-icon" aria-hidden="true"></span>
              <span class="visually-hidden">Previous</span>
            </button>
            <button
              class="carousel-control-next"
              type="button"
              data-bs-target="#popularCarousel"
              data-bs-slide="next"
              style="z-index: 2; position: absolute"
            >
              <span class="carousel-control-next-icon" aria-hidden="true"></span>
              <span class="visually-hidden">Next</span>
            </button>
          </div>
        </section>
        <hr />

        <!-- 연령대별 인기 상품 -->
        <template v-for="(products, age_group) in top_products_by_age_group" :key="age_group">
          <section v-if="products && products.length > 0" class="mx-2 mb-4">
            <h2 class="text-center mb-4">{{ age_group }}대 인기 상품들!</h2>
            <div class="row d-flex justify-content-center">
              <div class="col-md-5" v-for="(p, index) in products" :key="p.product_pk">
                <div
                  class="card card-event mb-4 mx-auto"
                  @click="$router.push({ name: 'detailview', params: { productId: p.product_pk } })"
                >
                  <h5 class="card-header">{{ p.bank.kor_co_nm }}</h5>
                  <div class="card-body">
                    <h5 class="card-title">{{ p.fin_prdt_nm }}</h5>
                    <p class="card-text">가입방법 : {{ p.join_way }}</p>
                    <p class="card-text">가입자 수 : {{ p.likes_count }}</p>
                  </div>
                </div>
              </div>
            </div>
          </section>
        </template>
      </article>
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref } from "vue";
import axios from "axios";
import router from "@/router";

const most_like_products = ref([]);
const top_products_by_age_group = ref({});

onMounted(() => {
  axios
    .all([
      axios.get("http://127.0.0.1:8000/products/all/"),
      axios.get("http://127.0.0.1:8000/products/topProductsByAgeGroup/"),
    ])
    .then(
      axios.spread((allRes, ageGroupRes) => {
        const productsData = allRes.data;
        productsData.sort((a, b) => b.likes_count - a.likes_count);
        for (let i = 0; i < Math.min(6, productsData.length); ++i) {
          most_like_products.value.push(productsData[i]);
        }
        top_products_by_age_group.value = ageGroupRes.data;
        console.log(top_products_by_age_group.value); // 데이터 구조 확인
      })
    )
    .catch((error) => {
      console.error("Error fetching products:", error);
      window.alert("error");
    });
});

const Carousel_product_ClickEvent = function (id) {
  router.push({ name: "detailview", params: { productId: id } });
};
</script>

<style scoped>
.flexbox {
  display: flex;
  align-items: center;
}

.flexbox h1 {
  margin-right: 20px;
}

.flexbox img {
  max-height: 3rem;
  margin-left: 10px;
}

#popularCarousel {
  margin: 1;
  padding: 2;
}

.card-event {
  box-shadow: 0 14px 28px rgba(0, 0, 0, 0.25), 0 10px 10px rgba(0, 0, 0, 0.22);
  cursor: pointer;
  transition: transform 0.1s ease;
  background-color: #f8f9fa;
}

.card-event:hover {
  transform: scale(1.01);
}

.card-event:active {
  transform: scale(0.99);
}

.card-header {
  background-color: #007bff;
  color: white;
  font-size: 1rem;
}

.card-body {
  font-size: 0.9rem;
}

h1,
h2 {
  color: #130e11;
  font-weight: bold;
}

.carousel-control-prev-icon,
.carousel-control-next-icon {
  background-color: #007bff;
  border-radius: 50%;
}
</style>
