import sqlite3

conn = sqlite3.connect('empresa.db')
cursor = conn.cursor()

# Atualizar o salário de Pedro Santos
cursor.execute("UPDATE funcionarios SET salario = 5000 WHERE nome = 'Pedro Santos'")
cursor.execute("UPDATE funcionarios SET salario = salario * 1.05")

cursor.execute("SELECT * FROM funcionarios")
funcionarios = cursor.fetchall()

# Exibir os resultados atualizados
for funcionario in funcionarios:
    print(funcionario)
    
conn.commit()
conn.close()