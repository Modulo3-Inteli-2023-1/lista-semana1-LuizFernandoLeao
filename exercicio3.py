#  Se achar necessario, faça import de outras bibliotecas
#  Nome: Luiz Fernando Leao


# Crie a função que será avaliada no exercício aqui

def soma_dos_aninhados(lista_aninhada):
    soma = 0
    for lista in lista_aninhada:
        for num in lista:
            soma += num
    return soma

# Uso da função:
lista = [[11, 22], [33], [44, 55, 66]]
resultado = soma_dos_aninhados(lista)
print(resultado)  # Output: 231

outra_lista = [[1, 2, 3, 4], [3, 3], [4, 6]]
resultado_outra_lista = soma_dos_aninhados(outra_lista)
print(resultado_outra_lista)  # Output: 26


# Teste a sua função aqui (caso ache necessário)
