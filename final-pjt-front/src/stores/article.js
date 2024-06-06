import { ref, computed } from "vue";
import { defineStore } from "pinia";
import axios from "axios";
import { useAccountStore } from "./account";
import { useRouter } from "vue-router";

export const useArticleStore = defineStore(
  "article",
  () => {
    const router = useRouter();
    const accountStore = useAccountStore();
    const article_URL = ref("http://127.0.0.1:8000/articles");
    const articles = ref(null);
    const total_articles = ref(0);
    const getArticles = async function () {
      try {
        const response = await axios({
          method: "get",
          url: `${article_URL.value}/list/`,
        });
        articles.value = response.data;
        // console.log(response);
        return true;
      } catch (e) {
        return false;
      }
    };
    const postArticles = async function (info) {
      try {
        const response = await axios({
          method: "post",
          url: `${article_URL.value}/post/`,
          data: {
            ...info,
          },
          headers: {
            Authorization: `Token ${accountStore.key}`,
          },
        });
        return response.data;
      } catch (e) {
        return false;
      }
    };

    const getDetailArticles = async function (article_id) {
      try {
        const response = axios({
          method: "get",
          url: `${article_URL.value}/${article_id}/detail/`,
        });
        return response;
      } catch (e) {
        return false;
      }
    };

    const fixArticles = async function (article_id, formData) {
      try {
        const res = await axios({
          method: "put",
          url: `${article_URL.value}/${article_id}/put/`,
          data: { ...formData },
          headers: {
            Authorization: `Token ${accountStore.key}`,
          },
        });
        router.go(-1);
        return res;
      } catch (e) {
        window.alert("에러 ! 다시 한번 더 하세요");
        // console.log(e);
        router.go(-1);
        return false;
      }
    };

    const deleteArticles = async function (article_id) {
      try {
        const res = await axios({
          method: "delete",
          url: `${article_URL.value}/${article_id}/delete/`,
          headers: {
            Authorization: `Token ${accountStore.key}`,
          },
        });
        router.push({ name: "board" });
        return res;
      } catch (e) {
        window.alert("에러 ! 다시 한번 더 하세요");
        router.push({ name: "board" });
      }
    };

    const deleteComment = async function (article_id, comment_id) {
      try {
        const res = await axios({
          method: "delete",
          url: `${article_URL.value}/${article_id}/comments/${comment_id}/`,
          headers: {
            Authorization: `Token ${accountStore.key}`,
          },
        });
        return res;
      } catch (e) {
        window.alert("에러 ! 다시 한번 더 하세요");
        router.go(-1);
      }
    };

    const updateArticleViewsCount = function (article_id) {
      try {
        const response = axios({
          method: "patch",
          url: `${article_URL.value}/${article_id}/detail/`,
        });
        return response;
      } catch (e) {
        return false;
      }
    };

    return {
      article_URL,
      articles,
      total_articles,
      getArticles,
      postArticles,
      getDetailArticles,
      fixArticles,
      deleteArticles,
      deleteComment,
      updateArticleViewsCount,
    };
  },
  { persist: true }
);
