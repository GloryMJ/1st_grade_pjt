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
      if (rateData.intr_rate !== null && rateData.intr_rate2 !== null) {
        chartData.push({
          x: rateData.intr_rate,
          y: rateData.intr_rate2 - rateData.intr_rate,
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
            backgroundColor: "rgba(214, 34, 32, 0.8)", // 진한 색상
            borderColor: "rgba(214, 34, 32, 1)",
            borderWidth: 2, // 더 굵게 설정
            pointRadius: 6, // 점의 크기 설정
            pointBackgroundColor: "rgba(214, 34, 32, 1)", // 점의 배경색을 더 진하게 설정
            pointBorderColor: "rgba(214, 34, 32, 1)",
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
              text: "기본금리",
              display: true,
            },
          },
          y: {
            beginAtZero: true,
            title: {
              text: "우대금리 - 기본금리",
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
