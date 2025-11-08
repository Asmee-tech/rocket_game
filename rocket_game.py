import pygame
import time
from pygame.locals import*
pygame.init()
screen=pygame.display.set_mode((500,500))
x=40
y=100
keys=[False,False,False,False]
rocimg=pygame.image.load("rocket.png")
bg=pygame.image.load("galaxy.jpg")





run=True
while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        if event.type==KEYDOWN:
            if event.key==K_UP:
                keys[0]=True
            elif event.key==K_DOWN:
                keys[2]=True 
            elif event.key==K_LEFT:
                keys[1]=True
            elif event.key==K_RIGHT:
                keys[3]=True
        if event.type==KEYUP:
            if event.key==K_UP:
                keys[0]=False
            elif event.key==K_DOWN:
                keys[2]=False 
            elif event.key==K_LEFT:
                keys[1]=False
            elif event.key==K_RIGHT:
                keys[3]=False
    if keys[0]:
        if y>0:
            y-=5
    elif keys[2]:
        if y<500:
            y+=5
            
        
            
    screen.blit(bg,(0,0))
    screen.blit(rocimg,(x,y))
    y+=3
    time.sleep(0.02)
    pygame.display.update()
    

pygame.quit()