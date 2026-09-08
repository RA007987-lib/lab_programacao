const form = document.getElementById("form");
const inProduto = document.getElementById("inProduto");
const inPreco = document.getElementById("inPreco");
const outPromocao = document.getElementById("outPromocao");
const outTerceiro = document.getElementById("outTerceiro");

form.addEventListener("submit", function (e) {

    e.preventDefault();

    const produto = inProduto.value;
    const preco = Number(inPreco.value);

    const valorPromocao = preco * 2 + preco * 0.5;
    const valorTerceiro = preco * 0.5;

    outPromocao.textContent =
        produto + " - Promoção: Leve 3 por R$: " +
        valorPromocao.toFixed(2);

    outTerceiro.textContent =
        "O 3º produto custa apenas R$: " +
        valorTerceiro.toFixed(2);

});