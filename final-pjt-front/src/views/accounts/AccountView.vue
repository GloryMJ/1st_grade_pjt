<template>
  <div>
    <div class="container" id="container" :class="{ 'right-panel-active': rightPanelActive }">
      <div class="form-container sign-up-container">
        <form @submit.prevent="signupEvent" ref="signupref">
          <h1>회원가입</h1>
          <input type="email" placeholder="이메일" name="email" required />
          <input type="password" placeholder="비밀번호" name="password1" required />
          <input type="password" placeholder="입력한 비밀번호를 다시 입력하세요" name="password2" required />
          <input type="text" placeholder="이름" name="name" required />
          <input type="text" placeholder="닉네임" name="nickname" required />
          <div class="form-group-inline">
            <div>
              <label for="gender">성별</label>
              <select name="gender" id="gender" class="form-select form-select mb-3">
                <option value="1">남자</option>
                <option value="2">여자</option>
              </select>
            </div>
            <div>
              <label for="age_group">연령대</label>
              <select name="age_group" id="age_group" class="form-select form-select mb-3">
                <option value="10">10대</option>
                <option value="20">20대</option>
                <option value="30">30대</option>
                <option value="40">40대</option>
                <option value="50">50대</option>
                <option value="60">60대</option>
                <option value="70">70대</option>
                <option value="80">80대</option>
              </select>
            </div>
          </div>
          <input type="submit" value="회원가입" class="button-design" />
          <p v-show="signupState === 1" style="color: red">
            <b>이메일 혹은 닉네임이 이미 사용되었습니다. 다른 정보로 시도해 주세요!</b>
          </p>
        </form>
      </div>
      <div class="form-container sign-in-container">
        <form @submit.prevent="loginEvent">
          <h1>로그인</h1>
          <input type="email" placeholder="Email" name="email" :value="signupEmail.value" required />
          <input type="password" placeholder="Password" name="password" :value="signupPassword.value" required />
          <input type="submit" value="로그인" class="button-design" />
          <p v-show="loginFail" style="color: red"><b>로그인에 실패했습니다. 다시 한번 더 해주세요!</b></p>
        </form>
      </div>
      <div class="overlay-container">
        <div class="overlay">
          <div class="overlay-panel overlay-left">
            <h1>계정이 있으신가요?</h1>
            <p>로그인 해서 더 많은 기능을 이용해 보세요!</p>
            <button class="ghost" id="signIn" @click="rightPanelActive = !rightPanelActive">로그인 하기</button>
          </div>
          <div v-if="signupState <= 1" class="overlay-panel overlay-right">
            <h1>처음인가요?</h1>
            <p>회원가입해서 더 많은 기능을 이용해 보세요</p>
            <button class="ghost" id="signUp" @click="rightPanelActive = !rightPanelActive">회원 가입</button>
          </div>
          <div v-else class="overlay-panel overlay-right">
            <h1>환영합니다!</h1>
            <p>한번 더 로그인을 해 주세요</p>
            <!-- <button class="ghost" id="signUp" @click="rightPanelActive = !rightPanelActive">회원 가입</button> -->
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref } from "vue";
import axios from "axios";
import { useAccountStore } from "@/stores/account";
import { useRoute, useRouter } from "vue-router";
const route = useRoute();
const router = useRouter();

const accountStore = useAccountStore();

const rightPanelActive = ref(false);
const loginFail = ref(false);
const signupState = ref(0);
const signupEmail = ref("");
const signupPassword = ref("");
const signupref = ref(null);

const loginEvent = function (event) {
  const loginForm = new FormData(event.target);
  const info = {};
  loginForm.forEach((value, key) => {
    info[key] = value;
  });
  accountStore.login(info).then((res) => {
    if (res === false) {
      loginFail.value = true;
    } else {
      router.push({ name: "Home" });
    }
  });
};

const signupEvent = function (event) {
  const signUpForm = new FormData(event.target);
  const info = {};
  signUpForm.forEach((value, key) => {
    info[key] = value;
  });
  accountStore.signup(info).then((res) => {
    console.log(res);
    if (res === false) {
      signupState.value = 1;
    } else {
      signupEmail.value = info.email;
      signupPassword.value = info.password1;
      rightPanelActive.value = false;
      signupState.value = 2;
      loginFail.value = false;

      signupref.value.reset();

      // 로그인 폼으로 이동한 후 이메일과 비밀번호 설정
      setTimeout(() => {
        const emailInput = document.querySelector('.sign-in-container input[name="email"]');
        const passwordInput = document.querySelector('.sign-in-container input[name="password"]');
        if (emailInput) emailInput.value = signupEmail.value;
        if (passwordInput) passwordInput.value = signupPassword.value;
      }, 0);
    }
  });
};

onMounted(() => {
  if (accountStore.isLogin) router.push({ name: "Home" });
});
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css?family=Montserrat:400,800");

* {
  box-sizing: border-box;
}

