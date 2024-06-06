<template>
  <section class="exchange-result-section">
    <div v-if="rates?.ttBuyingPrice" class="exchange-card">
      <div class="card text-center">
        <div class="card-header">
          <img :src="getFlagUrl(rates.currencyCode)" alt="국기" class="flag-icon" /> {{ rates.currencyCode }} &#8594;
          <img :src="getFlagUrl(base)" alt="국기" class="flag-icon" /> {{ base }}
        </div>
        <div class="card-body">
          <div class="card-text">
            <p class="font-sizeup">{{ amount }} {{ rates.currencyCode }}</p>
            <p>&#8594;</p>
            <span class="font-sizeup">{{ (amount * rates.ttBuyingPrice).toFixed(3) }} {{ base }}</span>
          </div>
        </div>
      </div>
    </div>
    <br />
    <div v-if="rates?.ttSellingPrice" class="exchange-card">
      <div class="card text-center">
        <div class="card-header">
          <img :src="getFlagUrl(base)" alt="국기" class="flag-icon" /> {{ base }} &#8594;
          <img :src="getFlagUrl(rates.currencyCode)" alt="국기" class="flag-icon" /> {{ rates.currencyCode }}
        </div>
        <div class="card-body">
          <div class="card-text">
            <p class="font-sizeup">{{ amount }} {{ base }}</p>
            <p>&#8594;</p>
            <span class="font-sizeup">{{ (amount / rates.ttBuyingPrice).toFixed(3) }} {{ rates.currencyCode }}</span>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, defineProps } from "vue";

const props = defineProps({
  amount: {
    type: [String, Number],
    required: true,
  },
  rates: {
    type: Object,
    default: () => ({}),
  },
  currencyCode: {
    type: String,
  },
});

const base = ref("KRW");

const getFlagUrl = (code) => {
  const countryMapping = {
    USD: "us",
    JPY: "jp",
    EUR: "eu",
    GBP: "gb",
    CAD: "ca",
    AUD: "au",
    NZD: "nz",
    HKD: "hk",
    SGD: "sg",
    VND: "vn",
    MXN: "mx",
    BRL: "br",
    TRY: "tr",
    KRW: "kr",
  };
  return `https://flagcdn.com/16x12/${countryMapping[code]}.png`;
};
</script>

<style scoped>
.exchange-result-section {
  max-width: 600px;
  margin: 0 auto;
}

.exchange-card {
  background-color: #ffffff;
  border: 1px solid #e0e0e0;
  border-radius: 10px;
  padding: 20px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.card-header {
  font-size: 1.25rem;
  font-weight: bold;
  color: #007bff;
  border-bottom: 1px solid #e0e0e0;
  padding-bottom: 10px;
}

.card-header .flag-icon {
  margin-right: 8px;
}

.card-text {
  font-size: 1rem;
  color: #333333;
}

.font-sizeup {
  font-size: 1.5rem;
  color: #007bff;
  font-weight: bold;
}

.card-body p {
  margin: 0;
  font-size: 1.25rem;
}
</style>
