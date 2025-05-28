document.getElementById("cadastroForm").addEventListener("submit", function (e) {
    e.preventDefault();
    const email = document.getElementById("email").value;
    const senha = document.getElementById("senha").value;
  
    alert(`Cadastro realizado com:\nEmail: ${email}\nSenha: ${senha}`);
  });
  