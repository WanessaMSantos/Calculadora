def calc (num1, num2, operacao):
    if (operacao == 1):
        return num1 + num2
    elif (operacao == 2):
        return num1 - num2
    elif (operacao == 3):
        return num1 * num2
    elif (operacao == 4):
        return num1 / num2

    else:
        return 0

while (executar == True):
    print("Qual operação vocẽ quer realizar?")
    print("1: soma 2: subtração 3: multiplicação 4: divisão 0: sair")
    operacao int(input ())
    if (operacao < 0)or (operacao > 4):
        print("Opção inválida, tente novamente!")
    elif (operacao == 0):
        executar = False
    else:
        print("Digite o primeiro número da operação: ")
        num1 = int(input())
        print("Digite o segundo número da operação: ")
        num2 = int(input())
        resultado = calc(num1, num2, operacao)
        print("O resultado é: " + resultado)