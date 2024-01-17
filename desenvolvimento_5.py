def calculadora():
    while True:
        print("\nSelecione a operação:")
        print("1: Soma")
        print("2: Subtração")
        print("3: Multiplicação")
        print("4: Divisão")
        print("0: Sair")

        escolha = input("Digite o número da operação desejada: ")

        if escolha == '0':
            print("Saindo da calculadora. Até mais!")
            break
        elif escolha in ('1', '2', '3', '4'):
            num1 = float(input("Digite o primeiro valor: "))
            num2 = float(input("Digite o segundo valor: "))

            if escolha == '1':
                resultado = num1 + num2
                print("Resultado: {}".format(resultado))
            elif escolha == '2':
                resultado = num1 - num2
                print("Resultado: {}".format(resultado))
            elif escolha == '3':
                resultado = num1 * num2
                print("Resultado: {}".format(resultado))
            elif escolha == '4':
                if num2 != 0:
                    resultado = num1 / num2
                    print("Resultado: {}".format(resultado))
                else:
                    print("Não é possível dividir por zero. Tente novamente.")
        else:
            print("Essa opção não existe. Tente novamente.")


if __name__ == "__main__":
    calculadora()