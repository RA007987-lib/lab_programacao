const frm=document.querySelector("form")
const resp=document.querySelector("h3")
// cria um "ouvinte" de evento, acionado quando o botão submitir foi clicado.
frm.addEventListener("submit", (e)=> {
    const nome = frm.inNome.value // obtem valor cx texto
    resp.innerText = `Olá ${nome}`
    e.preventDefault() // evita o envio do form
})