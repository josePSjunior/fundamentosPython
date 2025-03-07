import sqlite3

conn = sqlite3.connect('empresa.db')
cursor = conn.cursor()

# Inserir funcionários na tabela
cursor.execute("INSERT INTO funcionarios (nome, cargo, salario) VALUES ('Ana Silva', 'Gestora', 3500)")
cursor.execute("INSERT INTO funcionarios (nome, cargo, salario) VALUES ('Pedro Santos', 'Programador', 2000)")
cursor.execute("INSERT INTO funcionarios (nome, cargo, salario) VALUES ('Mariana Costa', 'Designer', 2500)")
cursor.execute("INSERT INTO funcionarios (nome, cargo, salario) VALUES ('Julia Pereira', 'Professora', 2300)")
cursor.execute("INSERT INTO funcionarios (nome, cargo, salario) VALUES ('Maria Oliveira', 'Medica', 3000)")

# Guardar mudanças e fechar conexão
conn.commit()
conn.close()