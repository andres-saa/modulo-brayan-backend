<script setup>
import { menuOptions } from './service/menuOptions';
import { onMounted, onBeforeUnmount, watch } from 'vue'
import { getProductsByCategory, getCategory, getMenu } from '@/service/productServices.js'
import { ref, computed } from 'vue';
import { PrimeIcons } from 'primevue/api';
import { changeProduct } from './service/productServices';
import { showSiteDialog, setShowDialog,showProductDialog,setProductDialog,productDialog } from './service/state';
import { carro } from './service/cart';
import { useRouter } from 'vue-router';
import { adiciones } from '@/service/menu/adiciones/adiciones.js'
import {URI} from '@/service/conection'
import { useToast } from 'primevue/usetoast';

// import { cart } from './service/cart';
// import {vue} from 'vue';imp
import { cities } from './service/citiesService';
import { menuGlobal } from './service/menu/menu';
// import { PrimeIcons } from 'primevue/api';
import { formatoPesosColombianos } from './service/formatoPesos';
import TarjetaMenu from './components/TarjetaMenu.vue';
import { RouterLink } from 'vue-router';
import router from '@/router/index.js'
import { useCart } from './service/cart';
 
const screenWidth = ref(window.innerWidth);
console.log(screenWidth.value)
// Función para actualizar el valor del ancho de la pantalla
const updateScreenWidth = () => {
  screenWidth.value = window.innerWidth;
};

const toast = useToast();
// Escuchar el evento de cambio de tamaño de la ventana
window.addEventListener('resize', updateScreenWidth);

// Limpieza al desmontar el componente
onBeforeUnmount(() => {
  window.removeEventListener('resize', updateScreenWidth);
});



const c_neigbor = ref(localStorage.getItem('currentNeigborhood'))

onMounted(() => {


  if (localStorage.getItem('cart')) {
    // localStorage.setItem('cart',{products:[],total:0})
    carro.value = JSON.parse(localStorage.getItem('cart'))
  }

  if (!localStorage.getItem('cart')) {
    localStorage.setItem('cart', JSON.stringify({ products: [], total: 0 }))
    // localStorage.setItem('totalCart',0)
  }

  console.log(JSON.parse((localStorage.getItem('menu'))))
  // cart.value = JSON.parse(localStorage.getItem('cart'))

  if (localStorage.getItem('menu')) {
    console.log('habia')
    menuOptions.value[0].menus = JSON.parse(localStorage.getItem('menu'))
  } else {

    //   getMenu().then(products => {
    //   menuOptions.value[0].menus = products
    //   localStorage.setItem("menu", JSON.stringify(products))

    //   if(!showSiteDialog.value){
    //     location.reload()
    //   }

    // })
    menuOptions.value[0].menus = menuGlobal
    localStorage.setItem('menu', JSON.stringify(menuGlobal))
  }


  if (!c_neigbor.value) {
    showSiteDialog.value = true
  }



})
const sitesImages = ref({
  Caney: 'https://drive.google.com/file/d/1LpmzmgBDOR-YAT4_SstyAldl1Nid-CF2/view?usp=sharing',
  'La Flora': 'https://backend.novatocode.online/read-site-cover/IMPERIO%20CANEY',
  Palmira: '	https://backend.novatocode.online/read-site-cover/IMPERIO%20PALMIRA',
  Bretaña: 'https://backend.novatocode.online/read-site-cover/IMPERIO%20BRETA%C3%91A',
  Jamundi: 'https://backend.novatocode.online/read-site-cover/IMPERIO%20JAMUNDI',
  Tulua: 'https://backend.novatocode.online/read-site-cover/IMPERIO%20TULUA',
  default: ''
})
const currenNeigborhood = ref({
  site: {
    name: 'default'
  }
})
const possibleNeigborhoods = ref()

const ruta = ref(router.currentRoute)
const vueMenu = ref(false)

const addcar =(product) => {
    useCart.add(product)  
    toast.add({ severity: 'success', summary: 'Agregado al carrito', detail: productDialog.value.name, life: 3000 });
}
const currenCity = ref({})

