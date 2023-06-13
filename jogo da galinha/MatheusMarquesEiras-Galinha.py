import pygame
from pygame import *
import os
from pathlib import Path

class carro:
    def __init__(self,posicao_x,posicao_y,velocidade):
        self.posicao_x = posicao_x
        self.posicao_y = posicao_y
        self.velocidade = velocidade

    def desenha_carro_direita_esquerda(self):
        pygame.draw.rect(janela,(255,0,0),(self.posicao_x,self.posicao_y,40,10))

        pygame.draw.rect(janela,(255,0,0),(self.posicao_x + 15,self.posicao_y - 10,20,10))

        pygame.draw.circle(janela,(250,250,250),(self.posicao_x + 4,self.posicao_y + 15),4)

        pygame.draw.circle(janela,(250,250,250),(self.posicao_x + 36,self.posicao_y + 15),4)

    def velocidade_carro_direita_esquerda(self):
        self.posicao_x -= self.velocidade

        if self.posicao_x < -60:
            self.posicao_x = 825
    
    def desenha_carro_esquerda_direita(self):
        pygame.draw.rect(janela,(255,0,0),(self.posicao_x,self.posicao_y,40,10))

        pygame.draw.rect(janela,(255,0,0),(self.posicao_x + 5,self.posicao_y - 10,20,10))

        pygame.draw.circle(janela,(250,250,250),(self.posicao_x + 4,self.posicao_y + 15),4)

        pygame.draw.circle(janela,(250,250,250),(self.posicao_x + 36,self.posicao_y + 15),4)
    
    def velocidade_carro_esquerda_direita(self):
        self.posicao_x += self.velocidade

        if self.posicao_x > 800:
            self.posicao_x = -60

class usuario:
    def __init__(self,posicao_inicial_x,posicao_inicial_y,velocidade):
        self.galinha = pygame.image.load(caminho_arquivo("galinha.png"))
        self.rect = pygame.Rect(posicao_inicial_x, posicao_inicial_y, self.galinha.get_width(), self.galinha.get_height())
        self.rect.topleft = posicao_inicial_x,posicao_inicial_y
        self.velocidade = velocidade

    def move(self):
        global galinhaEsquerda
        global galinhaDireita

        global imagemAtual
        
        if pygame.key.get_pressed()[K_a]:
            self.rect.x -= self.velocidade
            if self.rect.x < 0:
                self.rect.x += self.velocidade

            if imagemAtual > 3:
                imagemAtual = 0
            self.galinha = pygame.image.load(caminho_arquivo(galinhaEsquerda[int(imagemAtual)]))
            imagemAtual += 0.15
        if pygame.key.get_pressed()[K_d]:
            self.rect.x += self.velocidade
            if self.rect.x >= 768:
                self.rect.x -= self.velocidade

            if imagemAtual > 3:
                imagemAtual = 0
            
            self.galinha = pygame.image.load(caminho_arquivo(galinhaDireita[int(imagemAtual)]))
            imagemAtual += 0.15
        if pygame.key.get_pressed()[K_s]:
            self.rect.y += self.velocidade
            if self.rect.y >= 568:
                self.rect.y -= self.velocidade

            if imagemAtual > 3:
                imagemAtual = 0
            self.galinha = pygame.image.load(caminho_arquivo(galinhaEsquerda[int(imagemAtual)]))
            imagemAtual += 0.15
        if pygame.key.get_pressed()[K_w]:
            self.rect.y -= self.velocidade
            if self.rect.y < 20:
                self.rect.y += self.velocidade

            if imagemAtual > 3:
                imagemAtual = 0
            
            self.galinha = pygame.image.load(caminho_arquivo(galinhaEsquerda[int(imagemAtual)]))
            imagemAtual += 0.15

    def volta_comeco(self):
        self.rect.x = 382
        self.rect.y = 565
    
    def colisao(self, carro):
        jogador_rect = self.rect
        carro_rect = pygame.Rect(carro.posicao_x, carro.posicao_y, 40, 10)
        return jogador_rect.colliderect(carro_rect)

