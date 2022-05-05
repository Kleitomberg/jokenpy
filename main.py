#importações
import pygame
from random import choice
from time import sleep

#inicialização do pygame
pygame.init()
vitorias = 0
derrotas = 0
vida = 3
rouds = 1
round =" "
escolha = ""
computador = choice(['Pedra','Papel','Tesoura'])
# dimensões da tela em px
screen_width = 700
screen_height = 400

#definindo tela
tela = pygame.display.set_mode([screen_width, screen_height])

#modificando nome e icon
pygame.display.set_caption("Jokenpy")
icon = pygame.image.load("assets/imagens/icon.png")
pygame.display.set_icon(icon)

#carregar imagens
pedraImg = pygame.image.load('assets/imagens/pedra.png')
papelImg = pygame.image.load('assets/imagens/papel.png')
tesouraImg = pygame.image.load('assets/imagens/tesoura.png')
bgImg = pygame.image.load('assets/imagens/bg.png')
pressStartImg= pygame.image.load('assets/imagens/iniciar.png')

#textos

pygame.font.init()

fonte_padrao = pygame.font.get_default_font()
pedraLegenda = pygame.font.SysFont(fonte_padrao,20)
papelLegenda = pygame.font.SysFont(fonte_padrao,20)
tesouraLegenda = pygame.font.SysFont(fonte_padrao,20)
quantRoudsLegenda = pygame.font.SysFont(fonte_padrao, 16)
qunatVitoriasLegenda = pygame.font.SysFont(fonte_padrao, 16)
qunatDerrotasLegenda = pygame.font.SysFont(fonte_padrao, 16)

suajogadaFont = pygame.font.SysFont(fonte_padrao, 30)

textDerrotas= qunatDerrotasLegenda.render(f'Derrotas: {derrotas}',1,(255,255,255))
textVitorias= qunatVitoriasLegenda.render(f'Vitorias: {vitorias}',1,(255,255,255))
textRounds = quantRoudsLegenda.render(f'Round: {rouds}',1,(255,255,255))
textPapel = papelLegenda.render('Papel', 1,(255,255,255))
textPedra = pedraLegenda.render('Pedra', 1,(255,255,255))
textTesoura = tesouraLegenda.render('Tesoura', 1,(255,255,255))
textsuaJogada = suajogadaFont.render('Faça sua jogada', 1,(255,255,255))

textVitoria = suajogadaFont.render("Venceu o Round!", 1,(255,255,255))

textVidas = qunatDerrotasLegenda.render(f'Vidas: {vida}', 1, (255,255,255))
textDerrota = suajogadaFont.render("Perdeu o Round!", 1,(255,255,255))
textEmpate = suajogadaFont.render("Deu empate!!", 1,(255,255,255))
textVazio = suajogadaFont.render(" ", 1, (255,255,255))

#sound and music
pygame.mixer.music.load('assets/audio/S31-Night Prowler.ogg')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.5)

click = pygame.mixer.Sound('assets/audio/click.wav')
#variavel de inicialização
iniciar = False
continua = True



def end():

    tela.fill([0, 71, 171])
    tela.blit(textResultado, (280, 110))
    tela.blit(textVitorias, (320, 150))
    tela.blit(textDerrotas, (320, 180))
    tela.blit(textRounds, (320, 210))


def stat():

    tela.fill([140, 82, 255])

    opcoesbg = pygame.sprite.Group()
    background = pygame.sprite.Sprite(opcoesbg)
    background.image = bgImg
    background.rect = pygame.Rect(0, 0, 700, 400)

    pressStrat = pygame.sprite.Sprite(opcoesbg)
    pressStrat.image = pressStartImg

    pressStrat.rect = pygame.Rect(280,310,456,90)



    opcoesbg.draw(tela)


#função que exibi coisas na tela
def desenhar():


    textVitoria = suajogadaFont.render(f"{round}", 1, (255, 255, 255))
    tela.fill([0, 71, 171])
    pygame.mixer.music.set_volume(0.1)
    opcoes = pygame.sprite.Group()

    pedra = pygame.sprite.Sprite(opcoes)
    pedra.image =pedraImg
    pedra.image = pygame.transform.scale(pedra.image,[80,80])
    pedra.rect = pygame.Rect(150, 150, 100, 100)

    papel = pygame.sprite.Sprite(opcoes)
    papel.image = papelImg
    papel.image = pygame.transform.scale(papel.image, [80, 80])
    papel.rect = pygame.Rect(300, 150, 100, 100)

    tesoura = pygame.sprite.Sprite(opcoes)
    tesoura.image = tesouraImg
    tesoura.image = pygame.transform.scale(tesoura.image, [80, 80])
    tesoura.rect = pygame.Rect(450, 150, 100, 100)

    #desenha os sprites que estão dentro do grupo

    opcoes.draw(tela)
    tela.blit(textVidas, (30, 30))
    tela.blit(textRounds, (600, 30))
    tela.blit(textVitorias, (90,30))
    tela.blit(textDerrotas, (160, 30))
    tela.blit(textPapel, (322,240))
    tela.blit(textPedra,(172,240) )
    tela.blit(textTesoura,(465,240))
    tela.blit(textsuaJogada,(265,110))
    current_time = pygame.time.get_ticks()
    message_end_time = 0

    if round !="FIM DE JOGO":
        if round == "Vitoria":

            message_end_time = pygame.time.get_ticks() + 1000
            if current_time < message_end_time:
                tela.blit(textResultado, (310, 320))
                pygame.display.flip()

            else:
                tela.blit(textVazio,(310, 320))
            pygame.display.update()

        if round == "Derrota":


            message_end_time = pygame.time.get_ticks() + 1000
            if current_time < message_end_time:
                tela.blit(textResultado, (310, 320))
                pygame.display.flip()
                pygame.display.update()
            else:
                tela.blit(textVazio,(310, 320))


            pygame.display.update()

        if round == "Empate":

            message_end_time = pygame.time.get_ticks() + 1000
            if current_time < message_end_time:
                tela.blit(textResultado, (280, 320))
                pygame.display.flip()
                pygame.display.update()
            else:
                tela.blit(textResultado,(280, 320))
                pygame.display.update()
    elif round =="FIM DE JOGO":
        tela.blit(textResultado, (280, 320))
        sleep(0.5)
        end()
    if not continua:
        tela.fill([0, 71, 171])

    pygame.display.update()









