import { ref, computed } from "vue";
import { defineStore } from "pinia";
import axios from "axios";
import { useRouter } from "vue-router";

export const useAccountStore = defineStore(
  "account",
  () => {
    const Account_URL = ref("http://127.0.0.1:8000/accounts");
    const key = ref(null);
    const userInfo = ref(null);
    const isLogin = computed(() => key.value !== null && key.value !== undefined);
    const basicProfile = ref("http://127.0.0.1:8000/static/accounts/basic_profile.jpg");
    const login = async function (info) {
      try {
        const response = await axios({
          method: "post",
          url: `${Account_URL.value}/login/`,
          data: {
            ...info,
          },
        });
        key.value = response.data.key;
        userInfo.value = response.data.user;
        // console.log(response.data.user);
        return true;
      } catch (e) {
        // console.log(e);
        return false;
      }
    };

    const logout = function () {
      key.value = null;
      userInfo.value = null;
    };

    const signup = async function (info) {
      try {
        const response = await axios({
          method: "post",
          url: `${Account_URL.value}/signup/`,
          data: {
            ...info,
          },
        });
        key.value = response.data.key;
        userInfo.value = response.data.user;
        // console.log(response);
        return true;
      } catch (e) {
        // console.log(e);
        return false;
      }
    };

    const updateProfile = async function (user_pk, image) {
      try {
        const response = await axios({
          method: "post",
          url: `${Account_URL.value}/update/profileImageUpdate/${user_pk}/`,
          data: image,
          headers: {
            Authorization: `Token ${key.value}`,
            "Content-Type": "multipart/form-data",
          },
        });
        userInfo.value.image = `http://127.0.0.1:8000${response.data.image}`;
        return response;
      } catch (e) {
        return e;
      }
    };

    const updateInfo = async function (user_pk, info) {
      try {
        const response = await axios({
          method: "patch",
          url: `${Account_URL.value}/update/profileInfoUpdate/${user_pk}/`,
          data: info,
          headers: {
            Authorization: `Token ${key.value}`,
          },
        });

        for (const key in info) {
          userInfo.value[key] = info[key];
        }
        return true;
      } catch (e) {
        window.alert("에러");
        return false;
      }
    };

    const profileImage = computed(() => {
      if (
        !isLogin.value ||
        userInfo.value == null ||
        userInfo.value.image === undefined ||
        userInfo.value.image === null ||
        userInfo.value.image === ""
      ) {
        return "http://127.0.0.1:8000/static/accounts/basic_profile.jpg";
      } else return userInfo.value.image;
    });

    return { key, userInfo, login, isLogin, logout, signup, basicProfile, updateProfile, profileImage, updateInfo };
  },
  { persist: true }
);
