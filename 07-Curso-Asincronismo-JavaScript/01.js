/* Asincronismo
 JS es un lenguaje de programación asíncrono y no bloqueante con un controlador 
 de eventos conocido como event loop implementado en un único hilo para las interfaces
 de entrada y de salida.

 Acciones que no suceden al mismo tiempo.
*/

/* Memory Heap
    https://felixgerschau.com/javascript-memory-management/#:~:text=The%20heap%20is%20a%20different,also%20called%20dynamic%20memory%20allocation.
    https://developer.mozilla.org/es/docs/Web/JavaScript/Memory_Management
*/

function multiplicarNum(num) {
    return num - 2;
}

function calcular() {
    let numero = 10-2
    return multiplicarNum(numero)
}

console.log(calcular());

alert("Hello World");