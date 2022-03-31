def binvet(n_max): #Cria uma lista de Binários
    a = []
    for i in range(0, n_max):
        a.append("{0:b}".format(i + 1))

    return a


def cardsgen(num, b):  # função geradora de cartões

    cards = []  # cria matriz cartão
    for i in range(num):
        cards.append([])

    for i in range(len(b)):  # interar sobre a lista dos binários
        binarioat = b[len(b) - i - 1]  # binário atual decrescente
        n_card = len(binarioat)  # tamanho do binário
        for a in binarioat:  # interar sobre cada elemento binário
            if a == '1':  # verificar se o número pertence a tal posição

                cards[n_card - 1].append(len(b) - i)  # adiciona o número a tal cartão
            n_card = n_card - 1

    return cards




n_cartoes=int(input("Insira o número de cartões\n")) #receber número de cartões
n_max=2**n_cartoes -1 # Verifica o número maximo possivel
vetorBinarios=binvet(n_max) #retorna lista de número em binário
cartoes=cardsgen(n_cartoes, vetorBinarios) #Retorna os Cartões

print("Agora pense em um número de 1 a\n",n_max )
a=0
for i in range(len(cartoes)):
    b=str(cartoes[i])
    R=input("Seu número está aqui/n? s\n"+b)
    if R=='s':
     a=a+2**i
print("Seu número é",a)
