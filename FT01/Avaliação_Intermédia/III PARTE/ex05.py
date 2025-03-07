import sqlite3

conn = sqlite3.connect('empresa.db')
cursor = conn.cursor()

#Eliminar todos os funcionários com um salário inferior a 3000
cursor.execute("DELETE FROM funcionarios WHERE salario < 3000")

# Consultar todos os funcionários restantes para verificar se foram eliminados corretamente
cursor.execute("SELECT * FROM funcionarios")
funcionarios = cursor.fetchall()

# Exibir os resultados restantes
for funcionario in funcionarios:
    print(funcionario)

conn.commit()
conn.close()