import random

class Cavaleiro:
    seq=0

    def __init__(self,chapeu):
        self.__class__.seq+=1
        self.id=self.__class__.seq
        self.chapeu=chapeu
    def __str__(self):
        return "Cavaleiro "+str(self.id)+" Chapeu: "+str(self.chapeu)

cavaleiros=[]
for i in range(0,10):
    x=0
    while True:
        x=random.randint(-9, 9)
        if x!=0:
            break;

    cavaleiros.append(Cavaleiro(x))

for cav in cavaleiros:
    print(cav)

init= random.randint(1,10)-1
print("primeira escolha foi o cavaleiro "+str(init+1))
cavAtual=cavaleiros[init]
chap = cavAtual.chapeu

print("O número do chapeu dele é chapeu dele é "+str(cavAtual.chapeu))
at = init
while len(cavaleiros) > 1:

    tamanho = len(cavaleiros)
    contador =0

    if(chap>0):
        while contador!=abs(chap):
            at += 1
            if at >= len(cavaleiros):
                at = 0
            cavAtual=cavaleiros[at]
            print("O cavaleiro Atual é o "+str(cavAtual)+" Contagem:"+str(contador+1))
            contador+=1

    if (chap < 0):
        while contador != abs(chap):

            cavAtual = cavaleiros[at-1]
            print("O cavaleiro Atual é o "+str(cavAtual)+" Contagem:"+str(contador+1))
            contador += 1
            at -= 1
            if at < 0:
                at = len(cavaleiros) - 1

    print("o cavaleiros escolhido para ser removido dessa vez foi o "+str(cavAtual))
    chap=cavAtual.chapeu
    cavaleiros.remove(cavAtual)




print("###################################################")
print("##O CAVALEIRO ESCOLHIDO É O "+str(cavaleiros[0])+"##")
print("###################################################")