if __name__ == '__main__':  # verificação padrão do python



    #Loop inifinito
    while continua:
        textVidas = qunatDerrotasLegenda.render(f'Vidas: {vida}', 1, (255, 255, 255))
        if round =="Empate" or round ==" ":
            textResultado = suajogadaFont.render(f"{round}", 1, (255, 255, 255))
        elif round=="Derrota":
            textResultado = suajogadaFont.render(f"{round}", 1, (168, 50, 58))
        elif round== "Vitoria":
            textResultado = suajogadaFont.render(f"{round}", 1, (50, 168, 115))
        elif round =="FIM DE JOGO":
            textResultado = suajogadaFont.render(f"{round}", 1, (255, 221, 31))

        textRounds = quantRoudsLegenda.render(f'Round: {rouds}', 1, (255, 255, 255))
        textDerrotas = qunatDerrotasLegenda.render(f'Derrotas: {derrotas}', 1, (255, 255, 255))
        textVitorias = qunatVitoriasLegenda.render(f'Vitorias: {vitorias}', 1, (255, 255, 255))



            #continua = False

        comandos = pygame.event.get()


        for comando in comandos:
            if comando.type == pygame.QUIT:
                continua = False

            if comando.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                click.play()
                if iniciar:
                    pass

                #print(pos)
                computador = choice(['Pedra','Papel','Tesoura'])

                if not iniciar:
                    if (pos[0] >=280 and pos[0] <= 406) and (pos[1] >=320 and pos[1]<=349):
                        iniciar = True
                else:
                    #verifica se o jogador clicou na pedra
                    if (pos[0] >=150 and pos[0] <= 250) and (pos[1] >=150 and pos[1]<=250):
                        rouds += 1
                        if (computador == "Tesoura"):
                            vitorias+=1
                            round="Vitoria"
                            tela.blit(textVitoria, (280, 320))
                            sleep(2)

                        elif computador=="Papel":

                            round = "Derrota"
                            derrotas += 1
                            vida-=1
                            if vida <= 0:
                                round = "FIM DE JOGO"
                                end()
                            sleep(2)
                        elif computador=="Pedra":
                            round = "Empate"

                            pass
                        #print("Você clicou Pedra")
                        #print(f"Computador {computador}")

                    # verifica se o jogador clicou na Papel
                    elif (pos[0] >=300 and pos[0] <= 400) and (pos[1] >=150 and pos[1]<=250):
                        rouds += 1
                        if (computador == "Tesoura"):
                            derrotas+=1
                            round = "Derrota"
                            vida -= 1
                            if vida <= 0:
                                round = "FIM DE JOGO"
                                end()
                            sleep(1)
                        elif computador=="Papel":
                            round = "Empate"

                        elif computador=="Pedra":
                            vitorias+=1
                            round = "Vitoria"




                        #print("Você clicou no Papel")
                        #print(f"Computador {computador}")

                    # verifica se o jogador clicou na Tesoura

                    elif (pos[0] >=450 and pos[0] <= 550) and (pos[1] >=150 and pos[1]<=250):
                        rouds += 1
                        if (computador == "Tesoura"):
                            round = "Empate"

                            sleep(2)
                        elif computador == "Papel":
                            vitorias+=1
                            round = "Vitoria"

                            sleep(2)
                        elif computador == "Pedra":
                            derrotas += 1
                            round = "Derrota"
                            vida -= 1
                            if vida <= 0:
                                round = "FIM DE JOGO"

                            sleep(0.5)
                        #print("Você clicou Em tesoura")
                        #print(f"Computador {computador}")

                #outras condições de comandos possivels

        if iniciar:
            desenhar()

        if not iniciar:
            stat()
        pygame.display.update()
    print("Fim de jogo! ")
    print(f"Dos 3 rouds disputados voce ganhou {vitorias} e perdeu {derrotas}")


