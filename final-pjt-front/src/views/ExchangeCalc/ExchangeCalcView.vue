<template>
  <div>
    <h1>환율계산기</h1>
    <section class="mx-3 mt-3">
      <ExchangeCalcForm v-model:currencyCode="currencyCode" v-model:amount="amount" />
      <ExchangeCalcFormResult :amount="amount" />
    </section>
  </div>
</template>

<script setup>
import { ref } from "vue";
import ExchangeCalcForm from "@/components/ExchangeCalc/ExchangeCalcForm.vue";
import ExchangeCalcFormResult from "@/components/ExchangeCalc/ExchangeCalcFormResult.vue";

const currencyCode = ref("USD");
const amount = ref(0);
</script>

<style scoped></style>
