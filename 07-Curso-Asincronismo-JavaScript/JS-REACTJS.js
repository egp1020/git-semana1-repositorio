// Template Literals

let nombre = "Estefanía";
const apellido = "Garcés Pérez";

console.log(nombre + " "+ apellido);
console.log(`${nombre} ${apellido}`);

// Ejemplo React
/* function componenteColor({ backgroundColor }){
    return (<div className = {`bg-color-${backgroundColor}`}>Hola</div>)
} */

// Shorthand property names
const edad = 21;
const twitter = 'http://twitter.com/egp1020';

const persona = {
    nombre: nombre,
    edad: edad,
    twitter: twitter,
};

const persona_prueba = {
    nombre,
    edad,
    twitter,
};

console.log(persona)
console.log(persona_prueba)

// Ejemplo con React
/* function componenteEstado({initialState, totalCount}){
    const [state, setState] = useState({initialState, totalCount});
} */

// Arrow Functions
function nombreFuncion(){
    return "hola";
}

const funcionFlecha  = () => {
    return "hola";
}
const funcionFlechaLinea  = () => "hola";
a = nombreFuncion();
b = funcionFlecha();
c = funcionFlechaLinea();

console.log(a)
console.log(b)
console.log(c)

// Ejemplo con React
/* function ListaTareas({}){
    return (
        <ul>
            {listado.map(elemento => (<li>{elemento.nombre}</li>))}
        </ul>
    )
} */

// Destructuring
const cuadrado = {
    x:10,
    y:10,
};

const calcularArea = cuadrado => cuadrado.x * cuadrado.y;
let valor = calcularArea(cuadrado);
console.log(valor);

const calcularAreaPrueba = cuadrado => {
    const {x,y} = cuadrado;
    return x*y;
}

valor = calcularAreaPrueba(cuadrado)
;
console.log(valor);