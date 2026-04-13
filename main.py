from pygame import *
import sys

init()

window = display.set_mode((1280,720))

#fazer o fundo - RGB



raio_x = 140
timer = 0
nuvem_x=800
nuvem_y=100
velocidade_nuvem=3
running = True
velocidade_nuvem2=-4
clock=time.Clock()


matue_img = image.load("matue.png")
matue_img = transform.scale(matue_img, (180,200))

batman_font = font.Font("fontecarai.otf", 40)

mixer.music.load("matue.mp3")
mixer.music.play(-1)

#programa para fazer o programa fechar com o X do windows
#se for desenhar alguma coisa, desenhar a partir do sys.exit()

background_color = (150,150,150)
while running:
    clock.tick(60)
    key_pressed = key.get_pressed()

    for ev in event.get():
        if ev.type == QUIT:
            quit()
            running = False
            sys.exit()
        if ev.type == KEYDOWN:
            key_pressed = ev.key
            if key_pressed == K_SPACE:
                background_color = (245,178,64)
    
    
    # if raio_x<400:
    #     background_color = (151, 209, 250)


    # if raio_x>800:
    #     background_color = (0, 209, 250)
    
    
    ##update
    dt = clock.get_time()/1000
    keys = key.get_pressed()


    #teclas
    if keys[K_d]:
        raio_x = raio_x + 100 *dt

    if keys[K_a]:
        raio_x = raio_x - 100 *dt

    #desenhar a partir daqui

    window.fill(background_color)

    draw.rect(window, (72, 157, 37), (0,600,1280,220))
    draw.rect(window, (100, 100, 100), (350, 360,200,240))
    draw.circle(window, (255, 242, 81), (raio_x,130), 60)
    draw.polygon(window, (242, 136, 59), ((350,360),(550,360),(450,200)))
    draw.rect(window, (13, 22, 100), (370, 460,50,70))
    draw.rect(window, (121, 77, 27), (450, 430,75,170))
    draw.circle(window, (0,0,0), (470,520), 7)
    draw.line(window, (255, 242, 81), (raio_x - 60,130), (raio_x - 120,130), 10)
    draw.line(window, (255, 242, 81), (raio_x +60 ,130), (raio_x + 120,130), 10)
    draw.line(window, (255, 242, 81), (raio_x,190), (raio_x,250), 10)
    draw.line(window, (255, 242, 81), (raio_x,70), (raio_x,10), 10)
    draw.rect(window, (101, 67, 33), (1000, 240, 80, 400))
    draw.circle(window, (0, 128, 0), (1040,300), 100)


    #nuvem
    nuvem_x += velocidade_nuvem

    if nuvem_x > 1350:
        nuvem_x = -350

    #while not (nuvem_x == 1300):
    #    nuvem_x += velocidade_nuvem2

    # while True:
    #     nuvem_x += velocidade_nuvem
    #     if nuvem_x > 1000:
    #         break

    draw.circle(window, (255,255,255), (nuvem_x,nuvem_y),(70))
    draw.circle(window, (255,255,255), (nuvem_x+100,nuvem_y),(70))
    draw.circle(window, (255,255,255), (nuvem_x+200,nuvem_y),(70))
    draw.circle(window, (255,255,255), (nuvem_x+300,nuvem_y),(70))


    #desenhar imagem
    window.blit(matue_img, (600,450))

    #desenhar texto
    batman_text = batman_font.render("As vezes eu fumo um baseado", True, (0,0,0))
    window.blit(batman_text, (570,400))

    display.update()