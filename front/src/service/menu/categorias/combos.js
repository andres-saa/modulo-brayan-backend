import { fotos } from "../fotos"
import { adicionesHamburguesas } from "../adiciones/adicionesHamburguesas"
import { adicioneSalchipapas } from "../adiciones/adicionesSalchipapas"
import { topings } from "../adiciones/Topings"

const categoryCombos = {
    "category": { "id": 6, "name": "Bebidas" },
    "products": [

        {
            id: 37,
            name: "BURGERMONSTER 3X2",
            price: 50000,
            description: "",
            category_id: 6,
            adiciones:adicionesHamburguesas,
            get img_96x96() {return fotos[this.id]['96x96']},
            get img_300x300() {return fotos[this.id]['300x300']},
            get img_600x600() {return fotos[this.id]['600x600']},
           //cuando registres un combo la adicion la pones referenciando el archivo de las adiciones como tal en bade al tipo de combo

        },
        {
            id: 37,
            name: "MADURIMONSTER+GASEOSA 400 ML",
            price: 35500,
            description: "",
            category_id: 6,
            adiciones:adicioneSalchipapas,
            get img_96x96() {return fotos[this.id]['96x96']},
            get img_300x300() {return fotos[this.id]['300x300']},
            get img_600x600() {return fotos[this.id]['600x600']},
           //cuando registres un combo la adicion la pones referenciando el archivo de las adiciones como tal en bade al tipo de combo

        },
        {
            id: 37,
            name: "PORKYMONSTER + GASEOSA 400 ML",
            price: 49000,
            description: "",
            category_id: 6,
            adiciones:adicioneSalchipapas,
            get img_96x96() {return fotos[this.id]['96x96']},
            get img_300x300() {return fotos[this.id]['300x300']},
            get img_600x600() {return fotos[this.id]['600x600']},
           //cuando registres un combo la adicion la pones referenciando el archivo de las adiciones como tal en bade al tipo de combo

        },
        {
            id: 37,
            name: "RANCHIMONSTER + GASEOSA 400 ML",
            price: 46000,
            description: "",
            category_id: 6,
            adiciones:adicioneSalchipapas,
            get img_96x96() {return fotos[this.id]['96x96']},
            get img_300x300() {return fotos[this.id]['300x300']},
            get img_600x600() {return fotos[this.id]['600x600']},
           //cuando registres un combo la adicion la pones referenciando el archivo de las adiciones como tal en bade al tipo de combo

        },
      
       ]
}

export {categoryCombos}