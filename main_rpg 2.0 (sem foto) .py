import random
from time import sleep
import sys
#Meu primeiro jogo rpg com escolhas do usuario

#Funções a mais necessarias
#Atributos
atributos={"vida":1,
            "sorte":1,
            "ataque":1,
            "defesa":1,
            "inteligencia":1}

class monstros():
    def __init__(self,nome,raça,vida,defesa,ataque,velocidade,xp):
        self.nome=nome
        self.raça=raça
        self.vida=vida
        self.defesa=defesa
        self.ataque=ataque
        self.velocidade=velocidade
        self.xp=xp

goblin1=monstros(nome='Goblin',
                raça='Goblin',
                vida=5,
                defesa=2,
                ataque=3,
                velocidade=5,
                xp=3)

esqueleto1=monstros(nome='Esqueleto',
                raça='Ex-humano',
                vida=9,
                defesa=5,
                ataque=4,
                velocidade=6,
                xp=5)


livro_1=monstros(nome='Contos de um espadachim',
                raça='livro magico',
                vida=2,
                defesa=1,
                ataque=1,
                velocidade=2,
                xp=0.5)

livro_2=monstros(nome='O Grimório das Sombras Esquecidas',
                raça='livro magico',
                vida=2,
                defesa=1,
                ataque=1,
                velocidade=2,
                xp=0.5)

livro_3=monstros(nome='Anatomia dos Ossos Vivos',
                raça='livro magico',
                vida=2,
                defesa=1,
                ataque=1,
                velocidade=2,
                xp=0.5)

livro_4=monstros(nome='Crônicas da Encruzilhada Perdida',
                raça='livro magico',
                vida=2,
                defesa=1,
                ataque=1,
                velocidade=2,
                xp=0.5)

livro_5=monstros(nome='O Último Canto do Golem de Pedra',
                raça='livro magico',
                vida=2,
                defesa=1,
                ataque=1,
                velocidade=2,
                xp=0.5)

livro_6=monstros(nome='A Forja da Luz Eterna',
                raça='livro magico',
                vida=2,
                defesa=1,
                ataque=1,
                velocidade=2,
                xp=0.5)



#função para dano, fuga e defesa contra o monstro
def dfd_jgd(monstro_atacante):
    sleep(1.5)
    print("<------------------------------------------------------------------------------->")
    print(f'\nVoce esta enfrentando o {monstro_atacante.nome}, da raça {monstro_atacante.raça}.')
    while monstro_atacante.vida>0:
        acao=input('\nOque voce deseja fazer?'
                '\n1. Atacar'
                '\n2. Defender'
                '\n3. Fugir'
                '\nOque voce ira fazer?:  ')
        print("<------------------------------------------------------------------------------->")
        #Dar dano ao monstro
        if acao=='1':
            print('lembre-se, cada ação tem uma reação...')
            dano_total=atributos["ataque"]/monstro_atacante.defesa
            monstro_atacante.vida-=dano_total
            print("<------------------------------------------------------------------------------->")
            print(f'Voce causou {dano_total} de dano ao {monstro_atacante.nome}, a vida dele agora é {monstro_atacante.vida}')
            #turno do monstro
            dano_do_monstro=monstro_atacante.ataque/atributos["defesa"]
            atributos["vida"]-=dano_do_monstro
            print(f'Voce recebeu {dano_do_monstro} de dano, no momento sua vida esta em {atributos["vida"]}')
            print("<------------------------------------------------------------------------------->")
            if atributos["vida"]<=0:
                print('Sua vida chegou a 0, infelizmente voce morreu...')
                sys.exit()
            if monstro_atacante.vida<=0:
                print(f'Parabens voce derrotou o {monstro_atacante.nome}!!')

            if monstro_atacante.defesa>atributos["ataque"]:
                print(f'A defesa do {monstro_atacante.nome} é maior que seu dano de ataque, sendo assim ataque anulado, se deu mal ih ih ih ih.')

        #dar a fuga no monstro, tu é mo covarde se usa isso aqui
        if acao=='2':
            dano_ao_jg=monstro_atacante.ataque/atributos["defesa"]
            print(f'Voce tomou {dano_ao_jg} de dano')
            atributos["vida"]-=dano_ao_jg
            print(f'Sua vida agora é {atributos["vida"]}')
            chance_volta1=random.randint(1,5)
            if atributos["vida"]<=0:
                print('Sua vida chegou a 0, infelzimente voce morreu...')
                sys.exit()
            if chance_volta1>=4:
                defesa_monstro=random.randint(1,4)
                dano_total=atributos["ataque"]/(monstro_atacante.defesa+defesa_monstro)
                monstro_atacante.vida-=dano_total
                print(f'Voce conseguiu contra-atacar o  {monstro_atacante.nome} dando {dano_total} de dano nele.')
            
        #defender contra o monstro, acho que ta no meta
        elif acao=='3':
            chance_de_fuga=random.randint(1,5)
            fuga=atributos["sorte"]+chance_de_fuga
            if fuga>monstro_atacante.velocidade:
                print(f'Parabens!! Voce conseguiu fugir do {monstro_atacante.nome}')
                break
                    
            else:
                print('Se fudeu!! Fuga não foi sucedida, ataca ele ai covarde!')
        
    if monstro_atacante.vida<=0:
        pontos_atributos.append(monstro_atacante.xp)
        print(f'Ao matar o {monstro_atacante.nome} você conseguiu {monstro_atacante.xp} de pontos para colocar nos atributos, atualmente voce tem {pontos_atributos} pontos.')
        add_atributos=atribuir_atributos()
            
           
