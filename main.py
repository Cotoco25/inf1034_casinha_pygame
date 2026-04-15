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
velocidade_nuvem2=-3
clock=time.Clock()



matue_img = image.load("matue.png")
matue_img = transform.scale(matue_img, (180,200))

batman_font = font.Font("fontecarai.otf", 40)

mixer.music.load("matue.mp3")
mixer.music.set_volume(0.3)
mixer.music.play(-1)
feijao = mixer.Sound("feijao-com-farinha.mp3")
baby1 = mixer.Sound("baby1.mp3")
baby2 = mixer.Sound("baby2.mp3")
baby3 = mixer.Sound("baby3.mp3")

#programa para fazer o programa fechar com o X do windows
#se for desenhar alguma coisa, desenhar a partir do sys.exit()
modo_fundo = False

uuu=255
iii=188
ooo=99
background_color = (uuu, iii, ooo)

modo_mouse = False

aaa = (uuu-(600//5.75))
bbb = (iii+(600//25))
ccc = (ooo+(600//3.95))


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
                modo_fundo = not modo_fundo
        if ev.type == KEYDOWN:
            key_pressed = ev.key
            if key_pressed == K_x:
                modo_mouse = not modo_mouse


        if ev.type == MOUSEBUTTONDOWN:
            if raio_x >0 and raio_x < 430 and modo_fundo == False:
                if ev.button == 2:
                    baby1.play()

        if ev.type == MOUSEBUTTONDOWN:
            if raio_x >430 and raio_x < 860 and modo_fundo == False:
                if ev.button == 2:
                    baby2.play()

        if ev.type == MOUSEBUTTONDOWN:
            if raio_x >860 and raio_x < 1350 and modo_fundo == False:
            #if background_color == (13, 29, 92):
                if ev.button == 2:
                    baby3.play()

        if ev.type == MOUSEBUTTONDOWN:
            if modo_fundo == True:
                if ev.button == 2:
                    feijao.play()


        if modo_fundo:
            background_color = (245,178,64)
        else:
                if modo_mouse == False:
                    if raio_x < 600:
                        background_color = (uuu-(raio_x)//5.75, iii+(raio_x//25), ooo+(raio_x//3.95))
                    else:
                        if raio_x >= 600:
                            background_color = (aaa-((raio_x-600)//5), bbb-((raio_x-600)//4.3), ccc-((raio_x-600)//4.5))
                else:
                    if modo_mouse == True:
                        if raio_x < 600:
                            background_color = (uuu-(raio_x)//5.75, iii+(raio_x//25), ooo+(raio_x//3.95))
                        else:
                            if raio_x >= 600:
                                background_color = (aaa-((raio_x-600)//5), bbb-((raio_x-600)//4.3), ccc-((raio_x-600)//4.5))

    #if modo_mouse == True:
        #print(mouse_x)
    #print(background_color)


    ##update
    dt = clock.get_time()/1000
    keys = key.get_pressed()

    mouse_x, mouse_y = mouse.get_pos()



    #teclas

    if modo_mouse == True:
        raio_x = (mouse_x)


    #if modo_mouse == False:
    if raio_x<1350:
        if keys[K_d]:
                raio_x = raio_x + 100 *dt
    if raio_x > 10:
        if keys[K_a]:
                raio_x = raio_x - 100 *dt
    if raio_x <1350:
        if ev.type == MOUSEBUTTONDOWN:
            if ev.button == 1:
                raio_x = raio_x + 100 *dt
    if raio_x > -50:
        if ev.type == MOUSEBUTTONDOWN:
            if ev.button == 3:
                raio_x = raio_x - 100 *dt
    
    



    #desenhar a partir daqui

    window.fill(background_color)

    if modo_mouse == False:
        draw.line(window, (255, 242, 81), (raio_x-60,130), (raio_x-120,130), 10)
        draw.line(window, (255, 242, 81), (raio_x+60 ,130), (raio_x+120,130), 10)
        draw.line(window, (255, 242, 81), (raio_x,190), (raio_x,250), 10)
        draw.line(window, (255, 242, 81), (raio_x,70), (raio_x,10), 10)
        draw.circle(window, (255, 242, 81), (raio_x,130), 60)    
    draw.rect(window, (101, 67, 33), (1000, 240, 80, 400))
    draw.circle(window, (0, 128, 0), (1040,300), 100)
    draw.rect(window, (72, 157, 37), (0,600,1280,220))
    draw.rect(window, (100, 100, 100), (350, 360,200,240))
    draw.polygon(window, (242, 136, 59), ((350,360),(550,360),(450,200)))
    draw.rect(window, (13, 22, 100), (370, 460,50,70))
    draw.rect(window, (121, 77, 27), (450, 430,75,170))
    draw.circle(window, (0,0,0), (470,520), 7)

    if modo_mouse == True:
        draw.line(window, (255, 242, 81), (mouse_x-60,mouse_y), (mouse_x-120,mouse_y), 10)
        draw.line(window, (255, 242, 81), (mouse_x+60 ,mouse_y), (mouse_x+120,mouse_y), 10)
        draw.line(window, (255, 242, 81), (mouse_x,mouse_y+60), (mouse_x,mouse_y+120), 10)
        draw.line(window, (255, 242, 81), (mouse_x,mouse_y-60), (mouse_x,mouse_y-120), 10)
        draw.circle(window, (255, 242, 81), (mouse_x,mouse_y), 60)    

    #nuvem
    nuvem_x += velocidade_nuvem
    
    if nuvem_x <= -380 or nuvem_x >= 1350:
        velocidade_nuvem = -velocidade_nuvem

    #if nuvem_x > 1350:
    #    nuvem_x = -350

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