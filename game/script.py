
import os
import sys
def acerto():
    print(linha(115))
    print("PARABÉNS VOCÊ ACERTOU".center(115))
    print(linha(115))

def bug_item():
    print('ESCOLHA O ITEM CERTO!!!')
    input('COMO PUNIÇÃO POR QUEBRAR AS REGRAS, SEU JOGO SERÁ RESETADO')
    restart_program()
item=0
def boss1():
    input("APERTE ENTER PARA CONTINUAR: ")
    os.system("cls")
    print("AQUI È O BOSS FINAL , NELE VOCÊ TERÁ QUE RESPONDER 3 PERGUNTAS ")
    print("SE DURANTE O SEU PERCURSO PEGOU ALGUM ITEM ELE IRÁ TE AJUDAR AGORA")
    print (" SE PEGOU O PRIMIERO ITEM, ELE É UMA ESPADA. ASSIM NÃO PRECISARÁ RESPONDER UMA PERGUNTA \nSE PEGOU O SEGUNDO ITEM, ELE É UMA ARMADURA. ASSIM TERÁ UMA DICA NA SEGUNDA PERGUNTA\nSE PEGOU O TERCEIRO ITEM, ELE É UM......CALMA AÍ UM LÁPIS? PRA QUE VC USARIA UM LAPIS. VOCÊ NÂO TERÀ NENHUMA VANTAGEM "  )


    
    
    if item==0:
        print("NO CAMINHO DE CASA ATÉ O MERCADO, UMA SENHORA CONTA 1O ÁRVORES A SUA DIREITA. APÓS AS COMPRAS, ELA VOLTA PARA CASA E CONTA 10 ÁRVORES A SUA ESQUERDA. QUANTAS ÁRVORES ELA VIU NO TOTAL NESSE DIA?")
        resposta1=int(input())
        if resposta1==10:
            acerto()
            print("PRÓXIMA PERGUNTA")
            print(" FÁBIO FOI SOZINHO ATÉ A PADARIA NO CENTRO DA CIDADE. DURANTE O PERCURSO, ENCONTROU DUAS GAROTAS PASSEANDO COM TRÊS CACHORROS, QUE ESTAVAM BRINCANDO COM DOIS GATOS, QUE, POR SUA VEZ, TINHAM DOIS DONOS. QUANTOS SERES NO TOTAL FORAM COM FÁBIO ATÉ A PADARIA?")
            resposta2=int(input())
            if resposta2==0:
                os.system("cls")
                print("VOCÊ RESPONDEU TODAS AS PERGUNTAS CORRETAMENTE E DERROTOU O BOSS")
                input("ENTER PARA SAIR DO CALABOUÇO: ")
                os.system("cls")
                print(linha(115))
                print("VOCÊ FUGIU. OBRIGADO POR JOGAR.".center(115))
                print(linha(115))
                quit()
            else:
                morte_monstro()
        else:
            morte_monstro()


def boss2():
    input("APERTE ENTER PARA CONTINUAR: ")
    os.system("cls")
    print("AQUI È O BOSS FINAL , NELE VOCÊ TERÁ QUE RESPONDER 3 PERGUNTAS ")
    print("SE DURANTE O SEU PERCURSO PEGOU ALGUM ITEM ELE IRÁ TE AJUDAR AGORA")
    print (" SE PEGOU O PRIMIERO ITEM, ELE É UMA ESPADA. ASSIM NÃO PRECISARÁ RESPONDER UMA PERGUNTA \nSE PEGOU O SEGUNDO ITEM, ELE É UMA ARMADURA. ASSIM TERÁ UMA DICA NA SEGUNDA PERGUNTA\nSE PEGOU O TERCEIRO ITEM, ELE É UM......CALMA AÍ UM LÁPIS? PRA QUE VC USARIA UM LAPIS. VOCÊ NÂO TERÀ NENHUMA VANTAGEM "  )
    if item==0:
        print("PRIMEIRA PERGUNTA")
        print("A MÃE DE MARIA TEM CINCO FILHAS: FAFÁ, FEFÊ, FIFI, FOFÓ E? QUAL É O NOME DA QUINTA FILHA?")
        resposta=input()
        if resposta=="Maria" or "MARIA" or "maria":
            acerto()
            print("PRÓXIMA PERGUNTA")
            print("NO CAMINHO DE CASA ATÉ O MERCADO, UMA SENHORA CONTA 1O ÁRVORES A SUA DIREITA. APÓS AS COMPRAS, ELA VOLTA PARA CASA E CONTA 10 ÁRVORES A SUA ESQUERDA. QUANTAS ÁRVORES ELA VIU NO TOTAL NESSE DIA?")
            print("DICA= PENSAR QUE APENAS INVERTE O LADO")
            resposta1=int(input())
            if resposta1==10:
                acerto()
                print("PRÓXIMA PERGUNTA")
                print(" FÁBIO FOI SOZINHO ATÉ A PADARIA NO CENTRO DA CIDADE. DURANTE O PERCURSO, ENCONTROU DUAS GAROTAS PASSEANDO COM TRÊS CACHORROS, QUE ESTAVAM BRINCANDO COM DOIS GATOS, QUE, POR SUA VEZ, TINHAM DOIS DONOS. QUANTOS SERES NO TOTAL FORAM COM FÁBIO ATÉ A PADARIA?")
                resposta2=int(input())

                if resposta2==0:
                    os.system("cls")
                    print("VOCÊ RESPONDEU TODAS AS PERGUNTAS CORRETAMENTE E DERROTOU O BOSS")
                    input("ENTER PARA SAIR DO CALABOUÇO: ")
                    os.system("cls")
                    print(linha(115))
                    print("VOCÊ FUGIU. OBRIGADO POR JOGAR.".center(115))
                    print(linha(115))
                    quit()
                else:
                    morte_monstro()
            else:
                morte_monstro()
        else:
            morte_monstro()


