<template>
  <div>
    <section class="rounded-3 bg-dark p-2 d-flex justify-content-center">
      <div v-if="!accountStore.isLogin" @click="moveLogin" style="cursor: pointer">
        <span style="color: white">로그인</span>
      </div>
      <div
        v-else
        class="d-flex justify-content-center mini-profile"
        style="color: white; cursor: pointer"
        @click="moveProfile"
      >
        <img :src="accountStore.profileImage" width="30px" height="30px" alt="" />
        <div class="info mx-2">
          <p>{{ accountStore.userInfo.nickname }}</p>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { useAccountStore } from "@/stores/account";
import { computed } from "vue";
import { useRouter } from "vue-router";
const router = useRouter();
const accountStore = useAccountStore();

const profileImage = computed(() => {
  if (accountStore.userInfo === null) return accountStore.basicProfile;
  if (accountStore.userInfo.image === null || accountStore.userInfo.image === "") {
    return accountStore.basicProfile;
  } else {
    return accountStore.image;
  }
});

const moveLogin = () => {
  router.push({ name: "account" });
};

const moveProfile = () => {
  router.push({ name: "profile" });
};
</script>
<style scoped>
.mini-profile {
  width: 50px;
  height: 30px; /* 높이 고정 */
  transition: 0.3s;
  overflow: hidden;
}

.mini-profile:hover {
  width: 150px;
  height: 30px !important; /* 높이 고정 */
}

.mini-profile:hover .info {
  display: block;
  color: white;
}

.info {
  display: none;
  transition: 0.3s;
  overflow: visible;
  white-space: nowrap;
}
</style>
