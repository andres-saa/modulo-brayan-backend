<template>

   

<p  class="nombre-sesion mb-8  text-center text-4xl" style="background-color: #ffede1;"> <i class="text-4xl pr-3" :class="PrimeIcons.SHOPPING_CART"></i>TU CARRITO</p>


    <div sty class=" contenedor-principal  grid md:col-12 xl:col-8 xl:ml-auto xl:mr-auto clase" v-if="products.length>0" style="margin-bottom: 5rem;he">

        <div class=" productos-scroll col-12 xl:col-7   md:pl-4 md:pr-6  p-2" style="">
            <div v-for=" product in products" class="producto-list grid mb-6 contenedor-producto "
                style="background-color: ; ">

                <img class=" mr-2 md:mr-6 pl-0 p-2  " style="background-color: #ffede1
; object-fit: contain;height: 7rem;width: 7rem; border-radius:50% ;"
                        :src="product.product.img_96x96"
                        alt=""> 

                <div class="nombre-produc ml-2  col p-1 " style="border-radius: 0 1.5rem 1.5rem 1.5rem; background-color: #ffede1
;height:100% ;display: flex; flex-direction:column ;justify-content: space-between; position: ">
                    

                        
                
                    <div class="col-12 mr-8"
                            style="background-color: ;text-transform: uppercase;  font-weight:bold ; width: 100%;height:1rem; display: flex;  justify-content: space-between;padding: 1rem; ">
                            <p class="xl:text-l md:text-l text-l" style="height: min-content;">{{ product.quantity }} {{ product.product.name }}</p>
                            <p class="xl:text-l md:text-xl" style="height: min-content;"> {{ formatoPesosColombianos(product.product.price * product.quantity) }}</p>

                            
                    </div>

                    <div   class="col-12" style="text-transform: lowercase;text-align: ;  gap:2rem ;height: 4rem;overflow:hidden ; width: auto; display: flex; padding-right: 10rem ; justify-content: space-between; ; ">
                            <p v-if="!isSmallScreen" class="" style="height: auto;">{{ product.product.description }} </p>
                            

                    <div class="contador "
                    
                    >
                        
                    <button
                            style=
                             "  
                            display: flex; 
                            align-items: center;
                            justify-content: center;  
                            border: none; 
                            font-size: 3vh; 
                            background-color: transparent;
                            "
    
                            @click="remove(product.product)"> <i :class="PrimeIcons.MINUS"> </i> 
                    
                    </button>
    
                    <input class="cantidad"
                            style="font-size: 1.5rem; text-align: center; width: 30px; border: 1px none;  " readonly
                            type="text" :value="product.quantity">
                            
                    <button
                            style="  display: flex; align-items: center;justify-content: center; border: none;font-weight: bold; font-size: 3vh;background-color: transparent;"
                            @click="add(product.product)"> <i :class="PrimeIcons.PLUS"> </i> </button>
    
                    
                    </div> 
                            
                    </div>

                   
             
                    <div class="triangulo"></div>
                </div>

                
                

                
                
               

              

  


          </div>
        </div>

 

        <div class=" col-12 xl:col-5   " style="position: relative; border-radius: 2rem;height: 80vh; max-height: 720px;overflow-y: auto ;border: 10px solid;padding:0 1rem ;background-color: white; ">
                <div class="notch" style="display: flex; align-items: center; width: 30%; background-color: black; border-radius: 0 0 1rem 1rem; height: 2rem; position: sticky; top: 0; left: 35%;">
                <div class="led" style="position:absolute ;right: 1rem; width: 0.7rem; height: 0.7rem; background-color: var(--primary-color); border-radius: 50%;: 1rem"></div>
            
                </div>
                <p class="text-2xl" style="font-weight: bold;">RESUMEN </p>

                <!-- <input style="border-radius: 20px; " class="col-12 " type="text" name="" id=""> -->
            
                <div class="productos">
                <div class="producto" v-for="product in products"
                    style="display: flex; justify-content: space-between; align-items:center ;">

                    <p class="" style="text-transform: uppercase; min-width: max-content;margin: 0; padding: 0.5rem 0"> <span>{{ product.quantity }}</span> <span>{{ product.product.name
                    }}</span> </p>

                
                    <p style="font-weight: bold;height: ;">{{ formatoPesosColombianos(product.quantity * product.product.price) }}
                    </p>

                </div>
                </div>
            

                <div style="width: 100%; border-bottom: 2px solid; margin-top:0rem;"></div>
                <div class="text-xl" style="; width: 100%; display: flex; justify-content: space-between; margin: 1rem 0;">

                    <span style="font-weight: bold;"> TOTAL </span>
                    <span style="font-weight: bold;"> {{ formatoPesosColombianos(total) }} </span>

                </div>

                <p class="text-2xl mt-4" style="font-weight: bold;">NOTAS DE TU PEDIDO</p>

                <input style=" border-radius: 20px; height:20rem;margin-bottom: 2rem; border;" class="col-12 " type="text" name="" id="">
                <div style="padding: 2rem; background-color: white; position:sticky;bottom: 0rem; display: flex;width: 100%; display: flex;align-items: center; justify-content: center;">
                    <button style=" width: 80%;border:none; background-color: var(--primary-color); color: white; border-radius: 5rem; padding: 1rem;"> <span class="text-xl" style="font-weight: bold;margin-top: 5rem;">REALIZAR PEDIDO</span></button>

                </div>
                <!-- <textarea cla style=" font-size: 1.5rem; resize: none; height: max-content;" class="col-12 text-xl" name="" id="" cols="30" rows="10"></textarea> -->


        </div>

       
    </div>

    <div class="col-12 m-auto d-flex" v-else style="display: flex; flex-direction: column; justify-content: center; text-align: center; height: 80vh; align-items: center; ">
        <i class="col-12" style="font-size: 30vh;" :class="PrimeIcons.SHOPPING_CART"></i>
        <i class="col-12" style="font-size: 5vh;"> Tu carrito esta vacio </i>
    
    </div>

