<template>
  <div class="container">
    <h1>{{ accountStore.userInfo.nickname }} 프로필 수정하기</h1>
    <hr />

    <h3>프로필 이미지 업로드</h3>
    <form @submit.prevent="profileImageUpdateEvent" enctype="multipart/form-data">
      <section class="d-flex flex-row align-items-center justify-content-evenly">
        <div>
          <p>프로필 현재 사진</p>
          <img :src="accountStore.profileImage" width="200px" />
        </div>
        <div>
          <label for="image-update" class="form-label">이미지 업로드</label>
          <input type="file" name="image" id="image-update" class="form-control" />
        </div>
      </section>
      <input type="submit" value="프로필 변경" class="mx-5 mt-4 btn btn-primary" />
    </form>

    <hr />
    <h3>정보 업데이트</h3>
    <section mx-4>
      <form class="mx-5 px-5" @submit.prevent="profileInfoUpdateEvent">
        <label for="name" class="form-label">이름</label>
        <input type="text" class="form-control" name="name" :value="accountStore.userInfo.name" id="name" />
        <br />
        <label for="nickname" class="form-label">닉네임</label>
        <input type="text" class="form-control" name="nickname" :value="accountStore.userInfo.nickname" id="nickname" />
        <br />
        <label for="gender" class="form-label">성별</label>
        <select class="form-select" name="gender" id="gender">
          <option value="1" :selected="accountStore.userInfo.gender == 1">남자</option>
          <option value="2" :selected="accountStore.userInfo.gender == 2">여자</option>
        </select>
        <br />
        <label for="age_group" class="form-label">연령대</label>
        <select class="form-select" name="age_group" id="age_group">
          <option value="10" :selected="accountStore.userInfo.age_group == 10">10대</option>
          <option value="20" :selected="accountStore.userInfo.age_group == 20">20대</option>
          <option value="30" :selected="accountStore.userInfo.age_group == 30">30대</option>
          <option value="40" :selected="accountStore.userInfo.age_group == 40">40대</option>
          <option value="50" :selected="accountStore.userInfo.age_group == 50">50대</option>
          <option value="60" :selected="accountStore.userInfo.age_group == 60">60대</option>
          <option value="70" :selected="accountStore.userInfo.age_group == 70">70대</option>
          <option value="80" :selected="accountStore.userInfo.age_group == 80">80대</option>
        </select>
        <br />
        <label for="location" class="form-label">위치</label>
        <input type="text" class="form-control" name="location" :value="accountStore.userInfo.location" id="location" />
        <br />

        <input type="submit" value="정보 변경" class="mx-5 mt-4 btn btn-primary" />
      </form>
    </section>
  </div>
</template>

<script setup>
import { useAccountStore } from "@/stores/account";
import { computed, onMounted } from "vue";
import { useRouter } from "vue-router";
const accountStore = useAccountStore();
const router = useRouter();
const gender = computed(() => {
  return accountStore.userInfo.gender === 1 ? "남자" : "여자";
});

onMounted(() => {
  if (!accountStore.isLogin) {
    window.alert("로그인 해주세요!");
    router.push({ name: "account" });
  }
});

const profileImageUpdateEvent = function (event) {
  if (event.target.image.files?.[0]) {
    const uploadFile = event.target.image.files[0];
    const formData = new FormData();
    formData.append("image", uploadFile);
    accountStore.updateProfile(accountStore.userInfo.id, formData);
  }
};

const profileInfoUpdateEvent = function (event) {
  const info = {};
  console.log(event.target);

  new FormData(event.target).forEach((value, key) => {
    info[key] = value;
  });
  accountStore
    .updateInfo(accountStore.userInfo.id, info)
    .then((res) => {
      router.push({ name: "profile" });
    })
    .catch((e) => {
      console.log(e);
      window.alert("error");
    });
};
</script>