const changePossiblesNeigborhoods = () => {
  const neigborhoods = []

  currenCity.value.sites.map(site => {
    site.neigborhoods.map(neigborhood => {
      neigborhoods.push({ name: neigborhood.name, neigborhood: neigborhood, site: site })
      console.log(site)
    })
  })

  possibleNeigborhoods.value = neigborhoods
}
watch(currenCity, () => { changePossiblesNeigborhoods() })

const setNeigborhood = () => {
  localStorage.setItem('currentNeigborhood', JSON.stringify({ currenCity: currenCity.value.name, currenNeigborhood: currenNeigborhood.value.neigborhood, currenSite: currenNeigborhood.value.site.name }))
  console.log(localStorage.getItem('currentNeigborhood'))
  // setShowDialog()
  location.reload();
}

const checked = ref({ })

const searchCountry = (event) => {
  setTimeout(() => {
    if (!event.query.trim().length) {
      autoFilteredValue.value = [...autoValue.value];
    } else {
      autoFilteredValue.value = autoValue.value.filter((country) => {
        return country.name.toLowerCase().startsWith(event.query.toLowerCase());
      });
    }
  }, 250);
};

console.log(router.currentRoute)

const topbarMenuClasses = computed(() => {
  return {
    'layout-topbar-menu-mobile-active': topbarMenuActive.value
  };
});

const topbarMenuActive = ref(false);

</script>

<template>
  <router-view class="col-12 p-0 m-0" :class="screenWidth<500 && ruta.fullPath == '/cart'? 'fondo-movil':'fondo-pc'"  />

</template>

<style scoped>
@keyframes rot {
  0% {
    transform: translatey(-50%) scale(1.25, 0.75);
  }

  50% {
    transform: translatey(-150%) scale(1, 1);
  }

  100% {
    transform: translatey(-50%) scale(1.25, 0.75);
  }
}


.imagen {
  margin: 200px;
  width: 100px;
  /* overflow: hidden;  */
  animation: rot 0.7s infinite;
  transform-origin: center bottom;
}

.img-cart:hover {
  transform: scale(1.3);
}

.img-cart {
  transition: all .3s ease;
}







@media (min-width: 767px) {
  .scroll{
  max-height:700px ;overflow-y: auto;

}

.add-car{
  width: 50%;
}
}

.led{
    animation: cambiaColor 1s infinite; /* 3s de duración, animación infinita */
}
    @keyframes cambiaColor {
      0% { background-color: rgb(0, 0, 0); }
      50% { background-color: rgb(30, 255, 0); }
      100% { background-color: var(--primary-color); }
    }
.img-before {
  /* background-color: rgba(0, 0, 0, 0.235); */
  width: 100%;
  height: 100%;
  position: absolute;
  top: 0%;
  left: 0;
  z-index: 1000;
  display: flex;
  align-items: center;
  justify-content: center;

}

.carro:hover {
  /* transform: scalex(1.2); */
  background-color: #ff62004a;
  cursor: pointer
}

.menu-button-new {
  background-color: var(--primary-color);
  /* padding: 1rem; */
  /* margin: 0 1rem; */
  border: none;
  font-size: 20px;
  /* transition: all  0.3s; */
  /* font-weight: bold; */
  border-radius: 10px;
  color: #fff;
  width: 300px;
  transition: all 0.3s ease;
  text-align: center;

}

.fondo-movil{
  background-color: var(--primary-color);
}

.fondo-pc{
  background-color: #ffffff;
}
.img-cont {
  width: 100%;
  height: 100%;
  margin: 0;
  padding: 0;
  position: relative;
  overflow: hidden;
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 10px;


}

.default-image {
  filter: blur(10px);
  position: relative;
}
*:focus{
 border: none;
 outline: none;
}
.default-image::before {
  content: 'hola';
  width: 100%;
  background-color: rgba(177, 99, 9, 0.1);
  height: 100%;
  position: absolute;
  top: 0;
  left: 0;
}

.selected{
  background-color:#ff620050 
}

.menu-button-new:hover {
  /* filter: brightness(1.5);  
   */
  background-color: black;
  cursor: pointer;

}




.cart {

  box-shadow: 0px 0px 30px rgba(0, 0, 0, 0.4);



}

.img-cont {
  background-color:rgb(255, 226, 192);
  /* display: flex; */
  /* justify-content: flex-start; */
  align-items: start;

  /* box-shadow: 30px 0px 30px rgba(0, 0, 0, 0.5); */
  height: 100%;
  /* flex-direction: column; */
}