def boss3():
    input("APERTE ENTER PARA CONTINUAR: ")
    os.system("cls")
    print("AQUI È O BOSS FINAL , NELE VOCÊ TERÁ QUE RESPONDER 3 PERGUNTAS ")
    print("SE DURANTE O SEU PERCURSO PEGOU ALGUM ITEM ELE IRÁ TE AJUDAR AGORA")
    print (" SE PEGOU O PRIMIERO ITEM, ELE É UMA ESPADA. ASSIM NÃO PRECISARÁ RESPONDER UMA PERGUNTA \nSE PEGOU O SEGUNDO ITEM, ELE É UMA ARMADURA. ASSIM TERÁ UMA DICA NA SEGUNDA PERGUNTA\nSE PEGOU O TERCEIRO ITEM, ELE É UM......CALMA AÍ UM LÁPIS? PRA QUE VC USARIA UM LAPIS. VOCÊ NÂO TERÀ NENHUMA VANTAGEM "  )
    if item==0:
        print("PRIMEIRA PERGUNTA")
        print("A MÃE DE MARIA TEM CINCO FILHAS: FAFÁ, FEFÊ, FIFI, FOFÓ E? QUAL É O NOME DA QUINTA FILHA?")
        resposta=input()
        if resposta=="Maria" or "MARIA" or "maria":
            acerto()
            print("PRÓXIMA PERGUNTA")
            print("NO CAMINHO DE CASA ATÉ O MERCADO, UMA SENHORA CONTA 1O ÁRVORES A SUA DIREITA. APÓS AS COMPRAS, ELA VOLTA PARA CASA E CONTA 10 ÁRVORES A SUA ESQUERDA. QUANTAS ÁRVORES ELA VIU NO TOTAL NESSE DIA?")
            resposta1=int(input())
            if resposta1==10:
                acerto()
                print("PRÓXIMA PERGUNTA")
                print(" FÁBIO FOI SOZINHO ATÉ A PADARIA NO CENTRO DA CIDADE. DURANTE O PERCURSO, ENCONTROU DUAS GAROTAS PASSEANDO COM TRÊS CACHORROS, QUE ESTAVAM BRINCANDO COM DOIS GATOS, QUE, POR SUA VEZ, TINHAM DOIS DONOS. QUANTOS SERES NO TOTAL FORAM COM FÁBIO ATÉ A PADARIA?")
                resposta2=int(input())
                if resposta2==0:
                    os.system("cls")
                    print("VOCÊ RESPONDEU TODAS AS PERGUNTAS CORRETAMENTE E DERROTOU O BOSS")
                    input("ENTER PARA SAIR DO CALABOUÇO: ")
                    os.system("cls")
                    print(linha(115))
                    print("VOCÊ FUGIU. OBRIGADO POR JOGAR.".center(115))
                    print(linha(115))
                    quit()
                else:
                    morte_monstro()
            else:
                morte_monstro()
        else:
            morte_monstro()

def boss0():
    input("APERTE ENTER PARA CONTINUAR: ")
    os.system("cls")
    print("AQUI È O BOSS FINAL , NELE VOCÊ TERÁ QUE RESPONDER 3 PERGUNTAS ")
    print("SE DURANTE O SEU PERCURSO PEGOU ALGUM ITEM ELE IRÁ TE AJUDAR AGORA")
    print (" SE PEGOU O PRIMIERO ITEM, ELE É UMA ESPADA. ASSIM NÃO PRECISARÁ RESPONDER UMA PERGUNTA \nSE PEGOU O SEGUNDO ITEM, ELE É UMA ARMADURA. ASSIM TERÁ UMA DICA NA SEGUNDA PERGUNTA\nSE PEGOU O TERCEIRO ITEM, ELE É UM......CALMA AÍ UM LÁPIS? PRA QUE VC USARIA UM LAPIS. VOCÊ NÂO TERÀ NENHUMA VANTAGEM "  )

    if item==0:
        print("PRIMEIRA PERGUNTA")
        print("A MÃE DE MARIA TEM CINCO FILHAS: FAFÁ, FEFÊ, FIFI, FOFÓ E? QUAL É O NOME DA QUINTA FILHA?")
        resposta=input()
        if resposta=="Maria" or resposta=="MARIA" or resposta=="maria":
            acerto()
            print("PRÓXIMA PERGUNTA")
            print("NO CAMINHO DE CASA ATÉ O MERCADO, UMA SENHORA CONTA 1O ÁRVORES A SUA DIREITA. APÓS AS COMPRAS, ELA VOLTA PARA CASA E CONTA 10 ÁRVORES A SUA ESQUERDA. QUANTAS ÁRVORES ELA VIU NO TOTAL NESSE DIA?")
            resposta1=int(input())
            if resposta1==10:
                acerto()
                print("PRÓXIMA PERGUNTA")
                print(" FÁBIO FOI SOZINHO ATÉ A PADARIA NO CENTRO DA CIDADE. DURANTE O PERCURSO, ENCONTROU DUAS GAROTAS PASSEANDO COM TRÊS CACHORROS, QUE ESTAVAM BRINCANDO COM DOIS GATOS, QUE, POR SUA VEZ, TINHAM DOIS DONOS. QUANTOS SERES NO TOTAL FORAM COM FÁBIO ATÉ A PADARIA?")
                resposta2=int(input())
                if resposta2==0:
                    os.system("cls")
                    print("VOCÊ RESPONDEU TODAS AS PERGUNTAS CORRETAMENTE E DERROTOU O BOSS")
                    input("ENTER PARA SAIR DO CALABOUÇO: ")
                    os.system("cls")
                    print(linha(115))
                    print("VOCÊ FUGIU. OBRIGADO POR JOGAR.".center(115))
                    print(linha(115))
                    quit()
                else:
                    morte_monstro()
            else:
                morte_monstro()
        else:
            morte_monstro()

