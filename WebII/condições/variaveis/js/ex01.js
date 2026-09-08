const form = document.querySelector("#form");

form.addEventListener("submit", function(event) {

    event.preventDefault();

    const medicamento = document.querySelector("#inMedicamento").value;
    const preco = Number(document.querySelector("#inPreco").value);

    const valorPromocao = preco * 2;

    document.querySelector("#outPromocao").textContent =
        "Promoção de " + medicamento;

    document.querySelector("#outValor").textContent =
        "Leve 2 por apenas R$: " + valorPromocao.toFixed(2);
});