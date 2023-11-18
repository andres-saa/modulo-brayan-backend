<template>
  <div class="col-12 text-4xl">

    <p style="text-align: center;
      width: 100%;
      
      font-weight: bold;
  ">


      <span>COMBOS</span>
    </p>


  </div>

  
<div v-if="isSmallScreen" style=" ; width: auto; position: relative">
  <div  class="containr" ref="scrollContainer"  style=" background-color: transparent position: ; display: flex;gap:1rem ; overflow-x: auto;padding-left:0.1rem">

<div   style="margin:2rem 0;" v-for="product in [1,2,3,4]" class="item col-12 p-0">
  <TarjetaCombo   style="width: ;"    :img_id="product"></TarjetaCombo>     
 

</div>
<a style="width: auto; position: absolute; left: -2rem; ; padding: 0; transform: translateX(); "
  class="carousel-control-prev"  role="button" data-slide="prev">
  <span style="color: var(--primary-color); transform: ;font-size: 2rem ;" :class="PrimeIcons.ANGLE_DOUBLE_LEFT"
    aria-hidden="true"></span>
  <span class="sr-only">Previous</span>
</a>
<a style="width: auto; position: absolute; right: -2rem; padding: 0; transform: translateX(); "
  class="carousel-control-next"  role="button" data-slide="next">
  <span style="background-color: ; color: var(--primary-color); ;font-size: 2rem ;" :class="PrimeIcons.ANGLE_DOUBLE_RIGHT"
    aria-hidden="true"></span>
  <span class="sr-only">Next</span>
</a>

</div>

</div>
  


 
  <Carousel  v-else class=" m-auto xl:col-10 md"  :responsiveOptions="responsiveOptions"  style="height:max-content; padding: 0;margin: 0" :value="[1,2,3,4]" :numVisible="2" :numScroll="1"  >
        <template #item="slotProps" >
   
            <div class=" m-2 p-0  ">
                             <!-- <TarjetaMenu  style="   ;width: 90%;"  class=""  :product="slotProps.data"></TarjetaMenu> -->
              <TarjetaCombo :img_id="slotProps.data" class="tarjeta     "></TarjetaCombo>

            </div>
        
        </template>
    </Carousel>



  
</template>

<script setup>
import CarouselBanner from '@/components/CarouselBanner.vue'
// import CarouselSites from '../../components/CarouselSites.vue';
// import TarjetaCombo from '../../components/TarjetaCombo.vue';
import TarjetaCombo from './TarjetaCombo.vue';

import { ref, onMounted, onBeforeUnmount, computed } from 'vue';

import VueCarousel from 'vue-carousel';
import { PrimeIcons } from 'primevue/api';

const screenWidth = ref(window.innerWidth);

const isSmallScreen = computed(() => screenWidth.value < 960);

const updateScreenWidth = () => {
  screenWidth.value = window.innerWidth;
};

onMounted(() => {
  window.addEventListener('resize', updateScreenWidth);
});

onBeforeUnmount(() => {
  window.removeEventListener('resize', updateScreenWidth);
});







const responsiveOptions = [
  {
    breakpoint: '1400px',
    numVisible: 2,
    numScroll: 1
  },
  {
    breakpoint: '1250px',
    numVisible: 2,
    numScroll: 1
  },
  {
    breakpoint: '960px',
    numVisible: 1,
    numScroll: 1
  },
  {
    breakpoint: '575px',
    numVisible: 1,
    numScroll: 1
  }
]











const carouselRef = ref(null);
const touchStartY = ref(0);
const touchEndY = ref(0);

const onTouchStart = (event) => {
  touchStartY.value = event.touches[0].clientY;
};

const onTouchMove = (event) => {
  touchEndY.value = event.touches[0].clientY;
};

const onTouchEnd = () => {
  const deltaY = touchEndY.value - touchStartY.value;

  if (Math.abs(deltaY) > 50) {
    if (deltaY > 0) {
      // Realiza la acción de "swipe down".
      carouselRef.value.prev();
    } else {
      // Realiza la acción de "swipe up".
      carouselRef.value.next();
    }
  }
};







</script>

<style  scoped>
.tarjeta {
  /* margin:1rem */
}

::-webkit-scrollbar {
  width: 12px; /* Ancho de la barra de desplazamiento */
}

/* Estilo del pulgar de la barra de desplazamiento */
/* WebKit (Chrome, Safari) */
::-webkit-scrollbar-thumb {
  background-color: var(--primary-color); /* Color del pulgar de la barra de desplazamiento */
  border-radius: 6px; /* Radio de esquinas del pulgar */
}
</style>