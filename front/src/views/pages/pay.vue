<template>

    <p class="col-12 text-center text-4xl" style="font-weight: bold;"> <i class="text-4xl pr-3" :class="PrimeIcons.SHOPPING_CART"></i>Finalizar compra</p>
    <div class="border-2 rounded grid container lg:col-7 md:col-12 sm:col-12 m-auto" v-if="products.length>0">

        <div class="col-7 sumary izq grid pr-8  " style="height: min-content ; ">

            <span class="p-float-label col-6" style="display: flex; flex-direction: column;">
                <span style="padding-bottom: 1rem;" for="value">Nombre</span>
                <InputText id=""  type="text" :class="{ 'p-invalid': errorMessage }" aria-="text-error" />
          
            </span>
            <span  class="p-float-label col-6" style="display: flex; flex-direction: column;">
                <span style="padding-bottom: 1rem; font-weight: ;"  for="value">Apellidos</span>
                <InputText id=""  type="text" :class="{ 'p-invalid': errorMessage }" aria-="text-error" />
          
            </span>
            <span class="p-float-label col-6" style="display: flex; flex-direction: column;">
                <span style="padding-bottom: 1rem;" for="value">Barrio</span>
                <InputText id=""  :value="currenNeigborhood"  type="text" :class="{ 'p-invalid': errorMessage }" aria-="text-error" />
          
            </span>
           
            <span class="p-float-label col-6" style="display: flex; flex-direction: column;">
                <span style="padding-bottom: 1rem;" for="value">Telefono</span>
                <InputText id=""  type="number" :class="{ 'p-invalid': errorMessage }" aria-="text-error" />
          
            </span>

            <span class="p-float-label col-12" style="display: flex; flex-direction: column;">
                <span style="padding-bottom: 1rem;" for="value">Direccion</span>
                <InputText id=""  type="text" :class="{ 'p-invalid': errorMessage }" aria-="text-error" />
          
            </span>
            <span class="p-float-label col-6" style="display: flex; flex-direction: column;">
                <span style="padding-bottom: 1rem;" for="value">apartamento, casa, unidad, etc.</span>
                <InputText id=""  type="text" :class="{ 'p-invalid': errorMessage }" aria-="text-error" />
          
            </span>
            <!-- <span class="p-float-label col-6" style="display: flex; flex-direction: column;">
                <span style="padding-bottom: 1rem;" for="value">Name - Surname</span>
                <InputText id=""  type="text" :class="{ 'p-invalid': errorMessage }" aria-="text-error" />
          
            </span> -->
            <span class="p-float-label col-6" style="display: flex; flex-direction: column;">
                <span style="padding-bottom: 1rem;" for="value">Metodo de pago</span>
                 <Dropdown style="height: min-content;"  v-model="payMethod" :options="payMethods"   required="true" />
                
                
            </span>
        

        <!-- <Dropdown v-model="selectedCity" editable :options="possibleNeigborhoods"  placeholder="Select a City" class="w-full md:w-14rem" /> -->

     
            
           
        </div>









        <div id="contenido" class="col der grid p-5 mt-1 " style="height: min-content;">



            <div class="grid col-12" style="box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.424); border: 1px solid;">
                <p class="text-2xl" style="font-weight: bold;">RESUMEN </p>

                <!-- <input style="border-radius: 20px; " class="col-12 " type="text" name="" id=""> -->
                <div class="col-12 p-0" v-for="product in products"
                    style="display: flex; justify-content: space-between; align-items: center; ">

                    <p style="min-width: max-content;"> <span>{{ product.quantity }}</span> <span>{{ product.product.name
                    }}</span> </p>

                    <span
                        style="; width:100% ; overflow: hidden; border-top: 2px  ;  border-bottom: 5px  ;height: 1px; border-top-style: dotted; color:; margin: 0 1rem ;">

                    </span>

                    <p style="font-weight: bold;">{{ formatoPesosColombianos(product.quantity * product.product.price) }}
                    </p>

                </div>

                <div style="width: 100%; border-bottom: 2px solid; margin-top:1rem;"></div>
                <div class="text-xl" style="; width: 100%; display: flex; justify-content: space-between; margin-top: 1rem;">

                    <span style="font-weight: bold;"> TOTAL </span>
                    <span style="font-weight: bold;"> {{ formatoPesosColombianos(total) }} </span>

                </div>

                <p class="text-2xl mt-4" style="font-weight: bold;">NOTAS DE TU PEDIDO</p>

                <!-- <input style="border-radius: 20px; " class="col-12 " type="text" name="" id=""> -->
                <textarea  style=" font-size: 1.5rem; resize: none; " class="col-12 text-xl" name="" id="" cols="30" rows="3"></textarea>


            </div>

        </div>
    </div>

    <div class="col-12 m-auto d-flex" v-else style="display: flex; flex-direction: column; justify-content: center; text-align: center; height: 80vh; align-items: center; ">
        <i class="col-12" style="font-size: 30vh;" :class="PrimeIcons.SHOPPING_CART"></i>
        <i class="col-12" style="font-size: 5vh;"> Tu carrito esta vacio </i>
    
    </div>

</template>


<script setup>
import { ref, onMounted } from 'vue'
import { formatoPesosColombianos } from '../../service/formatoPesos';
import { PrimeIcons } from 'primevue/api';
import { useCart } from '../../service/cart';
import { useRoute } from 'vue-router';

const currenNeigborhood = JSON.parse(localStorage.getItem('currentNeigborhood')).currenNeigborhood.name








const payMethod = ref('')
const payMethods = ref(["Recoger en local", "Efectivo", "Pago con tarjeta (datafono)"])






















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


<style>
.container {
    /* background-color: rgb(0, 0, 0); */
}


.sumary {
    /* background-color: green; */
}

.izq {
    /* width: 100%; */

}

.cantidad {
    cursor: nomel;
}


.cantidad:focus-visible {
    outline: none;

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
</style>