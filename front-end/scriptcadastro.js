// Função para cadastrar produto
produtoForm.addEventListener('submit', (event) => {
    event.preventDefault(); // Evita o envio padrão do formulário

    const codigo = document.getElementById('codigo').value;
    const marca = document.getElementById('marca').value;
    const tipo = document.getElementById('tipo').value;
    const categoria = document.getElementById('categoria').value;
    const preco = document.getElementById('preco').value;
    const custo = document.getElementById('custo').value;
    const observacoes = document.getElementById('observacoes').value;

    // Cria a anotação na parte inferior da tela
    const anotacao = document.createElement('div');
    anotacao.classList.add('anotacao'); // Adiciona uma classe para estilizar
    anotacao.innerHTML = `
        <h2>Produto Cadastrado</h2>
        <table border="1">
          <tr><th>Código:</th><td>${codigo}</td></tr>
          <tr><th>Marca:</th><td>${marca}</td></tr>
          <tr><th>Tipo:</th><td>${tipo}</td></tr>
          <tr><th>Categoria:</th><td>${categoria}</td></tr>
          <tr><th>Preço:</th><td>R$ ${preco}</td></tr>
          <tr><th>Custo:</th><td>R$ ${custo}</td></tr>
          <tr><th>Observações:</th><td>${observacoes}</td></tr>
        </table>
    `;
    tabela.appendChild(anotacao); // Adiciona a anotação à tabela

    // Limpa os campos do formulário
    produtoForm.reset();
});
