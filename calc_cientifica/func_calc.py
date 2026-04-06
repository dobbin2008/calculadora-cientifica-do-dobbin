import soma
import sub
import mult
import divi
import pwr
import squarert 
import cotacao
def calc():
    op = input("Qual operação você deseja utilizar? Digite o nome da operação sem acento. " ).strip().lower()
    a = float(input("Qual o primeiro número? "))
    b = float(input("E o segundo? "))
    
    match op:
        case "soma":
            print("Seu resultado é ", soma.soma(a, b))
        case "subtracao": 
            print("Seu resultado é ", sub.sub(a, b))
        case "divisao": 
            print("Seu resultado é ", divi.divi(a, b))
        case "multiplicacao": 
            print("Seu resultado é ", mult.mult(a, b))
        case "potencia": 
            print("Seu resultado é ", pwr.pwr(a, b))
        case "raiz quadrada": 
            print("Seu resultado é ", squarert.sqrt(a))
        case "conversão": 
            print("O valor do dolár é ", cotacao.cotacao_dolar())
            dol = input("Deseja converter o primeiro valor?")
            if dol == "sim":
                print(a/cotacao.cotacao_dolar())
            else: print("Fim do programa")
        case _ :
            print("Algo deu errado, será você digitou algo errado sem querer?")
        
    