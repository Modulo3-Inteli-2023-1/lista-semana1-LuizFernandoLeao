#  Se achar necessario, faça import de outras bibliotecas
#  Nome: Luiz Fernando Leao


# Crie a função que será avaliada no exercício aqui

def multiplas_operacoes(a1, a2):
    # Soma
    soma = a1 + a2

    # Subtração
    subtracao = a1 - a2

    # Multiplicação
    multiplicacao = a1 * a2

    # Divisão (evitando divisão por zero)
    if a2 != 0:
        divisao = a1 / a2
    else:
        divisao = 0

    return (soma, subtracao, multiplicacao, divisao)

# Uso da função:
a1 = 2
a2 = 4
resultado = multiplas_operacoes(a1, a2)
print(resultado)


# Teste a sua função aqui (caso ache necessário)