.imagen {
  /* position: fixed; */
  width: 100%;
  height: auto;
  object-fit: contain;
  transition: all ease 0.5s;
  /* margin-left: 1vw; */
  border-radius: 50px;

  /* filter: drop-shadow(-2px 2px 15px rgba(0, 0, 0, 0.7)); */

}

.imagen:hover {
  transform: scale(1.1);
  ;

  /* box-shadow: 0px 0px 30px rgba(0, 0, 0, 1); */
  filter: brightness(1.2) drop-shadow(-2px 2px 15px rgba(0, 0, 0, ));
  /* filter: drop-shadow(-2px 2px 15px rgba(0, 0, 0, 0.7)); */

}

.producto {
  /* filter: brightness(1.2); */
}

.info {
  /* padding-left: 10%; */

  /* padding-top: 5%; */
  display: flex;
  flex-direction: column;
  align-items: fle;
  /* gap: 10px; */
  /* box-shadow: 0px 0px 30px rgba(0, 0, 0, 1); */
}

.ordenar {
  transition: all 0.2s ease;
  border: 2px solid var(--primary-color);
  /* // font-weight: bold; */
  font-size: 20px;
  /* // margin-bottom: 200px; */
  background-color: transparent;
  border-radius: 5px;
}

.carro {

  border: none;
  /* // font-weight: bold; */
  /* font-size: 20px; */
  /* // margin-bottom: 200px; */
  background-color: transparent;
  border-radius: 5px;
  margin: auto;
  /* border-radius:; */
}

.whatsapp:hover {
  transform: scale(1.1);
}

.ver-mas:hover {
  background-color: var(--primary-color);
  transform: scale(1.1);



  color: #fff;
  cursor: pointer;
}


/* // .icono{
//     color: var(--primary-color);
// } */
.ver-mas:hover>.icono {
  /* // background-color: var(--primary-color);

// display: none; */
  color: #fff;
  transform: translateX(5px);
}

.info-header {
  display: flex;
  justify-content: space-between;
  /* align-items: center; */
  /* gap: 20px; */
}

.salsa {
  display: flex;
  width: 100%;
  justify-content: space-between;
  align-items: start;
  padding: 0;

  margin: 0;


}

.salsa:hover {
  color: var(--primary-color);
}

.salsas {
  display: flex;
  padding: 0;
  margin: 0;


}

.whatsapp {
    /* background-color: red; */
    /* min-width: 1024px; */
    width: 3rem;
    height: 3rem;
    display: flex;
    transition: all ease .3s;
    right: 5rem;
    bottom: 9rem;

    /* align-items: center; */
    justify-content: center;
    background-color: #25D366;
    border-radius: 50%;
    position: absolute;
 
  }
@media (max-width:500px)  {
  .whatsapp {
    /* background-color: red; */
    /* min-width: 1024px; */
    width: 4rem;
    height: 4rem;
    right: 5%;
    bottom: 130%;

  }
}

.adiciones {
  display: flex;
  padding: 0;
  margin: 0;

}

a{
  text-decoration: none;
}

.texto {
  /* width: 40%; */
  /* min-width: 200px; */
  padding-right: 20px;
  /* min-width: 200px; */
  /* margin-right: 20px; */
}

.icono {
  transition: all 0.2s ease;
  color: var(--primary-color);
  transform: translateX(-5px);
  font-weight: bold;
}

.title {}

.nombre-salsa::after {}


.animador {
  animation: para-aca 1s infinite ease;

}


@keyframes para-aca {
  0% {
    transform: translateX(0%);
  }

  50% {
    transform: translateX(100%)
  }

}

::-webkit-scrollbar {
  width: 1rem; /* Ancho de la barra de desplazamiento */
  padding-top: 1rem;
  position: absolute;
  display: none;
}
.clase{
    
}
/* Estilo del pulgar de la barra de desplazamiento */
/* WebKit (Chrome, Safari) */
::-webkit-scrollbar-thumb {
  background-color: rgb(255, 0, 0); /* Color del pulgar de la barra de desplazamiento */
  border-radius: 9px;
  border: 5px solid var(--primary-color);
  height: 10rem;
  width: 10rem;
  /* display: none;  */
}
</style>
