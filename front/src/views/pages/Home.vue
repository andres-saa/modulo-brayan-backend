<template>
  <div>
    <h1>Productos</h1>

    <Button @click="showProductDialog = !showProductDialog"
      style="background-color: black; border-radius: 0.5rem; font-weight: bold;margin-bottom: 2rem;">AGREGAR
      PRODUCTO</Button>
    <div class="grid ">
      <div class="col-12 md:col-6 lg:col-4 xl:col-3" v-for="product in products" :key="product.id">
        <div class="p-0" style=" border-radius: 1rem; overflow: hidden;     box-shadow: 0px 0px 20px rgba(0, 0, 0, 0.5);">
          <!-- <div>
          <img style="object-fit: contain; width: 100%;" :src="`${URI}/read_product_image/300/${product.product_name}`" alt="">
        </div> -->

          <div class="col-12 m-0 " style="background-color: rgb(255, 230, 0); box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.5)">
            <p class="text-xl p-1 " style="font-weight: bold; text-transform: uppercase; ">
              {{ product.product_name }}
            </p>
          </div>

          <div class="info p-3 pt-5">

            <div class="grid ">

<span class="text-l text-left col" style="font-weight:bold; min-width: max-content;">
  CATEGORIA
</span>

<p class="text-l text-right col" style="font-weight: ">
  <!-- {{ product.provider_id }} -->

  {{ categorieFropValue.find(objeto => objeto.category_id === product.category_id).category_name }}
</p>
</div>

            <div class="grid ">

              <span class="text-l text-left col" style="font-weight:bold; min-width: max-content;">
                DESCRIPCION
              </span>

              <p class="text-l text-right col" style="font-weight: ">
                {{ product.product_description }}
              </p>
            </div>



            <div class="grid ">

              <span class="text-l text-left col" style="font-weight:bold; min-width: max-content;">
                UNIDAD DE MEDIDA
              </span>

              <p class="text-l text-right col" style="font-weight: ">
                {{ product.unit_of_measure }}
              </p>
            </div>


            <div class="grid ">

              <span class="text-l text-left col" style="font-weight:bold; min-width: max-content;">
                PRECIO DE COMPRA
              </span>

              <p class="text-l text-right col" style="font-weight: ">
                {{ formatoPesosColombianos(product.product_purchase_price ) }}
              </p>
            </div>


            <div class="grid ">

              <span class="text-l text-left col" style="font-weight:bold; min-width: max-content;">
                PRECIO DE VENTA
              </span>
 
              <p class="text-l text-right col" style="font-weight: ">
                {{ formatoPesosColombianos(product.product_selling_price ) }} 
              </p>
            </div>

            <div class="grid ">

              <span class="text-l text-left col" style="font-weight:bold; min-width: max-content;">
                PROVEEDOR
              </span>

              <p class="text-l text-right col" style="font-weight: ">
                <!-- {{ product.provider_id }} -->

                {{ providerDropvalues.find(objeto => objeto.provider_id === product.provider_id).provider_name }}
              </p>
            </div>



          </div>




          <div class="botones col-12" style="display: flex; justify-content: end;">

            <button @click="deleteProduct(product.product_id)"
              style="color:white; background-color: rgb(255, 83, 83); border-radius: 0.5rem;border: none; font-weight: bold; padding:0.5rem 1rem ;  right: 1rem;">Eliminar</button>


          </div>

          <!-- Agrega el botón de eliminar y vincula el método deleteProduct -->

        </div>
      </div>

    </div>
  </div>












  <Dialog v-model:visible="showProductDialog" :style="{ width: '500px' }" header="Registrar un Usuario" :modal="true"
    class="p-fluid" style="background-color: white; border-radius: 1rem; overflow: hidden;">


    <div class="cont-dialog">


      <!-- <div class="foto">
                        <img v-if="urlPhotoProfile" :src="urlPhotoProfile" alt="Preview" >

                    </div> -->



      <div>
        <!-- <input type="file" @change="handleFileChange" /> -->

      </div>









      <div class="dialog-container">


        <div class="field">
          <label for="name">Nombre </label>
          <InputText v-model.trim="productName" required autofocus />
          
        </div>

        <span st style="padding-bottom: 1rem;color: #000;" for="value">Categoria</span>
                 <Dropdown class="mb-3" style="height: min-content;"  v-model="categoryValue" :options="categorieFropValue" optionLabel="category_name"   required="true" />


        

        <div class="field">
          <label for="description">Descripción </label>
          <InputText v-model.trim="productDescription" required autofocus />
        </div>

        <div class="field">
          <label for="purchasePrice">Precio de Compra </label>
          <InputText v-model.trim="productPurchasePrice" required autofocus />
        </div>

        <div class="field">
          <label style="" for="sellingPrice" >Precio de Venta </label>
          <InputText v-model.trim="productSellingPrice" required autofocus />
        </div>

        <span st style="padding-bottom: 1rem;color: #000;" for="value">Unidad de medida</span>
                 <Dropdown  class="mb-3" style="height: min-content;"  v-model="unidadValue" :options="unidadesDropValue"   required="true" />


                 <span st style="padding-bottom: 1rem;color: #000;" for="value">Proveedor</span>
                 <Dropdown class="mb-3" style="height: min-content;"  v-model="providervalue" :options="providerDropvalues" optionLabel="provider_name"  required="true" />



        <!-- 
                        <div class="field">
                            <label for="name">precio de venta</label>
                            <InputText id="name" v-model.trim="product.pecio" required="true" autofocus />
                        </div> -->


      </div>







      <Button class="text-center" @click="createProduct"
        style="background-color: black; border-radius: 0.5rem; font-weight: bold;margin-bottom: 2rem;"><span
          class="text-center col-12 p-0">AGREGAR PRODUCTO</span></Button>

    </div>











  </Dialog>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { URI, dropServ, categoryValue, providervalue, providerDropvalues, categorieFropValue,unidadValue,unidadesDropValue } from '../../service/conection';
