<template>
  <div class="exchange-form-container">
    <div class="exchange-form border border-dark rounded-3 shadow p-4 mb-5">
      <label for="call" class="label-font">통화 선택</label>
      <select id="call" v-model="currencyCode" @change="fetchRates" class="form-select">
        <option v-for="call in calls" :key="call.id" :value="call.code">
          <img :src="getFlagUrl(call.code)" alt="국기" class="flag-icon" /> {{ call.code }}
        </option>
      </select>
      <br />
      <label for="amount" class="label-font">현지 통화 혹은 한국금액(원) 입력</label>
      <input id="amount" type="number" v-model.number="amount" class="form-control" />
    </div>
    <ExchangeCalcFormResult :amount="amount" :rates="rates" :currencyCode="currencyCode" />
  </div>
</template>

<script setup>
import { ref, onMounted, computed, watch } from "vue";
import { useCounterStore } from "@/stores/counter";
import ExchangeCalcFormResult from "@/components/ExchangeCalc/ExchangeCalcFormResult.vue";

let id = 0;
const calls = ref([
  { id: id++, code: "USD", country: "us" },
  { id: id++, code: "JPY", country: "jp" },
  { id: id++, code: "EUR", country: "eu" },
  { id: id++, code: "GBP", country: "gb" },
  { id: id++, code: "CAD", country: "ca" },
  { id: id++, code: "AUD", country: "au" },
  { id: id++, code: "NZD", country: "nz" },
  { id: id++, code: "HKD", country: "hk" },
  { id: id++, code: "SGD", country: "sg" },
  { id: id++, code: "VND", country: "vn" },
  { id: id++, code: "MXN", country: "mx" },
  { id: id++, code: "BRL", country: "br" },
  { id: id++, code: "TRY", country: "tr" },
]);

const store = useCounterStore();
const currencyCode = ref(calls.value[0].code);
const amount = ref(0);
const rates = computed(() => store.rates);

const fetchRates = () => {
  store.getRates(currencyCode.value);
};

const getFlagUrl = (code) => {
  const country = calls.value.find((call) => call.code === code).country;
  return `https://flagcdn.com/16x12/${country}.png`;
};

onMounted(() => {
  fetchRates();
});

watch(currencyCode, () => {
  fetchRates();
});
</script>

<style scoped>
.exchange-form-container {
  max-width: 600px;
  margin: 0 auto;
}

.exchange-form {
  background-color: #ffffff;
  border: 1px solid #e0e0e0;
  border-radius: 10px;
  padding: 20px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.label-font {
  font-size: 1.25rem;
  color: #333333;
  margin-bottom: 10px;
}

.form-select,
.form-control {
  font-size: 1rem;
  padding: 10px;
  border: 1px solid #ced4da;
  border-radius: 5px;
  transition: border-color 0.3s;
}

.form-select:focus,
.form-control:focus {
  border-color: #007bff;
  outline: none;
  box-shadow: 0 0 5px rgba(0, 123, 255, 0.25);
}

.form-select option {
  display: flex;
  align-items: center;
}

.flag-icon {
  width: 16px;
  height: 12px;
  margin-right: 8px;
}

.form-control {
  margin-bottom: 15px;
}
</style>
