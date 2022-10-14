import random
from turtle import right, window_height

from PPlay.window import *
from PPlay.keyboard import *
from PPlay.sprite import *
from PPlay.gameobject import *
from PPlay.collision import *
from PPlay.gameimage import *

# Window
win_height = 750
win_width = 1000
win = Window(win_width, win_height)
title = win.set_title("SpaceInvaders")
bgImg = GameImage("background.png")

# Nave
nave = Sprite("spaceship.png")
nave.x = (win_width/2) - (nave.width/2)
nave.y = win_height - nave.height
velx = 300

# Tiro
tiro = Sprite("tiro.png")
tiro.x = nave.x
tiro.y = -100
vely = -300

# Game Window
gwin_height = 750
gwin_width = 1000
gwin = Window(win_width, win_height)
gtitle = gwin.set_title("SpaceInvaders")
gbImg = GameImage("background.png")

# MenuAssets
jogar = GameImage("jogar.png")
jogar.x = (win_width/2) - (jogar.width/2)
jogar.y = (win_height/2) - (jogar.height/2) - 200

dificuldade = GameImage("dificuldade.png")
dificuldade.x = (win_width/2) - (dificuldade.width/2)
dificuldade.y = (win_height/2) - (dificuldade.height/2) - 50

facil = GameImage("facil.png")
facil.x = (win_width/2) - (facil.width/2)
facil.y = (win_height/2) - (facil.height/2) - 150

medio = GameImage("medio.png")
medio.x = (win_width/2) - (medio.width/2)
medio.y = (win_height/2) - (medio.height/2)

dificil = GameImage("dificil.png")
dificil.x = (win_width/2) - (dificil.width/2)
dificil.y = (win_height/2) - (dificil.height/2) + 150

rank = GameImage("rank.png")
rank.x = (win_width/2) - (rank.width/2)
rank.y = (win_height/2) - (rank.height/2) + 100

sair = GameImage("sair.png")
sair.x = (win_width/2) - (sair.width/2)
sair.y = (win_height/2) - (sair.height/2) + 250

# Mouse & Keyboard
mouse = Window.get_mouse()
keyboard = Window.get_keyboard()

# Menu
def main_menu():
    while True:
        if (mouse.is_over_object(sair) and mouse.is_button_pressed(1)):
            pygame.quit()
            exit()
        if (mouse.is_over_object(dificuldade) and mouse.is_button_pressed(1)):
            level_menu()
        if (mouse.is_over_object(jogar) and mouse.is_button_pressed(1)):
            game_loop(velx, vely)

        bgImg.draw()
        jogar.draw()
        rank.draw()
        dificuldade.draw()
        sair.draw()
        win.update()

# Dificuldade
dificuldadeJogo = 1
def level_menu():
    while True:

        # Selecionar Dificuldadde
        if (mouse.is_over_object(facil) and mouse.is_button_pressed(1)):
            main_menu()
        if (mouse.is_over_object(medio) and mouse.is_button_pressed(1)):
            dificuldadeJogo = 2
            main_menu()
        if (mouse.is_over_object(dificil) and mouse.is_button_pressed(1)):
            dificuldadeJogo = 3
            main_menu()
        bgImg.draw()
        facil.draw()
        medio.draw()
        dificil.draw()
        win.update()

# Game
def game_loop(velx, vely):
    while True:
        if(keyboard.key_pressed("esc") == True):
            exit()

        # Nave mexendo de um lado para o outro
        if (nave.x > win_width - nave.width):
            velx *= -1
            if (velx > 0):
                velx *= -1
        if (nave.x < 0):
            velx *= -1
            if (velx < 0):
                velx *= -1
        # Tiro
        if(keyboard.key_pressed("SPACE") and tiro.y <= 0):
            tiro.y = nave.y - nave.height
            tiro.x = nave.x
        if(tiro.y < 0):
            tiro.y = -100

        tiro.y += vely * win.delta_time()


        nave.x += velx * win.delta_time()
        gbImg.draw()
        nave.draw()
        tiro.draw()
        gwin.update()


main_menu()