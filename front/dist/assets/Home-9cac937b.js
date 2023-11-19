import{_ as B,r as n,o as G,d as k,a as h,b as P,c as S,e,f as a,w as C,F as O,g as L,n as H,U as g,h as J,t as d,u as r,i as R,j as U,p as N,k as f,l as I,m as v,q as z,s as b,v as K,x as Q}from"./index-9f8dd084.js";const l=p=>(K("data-v-a11d55af"),p=p(),Q(),p),W=l(()=>e("h1",null,"Productos",-1)),X={class:"grid"},Y={class:"p-0",style:{"border-radius":"1rem",overflow:"hidden","box-shadow":"0px 0px 20px rgba(0, 0, 0, 0.5)"}},Z={class:"col-12 m-0",style:{"background-color":"rgb(255, 230, 0)","box-shadow":"0px 0px 10px rgba(0, 0, 0, 0.5)"}},ee={class:"text-xl p-1",style:{"font-weight":"bold","text-transform":"uppercase"}},oe={class:"info p-3 pt-5"},te={class:"grid"},se=l(()=>e("span",{class:"text-l text-left col",style:{"font-weight":"bold","min-width":"max-content"}}," CATEGORIA ",-1)),le={class:"text-l text-right col",style:{"font-weight":""}},ae={class:"grid"},re=l(()=>e("span",{class:"text-l text-left col",style:{"font-weight":"bold","min-width":"max-content"}}," DESCRIPCION ",-1)),ne={class:"text-l text-right col",style:{"font-weight":""}},ie={class:"grid"},de=l(()=>e("span",{class:"text-l text-left col",style:{"font-weight":"bold","min-width":"max-content"}}," UNIDAD DE MEDIDA ",-1)),ce={class:"text-l text-right col",style:{"font-weight":""}},ue={class:"grid"},pe=l(()=>e("span",{class:"text-l text-left col",style:{"font-weight":"bold","min-width":"max-content"}}," PRECIO DE COMPRA ",-1)),_e={class:"text-l text-right col",style:{"font-weight":""}},me={class:"grid"},he=l(()=>e("span",{class:"text-l text-left col",style:{"font-weight":"bold","min-width":"max-content"}}," PRECIO DE VENTA ",-1)),ge={class:"text-l text-right col",style:{"font-weight":""}},fe={class:"grid"},ve=l(()=>e("span",{class:"text-l text-left col",style:{"font-weight":"bold","min-width":"max-content"}}," PROVEEDOR ",-1)),be={class:"text-l text-right col",style:{"font-weight":""}},xe={class:"botones col-12",style:{display:"flex","justify-content":"end"}},ye=["onClick"],we={class:"cont-dialog"},Ve=l(()=>e("div",null,null,-1)),De={class:"dialog-container"},Ee={class:"field"},Pe=l(()=>e("label",{for:"name"},"Nombre ",-1)),Se=l(()=>e("span",{st:"",style:{"padding-bottom":"1rem",color:"#000"},for:"value"},"Categoria",-1)),Ce={class:"field"},Ie=l(()=>e("label",{for:"description"},"Descripción ",-1)),Te={class:"field"},ke=l(()=>e("label",{for:"purchasePrice"},"Precio de Compra ",-1)),Oe={class:"field"},Re=l(()=>e("label",{style:{},for:"sellingPrice"},"Precio de Venta ",-1)),Ue=l(()=>e("span",{st:"",style:{"padding-bottom":"1rem",color:"#000"},for:"value"},"Unidad de medida",-1)),Ne=l(()=>e("span",{st:"",style:{"padding-bottom":"1rem",color:"#000"},for:"value"},"Proveedor",-1)),Ae=l(()=>e("span",{class:"text-center col-12 p-0"},"AGREGAR PRODUCTO",-1)),$e={__name:"Home",setup(p){const x=n([]),u=n(!1),y=async()=>{try{const s=localStorage.getItem("products");if(s){x.value=JSON.parse(s);return}const o=await fetch(`${g}/products`);if(!o.ok)throw new Error(`HTTP error! Status: ${o.status}`);const i=await o.json();x.value=i,localStorage.setItem("products",JSON.stringify(i))}catch(s){console.error("Error fetching products:",s)}};G(y),k.categories(),k.providers(),n("");const T=n(null),A=async()=>{if(!T.value){console.error("No hay una imagen para subir.");return}try{const s=new FormData;s.append("file",T.value);const i=await(await fetch(`${g}/upload-product-image/${_.value}`,{method:"POST",body:s})).json();console.log(i),location.reload()}catch(s){console.error("Error al subir la imagen:",s)}},_=n("sin nombre"),w=n("sin descripcion"),V=n(0),D=n(0),$=async()=>{localStorage.removeItem("products"),u.value=!1;try{const s=_.value||"sin nombre",o=w.value||"sin descripcion",c=await(await fetch(`${g}/products`,{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({product_name:s,product_description:o,product_purchase_price:parseFloat(V.value)||0,product_selling_price:parseFloat(D.value)||0,unit_of_measure:v.value||"sin unidad",provider_id:b.value.provider_id,category_id:f.value.category_id})})).json();A(),y(),console.log(c)}catch(s){console.error("Error al crear el producto:",s)}},q=n(!1),j=async s=>{localStorage.removeItem("products");try{const o=await fetch(`${g}/products/${s}`,{method:"DELETE",headers:{"Content-Type":"application/json"}});o.ok?(M(),console.log(`Producto con ID ${s} eliminado exitosamente.`)):console.error("Error al eliminar el producto:",o.statusText)}catch(o){console.error("Error en la solicitud DELETE:",o)}finally{q.value=!1,y()}},M=()=>{};return(s,o)=>{const i=h("Button"),c=h("InputText"),E=h("Dropdown"),F=h("Dialog");return P(),S(O,null,[e("div",null,[W,a(i,{onClick:o[0]||(o[0]=t=>u.value=!u.value),style:{"background-color":"black","border-radius":"0.5rem","font-weight":"bold","margin-bottom":"2rem"}},{default:C(()=>[J("AGREGAR PRODUCTO")]),_:1}),e("div",X,[(P(!0),S(O,null,L(x.value,t=>(P(),S("div",{class:"col-12 md:col-6 lg:col-4 xl:col-3",key:t.id},[e("div",Y,[e("div",Z,[e("p",ee,d(t.product_name),1)]),e("div",oe,[e("div",te,[se,e("p",le,d(r(R).find(m=>m.category_id===t.category_id).category_name),1)]),e("div",ae,[re,e("p",ne,d(t.product_description),1)]),e("div",ie,[de,e("p",ce,d(t.unit_of_measure),1)]),e("div",ue,[pe,e("p",_e,d(r(U)(t.product_purchase_price)),1)]),e("div",me,[he,e("p",ge,d(r(U)(t.product_selling_price)),1)]),e("div",fe,[ve,e("p",be,d(r(N).find(m=>m.provider_id===t.provider_id).provider_name),1)])]),e("div",xe,[e("button",{onClick:m=>j(t.product_id),style:{color:"white","background-color":"rgb(255, 83, 83)","border-radius":"0.5rem",border:"none","font-weight":"bold",padding:"0.5rem 1rem",right:"1rem"}},"Eliminar",8,ye)])])]))),128))])]),a(F,{visible:u.value,"onUpdate:visible":o[8]||(o[8]=t=>u.value=t),style:H([{width:"500px"},{"background-color":"white","border-radius":"1rem",overflow:"hidden"}]),header:"Registrar un Usuario",modal:!0,class:"p-fluid"},{default:C(()=>[e("div",we,[Ve,e("div",De,[e("div",Ee,[Pe,a(c,{modelValue:_.value,"onUpdate:modelValue":o[1]||(o[1]=t=>_.value=t),modelModifiers:{trim:!0},required:"",autofocus:""},null,8,["modelValue"])]),Se,a(E,{class:"mb-3",style:{height:"min-content"},modelValue:r(f),"onUpdate:modelValue":o[2]||(o[2]=t=>I(f)?f.value=t:null),options:r(R),optionLabel:"category_name",required:"true"},null,8,["modelValue","options"]),e("div",Ce,[Ie,a(c,{modelValue:w.value,"onUpdate:modelValue":o[3]||(o[3]=t=>w.value=t),modelModifiers:{trim:!0},required:"",autofocus:""},null,8,["modelValue"])]),e("div",Te,[ke,a(c,{modelValue:V.value,"onUpdate:modelValue":o[4]||(o[4]=t=>V.value=t),modelModifiers:{trim:!0},required:"",autofocus:""},null,8,["modelValue"])]),e("div",Oe,[Re,a(c,{modelValue:D.value,"onUpdate:modelValue":o[5]||(o[5]=t=>D.value=t),modelModifiers:{trim:!0},required:"",autofocus:""},null,8,["modelValue"])]),Ue,a(E,{class:"mb-3",style:{height:"min-content"},modelValue:r(v),"onUpdate:modelValue":o[6]||(o[6]=t=>I(v)?v.value=t:null),options:r(z),required:"true"},null,8,["modelValue","options"]),Ne,a(E,{class:"mb-3",style:{height:"min-content"},modelValue:r(b),"onUpdate:modelValue":o[7]||(o[7]=t=>I(b)?b.value=t:null),options:r(N),optionLabel:"provider_name",required:"true"},null,8,["modelValue","options"])]),a(i,{class:"text-center",onClick:$,style:{"background-color":"black","border-radius":"0.5rem","font-weight":"bold","margin-bottom":"2rem"}},{default:C(()=>[Ae]),_:1})])]),_:1},8,["visible"])],64)}}},je=B($e,[["__scopeId","data-v-a11d55af"]]);export{je as default};