body {
  background: #f6f5f7;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  font-family: "Montserrat", sans-serif;
  height: 100vh;
  margin: -20px 0 50px;
}

h1 {
  font-weight: bold;
  margin: 0;
}

h2 {
  text-align: center;
}

p {
  font-size: 14px;
  font-weight: 100;
  line-height: 20px;
  letter-spacing: 0.5px;
  margin: 20px 0 30px;
}

span {
  font-size: 12px;
}

a {
  color: #333;
  font-size: 14px;
  text-decoration: none;
  margin: 15px 0;
}

button {
  border-radius: 20px;
  border: 1px solid #ff4b2b;
  background-color: #ff4b2b;
  color: #ffffff;
  font-size: 12px;
  font-weight: bold;
  padding: 12px 45px;
  letter-spacing: 1px;
  text-transform: uppercase;
  transition: transform 80ms ease-in;
}

.button-design {
  border-radius: 20px;
  border: 1px solid #ff4b2b;
  background-color: #ff4b2b;
  color: #ffffff;
  font-size: 12px;
  font-weight: bold;
  padding: 12px 45px;
  letter-spacing: 1px;
  text-transform: uppercase;
  transition: transform 80ms ease-in;
}

.button-design:focus {
  outline: none;
}

.button-design:active {
  transform: scale(0.95);
}

.button-design:hover {
  transform: scale(1.02);
}

button:active {
  transform: scale(0.95);
}

button:focus {
  outline: none;
}

button.ghost {
  background-color: transparent;
  border-color: #ffffff;
}

form {
  background-color: #ffffff;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  padding: 0 50px;
  height: 100%;
  text-align: center;
}

input {
  background-color: #eee;
  border: none;
  padding: 12px 15px;
  margin: 8px 0;
  width: 100%;
}

.container {
  background-color: #fff;
  border-radius: 10px;
  box-shadow: 0 14px 28px rgba(0, 0, 0, 0.25), 0 10px 10px rgba(0, 0, 0, 0.22);
  position: relative;
  overflow: hidden;
  width: 900px;
  max-width: 100%;
  min-height: 650px;
}

.form-container {
  position: absolute;
  top: 0;
  height: 100%;
  transition: all 0.6s ease-in-out;
}

.sign-in-container {
  left: 0;
  width: 50%;
  z-index: 2;
}

.container.right-panel-active .sign-in-container {
  transform: translateX(100%);
}

.sign-up-container {
  left: 0;
  width: 50%;
  opacity: 0;
  z-index: 1;
}

.container.right-panel-active .sign-up-container {
  transform: translateX(100%);
  opacity: 1;
  z-index: 5;
  animation: show 0.6s;
}

@keyframes show {
  0%,
  49.99% {
    opacity: 0;
    z-index: 1;
  }

  50%,
  100% {
    opacity: 1;
    z-index: 5;
  }
}

.form-group-inline {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.form-group-inline > div {
  flex: 1;
  margin-right: 10px; /* 필요에 따라 조정 */
}

.form-group-inline > div:last-child {
  margin-right: 0;
}

.overlay-container {
  position: absolute;
  top: 0;
  left: 50%;
  width: 50%;
  height: 100%;
  overflow: hidden;
  transition: transform 0.6s ease-in-out;
  z-index: 100;
}

.container.right-panel-active .overlay-container {
  transform: translateX(-100%);
}

.overlay {
  background: #ff416c;
  background: -webkit-linear-gradient(to right, #ff4b2b, #ff416c);
  background: linear-gradient(to right, #ff4b2b, #ff416c);
  background-repeat: no-repeat;
  background-size: cover;
  background-position: 0 0;
  color: #ffffff;
  position: relative;
  left: -100%;
  height: 100%;
  width: 200%;
  transform: translateX(0);
  transition: transform 0.6s ease-in-out;
}

.container.right-panel-active .overlay {
  transform: translateX(50%);
}

.overlay-panel {
  position: absolute;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  padding: 0 40px;
  text-align: center;
  top: 0;
  height: 100%;
  width: 50%;
  transform: translateX(0);
  transition: transform 0.6s ease-in-out;
}

.overlay-left {
  transform: translateX(-20%);
}

.container.right-panel-active .overlay-left {
  transform: translateX(0);
}

.overlay-right {
  right: 0;
  transform: translateX(0);
}

.container.right-panel-active .overlay-right {
  transform: translateX(20%);
}

.social-container {
  margin: 20px 0;
}

.social-container a {
  border: 1px solid #dddddd;
  border-radius: 50%;
  display: inline-flex;
  justify-content: center;
  align-items: center;
  margin: 0 5px;
  height: 40px;
  width: 40px;
}

footer {
  background-color: #222;
  color: #fff;
  font-size: 14px;
  bottom: 0;
  position: fixed;
  left: 0;
  right: 0;
  text-align: center;
  z-index: 999;
}

footer p {
  margin: 10px 0;
}

footer i {
  color: red;
}

footer a {
  color: #3c97bf;
  text-decoration: none;
}
</style>
