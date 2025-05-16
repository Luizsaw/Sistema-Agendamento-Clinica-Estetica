document.getElementById("form-agendamento").addEventListener("submit", async function (e) {
  e.preventDefault();

  const dados = {
    nome: document.getElementById("nome").value,
    email: document.getElementById("email").value,
    telefone: document.getElementById("telefone").value,
    data: document.getElementById("data").value,
    horario: document.getElementById("hora").value,
    servico: document.getElementById("servico").value,
  };

  try {
    const resposta = await fetch("http://192.168.0.158:5000/agendar", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(dados),
    });

    const resultado = await resposta.json();

    if (resposta.ok) {
      document.getElementById("mensagem").innerText = "Agendamento realizado com sucesso!";
    } else {
      document.getElementById("mensagem").innerText = "Erro: " + (resultado.detail || "Erro desconhecido.");
    }
  } catch (erro) {
    console.error(erro);
    document.getElementById("mensagem").innerText = "Erro de conexão com o servidor.";
  }
});

