<template>
  <div class="modal-overlay" @click.self="close">
    <div class="modal-content">
      <button class="close-button me-2 my-3" @click="close">닫기</button>
      <slot></slot>
    </div>
  </div>
</template>

<script setup>
import { defineEmits } from "vue";

const emit = defineEmits(["close"]);

const close = () => {
  emit("close");
};
</script>

<style scoped>
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000; /* 모달을 최상위에 표시 */
}

.modal-content {
  background: white;
  padding: 20px;
  border-radius: 10px;
  position: relative;
  z-index: 1001; /* 컨텐츠가 오버레이보다 앞에 표시 */
  width: 50%; /* 모달의 너비를 줄입니다. */
  max-width: 500px; /* 최대 너비 설정 */
  margin: 0 20px; /* 양쪽에 여백 추가 */
}

.close-button {
  position: absolute;
  top: 10px;
  right: 10px;
  background: none;
  border: none;
  font-size: 16px; /* 폰트 크기 줄이기 */
  cursor: pointer;
  padding: 0; /* 버튼 내부 여백 없애기 */
}
</style>
