<template>
  <div>
    <div v-if="!loading">
      <div class="card my-4">
        <div class="card-body">
          <div class="row row-cols-1 row-cols-md-2 row-cols-lg-4">
            <template v-for="colitem in column" :key="colitem">
              <div class="col">
              <div class="d-felx flex-column justify-content-center align-items-center mx-5 text-center">
                <p>{{ Optionsname[colitem] }}</p>
                <p>{{ props.info[colitem] }}</p>
              </div>
            </div>
            </template>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
const loading = ref(false);
const props = defineProps({
  info: Object,
  bank_type: {
    type: [String, Number],
  },
});
const column = ref([]);
onMounted(() => {
  for (let key in props.info) {
    if (key in Optionsname && props.info[key]) column.value.push(key);
  }
  // console.log(props.info);
  loading.value != loading.value;
});

const Optionsname = {
  intr_rate_type: "저축 금리 유형",
  intr_rate_type_nm: "저축 금리 유형명",
  save_trm: "저축 기간 [개월]",
  intr_rate: "저축 금리 [%]",
  intr_rate2: "최고 우대금리 [%]",
  rsrv_type: "적립 유형",
  rsrv_type_nm: "적립 유형명",

  mrtg_type_nm: "담보유형",
  rpay_type_nm: "대출상환유형",
  lend_rate_type_nm: "대출금리유형",
  lend_rate_min: "대출금리 최저",
  lend_rate_max: "대출금리 최고",
  lend_rate_avg: " 전월취급평균금리",
};
</script>

<style lang="scss" scoped></style>
