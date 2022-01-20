/* Variables */

var nombre = "Estefanía"; // var es la representación donde se guardarán valores.
console.log(nombre); // Estefanía

/*
    Al momento de estar generando una variable se generan dos estados de la variable que es: declaración e inicialización.
*/

// Declaración de variables
var nombre; // Variable declarada, sin valor

console.log(nombre); // undefined, espacio reservado cuando no tiene valor definido.

// Inicialización de variables
nombre = "Juanito"; // Variable declarada y valor asignado

console.log(nombre); // Juanito

var elementos = ["Celular", "Laptop", "Teclado"]; // Arreglo de elementos de tipo string, " = " es el operador de asignación.
console.log(elementos); // ["Celular", "Laptop", "Teclado"]
var primerElemento = elementos[0];  // Toma el primer elemento del arreglo.
console.log(primerElemento); // Celular --> String

var persona = { // Objeto de tipo persona
    nombre: "Estefanía", // Propiedad nombre con valor Estefanía
    apellido: "González", // Propiedad apellido con valor González
    edad: 25 // Propiedad edad con valor 25
}

console.log(persona); // { nombre: 'Estefanía', apellido: 'González', edad: 25 }
