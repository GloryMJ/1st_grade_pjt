<template>
  <div>
    <div class="section-wrapper">
      <Introduction />
    </div>
    <div class="section-wrapper">
      <Suggestion />
    </div>
    <div class="section-wrapper information">
      <Information />
    </div>
  </div>
</template>

<script setup>
import Introduction from "@/components/Homepage/Introduction.vue";
import Suggestion from "@/components/Homepage/Suggestion.vue";
import Information from "@/components/Homepage/Information.vue";
</script>

<style scoped>
.section-wrapper {
  margin-bottom: 50px;
}

.information {
  background-color: rgb(231, 249, 250);
}
</style>
