#  Se achar necessario, faça import de outras bibliotecas
#  Nome: Luiz Fernando Leao


# Crie a função que será avaliada no exercício aqui

def cumulativo(lista):
    cumulativa = []
    soma = 0

    for numero in lista:
        soma += numero
        cumulativa.append(soma)

    return cumulativa

# Uso da função:
lista = [2, 3, 4, 5]
resultado = cumulativo(lista)
print(resultado)


# Teste a sua função aqui (caso ache necessário)
