import {  ref } from "vue";

// const URI = 'https://backend.novatocode.online'

// const URI = 'http://localhost:8000'
// http://192.168.1.142:5173/

const URI = 'http://167.71.178.54:8100'


const providerDropvalues = ref([])
const categorieFropValue = ref([])
const categoryValue = ref({})
const providervalue = ref({})
const unidadValue = ref({})

const unidadesDropValue = ref([


  'kilogramo',
  'gramo',
  'litro',
  'gallón',
  'unidad',
  'par',
  'docena',
  'paquete',
  'rollo',
   
  // Puedes seguir agregando más unidades según sea necesario
])

const dropServ = {

  providers:async () => {
    try {
      const response = await fetch(`${URI}/providers`);
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }
      const data = await response.json();
      // Asigna los productos a la variable de estado
      providerDropvalues.value = data;
    } catch (error) {
      console.error('Error fetching products:', error);
    }
  },

  categories:async () => {
    try {
      const response = await fetch(`${URI}/categories`);
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }
      const data = await response.json();
      // Asigna los productos a la variable de estado
      categorieFropValue.value = data;
    } catch (error) {
      console.error('Error fetching products:', error);
    }
  }

  
}


  export {URI,dropServ,categoryValue,providervalue,providerDropvalues,categorieFropValue,unidadValue,unidadesDropValue}