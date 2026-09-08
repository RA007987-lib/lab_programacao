const form = document.getElementById("form");
const inValor = document.getElementById("inValor");
const outTempo = document.getElementById("outTempo");
const outTroco = document.getElementById("outTroco");
const outMensagem = document.getElementById("outMensagem");

form.addEventListener("submit", function (e) {

    e.preventDefault();

    const valor = Number(inValor.value);

    let tempo;
    let troco;

    if (valor < 1.00) {

        outMensagem.textContent = "Valor Insuficiente";
        outTempo.textContent = "";
        outTroco.textContent = "";

    } else if (valor < 1.75) {

        tempo = 30;
        troco = valor - 1.00;

        outTempo.textContent = "Tempo: " + tempo + " min";
        outTroco.textContent = "Troco R$: " + troco.toFixed(2);

    } else if (valor < 3.00) {

        tempo = 60;
        troco = valor - 1.75;

        outTempo.textContent = "Tempo: " + tempo + " min";
        outTroco.textContent = "Troco R$: " + troco.toFixed(2);

    } else {

        tempo = 120;
        troco = valor - 3.00;

        outTempo.textContent = "Tempo: " + tempo + " min";
        outTroco.textContent = "Troco R$: " + troco.toFixed(2);

    }

});