import{_ as T,r as s,o as C,a as _,b as m,c as f,e as o,f as c,w as h,F as b,g as I,n as D,U as v,h as R,t as A,v as N,x as O}from"./index-9f8dd084.js";const i=l=>(N("data-v-fe04a086"),l=l(),O(),l),$=i(()=>o("h1",null,"CATEGORIAS",-1)),P={class:"grid"},G={class:"p-0",style:{"border-radius":"1rem",overflow:"hidden","box-shadow":"0px 0px 20px rgba(0, 0, 0, 0.5)"}},U={class:"col-12 m-0",style:{"background-color":"rgb(255, 230, 0)","box-shadow":"0px 0px 10px rgba(0, 0, 0, 0.5)"}},V={class:"text-xl p-0",style:{"font-weight":"bold","text-transform":"uppercase"}},j={class:"botones col-12",style:{display:"flex","justify-content":"end"}},B=["onClick"],J={class:"cont-dialog"},L=i(()=>o("div",null,null,-1)),F={class:"dialog-container"},M={class:"field"},q=i(()=>o("label",{for:"name"},"Nombre ",-1)),z=i(()=>o("span",{class:"text-center col-12 p-0"},"AGREGAR PRODUCTO",-1)),H={__name:"category",setup(l){const d=s([]),n=s(!1),u=async()=>{try{const t=localStorage.getItem("categories");if(t)d.value=JSON.parse(t);else{const e=await fetch(`${v}/categories`);if(!e.ok)throw new Error(`HTTP error! Status: ${e.status}`);const a=await e.json();d.value=a,localStorage.setItem("categories",JSON.stringify(a))}}catch(t){console.error("Error fetching categories:",t)}};C(u),s(""),s(null);const g=s("sin nombre"),y=s("sin descripcion");s(0),s(0);const x=async()=>{localStorage.removeItem("categories"),n.value=!1;try{const t=g.value||"sin nombre",e=y.value||"sin descripcion",p=await(await fetch(`${v}/categories`,{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({category_name:t})})).json();u(),console.log(p)}catch(t){console.error("Error al crear el producto:",t)}},w=s(!1),E=async t=>{localStorage.removeItem("categories");try{const e=await fetch(`${v}/categories/${t}`,{method:"DELETE",headers:{"Content-Type":"application/json"}});e.ok?(S(),console.log(`Producto con ID ${t} eliminado exitosamente.`)):console.error("Error al eliminar el producto:",e.statusText)}catch(e){console.error("Error en la solicitud DELETE:",e)}finally{w.value=!1,u()}},S=()=>{};return(t,e)=>{const a=_("Button"),p=_("InputText"),k=_("Dialog");return m(),f(b,null,[o("div",null,[$,c(a,{onClick:e[0]||(e[0]=r=>n.value=!n.value),style:{"background-color":"black","border-radius":"0.5rem","font-weight":"bold","margin-bottom":"2rem"}},{default:h(()=>[R("AGREGAR CATEGORIA")]),_:1}),o("div",P,[(m(!0),f(b,null,I(d.value,r=>(m(),f("div",{class:"col-12 md:col-6 lg:col-4 xl:col-3",key:r.id},[o("div",G,[o("div",U,[o("p",V,A(r.category_name),1)]),o("div",j,[o("button",{onClick:K=>E(r.category_id),style:{color:"white","background-color":"rgb(255, 83, 83)","border-radius":"0.5rem",border:"none","font-weight":"bold",padding:"0.5rem 1rem",right:"1rem"}},"Eliminar",8,B)])])]))),128))])]),c(k,{visible:n.value,"onUpdate:visible":e[2]||(e[2]=r=>n.value=r),style:D([{width:"500px"},{"background-color":"white","border-radius":"1rem",overflow:"hidden"}]),header:"Registrar un Usuario",modal:!0,class:"p-fluid"},{default:h(()=>[o("div",J,[L,o("div",F,[o("div",M,[q,c(p,{modelValue:g.value,"onUpdate:modelValue":e[1]||(e[1]=r=>g.value=r),modelModifiers:{trim:!0},required:"",autofocus:""},null,8,["modelValue"])])]),c(a,{class:"text-center",onClick:x,style:{"background-color":"black","border-radius":"0.5rem","font-weight":"bold","margin-bottom":"2rem"}},{default:h(()=>[z]),_:1})])]),_:1},8,["visible"])],64)}}},W=T(H,[["__scopeId","data-v-fe04a086"]]);export{W as default};
