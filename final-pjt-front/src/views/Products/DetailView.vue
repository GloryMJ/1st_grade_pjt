<template>
  <div class="container">
    <div class="row">
      <!-- 좌상단 -->
      <div class="col-md-6">
        <div class="card text-center card-event ">
          <div class="card-header">
            <label v-if="product" class="label-font"> {{ product.product_pk }}</label>
          </div>
          <div class="card-body fs-1">
            <div v-if="product" @click="searchProduct(`${product.bank.kor_co_nm} ${product.fin_prdt_nm}`)">
              <label v-if="product.bank">{{ product.bank.kor_co_nm }}</label><br>
              <label>{{ product.fin_prdt_nm }}</label>
              <hr>
              <label v-if="product.infoproducts[0].intr_rate2">최고 우대 금리: {{ product.infoproducts[0].intr_rate2 }}</label>
              <label v-if="product.infoproducts[0].lend_rate_min">최저 금리: {{ product.infoproducts[0].lend_rate_min }}</label>
            </div>
          </div>
        </div>
        <hr>
        <div v-if="product">  
          <div v-if="product.bank_type == 1 || product.bank_type == 2">
            <div class="col-md-12 mt-3">
              <p v-if="product.join_member">
                <span>가입 대상 안내</span>
                <hr>
                <span>{{ product.join_member }}</span>
              </p>
              <p v-if="product.max_limit">
                <span>가입 한도액 안내</span>
                <hr>
                <span>{{ formatNumber(product.max_limit) }}</span>
              </p>
              <p v-if="product.spcl_cnd">
                <span>우대 조건 안내</span>
                <hr>
                <span>{{ product.spcl_cnd }}</span>
              </p>
              <p v-if="product.mtrt_int">
                <span>상세 조건 안내</span>
                <hr>
                <span>{{ product.mtrt_int }}</span>
              </p>
              <p v-if="product.etc_note">
                <span>기타 유의사항</span>
                <hr>
                <span>{{ product.etc_note }}</span>
              </p>
            </div>
          </div>
          <div v-else-if="product.bank_type == 3 || product.bank_type == 4">
            <div class="col-md-12 mt-3">
              <p v-if="product.loan_lmt">
                <span>대출 한도 안내</span>
                <hr>
                <span>{{ product.loan_lmt }}</span>
              </p>
              <p v-if="product.erly_rate_fee">
                <span>중도상환 수수료 안내</span>
                <hr>
                <span>{{ product.erly_rate_fee }}</span>
              </p>
              <p v-if="product.loan_inci_expn">
                <span>대출 부대비용 안내</span>
                <hr>
                <span>{{ product.loan_inci_expn }}</span>
              </p>
              <p v-if="product.dly_rate">
                <span>연체 이자율 안내</span>
                <hr>
                <span>{{ product.dly_rate }}</span>
              </p>
            </div>
          </div>
        </div>
      </div>
      <!-- 우상단 -->
      <div class="col-md-6">
        <div v-if="product">
          <div class="d-flex flex-column align-items-center">
            <DetailImage :product="product.fin_prdt_nm"/>
            <div class="text-center my-3 w-100" v-if="accountStore.isLogin">
              {{ res }}
              <form @submit.prevent="toggleLike">
                <input type="submit" :value="isjoined ? '해지하기' : '가입하기'" class="btn" :class="{'btn-primary' : !isjoined,  'btn-warning' : isjoined}"/>
              </form>
            </div>
            <div v-else class="my-3">
              <button class="btn btn-light" @click="$router.push({name : 'account'})">로그인 해서 상품 쉽게 가입하기</button>
            </div>
          </div>
        </div>
      </div>
    </div>
<!-- Option 정보 -->
    <section v-if="product && product.infoproducts">
      <h2>이자 관련 정보 목록</h2>
      <div v-for="infoproduct in product.infoproducts">
        <div v-if="filterType( product.bank_type,infoproduct)">
      <DetailOptionsInfo :info="infoproduct" :bank_type="product.bank_type"/>
      </div>
    </div>
    </section>
  </div>
</template>

<script setup>
import { onMounted, ref, computed } from "vue";
import { useRoute, useRouter } from "vue-router";
import { useAccountStore } from "@/stores/account";
import DetailOptionsInfo from "@/components/Product/DetailOptionsInfo.vue";
import axios from "axios";
import DetailImage from '@/components/Product/DetailImage.vue'
const router = useRouter();
const route = useRoute();
const accountStore = useAccountStore();
const res = ref(null);
const product = ref(null);
const isjoined = ref(false)
onMounted(() => {

  axios({
    method: "get",
    url: `http://127.0.0.1:8000/products/${route.params.productId}/detail/`,
  })
    .then((res) => {
      product.value = res.data;
      if (accountStore.isLogin && accountStore.userInfo.like_products.some(e => e==route.params.productId)) {
        isjoined.value = true;
      }
      else {
        isjoined.value=false;
      }
    })
    .catch((e) => {
      window.alert("에러!");
      console.log(e)
      router.go(-1);
    });
  
});

const toggleLike = async function (event) {
axios({
  method: "patch",
  url: `http://127.0.0.1:8000/products/${route.params.productId}/likes/`,
  headers: {
    Authorization: `Token ${accountStore.key}`,
  },
})
  .then((res) => {
    console.log(res)
    if (res.data.result == "add") {
      isjoined.value = true
      accountStore.userInfo.like_products.push(Number(route.params.productId))
      console.log(accountStore.userInfo.like_products)
    }
    else {
      isjoined.value = false
      accountStore.userInfo.like_products.splice(accountStore.userInfo.like_products.findIndex((e) => e ==  route.params.productId), 1)
      console.log(accountStore.userInfo.like_products)
    }
  })
  .catch((e) => {
    window.alert("에러낫쑝!");
  });
};

const formatNumber = (value) => {
  return value.toLocaleString(); 
}

const searchProduct = (searchName) => {
  window.open(`https://search.naver.com/search.naver?query=${searchName}`)
}

const filterType = function (bank_type, info) {
  // console.log(bank_type, info)
  if (bank_type == 1 || bank_type == 2) {
    if (info["intr_rate_type"]!== undefined && info["intr_rate_type"]!== null) return true;
    else return false;
  } else {
    if (info["lend_rate_max"]!== undefined && info["lend_rate_max"]!== null) return true;
    else return false;
  }
};
</script>

<style scoped>
.card-event {
  box-shadow: 0 7px 14px rgba(0, 0, 0, 0.25), 0 5px 5px rgba(0, 0, 0, 0.22);
  cursor: pointer;
  transition: transform;
  transition-duration: 0.1s;
}
.card-event:hover {
  transform: scale(1.01);
}

.card-event:active {
  transform: scale(0.99);
}

p {
  font-size: 14px;
  font-weight: 100;
  line-height: 20px;
  letter-spacing: 0.5px;
  margin: 20px 0 30px;
}

.btn:hover{
  transform: scale(1.01);
}
.btn:active{
  transform: scale(0.99);
}



</style>
