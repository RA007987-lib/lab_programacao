const form = document.getElementById("form");
const inPermitida = document.getElementById("inPermitida");
const inCondutor = document.getElementById("inCondutor");
const outSituacao = document.getElementById("outSituacao");

form.addEventListener("submit", function (e) {

    e.preventDefault();

    const permitida = Number(inPermitida.value);
    const condutor = Number(inCondutor.value);

    if (condutor <= permitida) {

        outSituacao.textContent = "Situação: Sem Multa";

    } else if (condutor <= permitida * 1.20) {

        outSituacao.textContent = "Situação: Multa Leve";

    } else {

        outSituacao.textContent = "Situação: Multa Grave";

    }

});