import { uploadProductImage, } from '@/service/sendFileService'
import { formatoPesosColombianos } from '../../service/formatoPesos';



// Define el estado de los productos usando ref
const products = ref([]);
const showProductDialog = ref(false)

// Define la función para obtener los productos
const getProducts = async () => {
  try {
    // Intenta obtener los productos del localStorage
    const storedProducts = localStorage.getItem('products');

    // Si hay datos en el localStorage, asigna directamente a products.value
    if (storedProducts) {
      products.value = JSON.parse(storedProducts);
      return;
    }

    // Si no hay datos en el localStorage, realiza la llamada a la API
    const response = await fetch(`${URI}/products`);
    
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }

    const data = await response.json();
    
    // Asigna los productos a la variable de estado
    products.value = data;

    // Guarda los productos en el localStorage
    localStorage.setItem('products', JSON.stringify(data));
  } catch (error) {
    console.error('Error fetching products:', error);
  }
};

// Usa onMounted para llamar a la función cuando el componente se monta
onMounted(getProducts);
dropServ.categories()
dropServ.providers()

// Devuelve el estado de los productos para usar en el template


const urlPhotoProfile = ref('');
const file = ref(null);

const handleFileChange = (event) => {
  // Accede al archivo seleccionado a través del objeto de evento
  const selectedFile = event.target.files[0];

  if (selectedFile) {
    // Actualiza la referencia al archivo
    file.value = selectedFile;

    // Crea una URL para la vista previa de la imagen
    urlPhotoProfile.value = URL.createObjectURL(selectedFile);
  }
};

const uploadImage = async () => {
  if (!file.value) {
    console.error('No hay una imagen para subir.');
    return;
  }

  try {
    const formData = new FormData();
    formData.append('file', file.value);

    const response = await fetch(`${URI}/upload-product-image/${productName.value}`, {
      method: 'POST',
      body: formData,
    });

    // Manejar la respuesta según tus necesidades
    const responseData = await response.json();

    console.log(responseData);
    location.reload()
  } catch (error) {
    console.error('Error al subir la imagen:', error);
  }
};




const agregarProducto = () => {

  // createProduct()
  uploadImage()
  location.reload



}



const productName = ref("sin nombre");
const productDescription = ref("sin descripcion");
const productPurchasePrice = ref(0);
const productSellingPrice = ref(0);


