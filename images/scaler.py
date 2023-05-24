import pygame

pygame.init()
pygame.image.save(pygame.transform.scale_by(pygame.image.load(input("Name of input file: ")), int(input("Scale factor"))), input("Name of output file: "))