def bug_andar():
    os.system("cls")
    print("APÓS O AVENTUREIRO NÃO SEGUIR AS INSTRUÇÕES, ELE DA DE CARA NA PAREDE, CAI PARA TRÁS E BATE A CABEÇA NO CHÃO......")
    print("POR FAVOR SIGA AS INSTRUÇÕES!!!!!".center(115))
    print(linha(tam=115))
    print("VOCÊ MORREU".center(115))
    print(linha(tam=115))
    input("APERTE ENTER PARA RECOMEÇAR")
    os.system("cls")
    game()

def morte_monstro():
    os.system('cls')
    print(linha(115))
    print('VOCÊ ERROU A QUESTÃO E O MONSTRO TE ATACOU.... VOCÊ MORREU').center(115)
    print(linha(115))


def bug_luta():
    os.system("cls")
    print("")
    print("APÓS O AVENTUREIRO NÃO ESCOLHER ENTRE LUTAR OU CORRER, ELE FICA PARADO SEM SABER O QUE FAZER E È ATACADO PELO MONSTRO ")
    print("")
    print(linha(tam=115))
    print("VOCÊ MORREU".center(115))
    print(linha(tam=115))
    input("ENTER PARA RECOMEÇAR")
    os.system("cls")
    game()

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)


def linha(tam=42):
    return "-" * tam


