<template>
  <section>
    <form @submit.prevent="showSubscribeModal">
      <div class="row d-flex justify-content-center">
        <div class="col-auto">
          <p class="pt-2">
            <strong>Sign up for our newsletter</strong>
          </p>
        </div>
        <div class="col-md-5 col-12">
          <div class="form-outline form-white mb-4">
            <input type="email" v-model="email" id="form5Example2" class="form-control" required />
            <label class="form-label" for="form5Example2">Email address</label>
          </div>
        </div>
        <div class="col-auto">
          <button type="submit" class="btn btn-outline-light mb-4">Subscribe</button>
        </div>
      </div>
    </form>

    <!-- Subscribe Modal -->
    <transition name="modal">
      <div class="modal" tabindex="-1" :class="{ show: showModal }" v-if="showModal">
        <div class="modal-dialog animate__animated animate__zoomIn">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title">구독 확인</h5>
              <button type="button" class="btn-close" @click="closeModal"></button>
            </div>
            <div class="modal-body">
              <img src="@/assets/img/logo.png" alt="">
              <p>더 풍요로운 삶을 위한 금융 가이드 <br> Finance Navigator를 구독하시겠습니까?</p>
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-secondary" @click="closeModal">취소</button>
              <button type="button" class="btn btn-primary" @click="subscribe">구독</button>
            </div>
          </div>
        </div>
      </div>
    </transition>
  </section>
</template>

<script setup>
import { ref } from 'vue';
import axios from 'axios';

const email = ref('');
const showModal = ref(false);

const showSubscribeModal = () => {
  showModal.value = true;
};

const closeModal = () => {
  showModal.value = false;
};

const subscribe = async () => {
  closeModal();
  try {
    await sendSubscriptionEmail(email.value);
    alert('구독해주셔서 감사합니다!');
  } catch (error) {
    console.error('Failed to subscribe:', error);
    alert('구독에 실패했습니다. 다시 시도해주세요.');
  }
};

const sendSubscriptionEmail = async (email) => {
  await axios.post('http://localhost:8000/subscribe/', { email });
};
</script>

<style scoped>
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

.modal-title {
  text-align: justify;
  color: blue;
  font-weight: 600;
}

.modal-dialog {
  position: relative;
  margin: 10% auto;
  max-width: 500px;
  width: auto;
}

.modal-content {
  color: black;
  font-weight: 600;
}
</style>
