import script
from pygame import mixer
mixer.init()
mixer.music.load('music1.wav')
mixer.music.play(loops=-1)
lista=["JOGAR","SAIR","INSTRUÇÕES <-------- RECOMENDADO "]
def cabecalho():
    print(script.linha())
    print("BEM VINDO AO KNOWLEDGE GAME".center(42))
    print(script.linha())
    c=1
    for item in lista:
        print(f"{c}-{item}")
        c+=1
    print(script.linha())
    opc=input("INSIRA UMA OPÇÃO: ")
    if opc=="1":
        script.os.system("cls")
        nome=input("INSIRA SEU NOME: ")
        script.os.system("cls")
        print("OLÁ,",nome,"\n VOCÊ ESTÁ PERDIDO DENTRO DE UM CALABOUÇO APÓS TER A BRILHANTE IDEIA DE SEGUIR UMA VOZ MISTERIOSA ATÈ UM BURACO NO MEIO DA FLORESTA")
        input("ENTER PARA COMEÇAR: ")
        script.os.system("cls")
        script.game()    
    if opc=="2":
        quit()
    if opc=="3":
        script.os.system("cls")
        print("Instruções do jogo em geral")
        print('W - Frente')
        print('A - Esquerda')
        print('D - Direita')
        print('O sistema de batalhas é baseado em questões.Se caso você pegue uma espada mais poderosa por exemplo, as questões da batalha vão ficando mais faceis')
        
        input("APERTE ENTER PARA VOLTAR AO MENU ")
        script.os.system("cls")
        cabecalho()
    else:
        script.os.system("cls")
        cabecalho()

cabecalho()