/* empty css                                                                     */import{_ as w,y as z,a as k,b as o,c as s,e,u as d,U as I,z as M,t as g,f as C,j as T,A as b,P as V,B,r as y,C as E,o as f,D as P,E as l,G as j,H as N,F as _,g as v,I as h,J as W,w as A,v as D,x as L,h as O}from"./index-9f8dd084.js";const U={class:"cont",style:{"background-color":"white"}},F=["src"],G={style:{height:"2rem",display:"flex","padding-top":"1rem"}},H={style:{"font-size":"1rem","font-weight":"bold"}},R={class:"info"},J={class:"text-xl",style:{"font-size":"rem","font-weight":"bold"}},q={__name:"TarjetaMenu",props:{product:{type:Object,default:{}}},setup(r){const a=r,m=z(),p=c=>{B.add(c),m.add({severity:"success",summary:"Agregado al carrito",detail:a.product.name,life:3e3})},n=c=>{c.target.src="https://novatocode.online/assets/logo-f2daca0e.png"};return(c,i)=>{const u=k("Toast");return o(),s("div",U,[e("div",{class:"imagen-cont",style:{position:""},onClick:i[0]||(i[0]=x=>d(M)(r.product))},[e("img",{class:"imagen",onError:n,src:`${d(I)}/read_product_image/300/${a.product.id}`,alt:""},null,40,F)]),e("div",G,[e("p",H,g(a.product.name),1)]),C(u,{style:{"box-shadow":"none"}}),e("div",R,[e("div",J,g(d(T)(a.product.price)),1),e("button",{onClick:i[1]||(i[1]=x=>p(a.product)),class:"add-cart-btn"},[e("i",{class:b(["icono text-xl lg:text-4xl p-2",d(V).SHOPPING_CART])},null,2)])])])}}},K=w(q,[["__scopeId","data-v-ba92e83b"]]);const Q=r=>(D("data-v-c0de3e49"),r=r(),L(),r),X=Q(()=>e("p",{style:{"text-align":"center",width:"100%","font-size":"36px","font-weight":"bold"}},[O(" Monster "),e("span",{style:{color:"var(--primary-color)"}},"Menu")],-1)),Y={key:0,style:{top:"5rem",position:"sticky","z-index":"50","background-color":"white",height:"6rem",outline:"2rem solid white","margin-bottom":"3rem",padding:"2rem",display:"flex"},class:""},Z={class:"grid col-12 m-0",style:{"margin-bottom":"",outline:"0.6rem solid var(--primary-color)",padding:"0rem 0","border-radius":"100px",height:"min-content","background-color":"white"}},ee={class:"",style:{padding:"0",display:"flex","z-index":"2",width:"100%",height:"100%",left:"0","overflow-x":"auto"}},te=["onClick"],oe={class:"d-flex flex-wrap justify-content-center align-items-center"},se=["onClick"],ae={class:"grid xl:col-10 xl:m-auto",style:{"background-color":"","margin-bottom":"5rem"}},ne={class:"xl:col-3 lg:col-4 md:p-3 col-6 p-1"},re={__name:"MenuView",setup(r){const a=y(window.innerWidth),m=E(()=>a.value<720),p=()=>{a.value=window.innerWidth};f(()=>{window.addEventListener("resize",p)}),P(()=>{window.removeEventListener("resize",p)});const n=y(l.value[0].menus[0]);y({});const c=u=>{n.value=u,console.log(u)};return j(l,()=>{n.value={category:l.value[0].menus[1].category,products:l.value[0].menus[1].products},console.log("cambio")}),f(async()=>{N.value=!0}),(u,x)=>{const $=k("Toolbar");return o(),s(_,null,[X,m.value?(o(),s("div",Y,[e("div",Z,[e("div",ee,[(o(!0),s(_,null,v(d(l)[0].menus,t=>(o(),s("div",{class:"",style:{},key:t.category.name},[e("button",{style:{margin:"0.5rem",padding:"0.1rem 1rem","border-radius":"100px","background-color":"#00000015"},class:b(["menu-button",(n.value.category.name==t.category.name,"")]),onClick:S=>c({category:t.category,products:t.products})},g(t.category.name),11,te)]))),128))])])])):h("",!0),m.value?h("",!0):(o(),W($,{key:1,style:{"margin-bottom":"1rem"}},{center:A(()=>[e("div",oe,[(o(!0),s(_,null,v(d(l)[0].menus,t=>(o(),s("div",{key:t.category.name},[e("button",{class:b(["menu-button",n.value.category.name==t.category.name?"selected":""]),onClick:S=>c({category:t.category,products:t.products})},g(t.category.name),11,se)]))),128))])]),_:1})),e("div",ae,[n.value?(o(!0),s(_,{key:0},v(n.value.products,t=>(o(),s("div",ne,[C(K,{style:{width:"100%"},class:"",product:t},null,8,["product"])]))),256)):h("",!0)])],64)}}},de=w(re,[["__scopeId","data-v-c0de3e49"]]);export{de as default};