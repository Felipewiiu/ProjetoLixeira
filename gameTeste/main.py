import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()               #Isto inicializa todas funções da biblioteca

pygame.mixer.music.set_volume(0.1)
musica_de_fundo = pygame.mixer.music.load('fundo.mp3')
pygame.mixer.music.play(-1)

som_acertou = pygame.mixer.Sound('acertou.wav')
som_errou = pygame.mixer.Sound('errou.wav')


largura = 800
altura = 600

x = 400                                       #largura/x divide a tela
y = 550

preto = (0,0,0)

x_vermelho = randint(40, 750)
y_vermelho = randint(50, 560)

pontos = 0
fonte = pygame.font.SysFont('arial', 40,True, True)

tela = pygame.display.set_mode((largura, altura))   #tamanho da tela
pygame.display.set_caption('Jogo Teste')            #troca o nome da tela do jogo

relogio = pygame.time.Clock()                       #constância para taxa de fps

class Garrafa(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('garrafa.jpg'))
        self.image = self.sprites[0]

while True:             #criando loop
    relogio.tick(60)                                #taxa de fps
    tela.fill(preto)                              #faz a tela resetar e ficar preta de novo

    mensagem = f'Pontos: {pontos}'
    texto_formatado = fonte.render(mensagem, True, (255, 255, 255))
    for event in pygame.event.get():                #detecta se algum evento ocorreu durante o jogo
        if event.type == QUIT:                      #fechar janela do jogo
            pygame.quit()
            exit()
        '''
        if event.type == KEYDOWN:                   #Este event faz o objeto se mexer, porém, não é contínuo         
            if event.key == K_LEFT:
                x = x - 20
            if event.key == K_RIGHT:
                x = x + 20
            if event.key == K_UP:
                y = y - 20
            if event.key == K_DOWN:
                y = y + 20'''

    if pygame.key.get_pressed()[K_LEFT]:                        #este faz o objeto se mover contínuamente
        x = x - 8
    if pygame.key.get_pressed()[K_RIGHT]:
        x = x + 8
    if pygame.key.get_pressed()[K_UP]:
        y = y - 8
    if pygame.key.get_pressed()[K_DOWN]:
        y = y + 8

    ret_vermelho = pygame.draw.rect(tela, (255,0,0), (x , y,50,50))
    ret_amarelo = pygame.draw.rect(tela, (255, 200, 0), (100, 5, 40, 50))
    ret_azul = pygame.draw.rect(tela, (0, 0, 255), (300, 5, 40, 50))
    ret_verde = pygame.draw.rect(tela, (0, 255, 0), (500, 5, 40, 50))

    if ret_amarelo.colliderect(ret_vermelho):
        x = (400)
        y = (550)

        print('Você errou a lixeira!')
        pontos = pontos - 5
        som_errou.play()

    if ret_azul.colliderect(ret_vermelho):
        x = (400)
        y = (550)

        print('Você errou a lixeira!')
        pontos = pontos - 5
        som_errou.play()

    if ret_verde.colliderect(ret_vermelho):
        x = (400)
        y = (550)

        print('Você acertou a lixeira! Parabéns!')
        pontos = pontos + 10
        som_acertou.play()

    tela.blit(texto_formatado, (550, 60))






    #if y >= altura:
    #    y = 0                      #Faz o retângulo se mover sozinho de cima para baixo
    #y = y + 10


    #pygame.draw.circle(tela, (0,150,100), (300,300,), 50)           #cirlulo (tela, (cor), (x,y), raio)
    #pygame.draw.line(tela, (100,100,100), (370,600), (370,0), 10)
    pygame.display.flip()                         #atualiza a tela de jogo