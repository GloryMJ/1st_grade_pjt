<template>
  <section class="info-section text-center animate-fade-in">
    <h2 class="info-title">미리 알아두면 좋은 정보</h2>
    <div class="info-boxes">
      <div class="info-box">
        <div class="info-text">
          <h3>대출금리?</h3>
          <p>
            대출금리!
            <br />
            아는 만큼 선택이 쉬워집니다!
          </p>
        </div>
        <a href="https://portal.kfb.or.kr/compare/loan.php" target="_blank">
          <img src="@/assets/img/loan.png" alt="대출 이미지" class="info-image" />
        </a>
      </div>
      <div class="info-box">
        <div class="info-text">
          <h3>예금금리?</h3>
          <p>
            예금금리!
            <br />
            아는 만큼 혜택이 커집니다!
          </p>
        </div>
        <a href="https://portal.kfb.or.kr/compare/receiving.php" target="_blank">
          <img src="@/assets/img/bankbook.png" alt="예금 이미지" class="info-image" />
        </a>
      </div>
      <div class="info-box">
        <div class="info-text">
          <h3>은행수수료?</h3>
          <p>
            은행 수수료!
            <br />
            아는 만큼 절약됩니다!
          </p>
        </div>
        <a href="https://portal.kfb.or.kr/compare/commission.php" target="_blank">
          <img src="@/assets/img/fee.png" alt="수수료 이미지" class="info-image" />
        </a>
      </div>
    </div>
  </section>
</template>

<script setup></script>

<style scoped>
.info-section {
  background-color: #f5f7fa;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  margin-top: 20px;
  animation: fadeIn 1s ease-in;
}

.info-title {
  font-size: 1.75rem;
  font-weight: bold;
  color: #007bff;
  margin-bottom: 20px;
}

.info-boxes {
  display: flex;
  justify-content: space-around;
  gap: 20px; /* 박스 사이의 간격 추가 */
}

.info-box {
  background-color: #ffffff;
  border: 1px solid #e0e0e0;
  border-radius: 10px;
  padding: 20px;
  width: 30%;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  display: flex; /* Flexbox 사용 */
  align-items: center; /* 수직 중앙 정렬 */
  justify-content: space-between; /* 공간을 양쪽에 나누어 줌 */
  transition: transform 0.3s, box-shadow 0.3s;
}

.info-box:hover {
  transform: translateY(-5px);
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

.info-box h3 {
  font-size: 1.25rem;
  color: #333;
  margin-bottom: 10px;
}

.info-box p {
  font-size: 0.875rem;
  color: #666;
}

.info-image {
  max-width: 70px;
  height: auto;
  margin-left: 20px;
}

.chatbot-msg {
  font-weight: bold;
  margin: 1rem;
  padding: 10px 20px;
  background-color: #007bff;
  color: #ffffff;
  border-radius: 5px;
  transition: background-color 0.3s;
}

.chatbot-msg:hover {
  background-color: #0056b3;
}

/* 애니메이션 */
@keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

.animate-fade-in {
  animation: fadeIn 1s ease-in;
}
</style>
