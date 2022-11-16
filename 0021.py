import pygame
#Inicializando o mixer PyGame
pygame.mixer.init()
#Iniciando o Pygame
pygame.init()
#Apontando o diretorio
pygame.mixer.music.load('grilo.mp3')
pygame.mixer.music.play()
#encerrar quando acabar de tocar
pygame.event.wait()