def game():
    print("AQUI É O INICIO DO CALABOUÇO, VOCÊ PODE IR SOMENTE PARA FRENTE")
    i=input()
    if i=='w' or i=='W':
        os.system("cls")
        print("ESSE É O SEGUNDO ANDAR E NELE NAO A ABOSLUTAMENTE NADA. VOCÊ ESCOLHE SE VAI PARA FRENTE OU PARA A ESQUERDA.")
        c=input()
        if c=='w' or c=='W':
            print('VOCÊ CHEGOU AO TERCEIRO ANDAR')
            print('VOCÊ ENCONTROU UM INIMIGO, CORRER OU LUTAR? PRESSIONE C PARA CORRER OU L PARA LUTAR')
            lll=input()
            if lll=='c' or lll=='C':
                print('VOCÊ CHEGOU AO QUARTO ANDAR, PODE IR PARA FRENTE OU PARA DIREITA')
                tt=input()
                if tt=='w' or tt=='W':
                    print('ESSE É O QUINTO ANDAR, VOCÊ PODE SEGUIR SOMENTE EM FRENTE')
                    yy=input()
                    if yy=='w' or yy=='W':
                        print('SEXTO ANDAR, AQUI TEMOS UM INIMIGO, PRESSIONE L PARA LUTAR OU C PARA CORRER')
                        y=input()
                        if y=='c' or y=='C':
                            print('SÉTIMO ANDAR, IR PARA FRENTE OU PARA DIREITA, CUIDADO A PRÓXIMA SALA A FRENTE É A SALA DO CHEFE')
                            input()
                            os.system('cls')
                            print('MAS VOCÊ NÃO ESTA ACHANDO TUDO ISSO MUITO FACIL ?')
                            print('APÓS CORRER DE TODOS OS INIMIGOS, ASSIM COMO CORRE DAS RESPONSABILIDADES NA VIDA, O AVENTUREIRO RETORNOU AO INICIO')
                            print(linha())
                            print('GAME OVER'.center(42))
                            print(linha())
                            game()
                        elif y=='l' or y=='L':
                            print('QUEM É O PAI DA COMPUTAÇÃO ?')
                            answer=input()
                            if answer=='Alan Turing' or answer=='alan turing':
                                acerto()
                                print('SÉTIMO ANDAR, IR PARA FRENTE OU PARA DIREITA, CUIDADO A PRÓXIMA SALA A FRENTE É A SALA DO CHEFE')
                                alo=input()
                                if alo=='w' or alo=='W':
                                    print('O CHEFE É UM ORC DE 4 METROS DE ALTURA')
                                elif alo=='d' or alo=='D':
                                    print('ESSA É UMA SALA VAZIA, VOCÊ PODE IR SOMENTE PARA DIREITA')
                                    j=input()
                                    if j=='D' or j=='d':
                                        print('ESSA É UMA SALA DE VENDA DE ITENS, PELA ALMA DE INIMIGOS. CADA INIMIGO TE CONCEDE 1 ALMA.')
                                        input('item1')
                                        input('item2')
                                        input('item3')
                                        print('VOCÊ PODE ESCOLHER OS ITENS BASEADO EM QUANTOS INIMGIGOS MATOU DURANTE A AVENTURA')
                                        print('VOCÊ MATOU 1 INIMIGO, LOGO PODE ESCOLHER SOMENTE O ITEM 1 , DIGITE O NUMERO DO RESPECTIVO DO ITEM QUE VOCÊ QUER.')
                                        item=input()
                                        if item=='1':
                                            print('VOCÊ PEGOU O ITEM 1, APERTE A PARA IR A SALA DO BOSS')
                                            o=input()
                                            if o=='A' or o=='a':
                                                print('VOCÊ CHEGOU A SALA DO BOSS')
                                                boss1()
                                            else:
                                                bug_andar()
                                        else:
                                            bug_item()        
                                    else:
                                        bug_andar()
                                else:
                                    bug_andar()  
                            else:
                                morte_monstro()
                        else:
                            bug_luta()
                    else:
                        bug_andar
                elif tt=='d' or tt=='D':
                    print('VOCÊ ENCONTROU UM INIMIGO, CORRER OU LUTAR ? PRESSIONE C PARA CORRER OU L PARA LUTAR')
                    f=input()
                    if f=='c' or f=='C':
                        print('VOCÊ PODE IR SOMENTE PARA FRENTE. ESSA SALA ESTA VAZIA')
                        j=input()
                        if j=='w' or j=='W':
                            print('CORRER DE TODOS INIMIGOS NÃO VAI TE LEVAR A UM BOM CAMINHO. A VOZ DO ALÉM SEMPRE TEM RAZÃO.')
                            print('VÁ PARA ESQUERDA PARA VOLTAR AO CAMINHO PRINCIPAL')
                            i=input()
                            if i=='a' or i=='A':
                                print('ESSE É O QUINTO ANDAR, VOCÊ PODE IR SOMENTE PARA A FRENTE')
                                j=input()
                                if j=='w' or j=='W':
                                    print('SEXTO ANDAR, AQUI TEMOS UM INIMIGO, CORRER OU LUTAR ?PRESSIONE C PARA CORRER OU L PARA LUTAR')
                                    j=input()
                                    if j=='c' or j=='C': 
                                        print('AO CORRER DE TODOS OS INIMIGOS ASSIM COMO CORRE DAS RESPONSABILIDADES NA VIDA, NOSSO PROTAGONISTA MORRE EM UMA ARMADILHA')
                                        restart_program()
                                    if j=='l' or j=='L':
                                        print('O INIMIGO É UM ZUMBI, ACERTE A QUESTÃO PARA VENCER.')
                                        print('UMA ARANHA ESTÁ SUBINDO UM MURO DE 10 METROS. DURANTE O DIA, ELA CONSEGUE SUBIR DOIS METROS, PORÉM TODAS AS NOITES, ELA DESCE UM METRO. EM QUANTO TEMPO ELA CONSEGUIRÁ CHEGAR AO TOPO?')
                                        resp=input()
                                        if resp=='8' or resp=='oito' or resp=='Oito':
                                            acerto()
                                            print('CHEGOU AO SÉTIMO ANDAR, VOCÊ PODE IR PARA FRENTE OU PARA A DIREITA, CUIDADO!! A FRENTE É A SALA DO CHEFE')
                                            j=input()
                                            if j=='w' or j=='W':
                                                print('VOCÊ CHEGOU A SALA DO CHEFE, PRESSIONE ENTER PARA INICIAR A BATALHA:')
                                                input()
                                                boss0()
                                            elif j=='d' or j=='D':
                                                print('ESSA É UMA SALA VAZIA, VOCÊ PDOE IR SOMENTE PARA A DIREITA')
                                                k=input()
                                                if k=='d' or k=='D':
                                                    print('ESSA É UMA SALA DE VENDA DE ITENS, PELA ALMA DE INIMIGOS. CADA INIMIGO TE CONCEDE 1 ALMA.')
                                                    input('item1')
                                                    input('item2')
                                                    input('item3')
                                                    print('VOCÊ PODE ESCOLHER OS ITENS BASEADO EM QUANTOS INIMGIGOS MATOU DURANTE A AVENTURA')
                                                    print('VOCÊ MATOU 1 INIMIGO, LOGO PODE ESCOLHER SOMENTE O ITEM 1, DIGITE O NUMERO DO RESPECTIVO ITEM QUE VOCÊ QUER.')
                                                    item=input()
                                                    if item=='1':
                                                        print('VOCÊ PEGOU O ITEM 1, APERTE A PARA IR A SALA DO BOSS')
                                                        o=input()
                                                        if o=='a' or o=='A':
                                                            print('VOCÊ CHEGOU A SALA DO BOSS')
                                                            boss1()
                                                    elif item=='2':
                                                        print('VOCÊ NÃO PODE PEGAR ESSE ITEM, COMO PUNIÇÃO POR TENTAR TRAPACEAR, RECOMECE O JOGO.') 
                                                        input()
                                                        restart_program()
                                                  
                                                    elif item=='3':
                                                        print('VOCÊ NÃO PODE PEGAR ESSE ITEM, COMO PUNIÇÃO POR TENTAR TRAPACEAR, RECOMECE O JOGO.')
                                                        input() 
                                                        restart_program()
                                                    else:
                                                        bug_item()
                                                else:
                                                    bug_andar()
                                            else:
                                                bug_andar()
                                        else:
                                            morte_monstro()
                                    else:
                                        bug_luta()
                                else:
                                    bug_andar()
                            else:
                                bug_andar()
                        else:
                            bug_andar()
                    elif f=='l' or f=='L':
                        print('O INIMIGO É UM ZUMBI, ACERTE A QUESTÃO PARA MATA-LÔ')
                        print('UMA FAMÍLIA RESOLVEU PASSEAR DE CARRO. NELE ENTRARAM 1 AVÔ, 2 PAIS, 2 FILHOS E 1 NETO. QUAL O NÚMERO MÍNIMO DE PESSOAS DENTRO DO VEÍCULO, AFINAL?')
                        resposta=input()
                        if resposta=='4' or resposta=='quatro' or resposta=='Quatro':
                            acerto()
                            print('VOCÊ PODE IR SOMENTE PARA FRENTE. ESSA SALA ESTA VAZIA')
                            a=input()
                            if a=='w' or a=='W':
                                print('ESSA SALA TAMBEM ESTA VAZIA, VÁ PARA ESQUERDA')
                                j=input()
                                if j=='a' or j=='A':
                                    print('QUINTO ANDAR, ESSA SALA ESTA VAZIA, VOCÊ PODE IR SOMENTE PARA FRENTE')
                                    K=input()
                                    if K=='w' or K=='W':
                                        print('SEXTO ANDAR, AQUI SE ENCONTRA UM INIMIGO, LUTAR OU CORRER ?PRESSIONE C PARA CORRER OU L PARA LUTAR')
                                        l=input()
                                        if l=='c' or l=='C':
                                            print('SÉTIMO ANDAR, VOCÊ PODE IR PARA FRENTE OU PARA A DIREITA.CUIDADO!! A PRÓXIA SALA EM FRENTE É A SALA DO CHEFE')
                                            j=input()
                                            if j=='w' or j=='W':
                                                print('VOCÊ CHEGOU A SALA DO CHEFE, PRESSIONE ENTER PARA INICIAR A BATALHA:')
                                            if j=='d' or j=='D':
                                                print('ESSA É UMA SALA VAZIA, VOCÊ PODE IR SOMENTE PARA A ESQUERDA')
                                                i=input()
                                                if i=='d' or i=='D':
                                                    print('ESSA É UMA SALA DE VENDA DE ITENS, PELA ALMA DE INIMIGOS. CADA INIMIGO TE CONCEDE 1 ALMA.')
                                                    input('item1')
                                                    input('item2')
                                                    input('item3')
                                                    print('VOCÊ PODE ESCOLHER OS ITENS BASEADO EM QUANTOS INIMGIGOS MATOU DURANTE A AVENTURA')
                                                    print('VOCÊ MATOU 1 INIMIGO, LOGO PODE ESCOLHER SOMENTE O ITEM 1, DIGITE O NUMERO DO RESPECTIVO ITEM QUE VOCÊ QUER.')
                                                    item=input()
                                                    if item=='1':
                                                        print('VOCÊ PEGOU O ITEM 1, APERTE A PARA IR A SALA DO BOSS')
                                                        o=input()
                                                        if o=='a' or o=='A':
                                                            print('VOCÊ CHEGOU A SALA DO BOSS')
                                                            boss1()
                                                    
                                                    elif item=='2':
                                                        print('VOCÊ NÃO PODE PEGAR ESSE ITEM, COMO PUNIÇÃO POR TENTAR TRAPACEAR, RECOMECE O JOGO.') 
                                                        input()
                                                        restart_program()
                                                  
                                                    elif item=='3':
                                                        print('VOCÊ NÃO PODE PEGAR ESSE ITEM, COMO PUNIÇÃO POR TENTAR TRAPACEAR, RECOMECE O JOGO.')
                                                        input() 
                                                        restart_program()
                                                    else:
                                                        bug_item()
                                                else:
                                                    bug_andar()
                                            else:
                                                bug_andar()
                                        elif l=='l' or l=='L':
                                            print('O INIMIGO É UM VAMPIRO, ACERTE A QUESTÃO PARA DERROTA-LO')
                                            print('QUANTOS CONTINENTES TEM O PLANETA ?')
                                            r=input()
                                            if r==6 or r=='seis' or r=='Seis':
                                                acerto()
                                                print('VOCÊ CHEGOU AO SÉTIM ANDAR, PDOE IR PARA FRENTE OU PARA A DIREITA. CUIDADO!!! A PRÓXIMA SALA A FRENTE É A DO CHEFE.')
                                                a=input()
                                                if a=='w' or a=='W':
                                                    print('CHEGOU A SALA DO CHEFE. APERTE ENTER PARA INICIAR A BATALHA:')
                                                    input()
                                                    boss0()
                                                elif a=='d' or a=='D':
                                                    print('ESSA É UMA SALA VAZIA, VOCÊ SÓ PODE IR PARA DIREITA')
                                                    b=input()
                                                    if b=='a' or b=='A':
                                                        print('ESSA É UMA SALA DE VENDA DE ITENS, PELA ALMA DE INIMIGOS. CADA INIMIGO TE CONCEDE 1 ALMA.')
                                                    input('item1')
                                                    input('item2')
                                                    input('item3')
                                                    print('VOCÊ PODE ESCOLHER OS ITENS BASEADO EM QUANTOS INIMGIGOS MATOU DURANTE A AVENTURA')
                                                    print('VOCÊ MATOU 1 INIMIGO, LOGO PODE ESCOLHER SOMENTE O ITEM 1, DIGITE O NUMERO DO RESPECTIVO ITEM QUE VOCÊ QUER.')
                                                    item=input()
                                                    if item=='1':
                                                        print('VOCÊ PEGOU O ITEM 1, APERTE A PARA IR A SALA DO BOSS')
                                                        o=input()
                                                        if o=='a' or o=='A':
                                                            print('VOCÊ CHEGOU A SALA DO BOSS')
                                                            boss1()
                                                    
                                                    elif item=='2':
                                                        print('VOCÊ NÃO PODE PEGAR ESSE ITEM, COMO PUNIÇÃO POR TENTAR TRAPACEAR, RECOMECE O JOGO.') 
                                                        input()
                                                        restart_program()
                                                  
                                                    elif item=='3':
                                                        print('VOCÊ NÃO PODE PEGAR ESSE ITEM, COMO PUNIÇÃO POR TENTAR TRAPACEAR, RECOMECE O JOGO.')
                                                        input() 
                                                        restart_program()
                                                    else:
                                                        bug_item()
                                                else:
                                                    bug_andar()
                                            else:
                                                morte_monstro()
                                        else:
                                            bug_luta()
                                    else:
                                        bug_andar()
                                else:
                                    bug_andar()
                            else:
                                bug_andar()
                        else:
                            morte_monstro()
                    else:
                        bug_luta()
                else:
                    bug_andar()   
            elif lll=='l' or lll=='L':
                print('O INIMIGO É UM ESQUELETO, ACERTE A QUESTÃO PARA PODER MATA-LÔ')
                print('QUAL A SIGLA DA CAPITAL DO BRASIL ?')
                resposta=input()
                if resposta=='DF'or resposta=='df':
                    acerto()
                    input("ENTER PARA CONTINUAR: ")
                    os.system('cls')
                    print('VOCÊ CHEGOU AO QUARTO ANDAR, PODE IR PARA FRENTE OU PARA A DIREITA')
                    andar=input()
                    if andar=='w' or andar=='W':
                        print('ESSE É O QUINTO ANDAR, VOCÊ PODE SEGUIR SOMENTE EM FRENTE')
                        uu=input()
                        if uu=='w' or uu=='W':
                            print('SEXTO ANDAR, ENCONTROU UM INIMIGO. ELE É MAIS FORTE QUE A HARPIA. PARA DERROTÁ-LO TERÁ QUE RESPONDER UMA QUESTÃO MAIS DIFÍCIL. PRESSIONE L PARA LUTAR OU C PARA CORRER')
                            ii=input()
                            if ii=="l" or ii=='L':
                                print('O INIMIGO É UM FANTASMA, VOCÊ PRECISA RESPONDER UMA PERGUNTA PARA PASSAR DELE')
                                print("SE, DURANTE UMA CORRIDA DE CARROS, VOCÊ DEIXA O SEGUNDO COLOCADO PARA TRÁS, QUAL É A SUA COLOCAÇÃO APÓS A ULTRAPASSAGEM?")
                                pergunta1=(input())
                                if pergunta1== "segundo" or "SEGUNDO":
                                    acerto()
                                    print("VOCÊ CHEGOU AO SÉTIMO ANDAR,VOCÊ PODE IR PARA FRENTE OU PARA A DIREITA.CUIDADO!!A SALA A FRENTE É A SALA DO CHEFE FINAL")
                                    k=input()
                                    if k=='w' or k=='W':
                                        input('ESSA É A SALA DO CHEFE,PRESSIONE ENTER PARA INICIAR A BATALHA:')
                                    elif k=='d' or k=='D':
                                        print('VOCÊ PODE IR SOMENTE PARA A DIREITA')
                                        kk=input()
                                        if kk=='d' or kk=='D':
                                            print('ESSA É UMA SALA DE VENDA DE ITENS, PELA ALMA DE INIMIGOS. CADA INIMIGO TE CONCEDE 1 ALMA.')
                                            input('item1')
                                            input('item2')
                                            input('item3')
                                            print('VOCÊ PODE ESCOLHER OS ITENS BASEADO EM QUANTOS INIMGIGOS MATOU DURANTE A AVENTURA')
                                            print('VOCÊ MATOU 2 INIMIGOS, LOGO PODE ESCOLHER ENTRE OS ITENS 1 E 2, DIGITE O NUMERO DO RESPECTIVO ITEM QUE VOCÊ QUER.')
                                            item=int(input())
                                            if item=='1':
                                                print('VOCÊ PEGOU O ITEM 1, APERTE A PARA IR A SALA DO BOSS')
                                                o=input()
                                                if o=='a' or o=='A':
                                                    print('VOCÊ CHEGOU A SALA DO BOSS')
                                                    item=1
                                                    boss1()
                                            elif item=='2':
                                                print('VOCÊ PEGOU O ITEM 2, APERTE  PARA IR A SALA DO BOSS') 
                                                o=input()
                                                if o=='a' or o=='A':
                                                    print('VOCÊ CHEGOU A SALA DO BOSS')
                                                    boss2()
                                            elif item=='3':
                                                print('VOCÊ NÃO PODE PEGAR ESSE ITEM, COMO PUNIÇÃO POR TENTAR TRAPACEAR, RECOMECE O JOGO.')
                                                input() 
                                                restart_program
                                            else:
                                                bug_item()    
                                        else:
                                            bug_andar()
                                    else:
                                        bug_andar()
                                else:
                                    morte_monstro()
                            elif ii=='c' or ii=='C':
                                print('SÉTIMO ANDAR, IR PARA FRENTE OU PARA A DIREITA? TOME CUIDADO, A SALA A FRENTE É A SALA DO CHEFE')
                                k=input()
                                if k=='w' or k=='W':
                                    input('ESSA É A SALA DO CHEFE,PRESSIONE ENTER PARA INICIAR A BATALHA:')
                                elif k=='d' or k=='D':
                                    print('VOCÊ PODE IR SOMENTE PARA A DIREITA')
                                    kk=input()
                                    if kk=='d' or kk=='D':
                                        print('ESSA É UMA SALA DE VENDA DE ITENS, PELA ALMA DE INIMIGOS. CASA INIMIGO TE CONCEDE 1 ALMA.')
                                        input('item1')
                                        input('item2')
                                        input('item3')
                                        item=input()
                                        if item=='1':
                                            print('VOCÊ PEGOU O ITEM 1, APERTE A PARA IR A SALA DO BOSS')
                                            o=input()
                                            if o=='A' or o=='a':
                                                print('VOCÊ CHEGOU A SALA DO BOSS')
                                                boss1()
                                        elif item=='2':
                                            print('VOCÊ NÃO PODE PEGAR ESSE ITEM, COMO PUNIÇÃO POR TENTAR TRAPACEAR, RECOMECE O JOGO')
                                            restart_program()
                                        elif item=='3':
                                            print('VOCÊ NÃO PODE PEGAR ESSE ITEM, COMO PUNIÇÃO POR TENTAR TRAPACEAR, RECOMECE O JOGO')
                                            restart_program()
                                    else:
                                        bug_andar()
                            else:
                                bug_luta()
                        else:
                            bug_andar()        
                    
                    elif andar=='d' or andar=='D':
                        print('VOCÊ ENCONTROU OUTRO INIMIGO, CORRER OU LUTAR ? PRESSIONE C PARA CORRER OU L PARA LUTAR')
                        gg=input()   
                        if gg=='c' or gg=='C':
                            print('AQUI É UMA SALA VAZIA')
                            print('VOCÊ PODE IR SOMENTE PARA A ESQUERDA')
                            jj=input()
                            if jj=='a' or jj=='A':
                                print('QUINTO ANDAR, VOCÊ PODE IR SOMENTE EM FRENTE')
                                uu=input()
                                if uu=='w' or uu=='W':
                                    print('SEXTO ANDAR, AQUI TEMOS UM INIMIGO, CORRER OU LUTAR ? PRESSIONE C PARA CORRER OU L PARA LUTAR')
                                    ii=input()
                                    if ii=="l" or ii=='l':
                                        print('O INIMIGO É UM FANTASMA, RESPONDA A QUESTÃO CORRETAMENTE PARA VENCE-LO')
                                        print(' UM CASAL TEM SEIS FILHOS HOMENS, CADA FILHO TEM UMA IRMÃ. QUANTAS PESSOAS HÁ NESSA FAMÍLIA NO TOTAL?')
                                        k=input()
                                        if k=='9' or k=='nove':
                                            input('SÉTIMO ANDAR, IR PARA FRENTE OU PARA DIREITA ? CUIDADO!! A PRÓXIMA SALA A FRENTE É A SALA DO CHEFE')
                                            k=input()
                                            if k=='w' or k=='W':
                                                print('VOCÊ CHEGOU NA SALA DO CHEFE? APERTE ENTER PARA INICIAR A BATALHA:')
                                                input()
                                                boss0()
                                            elif k=='d' or k=='D':
                                                print('ESSA É UMA SALA VAZIA')
                                                print('VOCÊ PODE IR SOMENTE PARA A DIREITA')
                                                kk=input()
                                                if kk=='d' or kk=='D':
                                                    print('ESSA É UMA SALA DE VENDA DE ITENS, PELA ALMA DE INIMIGOS. CADA INIMIGO TE CONCEDE 1 ALMA.')
                                                    input('item1')
                                                    input('item2')
                                                    input('item3')
                                                    print('VOCÊ PODE ESCOLHER OS ITENS BASEADO EM QUANTOS INIMGIGOS MATOU DURANTE A AVENTURA')
                                                    print('VOCÊ MATOU 2 INIMIGOS, LOGO PODE ESCOLHER ENTRE OS ITENS 1 E 2, DIGITE O NUMERO DO RESPECTIVO ITEM QUE VOCÊ QUER.')
                                                    item=input()
                                                    if item=='1':
                                                        print('VOCÊ PEGOU O ITEM 1, APERTE A PARA IR A SALA DO BOSS')
                                                        o=input()
                                                        if o=='a' or o=='A':
                                                            print('VOCÊ CHEGOU A SALA DO BOSS')
                                                            boss1()
                                                    
                                                    
                                                    elif item=='2':
                                                        print('VOCÊ PEGOU O ITEM 2, APERTE  PARA IR A SALA DO BOSS') 
                                                        o=input()
                                                        if o=='a' or o=='A':
                                                            print('VOCÊ CHEGOU A SALA DO BOSS')
                                                            boss2()
                                                  
                                                    elif item=='3':
                                                        print('VOCÊ NÃO PODE PEGAR ESSE ITEM, COMO PUNIÇÃO POR TENTAR TRAPACEAR, RECOMECE O JOGO.')
                                                        input() 
                                                        restart_program
                                                    else:
                                                        bug_item()
                                                else:
                                                    bug_andar()            
                                            else:
                                                bug_andar()    
                                        else:
                                            morte_monstro()
                                    elif ii=='c' or ii=='C':
                                        print('SÉTIMO ANDAR, IR PARA FRENTE OU PARA A DIREITA? TOME CUIDADO, A SALA A FRENTE É A SALA DO CHEFE')
                                        k=input()
                                        if k=='w' or k=='W':
                                            input('ESSA É A SALA DO CHEFE,PRESSIONE ENTER PARA INICIAR A BATALHA:')
                                        elif k=='d' or k=='D':
                                            print('VOCÊ PODE IR SOMENTE PARA A DIREITA')
                                            kk=input()
                                            if kk=='d' or kk=='D':
                                                print('ESSA É UMA SALA DE VENDA DE ITENS, PELA ALMA DE INIMIGOS. CADA INIMIGO TE CONCEDE 1 ALMA.')
                                            input('item1')
                                            input('item2')
                                            input('item3')
                                            print('VOCÊ PODE ESCOLHER OS ITENS BASEADO EM QUANTOS INIMGIGOS MATOU DURANTE A AVENTURA')
                                            print('VOCÊ MATOU 1 INIMIGO, LOGO PODE ESCOLHER SOMENTE O ITEM1, DIGITE O NUMERO DO RESPECTIVO ITEM QUE VOCÊ QUER.')
                                            item=input()
                                            if item=='1':
                                                print('VOCÊ PEGOU O ITEM 1, APERTE A PARA IR A SALA DO BOSS')
                                                o=input()
                                                if o=='a' or o=='A':
                                                    print('VOCÊ CHEGOU A SALA DO BOSS')
                                                    boss1()
                                                    
                                            elif item=='2':
                                                print('VOCÊ NÃO PODE PEGAR ESSE ITEM, COMO PUNIÇÃO POR TENTAR TRAPACEAR, RECOMECE O JOGO.') 
                                                input()
                                                restart_program()
                                                  
                                            elif item=='3':
                                                print('VOCÊ NÃO PODE PEGAR ESSE ITEM, COMO PUNIÇÃO POR TENTAR TRAPACEAR, RECOMECE O JOGO.')
                                                input() 
                                                restart_program()
                                                

                                            else:
                                                bug_item()    
                                        else:
                                            bug_andar()
                                    else:
                                        bug_luta()
                                else:
                                    bug_andar()  
                            else:
                                bug_andar()                     
                        elif gg=='l' or gg=='L':
                            print('ENCONTROU UM INIMIGO')
                            print('O INIMIGO É UM CAVALEIRO, ACERTE A QUESTÃO PARA VENCER')
                            print('QUAL É O SUCESSOR DO DOBRO DO ANTECESSOR DO SUCESSOR DO TRIPLO DE 2?')
                            resposta=input()
                            if resposta=='13' or resposta=='treze':
                                acerto()
                                print('AQUI É UMA SALA VAZIA')
                                print('VOCÊ SÓ PODE IR PARA A ESQUERDA')
                                m=input()
                                if m=='a' or m=='A':
                                    print('VOCÊ CHEGOU AO QUINTO ANDAR, PODE IR SOMENTE PARA FRENTE')
                                    j=input()
                                    if j=='w' or j=='W':
                                        print('SEXTO ANDAR, AQUI SE ENCONTRA UM VAMPIRO, CORRER OU LUTAR? PRESSIONE C PARA CORRER OU L PARA LUTAR')
                                        u=input()
                                        if u=='l' or u=='L':
                                            print('ACERTE A QUESTÃO PARA VENCER O INIMIGO')
                                            print('NO CAMINHO DE CASA ATÉ O MERCADO, UMA SENHORA CONTA 10 ÁRVORES A SUA DIREITA. APÓS AS COMPRAS, ELA VOLTA PARA CASA E CONTA 10 ÁRVORES A SUA ESQUERDA. QUANTAS ÁRVORES ELA VIU NO TOTAL NESSE DIA?')
                                            r=input()
                                            if r=='10' or r=='dez':
                                                print('SÉTIMO ANDAR, VOCÊ PODE IR PARA FRENTE OU PARA A DIREITA. CUIDADO!!! A PRÓXIMA SALA A FRENTE É A DO CHEFE.')
                                                a=input()
                                                if a=='w' or a=='W':
                                                    print('VOCÊ CHEGOU A SALA DO CHEFE, PRESSIONE ENTER PARA INICIAR A BATALHA:')
                                                    input()
                                                    boss0()
                                                elif a=='d' or a=='D':
                                                    print('ESSA SALA ESTA VAZIA, VOCÊ SÓ PODE IR SOMENTE PARA A DIREITA')
                                                    h=input()
                                                    if h=='d' or h=='D':
                                                        print('ESSA É UMA SALA DE VENDA DE ITENS, PELA ALMA DE INIMIGOS. CADA INIMIGO TE CONCEDE 1 ALMA.')
                                                        input('item1')
                                                        input('item2')
                                                        input('item3')
                                                        print('VOCÊ PODE ESCOLHER OS ITENS BASEADO EM QUANTOS INIMGIGOS MATOU DURANTE A AVENTURA')
                                                        print('VOCÊ MATOU 3 INIMIGOS, LOGO PODE ESCOLHER ENTRE OS ITENS 1, 2 E 3, DIGITE O NUMERO DO RESPECTIVO ITEM QUE VOCÊ QUER.')
                                                        item=input()
                                                        if item=='1':
                                                            print('VOCÊ PEGOU O ITEM 1, APERTE A PARA IR A SALA DO BOSS')
                                                            o=input()
                                                            if o=='a' or o=='A':
                                                                print('VOCÊ CHEGOU A SALA DO BOSS')
                                                                boss1()
                                                    
                                                    
                                                        elif item=='2':
                                                            print('VOCÊ PEGOU O ITEM 2, APERTE A PARA IR A SALA DO BOSS') 
                                                            o=input()
                                                            if o=='a' or o=='A':
                                                                print('VOCÊ CHEGOU A SALA DO BOSS')
                                                                boss2()
                                                            else:
                                                                bug_andar()
                                                        
                                                        elif item=='3':
                                                            print('VOCÊ PEGOU O ITEM 3, APERTE A PARA IR A SALA DO BOSS')
                                                            o=input() 
                                                            if o=='a' or o=='A':
                                                                print('VOCÊ CHEGOU A SALA DO BOSS')
                                                                boss3()
                                                        
                                                            else:
                                                                bug_andar()
                                                        else:
                                                            bug_item()
                                                        
                                                    else:
                                                        bug_andar()
                                                else:
                                                    bug_andar()
                                            else:
                                                morte_monstro()                
                                        else:
                                            bug_luta()
                                    else:
                                        bug_andar()                
                                else:
                                    bug_andar()
                            else:
                                morte_monstro()                    
                        else:
                            bug_luta()        
                    else:
                        bug_andar()
                else:
                    morte_monstro()
            else:
                bug_luta()
        
        elif c=='a' or c=='A':
            print('VOCÊ ENCONTROU UM INIMIGO, CORRER OU LUTAR ? PRESSIONE C PARA CORRER OU L PARA LUTAR')
            escolha=input()
            if escolha=='c' or escolha=='C':
                print('VOCÊ FUGIU E VOLTOU A ANTIGA SALA, O INICIO DO CALABOUÇO')
                input()
                game()
            elif escolha=='l' or escolha=='L':   
                print('HAHAHA, VOCÊ ENCONTROU UM DRAGÃO INVENCÍVEL.')
                print(linha())
                print('GAMER OVER')
                print(linha())
                input()
                os.system('cls')
            else:
                bug_luta()
        else:
            bug_andar()    
    else:
        bug_andar()
    

