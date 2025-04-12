# Relatório Explicativo

Introdução:
-
Este projeto teve como objetivo de criar um estoque de produtos de uma loja, onde seriam listados todos os itens em uma tabela, utilizando python com banco de dados, suas operações CRUD, e buscas filtradas.

Descrição da tabela e dos campos: 
-
  - __tablename__ = "produtos"  // Nomeia a tabela

  - id = db.Column(db.Integer, primary_key=True)  // Adiciona o campo "id" como chave primária
  - nome = db.Column(db.String(30), nullable=False)  // Adiciona o campo "nome" como string que não pode ser vazio
  - preco = db.Column(db.Float, nullable=False)  // Adiciona o campo "preco" como float que não pode ser vazio
  - quantidade = db.Column(db.Integer,nullable=False)  // Adiciona o campo "quantidade" como inteiro que não pode ser vazio

Capturas de telas do código:
- 
![captura-4](https://github.com/user-attachments/assets/b8b45bd7-53dc-4503-a103-71d0c7b5afec)
![captura-3](https://github.com/user-attachments/assets/62439039-c32b-4174-947b-0140f6b15bc3)
![captura-2](https://github.com/user-attachments/assets/231d2abd-3e33-4bc7-ad26-870c63b30c21)
![captura-1](https://github.com/user-attachments/assets/cecaf467-d994-4f4e-9679-587f8fb910a7)


Lista de bibliotecas utilizadas: 
-
- Flask
- SQLAlchemy

Descrições das funcionalidades implementadas:
-
- Homepage: na página inicial, percorre todos os produtos presentes no banco de dados, e retorna estes valores na variável "produtos", se nenhum estiver visível, mostra "Nenhum produto encontrado"
- Adicionar: por meio de um formulário, envia as informações para o banco de dados, criando um novo registro
- Editar: busca pelas informações do produto pelo id, e quando encontra, mostra as informações para serem alteradas em um formulário parecido com o de "adicionar"
- Remover: com base no id do produto, executa a função delete do banco de dados no registro com mesmo valor de id
- Pesquisar: por meio de um input na página inicial, recebe esse input e compara a informação, se or número busca por id, se não procura por nome