class botao():
    def __init__(self,texto,x,y,largura,altura,funcao):
        # Atributos padrões para verificações por motivos de performace
        self.clicou = False

        # Especifica o retangulo que sera desenhado
        self.retanguloConteiner = pygame.Rect(x,y,largura,altura)
        self.corBotao = (100,100,100)

        # escreve o texto na superficie
        self.texto = fonte_texto.render(texto,True,(255,255,255))
        # Obtem o tamanho do texto e o guarda dentro do retangulo que ira conter-lo
        self.retanguloTamnhoTexto = self.texto.get_rect(center=(self.retanguloConteiner.centerx, self.retanguloConteiner.centery))

        self.funcao = funcao

    def desenha_botao(self):
        # Desenha o retangulo especificado
        pygame,draw.rect(janela,self.corBotao,self.retanguloConteiner,border_radius=10)
        # Coloca o retangulo na tela
        janela.blit(self.texto,self.retanguloTamnhoTexto)

    def click(self):

        # Obtem a posição do maouse
        mouse = pygame.mouse.get_pos()

        # Verifica se o mouse esta dentro do botão
        if self.retanguloConteiner.collidepoint(mouse):
            
            # Muda a cor do botão quando o mouse esta dentro dele
            self.corBotao = (55,55,55)

            # Verifica se foi clicado com o botao direito
            if pygame.mouse.get_pressed()[0]:
                # Significa que ele clicou e somente uma booleana ira ser atribuida a essa variavel
                self.clicou = True
                
            # Quando a condição acima deixar de ser verdadeira ou seja o player deixou de pressionar o botao então a booleana volta a ser falsa por padrao e se executa a ação
            else:
                # Isso é feito dessa forma por conta de que aou se colocar uma grande quantidade de frames na execução do jogo essa ação seria executada varias vezes o que pode comprometer a performace do jogo em determinados dispositivos
                if self.clicou == True:
                    self.clicou = False
                    self.funcao()
        else:
            self.corBotao = (100,100,100)

def escreve_texto(texto,fonte,corTexto,posicaoX,posicaoY):
    textoEscrito = fonte.render(texto,True,corTexto)
    janela.blit(textoEscrito,(posicaoX,posicaoY))

def desenha_faixas():

    valorXPrimeiro = 725
    valorXSegundo = 775

    valorY = 141

    for i in range(2):
        for j in range(2):
            for z in range(8):
                pygame.draw.line(janela,(255,255,255),(valorXPrimeiro,valorY),(valorXSegundo,valorY),2)

                valorXPrimeiro -= 100
                valorXSegundo -= 100

            valorXPrimeiro = 725
            valorXSegundo = 775

            valorY += 66
        
        valorY += 118

def floresta():

    valorX = -5
    valorY = -15

    for i in range(2):
        for j in range(41):
            janela.blit(arvore, (valorX,valorY))

            valorX +=20
        valorX = -15
        valorY += 15

def desenha_chao():

    # calçada de cima
    pygame.draw.rect(janela,(124,252,0),(0,0,800,75))

    # calçada do meio
    pygame.draw.rect(janela,(124,252,0),(0,275,800,50))

    #calçada de baixo
    pygame.draw.rect(janela,(124,252,0),(0,525,800,75))


def joguinho():
    global jogo
    jogo = True

def infomacaozinha():
    global informacao
    informacao = True

def sairzinho():
    global Jogar
    Jogar = False

def retorna_padrao():
    global carro_um 
    global carro_dois
    global carro_tres
    global carro_quatro
    global carro_cinco
    global carro_seis
    global carro_sete
    global jogador

    carro_um = carro(625, 108, 5)
    carro_dois = carro(900,108,5)

    carro_tres = carro(500,174,8)
    carro_quatro = carro(800,240,7)


    carro_cinco = carro(0,358,6)
    carro_seis = carro(-100,424,9)
    carro_sete = carro(-170,490,14)

    jogador = usuario(382,565,3)

