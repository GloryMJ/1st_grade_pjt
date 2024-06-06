import HomeView from "@/views/HomeView.vue";
import BoardView from "@/views/Board/BoardView.vue";
import AccountView from "@/views/accounts/AccountView.vue";
import ProfileView from "@/views/accounts/ProfileView.vue";
import CreateBoard from "@/views/Board/CreateBoard.vue";
import BoardDetailView from "@/views/Board/BoardDetailView.vue";
import BoardFix from "@/views/Board/BoardFix.vue";
import ProfileFix from "@/views/accounts/ProfileFix.vue";
import ExchangeCalcView from "@/views/ExchangeCalc/ExchangeCalcView.vue";
import BankSearchView from "@/views/BankSearch/BankSearchView.vue";
import ProductListView from "@/views/Products/ProductListView.vue";
import ProductRecommendView from "@/views/Products/ProductRecommendView.vue";
import DetailView from "@/views/Products/DetailView.vue";

import { createRouter, createWebHistory } from "vue-router";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "Home",
      component: HomeView,
    },
    {
      path: "/board",
      name: "board",
      component: BoardView,
    },
    {
      path: "/account",
      name: "account",
      component: AccountView,
    },
    {
      path: "/profile",
      name: "profile",
      component: ProfileView,
    },
    {
      path: "/create-board",
      name: "createBoard",
      component: CreateBoard,
    },
    {
      path: "/detail-article/:article_id",
      name: "boardDetail",
      component: BoardDetailView,
    },
    {
      path: "/fix-board/:article_id",
      name: "fix-board",
      component: BoardFix,
    },
    {
      path: "/fix-profile",
      name: "fix-profile",
      component: ProfileFix,
    },
    {
      path: "/exchangecalc",
      name: "exchangecalc",
      component: ExchangeCalcView,
    },
    {
      path: "/banksearch",
      name: "banksearch",
      component: BankSearchView,
    },
    {
      path: "/productlist",
      name: "productlist",
      component: ProductListView,
    },
    {
      path: "/product-recommend",
      name: "productrecommend",
      component: ProductRecommendView,
    },
    {
      path: "/product-detail/:productId",
      name: "detailview",
      component: DetailView,
    },
  ],
});

export default router;
