import { ref } from 'vue';
import { defineStore } from 'pinia';
import axios from 'axios';

export const useCounterStore = defineStore('counter', () => {
  const rates = ref({});
  const API_URL = 'https://quotation-api-cdn.dunamu.com/v1/forex/recent?codes=FRX.KRW';

  const getRates = (currencyCode) => {
    axios({
      method: 'get',
      url: `${API_URL}${currencyCode}`
    })
      .then(response => {
        const data = response.data[0];
        rates.value = data;  // 모든 데이터를 저장
      })
      .catch(error => {
        console.log(error);
      });
  };

  return { rates, API_URL, getRates };
}, { persist: true });