def adicionar_atributos(nome_atributo):
    qnt_pts_atribuido=int(input(f"\nQuantos pontos voce deseja colocar no atributo {nome_atributo}?: "))
    sleep(1.5)
    while qnt_pts_atribuido>pontos_atributos:
        print("Voce não tem essa quantidade de pontos, tente novamente")
        sleep(1.5)
        qnt_pts_atribuido=int(input(f"Quantos pontos voce deseja colocar no atributo {nome_atributo} : "))
        sleep(0.5)

    atributos[nome_atributo]+=qnt_pts_atribuido
    pontos_atributos-=qnt_pts_atribuido
    print("<------------------------------------------------------------------------------->")
    print("No momento seus atributos estão assim:\n",atributos)
    print("E voce tem ",pontos_atributos,"pontos restando")
    print("<------------------------------------------------------------------------------->") 
    sleep(0.9)  



def atribuir_atributos():
    retomar='NAO'
    while retomar!='SIM':
        opcoes=int(input("\n1. Vida"
                    "\n2. Sorte"
                    "\n3. Ataque"
                    "\n4. Defesa"
                    "\n5. Inteligencia" 
                    ""

                    "\nDigite a opção desejada: "))
        if opcoes==1:
            adicionar_atributos("vida")
            retomar=input(f'\nHeroi {nome} voce ja acabou de distribuir seus pontos [sim/não]: ').upper()
            if retomar!="SIM":
                print("Voce tem: ",pontos_atributos,"pontos restando, gaste com sabedoria...")

        elif opcoes==2:
            adicionar_atributos("sorte")
            retomar=input(f'\nHeroi {nome} voce ja acabou de distribuir seus pontos [sim/não]: ').upper()
            if retomar!="SIM":
                print("Voce tem: ",pontos_atributos,"pontos restando, gaste com sabedoria...")

        elif opcoes==3:
            adicionar_atributos("ataque")
            retomar=input(f'\nHeroi {nome} voce ja acabou de distribuir seus pontos [sim/não]: ').upper()
            if retomar!="SIM":
                print("Voce tem: ",pontos_atributos,"pontos restando, gaste com sabedoria...")

        elif opcoes==4:
            adicionar_atributos("defesa")
            retomar=input(f'\nHeroi {nome} voce ja acabou de distribuir seus pontos [sim/não]: ').upper()
            if retomar!="SIM":
                print("Voce tem: ",pontos_atributos,"pontos restando, gaste com sabedoria...")

        elif opcoes==5:
            adicionar_atributos("inteligencia")
            retomar=input(f'\nHeroi {nome} voce ja acabou de distribuir seus pontos [sim/não]: ').upper()
            if retomar!="SIM":
                print("Voce tem: ",pontos_atributos,"pontos restando, gaste com sabedoria...")

        else:
            print("Por favor, escolha somente de 1-5.")


    


