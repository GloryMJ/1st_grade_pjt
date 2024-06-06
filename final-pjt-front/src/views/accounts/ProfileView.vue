<template>
  <div class="container" v-if="accountStore.isLogin">
    <h1>{{ accountStore.userInfo.nickname }} 프로필 정보</h1>
    <hr />

    <button @click="logoutEvent" class="btn btn-primary">로그 아웃</button>
    <button @click="fixProfileEvent" class="btn btn-primary mx-3">프로필 수정</button>
    <hr />

    <!-- OnMounted 처리 후 -->
    <div v-if="!loading">
      <article class="userInfoClass">
        <section class="mt-4 mb-4">
          <h4>프로필 사진</h4>
          <img :src="accountStore.profileImage" alt="profile_Img" width="200px" height="100%" />
        </section>
        <section>
          <hr />
          <h4>기본 정보</h4>
          <section class="mx-3">
            <ul class="list-group list-group-flush" style="font-size: 20px">
              <li class="list-group-item">이름 : {{ accountStore.userInfo.name }}</li>
              <li class="list-group-item">닉네임 : {{ accountStore.userInfo.nickname }}</li>
              <li class="list-group-item">성별 : {{ accountStore.userInfo.gender == 1 ? "남자" : "여자" }}</li>
              <li class="list-group-item">연령대 : {{ accountStore.userInfo.age_group }}대</li>
              <li class="list-group-item">
                위치 : {{ accountStore.userInfo.location ? accountStore.userInfo.location : "공 란" }}
              </li>
            </ul>
          </section>
        </section>
        <hr />
        <section>
          <h4>가입 상품 목록</h4>
          <div class="container" v-if="accountStore.userInfo.like_products.length">
            <div v-for="p in like_product_list" :key="p.product_pk">
              <div class="mx-5 mt-3">
                <div
                  class="card card-event"
                  @click="$router.push({ name: 'detailview', params: { productId: p.product_pk } })"
                >
                  <h5 class="card-header">{{ p.bank.kor_co_nm }}</h5>
                  <div class="card-body">
                    <h5 class="card-title">상품명 : {{ p.fin_prdt_nm }}</h5>
                    <p class="card-text">가입방법 : {{ p.join_way }}</p>
                    <p class="card-text">관심자 수 : {{ p.likes_count }}</p>
                    <!-- 버튼 클릭시 -> 상세 정보로 이동 -->
                  </div>
                </div>
              </div>
            </div>
          </div>

          <div class="container" v-else>
            <h4>비어있어요! 더 다양한 상품을 찾아보세요</h4>
          </div>
        </section>
      </article>
    </div>

    <!-- Onmounted 완료 전 -->
    <div v-else>
      <p>아직 로딩중이에요!</p>
    </div>
  </div>
</template>

<script setup>
import { useAccountStore } from "@/stores/account";
import { computed, onMounted, ref } from "vue";
import { useRouter } from "vue-router";
import axios from "axios";
const accountStore = useAccountStore();
const router = useRouter();
const gender = computed(() => {
  return accountStore.userInfo.gender === 1 ? "남자" : "여자";
});

const like_product_list = ref([]);
const loading = ref(true);
const profileImage = computed(() => {
  if (accountStore.userInfo === null) return accountStore.basicProfile;
  if (accountStore.userInfo.image === null || accountStore.userInfo.image === "") {
    return accountStore.basicProfile;
  } else {
    return accountStore.image;
  }
});
onMounted(() => {
  if (!accountStore.isLogin) {
    window.alert("로그인 해주세요!");
    router.push({ name: "account" });
  }
  if (accountStore.userInfo.like_products.length) {
    for (let productId of accountStore.userInfo.like_products) {
      axios({
        method: "get",
        url: `http://127.0.0.1:8000/products/${productId}/detail/`,
      })
        .then((res) => {
          like_product_list.value.push(res.data);
        })
        .catch((e) => {
          window.alert("에러!");
          router.go(-1);
        });
    }
  }

  loading.value = !loading.value;
});

const logoutEvent = () => {
  router.push({ name: "Home" });
  accountStore.logout();
};

const fixProfileEvent = () => {
  router.push({ name: "fix-profile" });
};
</script>

<style scoped>
.card-event {
  box-shadow: 0 14px 28px rgba(0, 0, 0, 0.25), 0 10px 10px rgba(0, 0, 0, 0.22);
  cursor: pointer;
  transition: transform;
  transition-duration: 0.1s;
}

.card-event:hover {
  transform: scale(1.01);
}

.card-event:active {
  transform: scale(0.99);
}
</style>
