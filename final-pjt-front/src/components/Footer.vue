<template>
  <!-- Footer -->
  <footer class="bg-dark text-center text-white">
    <div class="container p-4">
      <section class="mb-4">
        <a class="btn btn-outline-light btn-floating m-1" href="#!" role="button"><i class="fab fa-facebook-f"></i></a>
        <a class="btn btn-outline-light btn-floating m-1" href="#!" role="button"><i class="fab fa-twitter"></i></a>
        <a class="btn btn-outline-light btn-floating m-1" href="#!" role="button"><i class="fab fa-google"></i></a>
        <a class="btn btn-outline-light btn-floating m-1" href="#!" role="button"><i class="fab fa-instagram"></i></a>
        <a class="btn btn-outline-light btn-floating m-1" href="#!" role="button"><i class="fab fa-linkedin-in"></i></a>
        <a class="btn btn-outline-light btn-floating m-1" href="#!" role="button"><i class="fab fa-github"></i></a>
      </section>

      <EmailForm />

      <section>
        <div class="row">
          <div class="col-lg-8 d-flex justify-content-center align-items-center">
            <img src="@/assets/img/kb-logo.png" alt="국민은행" class="bank-logo" />
            <img src="@/assets/img/shinhan-logo.jpg" alt="신한은행" class="bank-logo" />
            <img src="@/assets/img/woori-logo.png" alt="우리은행" class="bank-logo" />
            <img src="@/assets/img/hana-logo.jpg" alt="하나은행" class="bank-logo" />
          </div>
          <div class="col-lg-4">
            <div class="accordion" id="footerAccordion">
              <div class="accordion-item">
                <h2 class="accordion-header" id="headingOne">
                  <button
                    class="accordion-button collapsed"
                    type="button"
                    data-bs-toggle="collapse"
                    data-bs-target="#collapseOne"
                    aria-expanded="false"
                    aria-controls="collapseOne"
                  >
                    은행별 금융상품
                  </button>
                </h2>
                <div
                  id="collapseOne"
                  class="accordion-collapse collapse"
                  aria-labelledby="headingOne"
                  data-bs-parent="#footerAccordion"
                >
                  <div class="accordion-body">
                    <ul class="list-unstyled">
                      <li>
                        <a
                          href="https://obank.kbstar.com/quics?page=C030037&QSL=F&_ga=2.18409786.224139304.1715837620-871769625.1715837620#loading"
                          class="text-white"
                        >
                          국민은행
                        </a>
                      </li>
                      <li><a href="https://bank.shinhan.com/index.jsp#020001000000" class="text-white">신한은행</a></li>
                      <li>
                        <a href="https://spot.wooribank.com/pot/Dream?withyou=PODEP0001" class="text-white">우리은행</a>
                      </li>
                      <li><a href="https://www.kebhana.com/cont/mall/index.jsp" class="text-white">하나은행</a></li>
                    </ul>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
    </div>

    <div class="text-center p-3" style="background-color: rgba(0, 0, 0, 0.2)">
      © 2024 Copyright:
      <a class="text-white" href="https://mdbootstrap.com/">MDBootstrap.com</a>
    </div>
  </footer>
</template>

<script setup>
import EmailForm from "./EmailForm.vue";
</script>

<style scoped>
.accordion-button {
  background-color: #343a40;
  color: #ffffff;
  border: none;
}
.accordion-button:focus {
  box-shadow: none;
}
.accordion-button:not(.collapsed) {
  color: #ffffff;
  background-color: #495057;
}
.accordion-body {
  background-color: #343a40;
  color: #ffffff;
}
.accordion-body a {
  color: #ffffff;
}
.accordion-body a:hover {
  text-decoration: underline;
}
.bank-logo {
  width: 100px;
  height: 50px;
  object-fit: contain;
  margin: 0 10px;
  border-radius: 30px;
}
</style>
