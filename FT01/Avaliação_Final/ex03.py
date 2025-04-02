# Escreve uma função em Python que dada uma lista de números imprime a soma dos valores dessa lista,
# o número de elementos da lista e a media desses valores. Implementa tratamento de exceções no teu código (try…except…else..finally). 

def processar_lista(lista):
    try:
        if not all(isinstance(numero, (int, float)) for numero in lista):
            raise ValueError("A lista deve conter apenas números")
        
        soma = sum(lista)
        num_elementos = len(lista)
        media = soma / num_elementos if num_elementos > 0 else 0 
    except ZeroDivisionError:
        print("Erro: Não é possível calcular a média de uma lista vazia")
    except ValueError as ve:
        print(f"Erro de valor: {ve}")
    except Exception as e:
        print(f"Erro inesperado: {e}")
    else:
        print(f"Soma: {soma}")
        print(f"Quantidade de elementos: {num_elementos}")
        print(f"Média dos valores: {media:.2f}")
    finally:
        print("Processamento da lista concluído")
        
try:
    lista = [float(x) for x in input("Digite os números separados por espaço:").split()]
    processar_lista(lista)
except Exception as e:
    print(f"Erro ao coler a entrada: {e}")