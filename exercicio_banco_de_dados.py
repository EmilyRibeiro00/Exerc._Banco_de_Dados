import sqlite3

conexao = sqlite3.connect('Banco')
cursor = conexao.cursor()

#1. Crie uma tabela chamada "alunos" com os seguintes campos: id(inteiro), nome (texto), idade (inteiro) e curso (texto).
cursor.execute('CREATE TABLE alunos(id INT, nome VARCHAR(100), idade INT, curso VARCHAR(100));')

#2. Insira pelo menos 5 registros de alunos na tabela que você criou no exercício anterior
cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(1,"Isadora",18,"Farmacia")')
cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(2,"Mateus",22,"Engenharia")')
cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(3,"Alejandro",19,"Medicina")')
cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(4,"Fernanda",21,"Enfermagem")')
cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(5,"Ruan",25,"BICT")')
cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(6,"Larissa",28,"Engenharia")')
cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(7,"Pedro",23,"Engenharia")')

#3. Consultas Básicas -> Escreva consultas SQL para realizar as seguintes tarefas:
# a) Selecionar todos os registros da tabela "alunos".
dados = cursor.execute('SELECT * FROM alunos')
for aluno in dados:
    print(aluno)

# b) Selecionar o nome e a idade dos alunos com mais de 20 anos.
dados = cursor.execute('SELECT * FROM alunos WHERE idade>20')
for aluno in dados:
    print(aluno)

# c) Selecionar os alunos do curso de "Engenharia" em ordem alfabética.
dados = cursor.execute('SELECT * FROM alunos WHERE curso="Engenharia" ORDER BY nome')
for aluno in dados:
    print(aluno)

# d) Contar o número total de alunos na tabela
cursor.execute('SELECT COUNT(*) AS total_alunos FROM alunos;')
resultado = cursor.fetchone()
total_alunos = resultado[0]
print("Total de alunos na tabela:", total_alunos)

#4. Atualização e Remoção
# a) Atualize a idade de um aluno específico na tabela.
cursor.execute('UPDATE alunos SET idade=26 WHERE nome="Ruan"')

# b) Remova um aluno pelo seu ID.
cursor.execute('DELETE FROM alunos where id=7')

#5. Criar uma Tabela e Inserir Dados -> Crie uma tabela chamada "clientes" com os campos: id (chave primária), nome (texto), 
#idade (inteiro) e saldo (float). Insira alguns registros de clientes na tabela.
cursor.execute('CREATE TABLE clientes(id INT PRIMARY KEY, nome VARCHAR(100), idade INT, saldo FLOAT);')

cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(1, "Mario", 25, 25631)')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(2, "Ana", 30, 12000.50)')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(3, "João", 40, 35000)')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(4, "Maria", 22, 8000)')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(5, "Pedro", 35, 27500.75)')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(6, "Julia", 28, 15000)')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(7, "Carlos", 45, 40000)')       

#6. Consultas e Funções Agregadas -> Escreva consultas SQL para realizar as seguintes tarefas:
# a) Selecione o nome e a idade dos clientes com idade superior a 30 anos.
dados = cursor.execute('SELECT * FROM clientes WHERE idade>30')
for cliente in dados:
    print(cliente)

# b) Calcule o saldo médio dos clientes.
cursor.execute('SELECT AVG(saldo) AS saldo_medio FROM clientes')
resultado = cursor.fetchone()
saldo_medio = resultado[0]
print("Saldo médio dos clientes:", saldo_medio)

# c) Encontre o cliente com o saldo máximo.
dados = cursor.execute('SELECT * FROM clientes ORDER BY saldo DESC LIMIT 1')
for cliente in dados:
    print(cliente)

# d) Conte quantos clientes têm saldo acima de 1000.
cursor.execute('SELECT COUNT(*) AS total_clientes FROM clientes WHERE saldo>1000;')
resultado = cursor.fetchone()
total_clientes = resultado[0]
print("Total de clientes na tabela:", total_clientes)

#7. Atualização e Remoção com Condições
# a) Atualize o saldo de um cliente específico.
cursor.execute('UPDATE clientes SET saldo=1000.95 WHERE nome="Carlos"')

# b) Remova um cliente pelo seu ID.
cursor.execute('DELETE FROM clientes where id=7')

#8. Junção de Tabelas -> Crie uma segunda tabela chamada "compras" com os campos: id(chave primária), cliente_id (chave estrangeira referenciando o 
#id da tabela "clientes"), produto (texto) e valor (real). Insira algumas compras associadas a clientes existentes na tabela "clientes".Escreva 
#uma consulta para exibir o nome do cliente, o produto e o valor de cada compra.

cursor.execute('CREATE TABLE compras (id INT PRIMARY KEY,cliente_id INT,produto VARCHAR(100),valor REAL,FOREIGN KEY (cliente_id) REFERENCES clientes(id))')

# Inserindo algumas compras associadas a clientes existentes na tabela "clientes"
compras = [
    (1, 1, "Smartphone", 1500.00),
    (2, 2, "Tablet", 800.00),
    (3, 3, "Livro", 30.00),
    (4, 4, "Fones de ouvido", 100.00),
    (5, 5, "Monitor", 300.00)
]

for compra in compras:
    cursor.execute('INSERT INTO compras (id, cliente_id, produto, valor) VALUES (?, ?, ?, ?)', compra)

# Escrevendo e imprimindo uma consulta para exibir o nome do cliente, o produto e o valor de cada compra
cursor.execute('''SELECT c.nome AS nome_cliente, co.produto, co.valor
                  FROM clientes c
                  JOIN compras co ON c.id = co.cliente_id''')

dados = cursor.fetchall()

print("Nome do Cliente | Produto | Valor")
for dado in dados:
    print(f"{dado[0]} | {dado[1]} | R${dado[2]:.2f}")

conexao.commit()
conexao.close
