import sys
from random import randint

import pygame
import random


class Mich:
    def __init__(self, name_image, x, y, width, height):  # конструктор.Создание свойств
        self.image = pygame.image.load(name_image)  # создание картинки
        self.image = pygame.transform.scale(self.image, (width, height)) #изменение размеров картинки под заданные
        self.rect=self.image.get_rect()# создание прям по границам картинки
        self.rect.x = x
        self.rect.y = y




    def draw_image(self):  # МЕТОД!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        screen.blit(self.image, (self.rect.x, self.rect.y))  # это отрисовка картинок на координатах x и y

    def move_mich(self):  # ПОСТОЯННОЕ ДВИЖЕНИЕ ВНИЗ
        self.rect.y -= 4
        if self.rect.y < 0:
            self.rect.y = 720
    def move_vorota(self,s):  # метод!!!!!!!!!!!!!!!!!!!!
        keys = pygame.key.get_pressed()
        if  self.rect.x >1280:
            self.rect.x= 0
        elif self.rect.x<-64:
            self.rect.x=1280
        if keys[pygame.K_LEFT]:
            self.rect.x -= s
        elif keys[pygame.K_RIGHT]:
            self.rect.x += s

pygame.init()  # обязательная каманда people
window_size = (1280, 720)
speed=8
egrok=0
protivnik=0
font = pygame.font.SysFont("Times New Roman",50)
screen = pygame.display.set_mode(window_size)  # создание экрана(окна) с размера 300x300
pygame.display.set_caption("БАСУХА В ДЕЛЕ РОДНЫЕ")  # название окна
backgound_color = (255, 255, 255)  # цвет
clock = pygame.time.Clock()  # создание игровово таймера
q=1280/5
vorota = Mich('ворота месси.png', 490, 0, 330, 98)
fon = Mich("футбольное поле месси.jpg", 0, 0, 1280, 720)
mich1 = Mich("мяч.png", random.randint(0,6)*q,  random.randint(720,2000), 128, 128)
mich2 = Mich("мяч.png", random.randint(0,6)*q, random.randint(720,2000),128 ,128)
mich3 = Mich("мяч.png", random.randint(0,6)*q, random.randint(720,2000), 128, 128)
mich4 = Mich("мяч.png", random.randint(0,6)*q, random.randint(720,2000), 128, 128)
mich5 = Mich("мяч.png",random.randint(0,6)*q , random.randint(720,2000), 128, 128)
mich6 = Mich("мяч.png", random.randint(0,6)*q,  random.randint(720,2000), 128, 128)
mich7 = Mich("мяч.png", random.randint(0,6)*q, random.randint(720,2000),128 ,128)
mich8 = Mich("мяч.png", random.randint(0,6)*q,  random.randint(720,2000), 128, 128)
mich_list = [mich1, mich2, mich3, mich4, mich5,mich6,mich7,mich8]
while True:  # игрововй таймер
    clock.tick(40)  # частота обновления таймераааааа
    fon.draw_image()
    text = font.render("СЧЁТ "+str(egrok)+":"+str(protivnik), True, (0, 0, 255))

    screen.blit(text,(50,50))

    if egrok>=25:
        fon = Mich("криштиану роналду.jpeg", 0, 0, 1280, 720)
    elif protivnik>=25:
        fon = Mich("месси фото.jpg", 0, 0, 1280, 720)
    if egrok>=25 and protivnik>=25:
        fon = Mich("друзья навсегда.jpg", 0, 0, 1280, 720)
    for i in mich_list:
        i.draw_image()
        i.move_mich()
        if vorota.rect.colliderect(i.rect) == True:
            i.rect.y=720
            egrok+=1
        if i.rect.y <= 0:
            protivnik +=1
    vorota.draw_image()
    vorota.move_vorota(speed)


    for event in pygame.event.get():  # проходимся по событиям
        if event.type == pygame.QUIT:  # если нажали на крестик
            sys.exit()  # выйти из ГОЙДА

    pygame.display.update()  # ОБНОВЛЕНИЕ ДИСПЛЕЯ
