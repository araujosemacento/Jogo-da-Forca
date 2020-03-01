import random
x = ["petcomputacao", "protelar", "prescrever", "proscrever", "paralelepipedo", "preeminente", "proeminente", "preposicao", "proposicao", "prolatar"]
y = random.choice(x)
w = ""
listaMostra = []
for i in range(0, len(y)):
    listaMostra.append('_')
    w += y[i] + " "
lista = w.split()
tentativas = 3
listaDigitado = []
while tentativas >= 1:
    print(listaMostra)

    a = input("\nDigite uma letra: ")
    if len(a) == 1:
        if a.isalpha() == True:
            if a in listaDigitado == True:
                print("\nLetra já digitada!")
                continue
            else:
                if a in lista:
                    if a in listaDigitado:
                        print("\nLetra já digitada!")
                        continue
                    else:
                        print("\nEsta letra pertence a palavra!")
                        listaDigitado.append(a)
                    
                else:
                    if a in listaDigitado:
                        print("\nLetra já digitada!")
                    else:
                        listaDigitado.append(a)
                        print("\nEsta letra não pertence à palavra")
                        tentativas -= 1
        else:
            print("\nDigite uma entrada válida \nTentativas restantes: " + str(tentativas) )
            continue
    else:
        print("\nDigite uma entrada válida")  

    for k in range (0, len(lista)):
        if(lista[k] == a):
            listaMostra[k] = a
    
    if listaMostra.count("_") == 0:
        print("\nVocê ganhou: " + y)
        break

    print("\nTentativas Restantes " + str(tentativas) )
if tentativas == 0:
    print("\nVocê perdeu a palavra era: " + y)
    