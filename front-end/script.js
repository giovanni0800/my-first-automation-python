const loginForm = document.getElementById('loginForm');
const produtoForm = document.getElementById('produtoForm');
const tabela = document.getElementById('tabela');

// Função para logar
loginForm.addEventListener('submit', (event) => {
    event.preventDefault(); // Evita o envio padrão do formulário

    const usuario = document.getElementById('usuario').value;
    const senha = document.getElementById('senha').value;

    // Simulação de login (sem validação real)
    if (usuario === 'admin@admin.com' && senha === '123') {
        window.location.href = 'cadastrar_itens.html'; // Redireciona para cadastrar_itens.html
    } else {
        alert('Usuário ou senha inválidos.');
    }
});

// Função para cadastrar produto
produtoForm.addEventListener('submit', (event) => {
    // ... (mesmo código da função original)
});
