#  Se achar necessario, faça import de outras bibliotecas


# Crie a função que será avaliada no exercício aqui

def tem_duplicados(lista):
    elementos_unicos = set()

    for elemento in lista:
        if elemento in elementos_unicos:
            return True
        elementos_unicos.add(elemento)

    return False

# Uso da função:

lista1 = [1, 2, 3, 4, 5, 2]
resultado1 = tem_duplicados(lista1)
print(resultado1)  # Output: True


# Teste a sua função aqui (caso ache necessário)
