## Implemente um programa que, dada uma letra (S, C ou V), indique o estado civil de uma pessoa.

estadocivil = input("Introduza Estado Civil [S;C;D;V]\n-->")

match estadocivil:
        case 'S':
            print("Solteiro(a)")
        case 'C':
            print("Casado(a)")
        case 'V':
            print("Viúvo(a)")
        case 'D':
            print("Divorciado(a)")
        case _:
            print("Estado civil não encontrado")