def desenha_jogo():
    janela.fill((0,0,0))

    desenha_chao()

    desenha_faixas()

    carro_um.desenha_carro_direita_esquerda()
    carro_um.velocidade_carro_direita_esquerda()

    carro_dois.desenha_carro_direita_esquerda()
    carro_dois.velocidade_carro_direita_esquerda()

    carro_tres.desenha_carro_direita_esquerda()
    carro_tres.velocidade_carro_direita_esquerda()

    carro_quatro.desenha_carro_direita_esquerda()
    carro_quatro.velocidade_carro_direita_esquerda()

    carro_cinco.desenha_carro_esquerda_direita()
    carro_cinco.velocidade_carro_esquerda_direita()

    carro_seis.desenha_carro_esquerda_direita()
    carro_seis.velocidade_carro_esquerda_direita()

    carro_sete.desenha_carro_esquerda_direita()
    carro_sete.velocidade_carro_esquerda_direita()

    janela.blit(ninho,(372,33))
                    
    floresta()

    janela.blit(jogador.galinha, jogador.rect)

def voltar_menu_inicial():
    global ganhou
    global continuar

    ganhou = False
    continuar = True
    retorna_padrao()

def escreve_texto_envelopado(superficie, texto, fonteTexto, corTexto, retanguloTexto, margem, corRetanguloConteiner, aa=False):
    y = retanguloTexto.top

    # altura da fonte fornecida com base em uma string de exemplo
    fontHeight = fonteTexto.size("Tg")[1]

    pygame.draw.rect(janela,corRetanguloConteiner,retanguloTexto)

    # enquanto tiver texto a ser processado
    while texto:
        i = 1
        
        # Acha o tamanho maximo que o retangulo conporta na sua largura a propria interação nao for maior que o texto analizada
        while fonteTexto.size(texto[:i])[0] < (retanguloTexto.width - (margem * 2)) and i < len(texto):
            i += 1

        # Se o texto ja foi envelopado ele procura pela ultima aparição do " " ente as palavras e começa aleitura de là
        if i < len(texto):
            i = texto.rfind(" ", 0, i) + 1

        # Renderiza o pequeno pedaço do texto
        textoRenderizado = fonteTexto.render(texto[:i], aa, corTexto)

        superficie.blit(textoRenderizado, (retanguloTexto.left + margem, y + margem))
        # Move o texto para a linha de baixo
        y += fontHeight + 2

        # Remove o texto do string original
        texto = texto[i:]

def caminho_arquivo(nome:str):
    caminho = os.path.dirname(os.path.realpath(__file__))
    caminhoAbsoluto = os.path.join(caminho, "imagens/", nome)
    return caminhoAbsoluto

