import sqlite3 # Import the sqlite3 module e permite a manipulaç]ao do banco de dados


conn = sqlite3.connect('empresa.db') # Conecta ao banco de dados chamado empresa.db
cursor = conn.cursor() # Cria um objeto cursor para executar comandos SQL

# Comsultar todos os funcionários
cursor.execute("SELECT * FROM funcionarios") # Executa a query para selecionar todos os funcionários
funcionarios = cursor.fetchall() # Pega todos os resultados da query

# Exibir os resultados
for funcionario in funcionarios: # Inicia um loop para iterar sobre cada registro na lista
    print(funcionario) # Imprime cada registro da lista
    
conn.close() # Fecha a conexão com o banco de dados
