from pygame import *
import sys

init()

window = display.set_mode((1280,720))

#fazer o fundo - RGB
window.fill((151, 209, 250))

batman_img = image.load("batman.png")
batman_img = transform.scale(batman_img, (180,200))

batman_font = font.Font("fontecarai.otf", 40)

#mixer.music.load("nome do arquivo.mp3")
#mixer.music.play()

#programa para fazer o programa fechar com o X do windows
#se for desenhar alguma coisa, desenhar a partir do sys.exit()
while True:
    for ev in event.get():
        if ev.type == QUIT:
            quit()
            sys.exit()
#desenhar a partir daqui
    draw.rect(window, (72, 157, 37), (0,600,1280,220))
    draw.rect(window, (100, 100, 100), (350, 360,200,240))
    draw.circle(window, (255, 242, 81), (140,130), 60)
    draw.polygon(window, (242, 136, 59), ((350,360),(550,360),(450,200)))
    draw.rect(window, (13, 22, 100), (370, 460,50,70))
    draw.rect(window, (121, 77, 27), (450, 430,75,170))
    draw.circle(window, (0,0,0), (470,520), 7)
    draw.line(window, (255, 0 ,255), (80,130), (20,130), 10)

    #desenhar imagem
    window.blit(batman_img, (600,450))

    #desenhar texto
    batman_text = batman_font.render("Sou batman", True, (0,0,0))
    window.blit(batman_text, (570,400))

    display.update()