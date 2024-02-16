import sqlite3

conexao = sqlite3.connect('Banco')
cursor = conexao.cursor()

#Criando tabela = cursor.execute('CREATE TABLE usuarios(id INT, nome VARCHAR(100), endereco VARCHAR(100), email VARCHAR(100));')

#Alterando o nome da tabela = cursor.execute('ALTER TABLE usuarios RENAME TO usuario')

#Adicionando coluna = cursor.execute('ALTER TABLE usuario ADD COLUMN telefoni INT')

#Renomeando coluna = cursor.execute('ALTER TABLE usuario RENAME COLUMN telefoni TO telefone')

#Excluindo uma tabela = cursor.execute('DROP TABLE testes')

#Adicionando informações = cursor.execute('INSERT INTO usuario(id,nome,endereco,email,telefone) VALUES(1,"Isadora","França","isa@gmail.com",912345678)')

#Deletando informação = cursor.execute('DELETE FROM usuario where id=1')

#Visualizando informações -> dados = cursor.execute('SELECT * FROM usuario')
#                            for usuario in dados:
#                               print(usuario)

#Atualizando informações = cursor.execute('UPDATE usuario SET endereco="Minas Gerais" WHERE nome="João Pedro"')

#Ordenando as informações -> dados = cursor.execute('SELECT * FROM usuario ORDER BY nome')
#                            for usuario in dados:
#                               print(usuario)

#Limitando a quantidade de informações -> dados = cursor.execute('SELECT * FROM usuario LIMIT 3')
#                                         for usuario in dados:
#                                            print(usuario)

#Obtendo só informações únicas -> dados = cursor.execute('SELECT DISTINCT * FROM usuario')
#                                 for usuario in dados:
#                                    print(usuario)

#Agrupando as informações -> dados = cursor.execute('SELECT nome FROM usuario GROUP BY nome HAVING id>3')
#                            for usuario in dados:
#                               print(usuario)

#============================================================================================================================================#
#JOIN's = combinando informações de duas ou mais tabelas (right,left,full,inner)

#O INNER JOIN retorna apenas os registros que têm correspondência em ambas as tabelas que estão sendo unidas.

#O LEFT JOIN retorna todos os registros da tabela à esquerda da junção (tabela esquerda), junto com os registros correspondentes da tabela 
#à direita (tabela direita), se houver correspondência

#O RIGHT JOIN é o inverso do LEFT JOIN. Ele retorna todos os registros da tabela à direita da junção (tabela direita), junto com os registros 
#correspondentes da tabela à esquerda (tabela esquerda), se houver correspondência.

#O FULL JOIN retorna todos os registros quando há uma correspondência em qualquer uma das tabelas que estão sendo unidas.

#============================================================================================================================================#

#Sub-consulta -> dados = cursor.execute('SELECT * FROM usuario WHERE nome IN (SELECT nome FROM gerentes)')
#                for usuario in dados:
#                   print(usuario)

conexao.commit()
conexao.close