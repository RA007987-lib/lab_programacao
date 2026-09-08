const form = document.getElementById("form");
const inValor = document.getElementById("inValor");
const inTempo = document.getElementById("inTempo");
const outValor = document.getElementById("outValor");

form.addEventListener("submit", function (e) {

    e.preventDefault();

    const valor = Number(inValor.value);
    const tempo = Number(inTempo.value);

    const blocos = Math.ceil(tempo / 15);

    const total = blocos * valor;

    outValor.textContent = "Valor a Pagar R$: " + total.toFixed(2);

});