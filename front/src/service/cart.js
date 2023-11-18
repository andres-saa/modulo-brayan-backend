import { ref } from "vue";


const carro = ref({products:[],total:0})

const add = (product) => {

    if (!localStorage.getItem('cart')){
        localStorage.setItem('cart',{products:[],total:0})
        // localStorage.setItem('totalCart',0)
    }
    const cart = {...JSON.parse(localStorage.getItem('cart'))}
    // const cart = {products:[],total:0}
    // localStorage.setItem('cart',JSON.stringify(cart.value))
    // console.log(JSON.parse(localStorage.getItem('cart')))
    cart.products.push(product)
    cart.total = Number(cart.total)+product.price
    localStorage.setItem('cart',JSON.stringify(cart))
    carro.value = cart
    console.log(localStorage.getItem('cart'))
}

const remove = (productToRemove) => {
    if (localStorage.getItem('cart')) {
        const cart = { ...JSON.parse(localStorage.getItem('cart')) };
        const indexToRemove = cart.products.findIndex((product) => {
            return product.name === productToRemove.name && product.price === productToRemove.price;
        });

        if (indexToRemove !== -1) {
            const removedProduct = cart.products.splice(indexToRemove, 1)[0];
            cart.total = Number(cart.total) - removedProduct.price;
            localStorage.setItem('cart', JSON.stringify(cart));
            carro.value = cart;
            console.log(localStorage.getItem('cart'));
        }
    }
}



const useCart = {
    add,
    remove
}



export {useCart,carro}