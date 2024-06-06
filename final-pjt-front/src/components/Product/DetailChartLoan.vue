<template>
  <div class="chart-container">
    <canvas ref="chartCanvas" width="200" height="200"></canvas>
  </div>
</template>

<script setup>
import { ref, onMounted, defineProps, watch } from "vue";
import { Chart, registerables } from "chart.js";
Chart.register(...registerables);

const props = defineProps({
  products: {
    type: Array,
  },
});

const chartCanvas = ref(null);
let chartInstance = null;

const refineData = (products) => {
  const chartData = [];
  for (let i = 0; i < products.length; i++) {
    const product = products[i];
    for (let j = 0; j < product.infoproducts.length; j++) {
      const rateData = product.infoproducts[j];
      if (rateData.lend_rate_min !== null && rateData.lend_rate_max !== null) {
        chartData.push({
          x: rateData.lend_rate_min,
          y: rateData.lend_rate_max - rateData.lend_rate_min,
          name: product.fin_prdt_nm,
        });
      }
    }
  }
  return chartData;
};

onMounted(() => {
  if (chartCanvas.value) {
    const ctx = chartCanvas.value.getContext("2d");

    const initialData = refineData(props.products);

    chartInstance = new Chart(ctx, {
      type: "scatter",
      data: {
        datasets: [
          {
            label: "금리 한눈에 보기",
            data: initialData,
            backgroundColor: "rgba(18, 10, 143, 0.8)", // 진한 색상
            borderColor: "rgba(18, 10, 143, 1)",
            borderWidth: 2, // 더 굵게 설정
            pointRadius: 6, // 점의 크기 설정
            pointBackgroundColor: "rgba(18, 10, 143, 1)", // 점의 배경색을 더 진하게 설정
            pointBorderColor: "rgba(18, 10, 143, 1)",
          },
        ],
      },
      options: {
        maintainAspectRatio: false,
        scales: {
          x: {
            type: "linear",
            position: "bottom",
            title: {
              text: "대출금리최저",
              display: true,
            },
          },
          y: {
            beginAtZero: true,
            title: {
              text: "대출금리최고 - 대출금리최저",
              display: true,
            },
          },
        },
        plugins: {
          tooltip: {
            callbacks: {
              label: function (context) {
                console.log(context);
                const label = context.dataset.label || "";
                const dataPoint = context.raw;
                return `${dataPoint.name})`;
              },
            },
          },
        },
      },
    });
  }
});

watch(
  () => props.products,
  (newProducts) => {
    if (chartInstance) {
      const updatedData = refineData(newProducts);
      chartInstance.data.datasets[0].data = updatedData;
      chartInstance.update();
    }
  }
);
</script>

<style scoped>
.chart-container {
  width: 400px;
  height: 400px;
  position: relative;
}
</style>
