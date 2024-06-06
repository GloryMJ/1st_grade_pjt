<template>
  <div id="carouselExampleIndicators" class="carousel slide" data-bs-ride="carousel">
    <div class="carousel-indicators">
      <button
        type="button"
        data-bs-target="#carouselExampleIndicators"
        data-bs-slide-to="0"
        class="active"
        aria-current="true"
        aria-label="Slide 1"
      ></button>
      <button
        type="button"
        data-bs-target="#carouselExampleIndicators"
        data-bs-slide-to="1"
        aria-label="Slide 2"
      ></button>
      <button
        type="button"
        data-bs-target="#carouselExampleIndicators"
        data-bs-slide-to="2"
        aria-label="Slide 3"
      ></button>
    </div>
    <div class="carousel-inner">
      <div class="carousel-item active">
        <img src="@/assets/img/slide1.jpeg" class="d-block w-100" alt="Comparing savings and deposit products" />
        <div class="carousel-caption d-none d-md-block">
          <h5>예금, 적금 상품을 손쉽게 비교해보세요!</h5>
        </div>
      </div>
      <div class="carousel-item">
        <img src="@/assets/img/slide2.png" class="d-block w-100" alt="Finding tailored loans" />
        <div class="carousel-caption d-none d-md-block">
          <h5>전세 대출, 주택담보대출 내게 맞춤형 대출은?</h5>
          <RouterLink :to="{ name: 'productlist' }" class="btn btn-primary">맞춤형 대출 알아보기</RouterLink>
        </div>
      </div>
      <div class="carousel-item">
        <img
          src="@/assets/img/slide3.webp"
          class="d-block w-100"
          alt="Checking today's exchange rates and finding nearby banks"
        />
        <div class="carousel-caption d-none d-md-block">
          <h5>오늘의 환율 시세는?</h5>
          <RouterLink :to="{ name: 'exchangecalc' }" class="btn btn-primary">자세히 보기</RouterLink>
        </div>
      </div>
    </div>
    <button
      class="carousel-control-prev"
      type="button"
      data-bs-target="#carouselExampleIndicators"
      data-bs-slide="prev"
    >
      <span class="carousel-control-prev-icon" aria-hidden="true"></span>
      <span class="visually-hidden">Previous</span>
    </button>
    <button
      class="carousel-control-next"
      type="button"
      data-bs-target="#carouselExampleIndicators"
      data-bs-slide="next"
    >
      <span class="carousel-control-next-icon" aria-hidden="true"></span>
      <span class="visually-hidden">Next</span>
    </button>
  </div>
</template>

<script setup></script>

<style scoped>
.carousel-item img {
  height: 400px;
  object-fit: cover;
}

.carousel-caption {
  background: rgba(240, 235, 235, 0.5);
  padding: 20px;
  border-radius: 10px;
}

.carousel-caption h5 {
  color: #2e1515;
  font-size: 1.5rem;
  margin-bottom: 10px;
}

.carousel-caption .btn {
  color: #ffffff;
  text-decoration: none;
}
</style>
