<template >
    <p style="text-align: center; width: 100%; font-size: 36px; font-weight: bold;">
        Monster <span style="color:var(--primary-color) ;">Menu</span>
    </p>

    <div v-if="isSmallScreen" style="top:5rem;width:; position: sticky;z-index: 50;background-color: white;height: 6rem;outline: 2rem solid white;margin-bottom: 3rem; padding: 2rem;display: flex" class="" >
        <div  class="grid col-12 m-0  " style="margin-bottom: ;  outline: 0.6rem solid var(--primary-color); padding: 0rem 0;border-radius: 100px;   ;  ; height: min-content; background-color: white;">

<div class="" 
    style=" padding: 0 ; display: flex;z-index: 2;width: 100%;height: 100%; left: 0; overflow-x: auto; ">
    <div class="" style="" v-for="section in menuOptions[0].menus" :key="section.category.name">
        <button
            style="margin: 0.5rem ; padding:  0.1rem 1rem ; border-radius: 100px; ; background-color: #00000015; ;"
            class="menu-button" @click="changesection({ category: section.category, products: section.products })"
            :class="currentSection.category.name == section.category.name ? '' : ''">
            {{ section.category.name }}
        </button>
        
    </div>


</div>

</div>
    </div>
    


    <!-- <div style="position: absolute; background-color: red; height: 30px; width: 100vw;left: 0;">holas</div> -->

    <Toolbar v-if="!isSmallScreen" style="margin-bottom: 1rem; ">
            <template #center>
                <div class=" d-flex flex-wrap justify-content-center align-items-center">
                    <div v-for="section in menuOptions[0].menus" :key="section.category.name">
                        <button class="menu-button"
                            @click="changesection({ category: section.category, products: section.products })"
                            :class="currentSection.category.name == section.category.name ? 'selected' : ''">
                            {{ section.category.name }}
                        </button>
                    </div>
                </div>
            </template>
        </Toolbar>

  
    

        <div class="grid  xl:col-10 xl:m-auto  " style="background-color: ; margin-bottom: 5rem;">

            <div v-if="currentSection" v-for="product in currentSection.products" class="xl:col-3 lg:col-4 md:p-3 col-6 p-1 ">
                <TarjetaMenu style="width: 100%;" class="" :product="product"></TarjetaMenu>

                <!-- <TarjetaMenu class=""></TarjetaMenu> -->
            </div>
        </div>









   
</template>

<script setup>
import TarjetaCombo from '../../components/TarjetaCombo.vue';
import TarjetaMenu from '../../components/TarjetaMenu.vue'
import { menuOptions } from '../../service/menuOptions';
import { ref, onMounted, onBeforeUnmount, computed,watch } from 'vue';
import { PrimeIcons } from 'primevue/api';
import { curentProduct, changeProduct } from '../../service/productServices';
import { menuGlobal } from '../../service/menu/menu';
import { ableMenu } from '../../service/menuOptions';
import { formatoPesosColombianos } from '../../service/formatoPesos';




const screenWidth = ref(window.innerWidth);

const isSmallScreen = computed(() => screenWidth.value < 720);

const updateScreenWidth = () => {
  screenWidth.value = window.innerWidth;
};

onMounted(() => {
  window.addEventListener('resize', updateScreenWidth);
});

onBeforeUnmount(() => {
  window.removeEventListener('resize', updateScreenWidth);
});


const currentSection = ref(menuOptions.value[0].menus[0])
const currentMenu = ref({})
const changesection = (section) => {
    currentSection.value = section
    console.log(section)
}


const setSection = () => {
    currentSection.value = { category: menuOptions.value[0].menus[1].category, products: menuOptions.value[0].menus[1].products }

    console.log('cambio')
}

watch(menuOptions, setSection);






onMounted(async () => {
    // changesection({category:localStorage.getItem('menu').category,products:localStorage.getItem('menu').products})
    // getMenu().then(products => currentSection.value = products[0])
    ableMenu.value = true
});

</script>

<style scoped>
.boton-menu {
    margin: 0;
    border: none;
    background-color: transparent;
    font-size: 20px;
    padding: 0 20px;
}

.menu-button {
    background-color: transparent;
    padding: 1rem;
    margin: 0 1rem;
    border: none;
    font-size: 20px;
    /* transition: all  0.3s; */
    /* font-weight: bold; */
}

.menu-button:hover {
    /* box-shadow: inset 0 0 5px rgba(0, 0, 0, 0.5); */
    /* transform: scale(1.1); */
    /* border-bottom:  2px red; */
    color: var(--primary-color);
    cursor: pointer;


}


::-webkit-scrollbar {
  width: 12px;
  display: none;


   /* Ancho de la barra de desplazamiento */
}

/* Estilo del pulgar de la barra de desplazamiento */
/* WebKit (Chrome, Safari) */
::-webkit-scrollbar-thumb {

  background-color: white; /* Color del pulgar de la barra de desplazamiento */
  border-radius: 6px; /* Radio de esquinas del pulgar */
  transform: translateY(40px);
  /* padding: 50px; */
  /* display: none; */
}

.selected {
    box-shadow: 0px 5px 0px var(--primary-color);
    /* font-weight: bold; */


}

.col-12 {
    width: 100vw;
    position: absolute;
    left: 0;
    padding: 1.5rem;
}</style>