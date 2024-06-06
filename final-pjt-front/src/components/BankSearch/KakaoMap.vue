<template>
  <div class="container">
    <section class="row justify-content-center mb-3">
      <div class="col-md-12">
        <KakaoMapForm @searchPlace="searchPlace" />
      </div>
    </section>
    <section class="row">
      <div class="col-xl-6 col-12">
        <div ref="mapContainer" style="width: 550px; height: 550px"></div>
      </div>
      <div class="col-xl-6 col-12 locationlist-container" ref="locationListContainer">
        <template v-for="rs in search.results" :key="rs.id">
          <div
            class="border border-dark p-2 mb-3 rounded-3 bank-item"
            :class="{ marker_selected_location: rs.id == place_id }"
            @click="clickLocation(rs.road_address_name)"
            :id="rs.id"
          >
            <h4>{{ rs.place_name }}</h4>
            <p>{{ rs.road_address_name }}</p>
          </div>
        </template>
      </div>
    </section>
  </div>
</template>

<script setup>
import { ref, onMounted, reactive, watch } from "vue";
import KakaoMapForm from "@/components/BankSearch/KakaoMapForm.vue";
import router from "@/router";
import { start } from "@popperjs/core";

const mapContainer = ref(null);
const map = ref(null);
const kakaoLoaded = ref(false); // Kakao Maps API 로드 여부를 추적
const place_id = ref(null);
const locationListContainer = ref(null);
const mapOption = reactive({
  center: {
    lat: 36.107176806766745,
    lng: 128.4178566648957,
  },
  draggable: false,
  level: 3,
});

const search = reactive({
  keyword: null,
  pgn: null,
  results: [],
});

onMounted(() => {
  const loadKakaoMap = (container) => {
    if (window.kakao && window.kakao.maps) {
      initMap(container);
    } else {
      const script = document.createElement("script");
      script.src = `https://dapi.kakao.com/v2/maps/sdk.js?appkey=${
        import.meta.env.VITE_APP_KAKAO_MAP_KEY
      }&autoload=false&libraries=services`;

      script.onload = () => {
        window.kakao.maps.load(() => {
          initMap(container);
        });
      };

      document.head.appendChild(script);
    }
  };

  const initMap = (container) => {
    const { center, level } = mapOption;
    map.value = new window.kakao.maps.Map(container, {
      center: new window.kakao.maps.LatLng(center.lat, center.lng),
      level,
    });
    kakaoLoaded.value = true; // Kakao Maps API 로드 완료
  };

  loadKakaoMap(mapContainer.value);
});

// 검색 완료시 호출되는 콜백함수
const placesSearchCB = (data, status, pgn) => {
  if (status === window.kakao.maps.services.Status.OK) {
    // 검색된 장소 위치 기준으로 지도 범위 재설정 -> LatLngBounds 객체에 좌표를 추가하는 과정
    const bounds = new window.kakao.maps.LatLngBounds();
    for (let i = 0; i < data.length; i++) {
      displayMarker(data[i]);
      bounds.extend(new window.kakao.maps.LatLng(data[i].y, data[i].x));
    }

    // 검색된 장소 위치 기준으로 지도 범위 재설정
    map.value.setBounds(bounds);
  }
};

const scrollToLocation = function (id) {
  const box = document.getElementById(id);
  box.scrollIntoView({ behavior: "smooth", block: "start" });
};

// 지도에 마커 표시하기
const displayMarker = (place) => {
  // 마커를 생성하기
  const marker = new window.kakao.maps.Marker({
    map: map.value,
    position: new window.kakao.maps.LatLng(place.y, place.x),
    clickable: true,
  });

  kakao.maps.event.addListener(marker, "click", function () {
    place_id.value = Number(place.id);
    scrollToLocation(place.id);
  });
};

const searchPlace = (place) => {
  if (!kakaoLoaded.value) {
    // Kakao Maps API 로드 확인
    console.error("Kakao Maps API is not loaded yet");
    return;
  }

  const keyword = place.trim();
  if (keyword.length === 0) {
    return;
  }

  const ps = new window.kakao.maps.services.Places();
  ps.keywordSearch(keyword, (data, status, pgn) => {
    search.keyword = keyword;
    search.pgn = pgn;
    search.results = data;
    placesSearchCB(data, status, pgn);
  });
};

// Kakao Maps API 로드 여부를 감시
watch(kakaoLoaded, (newVal) => {
  if (newVal) {
    console.log("Kakao Maps API loaded successfully");
  }
});

const clickLocation = function (search) {
  window.open(`https://map.kakao.com/?q=${search}`);
};
</script>

<style scoped>
.bank-item {
  box-shadow: 0 0 3px;
  transition-property: transform, background-color;
  transition-duration: 0.2s, 0.2s;
}

.bank-item:hover {
  transform: scale(1.02);
  background-color: ghostwhite;
}

.bank-item:active {
  transform: scale(0.99);
  background-color: antiquewhite;
}

@keyframes bank-item-hover {
  to {
    transform: scale(1.02);
  }
}

.marker_selected_location {
  transition: border, transform;
  transition-duration: 0.1s, 0.1s;
  border: 5px solid #f5bca9 !important;
  transform: scale(1.03);
}

.locationlist-container {
  overflow: auto;
  border: solid 2px black;
  padding-top: 10px;
  height: 550px;
}

.locationlist-container::-webkit-scrollbar {
  width: 10px;
}
.locationlist-container::-webkit-scrollbar-thumb {
  background-color: black;
  border-radius: 10px;
  background-clip: padding-box;
}
.locationlist-container::-webkit-scrollbar-track {
  background-color: grey;
  border-radius: 10px;
  box-shadow: inset 0px 0px 5px white;
}
</style>
