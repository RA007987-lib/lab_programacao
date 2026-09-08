const form = document.getElementById("form");
const inNumero = document.getElementById("inNumero");
const outResultado = document.getElementById("outResultado");

form.addEventListener("submit", function (e) {

    e.preventDefault();

    const numero = Number(inNumero.value);

    if (numero % 2 == 0) {
        outResultado.textContent = numero + " é par";
    } else {
        outResultado.textContent = numero + " é ímpar";
    }

});