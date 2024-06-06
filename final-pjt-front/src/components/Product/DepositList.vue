<template>
  <div v-if="loading">Loading...</div>
  <div v-else>
    <table class="table table-striped">
      <thead>
        <tr>
          <th>선택</th>
          <th>금융회사 이름</th>
          <th>금융상품 이름</th>
          <th>가입방법</th>
          <th @click="sortTable('intr_rate_type')">저축금리유형</th>
          <th @click="sortTable('intr_rate')">저축금리</th>
          <th @click="sortTable('intr_rate2')">우대금리</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="product in sortedProducts" :key="product.fin_prdt_cd">
          <template v-if="filter_bank(product.bank.fin_co_no)">
            <td><input type="checkbox" @change="toggleSelection(product)" :checked="isSelected(product)" /></td>
            <td>{{ product.bank.kor_co_nm }}</td>
            <td class="bankListItem" @click="detailView(product.product_pk)">{{ product.fin_prdt_nm }}</td>
            <td>{{ product.join_way }}</td>
            <td>{{ product.infoproducts[0].intr_rate_type }}</td>
            <td>{{ product.infoproducts[0].intr_rate }}</td>
            <td>{{ product.infoproducts[0].intr_rate2 }}</td>
          </template>
        </tr>
      </tbody>
    </table>
    <button
      class="btn btn-primary"
      @click="compareProducts"
      :disabled="selectedProducts.length === 0 || selectedProducts.length > 4"
    >
      내가 선택한 상품들 비교하기
    </button>
    <div v-if="showModal" class="modal" tabindex="-1" role="dialog">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">상품 비교</h5>
            <button type="button" class="close" @click="closeModal" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body">
            <table class="table table-bordered">
              <thead>
                <tr>
                  <th>금융회사 이름</th>
                  <th>금융상품 이름</th>
                  <th>가입방법</th>
                  <th>저축금리유형</th>
                  <th>저축금리</th>
                  <th>우대금리</th>
                  <th>상세 페이지</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="product in selectedProducts" :key="product.fin_prdt_cd">
                  <td>{{ product.bank.kor_co_nm }}</td>
                  <td>{{ product.fin_prdt_nm }}</td>
                  <td>{{ product.join_way }}</td>
                  <td>{{ product.infoproducts[0].intr_rate_type }}</td>
                  <td>{{ product.infoproducts[0].intr_rate }}</td>
                  <td>{{ product.infoproducts[0].intr_rate2 }}</td>
                  <td><button @click="goToDetailPage(product.product_pk)" class="btn btn-info">상세 보기</button></td>
                </tr>
              </tbody>
            </table>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" @click="closeModal">닫기</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from "vue";
import { useRoute, useRouter } from "vue-router";

const router = useRouter();
const route = useRoute();
const props = defineProps({
  products: Array,
  loading: Boolean,
  bank_filter: {
    type: [String, Number],
  },
});

const selectedProducts = ref([]);
const showModal = ref(false);
const sortKey = ref("");
const sortOrder = ref("asc");

const filter_bank = (bank_id) => {
  if (props.bank_filter == 0) {
    return true;
  } else {
    return bank_id == props.bank_filter;
  }
};

const detailView = function (productId) {
  router.push({ name: "detailview", params: { productId: productId } });
};

const toggleSelection = (product) => {
  const index = selectedProducts.value.findIndex((p) => p.fin_prdt_cd === product.fin_prdt_cd);
  if (index === -1) {
    if (selectedProducts.value.length < 4) {
      selectedProducts.value.push(product);
    } else {
      alert("4개까지만 선택가능합니다!");
    }
  } else {
    selectedProducts.value.splice(index, 1);
  }
};

const isSelected = (product) => {
  return selectedProducts.value.some((p) => p.fin_prdt_cd === product.fin_prdt_cd);
};

const compareProducts = () => {
  showModal.value = true;
};

const closeModal = () => {
  showModal.value = false;
};

const goToDetailPage = (productId) => {
  closeModal();
  router.push({ name: "detailview", params: { productId: productId } });
};

const sortTable = (key) => {
  if (sortKey.value === key) {
    sortOrder.value = sortOrder.value === "asc" ? "desc" : "asc";
  } else {
    sortKey.value = key;
    sortOrder.value = "asc";
  }
};

const sortedProducts = computed(() => {
  if (!sortKey.value) return props.products;

  const sorted = [...props.products].sort((a, b) => {
    const aValue = a.infoproducts[0][sortKey.value];
    const bValue = b.infoproducts[0][sortKey.value];

    if (sortOrder.value === "asc") {
      return aValue < bValue ? -1 : aValue > bValue ? 1 : 0;
    } else {
      return aValue > bValue ? -1 : aValue < bValue ? 1 : 0;
    }
  });

  return sorted;
});
</script>

<style scoped>
table,
td,
th {
  border-collapse: collapse;
}

th {
  cursor: pointer;
}

.bankListItem {
  cursor: pointer;
}

.modal {
  display: block;
  background: rgba(0, 0, 0, 0.5);
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  overflow: auto;
}

.modal-dialog {
  position: relative;
  margin: 10% auto;
  max-width: 90%;
  width: auto;
}

.modal-content {
  background-color: #fff;
  padding: 20px;
  border: 1px solid #888;
  border-radius: 10px;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.5);
  overflow: hidden;
}

.modal-header,
.modal-body,
.modal-footer {
  padding: 10px 20px;
}

.modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 1px solid #e5e5e5;
}

.modal-title {
  font-size: 1.5rem;
  font-weight: bold;
}

.close {
  font-size: 1.5rem;
  border: none;
  background: none;
}

.modal-body {
  margin-top: 20px;
  padding-top: 0;
  border-top: none;
  overflow-y: auto;
  max-height: 60vh;
}

.modal-footer {
  text-align: right;
  border-top: 1px solid #e5e5e5;
}

.btn {
  padding: 10px 20px;
  border-radius: 5px;
  font-size: 1rem;
  font-weight: bold;
  transition: background-color 0.3s;
}

.btn-secondary {
  background-color: #6c757d;
  color: #fff;
  border: none;
}

.btn-secondary:hover {
  background-color: #5a6268;
}

.btn-info {
  background-color: #17a2b8;
  color: #fff;
  border: none;
}

.btn-info:hover {
  background-color: #138496;
}

.table-responsive {
  display: block;
  width: 100%;
  overflow-x: auto;
}

.table-bordered {
  width: 100%;
  border: 1px solid #dee2e6;
}

.table-bordered th,
.table-bordered td {
  border: 1px solid #dee2e6;
}

.table-bordered th {
  background-color: #f8f9fa;
  text-align: center;
  font-size: 1rem;
  white-space: nowrap;
}

.table-bordered td {
  text-align: center;
  vertical-align: middle;
  font-size: 0.875rem;
  white-space: nowrap;
}

.table-sm td,
.table-sm th {
  padding: 0.3;
}
</style>
