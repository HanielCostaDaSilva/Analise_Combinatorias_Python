def PermutacaoSimples(n):
    resultado = 1
    multiplicador = 2
    while multiplicador <= n:
        resultado = resultado*multiplicador
        multiplicador +=1
    return resultado


def PermutacaoCircular(n):
    n -= 1
    resultado=1
    multiplicador=2
    if (n<=1):
        print( "o valor de n é muito pequeno")
        return True

    while (multiplicador<=n):
        resultado= resultado* multiplicador
        multiplicador+= 1
    
    return resultado

def ArranjoSimples(n,p):
    resultadoN=1
    multiplicador=2
    b=n-p
    multiplicadorB=2
    resultadoB=1

    if(n<p):
        print("o número de termos do conjunto é maior que o número de elementos!")
        return False
    
    while(multiplicador<=n):
        resultadoN=resultadoN*multiplicador
        multiplicador +=1

    if(b==0 or b==1):
        b=1
               
    while(multiplicadorB<=b):
        resultadoB= resultadoB*multiplicadorB
        multiplicadorB +=1
    resultadoFinal= resultadoN//resultadoB
    return resultadoFinal
    

def ArranjoComRepeticao(n,p):
    '''print("utilizasse Arranjo com repetição para quando o número de elementos(n) é menor que o número de termos do conjunto(p) e aqueles podem ser repetidos. \n n>p")
    print("formula: A(n,p) = n**p")
    print(" ")
    '''
    
    if n<p:
        print("o primeiro valor não pode ser menor que o segundo valor!")
        return False
    resultadoFinal= n**p
    return resultadoFinal

def CombinacaoSimples(n,p):
    resultadoN=1
    multiplicadorN=2
    
    resultadoP=1
    multiplicadorP=2
    
    multiplicadorB=2
    resultadoB=1

    '''print("utilizasse a combinação simples para quando a ordem dos elementos não importa, ex: A,B é o mesmo que B,A, o numero de termos(n) pode ser igual ao número de termos do conjuntos(p)")
    print("formula: C(n,p) n!// p!(n-p)!")
    print(" ")
    '''
    b=n-p
  
    if(n<p):
        print("o número de termos do conjunto é maior que o número de elementos! O que dá a possibilidade de apenas uma combinação!")
        return 1
    

    while(multiplicadorN<=n):
        resultadoN=resultadoN*multiplicadorN
        multiplicadorN +=1
        
    if b>1:
        while(multiplicadorB<=b):
            resultadoB= resultadoB* multiplicadorB
            multiplicadorB +=1
        
    while(multiplicadorP<=p):
        resultadoP=resultadoP*multiplicadorP
        multiplicadorP +=1

    produto= resultadoP*resultadoB
    resultadoFinal= (resultadoN//produto)

    return resultadoFinal

resposta="sim"
elementos=0
conjunto=0

print("Bem vindo ao teste de combinações!")
while resposta=="sim":
    print("1- Permutação Simples \n 2-Permutação circular \n 3-Arranjo simples \n 4- Arranjo com repeteciçao \n 5- Combinação Simples")

    escolha= int(input("escreva o número do estilo que você deseja calcular: "))
    if (escolha==1):
        print(" ")
        n=int(input("Digite o número de elementos: (n) "))
        print(PermutacaoSimples(n))

    elif(escolha==2):
        print(" ")
        n=int(input("Digite o número de elementos: (n) "))   
        print(PermutacaoCircular(n))

    elif(escolha==3):
        n=int(input("Digite o número de elementos: (n) "))
        p=int(input("Digite o número de termos do conjunto: (p) "))
        print(ArranjoSimples(n,p))

    elif(escolha==4):
        print(" ")
        n=int(input("Digite o número de elementos: (n) "))
        p=int(input("Digite o número de termos do conjunto: (p) "))
        print(ArranjoComRepeticao(n,p))
        

    elif(escolha==5):
        print(" ")
        n=int(input("Digite o número de elementos: (n) "))
        p=int(input("Digite o número de termos do conjunto: (p) "))
        print(CombinacaoSimples(n,p))
   
    else:
        print("ERRO! Não foi escolhido nenhuma das opções acima " )
    resposta=str.lower(input("Deseja refazer a operação? "))

    while resposta!= "sim" and resposta!="nao" and resposta!="não" :
        resposta=str.lower(input("Digite sim ou não: "))

input("aperte a tecla 'Enter' para finalizar ")