const createProduct = async () => {
  localStorage.removeItem('products')
  showProductDialog.value = false
  try {
    // Asegurar que si el nombre o descripción son nulos, se envíen como "sin nombre" y "sin descripción"
    const nameToSend = productName.value || 'sin nombre';
    const descriptionToSend = productDescription.value || 'sin descripcion';

    const response = await fetch(`${URI}/products`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        product_name: nameToSend,
        product_description: descriptionToSend,
        product_purchase_price: parseFloat(productPurchasePrice.value) || 0,
        product_selling_price: parseFloat(productSellingPrice.value) || 0,
        unit_of_measure:unidadValue.value || 'sin unidad',
        provider_id:providervalue.value.provider_id,
        category_id:categoryValue.value.category_id

      }),
    });

    // Manejar la respuesta según tus necesidades
    const responseData = await response.json();
    uploadImage()
    getProducts()
    console.log(responseData);
  } catch (error) {
    console.error('Error al crear el producto:', error);
  }

};



const confirmationDialog = ref(false);

const confirmDelete = (productId) => {
  // Al hacer clic en "Eliminar", establece confirmationDialog en true
  confirmationDialog.value = true;

  // Al confirmar la eliminación, ejecuta deleteProduct
  const confirmed = ref(false);
  const handleConfirmation = () => {
    confirmed.value = true;
    deleteProduct(productId);
  };

  return {
    confirmed,
    handleConfirmation,
  };
};

const deleteProduct = async (productId) => {
  localStorage.removeItem('products')
  try {
    // Realiza la solicitud DELETE al servidor para eliminar el producto
    const response = await fetch(`${URI}/products/${productId}`, {
      method: 'DELETE',
      headers: {
        'Content-Type': 'application/json',
      },
    });

    if (response.ok) {
      // Actualiza la lista de productos después de eliminar el producto
      fetchProducts();
      console.log(`Producto con ID ${productId} eliminado exitosamente.`);
    } else {
      console.error('Error al eliminar el producto:', response.statusText);
    }
  } catch (error) {
    console.error('Error en la solicitud DELETE:', error);
  } finally {
    // Restablece el estado de confirmationDialog después de la operación
    confirmationDialog.value = false;
    // location.reload()
    getProducts()
  }
};

// Método para recuperar la lista de productos (puedes ajustar esto según tu implementación)
const fetchProducts = () => {
  // Realiza la lógica para obtener la lista actualizada de productos
  // y actualiza la variable 'products' con los nuevos datos.
};


</script>

<style scoped>
.boton-menu {
  margin: 0;
  border: none;
  background-color: transparent;
  font-size: 20px;
  padding: 0 20px;
}

.dialog-container {
  width: 100%;
  height: 100%;
  /* background-color: red; */
}

.salsa {
  display: flex;
  width: 100%;
  justify-content: space-between;
  align-items: start;
  padding: 0;
  margin: 0;
  color: black;


}

.salsas {
  display: flex;
  width: 100%;
  margin: 0;
  justify-content: space-around;
  color: black;
  padding: 0;

}

.texto {
  /* width: 40%; */
  /* min-width: 200px; */
  padding-right: 20px;
  /* min-width: 200px; */
  /* margin-right: 20px; */
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

label {
  color: #000;
}

.menu-button-new {
  background-color: var(--primary-color);
  padding: 1rem;
  margin: 0 1rem;
  border: none;
  font-size: 20px;
  /* transition: all  0.3s; */
  /* font-weight: bold; */
  border-radius: 10px;
  color: #fff;
  width: 300px;
  transition: all 0.3s ease;
}

.menu-button-new:hover {
  /* filter: brightness(1.5);  
   */
  background-color: black;
  cursor: pointer;
}



.menu-button:hover {
  /* box-shadow: inset 0 0 5px rgba(0, 0, 0, 0.5); */
  /* transform: scale(1.1); */
  /* border-bottom:  2px red; */
  color: var(--primary-color);
  cursor: pointer;


}

.selected {
  box-shadow: 0px 5px 0px var(--primary-color);
  /* font-weight: bold; */

}

.cont-dialog {
  display: flex;
  width: 100%;
  flex-direction: column;
  gap: 40px;
  height: 100%;
  /* align-items: center; */
  justify-content: center;
  /* border: 1px solid red; */
}

.incluye {
  width: 100%;
  /* height: 400px; */
  /* height: 100%; */
  background-color: rgb(160, 160, 160);
}

.foto {
  /* content: 'foto'; */
  width: 100%;
  height: 400px;
  /* height: 100%; */
  background-color: rgb(153, 151, 174);
}

.foto img {
  width: 100%;
  height: 100%;
  object-fit: cover;

  /* height: 100%; */
  /* background-color: rgb(25, 0, 255); */
}
</style>