#Pontos iniciais
pontos_atributos=0






#Informações iniciais
nome=input("\nBom dia caro... qual o seu nome mesmo? ")
sleep(1.5)
print("Ah sim!! Como eu pude esquecer um dos nomes mais memoraveis de toda o continente de Farlein, um dos nossos grandes Herois!!")
sleep(2)
print("Eu sou o Narrador e te acompanharei nessa sua jornada, espero que se acostume",nome, "ou não ih ih ih ih...")
sleep(1.5)


print("\n<--------------------------------------------------------------------------------------------------------------------->")
print("\n",atributos)



print("\nEsses são seus atributos atualmente, porem não se preocupe, eu vou te dar uma ajudinha com mais alguns pontos de atributos")

sleep(5)

print('\nConsiderando que voce é O Grande Heroi ja deve estar familiarizado com o sistema de atributos certo? Sendo assim, eu irei somente dar um breve resumo para que voce possa relembrar')
print("\n1. Vida -- O ponto mais importante, assim que chegar a 0 seu personagem sera resetado, e não se esqueça que ela não se regenera, ao perder vida voce ficara sem ate que suba seus atributos e recupere o ponto perdido"

        "\n2. Sorte -- Determina o quão bom sera o loot que voce vai encontrar nos baus e se voce vai conseguir ou não fugir de um inimigo"
        "\n3. Ataque -- Determina o seu dano ao inimigo"
        "\n4. Defesa -- Caso escolha defender, o ataque inimigo sera dividido pela sua defesa e tem uma chance de causar dano ao inimigo"
        "\n5. Inteligencia -- Determina a sua capacidade para desvendar segredos ou salas ocultas")

sleep(10)

print("\nVamos fazer o seguinte",nome,",iremos rolar dois dados que vão ate 20, diga a quantidade de vezes que voce quer que esses dados rolem, lembrando que somente as duas ultimas vezes é que vão contar para seus pontos de atributos.")
sleep(1.5)

qnt_rola_dados_inicial=int(input("\nDigite a quantidade de vezes que você quer rolar os dados: "))
sleep(1.5)
numero_dados_iniciais=0

while numero_dados_iniciais <qnt_rola_dados_inicial:
    d1_atributo_inicial=(random.randint(10,20))
    d2_atributo_inicial=(random.randint(10,20))
    qtd_atributos=d2_atributo_inicial+d1_atributo_inicial
    numero_dados_iniciais+=qtd_atributos

pontos_atributos+=qtd_atributos

print ("Voce tem",pontos_atributos, "pontos de atributo")
sleep(1.5)

#Distribuição dos pontos

print("\nAgora iremos colocar os seus pontos nos devidos atributos, a seguir, vai ter uma lista com seus atributos e seus numero, digite o numero do atributo e quantos pontos deseja colcoar la, lembrando que voce tem somente",pontos_atributos, "pontos para usar")
sleep(1.5)

retomar="NAO"
while retomar !="SIM":
    atribuir_atributos()
    retomar='SIM'

print(f"\nAcho que voce ja esta pronto para sua nova aventura!! Se prepare grande heroi {nome}!! (Cochica: esse é mesmo o nome dele? que nome mais sem graça... )")

print('\nVoce acorda em um lugar desconhecido, ainda sem abrir os olhos sente a textura do chão, sente que tem muita sujeira, lodo, e um cheiro podre, ao finalmente abrir os olhos, se depara com um lugar em ruinas, parecia ser uma masmorra ')


sleep(10)

print("\nAo andar um pouco a frente voce se depara com um ser verde, com orelhas pontudas e dentes afiados, ele esta praticamente pelado, usando somente um short na parte de baixo")



sleep(5)

print('\nQuando voce ve aquele ser, voce fica cheio de medo, porem precisava passar por ele para sair daquele local, voce então entra em batalha com ele')
sleep(1.5)


