<template>
  <header>
    <Navbar />
    <Carousel />
  </header>

  <main>
    <RouterView v-slot="{ Component }">
      <Transition name="fade">
        <component :is="Component" />
      </Transition>
    </RouterView>
  </main>

  <Footer />
</template>

<script setup>
import { computed } from "vue";
import { useRoute } from "vue-router";
import Navbar from "@/components/Navbar.vue";
import Carousel from "@/components/Carousel.vue";
import Footer from "@/components/Footer.vue";

// 현재 라우트 경로를 확인하여 홈 페이지 여부를 판단
const route = useRoute();
const isHomePage = computed(() => route.path === "/");
</script>

<style scoped>
main {
  padding: 20px;
}

.fade-enter-active {
  transition: all 0.3s ease-out;
}

.fade-leave-active {
  transition: all 0.3s cubic-bezier(1, 0.5, 0.8, 1);
}

.fade-enter-from {
  transform: translateY(-20px);
  opacity: 0;
}

.fade-leave-to {
  transform: translateY(-20px);
  opacity: 0;
}
</style>