</template>


<script setup>
import { ref, onMounted, onBeforeUnmount, computed } from 'vue';
import { formatoPesosColombianos } from '../../service/formatoPesos';
import { PrimeIcons } from 'primevue/api';
import { useCart } from '../../service/cart';
import { useRoute } from 'vue-router';






// localStorage.removeItem('cart')




const screenWidth = ref(window.innerWidth);

const isSmallScreen = computed(() => screenWidth.value < 580);

const updateScreenWidth = () => {
  screenWidth.value = window.innerWidth;
};

onMounted(() => {
  window.addEventListener('resize', updateScreenWidth);
});

onBeforeUnmount(() => {
  window.removeEventListener('resize', updateScreenWidth);
});




















const products = ref([])
function contarObjetosRepetidos(arr) {
    const objetoContador = {};

    // Contar la cantidad de veces que se repite cada objeto por su nombre "producto"
    arr.forEach((objeto) => {
        const nombre = objeto.name;
        if (objetoContador[nombre]) {
            objetoContador[nombre].quantity++;
        } else {
            objetoContador[nombre] = {
                product: objeto,
                quantity: 1
            };
        }
    });

    // Crear un nuevo array con los resultados
    const resultado = Object.values(objetoContador).map((item) => item);

    return resultado;
}

const add = (product) => {
    useCart.add(product)
    products.value = contarObjetosRepetidos(JSON.parse(localStorage.getItem('cart')).products);
    total.value = JSON.parse(localStorage.getItem('cart')).total

}

const remove = (product) => {
    useCart.remove(product)
    products.value = contarObjetosRepetidos(JSON.parse(localStorage.getItem('cart')).products);
    total.value = JSON.parse(localStorage.getItem('cart')).total

}
// localStorage.removeItem('cart')

const total = ref()
onMounted(() => {
    products.value = contarObjetosRepetidos(JSON.parse(localStorage.getItem('cart')).products);
    total.value = JSON.parse(localStorage.getItem('cart')).total

})
// Ejemplo de uso
const miArray = [
    { name: 'producto1', price: 2000 },
    { name: 'producto2', price: 3000 },
    { name: 'producto1', price: 2000 },
    { name: 'producto3', price: 2500 },
    { name: 'producto2', price: 3000 },
];

const resultado = contarObjetosRepetidos(JSON.parse(localStorage.getItem('cart')).products);
console.log(resultado);


// const productos = ref


</script>


<style scoped>
*:focus{
    border: none;
}

.led{
    animation: cambiaColor 1s infinite; /* 3s de duración, animación infinita */
}
    @keyframes cambiaColor {
      0% { background-color: rgb(0, 0, 0); }
      50% { background-color: rgb(30, 255, 0); }
      100% { background-color: var(--primary-color); }
    }
.triangulo {
      width: 0;
      height: 0;
      border-left: 1rem solid transparent;
      border-right: 1rem solid transparent;
      border-bottom: 2rem solid #ffede1
; /* Altura del triángulo dependiendo del ancho */
      transform: rotate(-65deg);
      position: absolute;
      top: -1rem;
      left: -1.2rem;
    }


.container {
    background-color: rgb(0, 0, 0);
}

.fixed {
        position: fixed;
        width: 25%;
}
.scrollit {
        float: left;
        width: 71%
}
.sumary {
    /* background-color: green; */
}

.izq {
    /* width: 100%; */

}




.contenedor-producto{
    align-items: center;border-radius: 1rem;overflow: hidden;height: 7rem;position: relative;
}

@media (max-width: 991px) {
    .contenedor-producto{
    /* background-color: #ffffffea;align-items: center;border-radius: rem;overflow: hidden;height: 7rem;position: relative; */
}
}
.nombre-sesion{
    font-weight: bold;
    /* width: auto; */
    border-radius: 5rem;
}

.contenedor-principal{
    border-radius: 2rem;position: sticky;top: 100px; margin-bottom: 10rem; background-color: var(--primary-color);height: auto ;
}
.producto{
    border-bottom: 2px solid #00000020;
}



.cantidad:focus-visible {
    outline: none;

}

.imagen{
    height: 100px;object-fit: contain; 
}

.contador{
    background-color: white; 
    /* height: 3rem;  */
    
    display: flex;
    border-radius: 0.1rem;
    padding:0.1rem 1rem; 
    border: 2px solid var(--primary-color);
    border-radius: 1rem;
    /* bottom: 0.5rem; */
    position:absolute;
    right: 0.5rem;
    width: 8rem;
    height: 2.5rem;
    
}

i {
    font-weight: bold;
}

i:hover {
    color: var(--primary-color);
}

button:hover {
    cursor: pointer;
}

@media (min-width: 768px) and (max-width: 991px) {
  .clase {
   /* background-color: red; */
   min-width: 720px;
  }
}

@media (min-width: 1200px) and (max-width: 1920px) {
  .clase {
   /* background-color: red; */
   min-width: 1024px;
   
  }
  .productos-scroll{
    overflow-y: auto ;
    border-radius: 2rem;height: 80vh;overflow-y: auto; max-height: 720px 
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