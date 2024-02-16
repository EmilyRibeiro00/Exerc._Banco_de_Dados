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
for usuario in dados:
    print(usuario)

# b) Selecionar o nome e a idade dos alunos com mais de 20 anos.
dados = cursor.execute('SELECT * FROM alunos WHERE idade>20')
for usuario in dados:
    print(usuario)

# c) Selecionar os alunos do curso de "Engenharia" em ordem alfabética.
dados = cursor.execute('SELECT * FROM alunos WHERE curso="Engenharia" ORDER BY nome')
for usuario in dados:
    print(usuario)

# d) Contar o número total de alunos na tabela
cursor.execute('SELECT COUNT(*) AS total_alunos FROM alunos;')
resultado = cursor.fetchone()
total_alunos = resultado[0]
print("Total de alunos na tabela:", total_alunos)

#4. Atualização e Remoção
# a) Atualize a idade de um aluno específico na tabela.

# b) Remova um aluno pelo seu ID.

conexao.commit()
conexao.close