dfd=dfd_jgd(goblin1)


  
if goblin1.vida<=0:
    escolha=input('\nAo matar o goblin voce segue em frente, ate se ver em uma encruzilhada tendo apenas duas opções, esquerda ou direta, para onde voce vai ?: ') .upper()
    sleep(0.8)
else:
    escolha=input('\nAo fugir covardemente do monstro voce ve uma encruzilhada tendo apenas duas opções, esquerda ou direta, para onde voce vai?: ').upper()
    sleep(0.8)

sleep(2)


#Escolha encruzilhada
if escolha=='ESQUERDA':
    print('\nAo escolher a esquerda voce se depara com um calabouço, cheio de esqueletos presos, parece que ja estão la a um BOOOM tempo ')
    sleep(2)

    sleep(4)
    print('Voce tenta abrir a cela em que eles estão, tentando ver se tem algo que vale a pena pegar, porem... ao abrir a cela o esqueleto pula em cima de voce, fazendo com que voce tenha que lutar contra ele para conseguir sair daquele local')
    dfd=dfd_jgd(esqueleto1)
    if esqueleto1.vida<=0 and atributos['inteligencia']>7:
        print('\nAo matar o esqueleto voce ve que em um lugar em que ele deu um golpe, parecia ser fragil, como se fosse de papel, voce então tentar rasgar e acha um bau!!')
        sleep(0.9)


        bau1_sorte=random.randint(1,atributos['sorte'])
        atributos["ataque"]+=bau1_sorte
        print(f'Quando voce abre o bau, da de cara com uma espada simplesmente magnifica, fazendo com que seu ataque aumente em {bau1_sorte} pontos')
        sleep(0.9)

        sleep(0.8)
        print(f'\nAtualmente voce tem {atributos["ataque"]} pontos de ataque ')

    if esqueleto1.vida<=0:
        print('Parabens por ter matado o esqueleto!!')

    else:
        print('Fugiu ne covarde')


if escolha=='DIREITA':
    print('\nAo escolher a esquerda voce se depara com uma biblioteca, tem varios livros empoerados, rasgados, sem a capa...  bem avariados... ')


    print('\nVoce pega nos livros tentando entender oque eles são, pois não parecem ser normais, voce sente algo diferente deles, algo como se sua intuição disse que são perigosos... e ao olhar para tras voce percebe que estava certo... tinha meia duzia de livros voando em sua direção, forçando voce a entrar em combate com eles para que pudesse sair daquele local')
    dfd=dfd_jgd(livro_1)
    dfd=dfd_jgd(livro_2)
    dfd=dfd_jgd(livro_3)
    dfd=dfd_jgd(livro_4)
    dfd=dfd_jgd(livro_5)
    dfd=dfd_jgd(livro_6)

livros_magicos=livro_1.vida,livro_2.vida,livro_3.vida,livro_4.vida,livro_5.vida,livro_6.vida
livros_magicos_vida=sum(livros_magicos)
if livros_magicos_vida<=0 and atributos['inteligencia']>7:
    print('\nQuando finalmente voce mata todos os livros voadores, voce finalmente consegue respirar um pouco, e percebe que tem um vão no lugar aonde os livros sairam, voce então decide se aproximar e ve que tem um livro aparentemente te chamando...')


    bau1_sorte=random.randint(1,atributos['sorte'])
    atributos["inteligencia"]+=bau1_sorte
    print(f'\nAo chegar perto desse livro é como se o conhecimento simplesmente entrasse na sua mente, fazendo com que sua inteligencia aumente em {bau1_sorte} pontos')
    sleep(0.9)
    print(f'\nAtualmente voce tem {atributos["inteligencia"]} pontos de inteligencia ')

sleep(1.5)
print('\n \nAte agora o RPG é somente isso, agradeço por ter jogado ate aqui e ate a proxima versão, fiz ele somente com o intuito de entender melhor a logica de programação, dicionarios, listas, um pouco da matematica, a sintaxe, e eu acho que foi muito bom para mim esse aprendizado, agradeço de verdade por ter jogado durante esses 2 minutos ih ih ih')