if __name__ == "__main__":

    retanguloFinal = None

    pygame.init()
    pygame.font.init()

    fonte_titulo = pygame.font.SysFont("arialblack", 30)
    fonte_texto = pygame.font.SysFont("arialblack",20)

    textoInfo = """Este programa foi feito usando por Matheus Marques Eiras estudante de bachalelado em Ciência da computação no Instituto Federal do Paraná campus Pinhais (IFPR - Pinhais)"""

    janela = pygame.display.set_mode((800,600))

    pygame.display.set_caption("Jogo da Galinha")

    relogio = pygame.time.Clock()

    carro_um = carro(625, 108, 5)
    carro_dois = carro(900,108,5)

    carro_tres = carro(500,174,8)
    carro_quatro = carro(800,240,7)


    carro_cinco = carro(0,358,6)
    carro_seis = carro(-100,424,9)
    carro_sete = carro(-170,490,14)

    jogador = usuario(382,565,3)

    imagemAtual = 0

    arvore = pygame.image.load(caminho_arquivo("arvore.png"))

    ninho = pygame.image.load(caminho_arquivo("ninho.png"))

    imagemWASD = pygame.image.load(caminho_arquivo("wasd.png"))

    imagemP = pygame.image.load(caminho_arquivo("p.png"))

    venceu = pygame.image.load(caminho_arquivo("galinha_final.jpg"))
    imagemFundoVenceu = pygame.transform.scale(venceu, (800, 600))

    Jogar = True

    ganhou = False

    jogo = False

    informacao = False

    continuar = True

    tempoGanhou = 0

    Jogar = botao("jogar",250,150,300,50,joguinho)
    informaçoes = botao("Informações e comandos",250,250,300,50,infomacaozinha)
    sairMenuInicial = botao("Sair",250,350,300,50,sairzinho)

    jogarNovamente = botao("Jogar novamente?",100,350,250,50,voltar_menu_inicial)
    sairMenuFinal = botao("Sair",450,350,250,50,sairzinho)

    galinhaEsquerda = ["galinha_esquerda_parada.png","galinha_esquerda_andando.png","galinha_esquerda_parada2.png","galinha_esquerda_andando2.png"]
    galinhaDireita = ["galinha_direita_parada.png","galinha_direita_andando.png","galinha_direita_parada2.png","galinha_direita_andando2.png"]

    retanguloConteinerInformacao = pygame.Rect(50,400,700,150)

    while Jogar:
        relogio.tick(100)

        janela.fill((0,0,0))

        for event in pygame.event.get():
            if event.type == QUIT:
                Jogar = False
            if event.type == pygame.KEYDOWN:
                if pygame.key.get_pressed()[K_p]:
                    jogo = False
                    informacao = False
                    retorna_padrao()
        
        if jogo:
            if ganhou:
                tempoAtual = pygame.time.get_ticks()

                tempoAtual = tempoAtual - tempoGanhou 
                desenha_jogo()

                if tempoAtual > 500:
                    janela.fill((0,0,0))

                    janela.blit(imagemFundoVenceu,(0,0))
                    escreve_texto("Parabens você chegou ao outro lado",fonte_titulo,(255,255,255),100,250)
                    escreve_texto("Jogar novamente?",fonte_texto,(255,255,255),325,300)

                    jogarNovamente.desenha_botao()
                    jogarNovamente.click()

                    sairMenuFinal.desenha_botao()
                    sairMenuFinal.click()

            else:
                desenha_jogo()

                if continuar:
                    jogador.move()
                
                # pygame.draw.rect(janela,(255,0,0),(0,0,800,40))
                retanguloFinal = Rect(0,0,800,50)

                if jogador.rect.colliderect(retanguloFinal):
                    continuar = False
                    valorX = jogador.rect.x - 382
                    valorY = jogador.rect.y -35

                    if valorX > 0:
                        jogador.rect.x -= 1
                        if imagemAtual > 3:
                            imagemAtual = 0

                        jogador.galinha = pygame.image.load(caminho_arquivo(galinhaEsquerda[int(imagemAtual)]))

                        imagemAtual += 0.15

                    elif valorX < 0:
                        jogador.rect.x += 1
                        if imagemAtual > 3:
                            imagemAtual = 0

                        jogador.galinha = pygame.image.load(caminho_arquivo(galinhaDireita[int(imagemAtual)]))

                        imagemAtual += 0.15
                    
                    if valorY > 0:
                        jogador.rect.y -= 1
                        if imagemAtual > 3:
                            imagemAtual = 0

                        jogador.galinha = pygame.image.load(caminho_arquivo(galinhaEsquerda[int(imagemAtual)]))

                        imagemAtual += 0.15
                    
                    if valorX == 0 and valorY == 0:
                        jogador.galinha = pygame.image.load(caminho_arquivo("galinha.png"))
                        ganhou = True
                        tempoGanhou = pygame.time.get_ticks()

                if jogador.colisao(carro_um) or jogador.colisao(carro_dois) or jogador.colisao(carro_tres) or jogador.colisao(carro_quatro) or jogador.colisao(carro_cinco) or jogador.colisao(carro_seis) or jogador.colisao(carro_sete):
                    jogador.galinha = pygame.image.load(caminho_arquivo("galinha.png"))
                    jogador.volta_comeco()

        elif informacao:
            titulo = escreve_texto("Informaçoes e comandos",fonte_titulo,(255,255,255),300,25)
            
            janela.blit(imagemWASD,(50,90))

            escreve_texto("Use W A S D para se mover",fonte_texto,(255,255,255),300,175)

            # pygame.draw.rect(janela,(255,0,0),(50,400,700,150))

            janela.blit(imagemP,(65,225))

            escreve_texto("Presione P para voltar ao menu prinpal",fonte_texto,(255,255,255),300,285)

            escreve_texto_envelopado(janela, textoInfo, fonte_texto, (0,0,0), retanguloConteinerInformacao, 25, (100,100,100), True)

        else:
            escreve_texto("Por que a galinha atravessou a rua?",fonte_titulo,(255,255,255),110,50)

            Jogar.desenha_botao()
            Jogar.click()

            informaçoes.desenha_botao()
            informaçoes.click()

            sairMenuInicial.desenha_botao()
            sairMenuInicial.click()

        pygame.display.flip()