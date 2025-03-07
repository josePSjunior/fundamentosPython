import sqlite3

def menu():
    conn = sqlite3.connect('empresa.db')
    cursor = conn.cursor()
    
    while True:
        print("\nMenu DE GESTÃO DE FUNCIONÁRIOS")
        print("1. Adicionar funcionário")
        print("2. Listar funcionários")
        print("3. Atualizar salário")
        print("4. Eliminar funcionário")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            nome = input("Nome: ")
            cargo = input("Cargo: ")
            salario = float(input("Salário: "))
            cursor.execute("INSERT INTO funcionarios(nome, cargo, salario) VALUES(?,?,?)", (nome, cargo, salario))
            conn.commit()
        elif opcao == "2":
            cursor.execute("SELECT * FROM funcionarios")
            for funcionario in cursor.fetchall():
                print(funcionario)
        elif opcao == "3":
            nome = input("Nome do funcionário: ")
            novo_salario = float(input("Novo salário: "))
            cursor.execute("UPDATE funcionarios SET salario = ? WHERE nome = ?", (novo_salario, nome))
            conn.commit()
        elif opcao == "4":
            nome = input("Nome do funcionário a eliminar: ")
            cursor.execute("DELETE FROM funcionarios WHERE nome = ?", (nome,))
            conn.commit()
        elif opcao == "5":
            conn.commit()
            conn.close()
            break
        else:
            print("Opção inválida. Tente novamente.")

# Iniciar o menu
menu()
