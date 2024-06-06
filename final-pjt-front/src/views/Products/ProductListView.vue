<template>
  <div class="container">
    <h1 class="text-center my-4">금융상품 리스트</h1>

    <section class="me-3 mt-3 mb-5 w-25">
      <h4>은행 선택</h4>
      <select class="form-select" aria-label="Default select example" v-model="select_bank">
        <option selected value="0">All</option>
        <option value="0010001">우리은행</option>
        <option value="0010002">한국스탠다드차타드은행</option>
        <option value="0010016">대구은행</option>
        <option value="0010017">부산은행</option>
        <option value="0010019">광주은행</option>
        <option value="0010020">제주은행</option>
        <option value="0010022">전북은행</option>
        <option value="0010024">경남은행</option>
        <option value="0010026">중소기업은행</option>
        <option value="0010030">한국산업은행</option>
        <option value="0010927">국민은행</option>
        <option value="0011625">신한은행</option>
        <option value="0013175">농협은행주식회사</option>
        <option value="0013909">하나은행</option>
        <option value="0014674">주식회사 케이뱅크</option>
        <option value="0014807">수협은행</option>
        <option value="0015130">주식회사 카카오뱅크</option>
        <option value="0017801">토스뱅크 주식회사</option>
      </select>
    </section>

    <ul class="nav nav-tabs">
      <li class="nav-item">
        <a class="nav-link" :class="{ active: activeTab === 0 }" @click="selectTab(0, 'deposit')">예금</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" :class="{ active: activeTab === 1 }" @click="selectTab(1, 'saving')">적금</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" :class="{ active: activeTab === 2 }" @click="selectTab(2, 'jeonse_loan')">전세대출</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" :class="{ active: activeTab === 3 }" @click="selectTab(3, 'mortgage_loan')">주택담보대출</a>
      </li>
    </ul>
    <div class="tab-content">
      <div class="tab-pane fade" :class="{ 'show active': activeTab === 0 }">
        <button @click="openingModal" v-if="!loading" class="btn btn-primary">
          <span>{{ opening ? "목록 보기" : "금리 한 눈에 보기" }}</span>
        </button>
        <modal v-show="opening" @close="openingModal">
          <DetailChart :products="products" />
        </modal>
        <Transition name="slide-fade">
          <DepositList :products="products" :loading="loading" :bank_filter="select_bank" />
        </Transition>
      </div>
      <div class="tab-pane fade" :class="{ 'show active': activeTab === 1 }">
        <button @click="openingModal" v-if="!loading" class="btn btn-primary">
          <span>{{ opening ? "목록 보기" : "금리 한 눈에 보기" }}</span>
        </button>
        <modal v-show="opening" @close="openingModal">
          <DetailChart :products="products" />
        </modal>

        <Transition name="slide-fade">
          <SavingList :products="products" :loading="loading" :bank_filter="select_bank" />
        </Transition>
      </div>
      <div class="tab-pane fade" :class="{ 'show active': activeTab === 2 }">
        <button @click="openingModal" v-if="!loading" class="btn btn-primary">
          <span>{{ opening ? "목록 보기" : "금리 한 눈에 보기" }}</span>
        </button>
        <modal v-show="opening" @close="openingModal">
          <DetailChartLoan :products="products" />
        </modal>

        <Transition name="slide-fade">
          <JeonseList :products="products" :loading="loading" :bank_filter="select_bank" />
        </Transition>
      </div>
      <div class="tab-pane fade" :class="{ 'show active': activeTab === 3 }">
        <button @click="openingModal" v-if="!loading" class="btn btn-primary">
          <span>{{ opening ? "목록 보기" : "금리 한 눈에 보기" }}</span>
        </button>
        <modal v-show="opening" @close="openingModal">
          <DetailChartLoan :products="products" />
        </modal>

        <Transition name="slide-fade">
          <MortgageList :products="products" :loading="loading" :bank_filter="select_bank" />
        </Transition>
      </div>
    </div>
  </div>
</template>

<script setup>
import axios from "axios";
import { onMounted, ref } from "vue";
import DepositList from "@/components/Product/DepositList.vue";
import SavingList from "@/components/Product/SavingList.vue";
import JeonseList from "@/components/Product/JeonseList.vue";
import MortgageList from "@/components/Product/MortgageList.vue";
import DetailChart from "@/components/Product/DetailChart.vue";
import DetailChartLoan from "@/components/Product/DetailChartLoan.vue";
import Modal from "@/components/Product/Modal.vue";

const opening = ref(false);
const openingModal = () => {
  opening.value = !opening.value;
};

const products = ref([]);
const activeTab = ref(0);
const loading = ref(true);
const select_bank = ref(0);

const fetchProducts = async (type) => {
  loading.value = true;
  try {
    const response = await axios.get(`http://127.0.0.1:8000/products/${type}/`);
    console.log(response.data);
    products.value = response.data.new_products;
  } catch (error) {
    console.error("Error fetching products:", error);
  } finally {
    loading.value = false;
  }
};

const selectTab = (index, type) => {
  activeTab.value = index;
  fetchProducts(type);
};

onMounted(() => {
  fetchProducts("deposit");
});
</script>

<style>
.nav-link {
  cursor: pointer;
}

.slide-fade-enter-active {
  transition: all 0.3s ease-out;
}

.slide-fade-leave-active {
  transition: all 0.3s cubic-bezier(1, 0.5, 0.8, 1);
}

.slide-fade-enter-from,
.slide-fade-leave-to {
  transform: translateX(20px);
  opacity: 0;
}
</style>
