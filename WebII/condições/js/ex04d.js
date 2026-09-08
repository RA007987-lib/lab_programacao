const form = document.getElementById("form");
const inLadoA = document.getElementById("inLadoA");
const inLadoB = document.getElementById("inLadoB");
const inLadoC = document.getElementById("inLadoC");
const outResultado = document.getElementById("outResultado");
const outTipo = document.getElementById("outTipo");

form.addEventListener("submit", function (e) {

    e.preventDefault();

    const ladoA = Number(inLadoA.value);
    const ladoB = Number(inLadoB.value);
    const ladoC = Number(inLadoC.value);

    if (ladoA + ladoB <= ladoC ||
        ladoA + ladoC <= ladoB ||
        ladoB + ladoC <= ladoA) {

        outResultado.textContent =
            "Lados não podem formar um triângulo";

        outTipo.textContent = "";

    } else {

        outResultado.textContent =
            "Lados podem formar um triângulo";

        if (ladoA == ladoB && ladoB == ladoC) {

            outTipo.textContent = "Tipo: Equilátero";

        } else if (ladoA == ladoB ||
                   ladoA == ladoC ||
                   ladoB == ladoC) {

            outTipo.textContent = "Tipo: Isósceles";

        } else {

            outTipo.textContent = "Tipo: Escaleno";

        }
    }

});