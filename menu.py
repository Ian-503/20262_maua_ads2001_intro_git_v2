verdade=True
import calculadora
while verdade:

    numero = int(input('1 para somar,2 para subtrair, 3 para multiplicar, 4 para dividir, 0 para sair'))

    match numero:
        case 1: 
            numero1=int(input('qual o primeiro numero'))
            numero2=int(input('qual o segundo numero '))
            print(calculadora.somar(numero1,numero2))
        case 2: 
            numero1=int(input('qual o primeiro numero'))
            numero2=int(input('qual o segundo numero '))
            print(calculadora.subtrair(numero1,numero2))
        case 3: 
            numero1=int(input('qual o primeiro numero'))
            numero2=int(input('qual o segundo numero '))
            print(calculadora.multiplicar(numero1,numero2))
        case 0: 
            verdade=False        