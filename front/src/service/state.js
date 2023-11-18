import { ref } from "vue";

const showProductDialog = ref(false)
const showSiteDialog = ref(false)
const productDialog = ref({})


const setShowDialog =()=>{
    showSiteDialog.value = !showSiteDialog.value
    console.log('hola')
  }

  const setProductDialog =(product)=>{
    showProductDialog.value = !showProductDialog.value
    console.log('hola')
    if (product) {
      productDialog.value = product

    }
  }



export {showSiteDialog,setShowDialog,showProductDialog,setProductDialog,productDialog}