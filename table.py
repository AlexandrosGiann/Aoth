import pygame
import ctypes
ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
pygame.init()

wn = pygame.display.set_mode((815, 500))

pygame.display.set_caption("table")

The_icon = pygame.image.load("8kxAuY-H-uM1Y6z7CY6ojIPFsBRAGFDUbpBdJhqHEr6Fr6DU.png")

pygame.display.set_icon(The_icon)

Table = []

data_font = pygame.font.Font("freesansbold.ttf", 32)


def draw_columns(List, x, y):
    counter = 5
    l1 = []

    for i in range(len(List)):
        pygame.draw.rect(wn, (0, 0, 0), (x + counter - 5, y, 100, 50))
        pygame.draw.rect(wn, (255, 255, 255), (x + counter, y + 5, 90, 40))
        data = str(List[i])
        l = [x + counter, y + 5, x + counter + 90, y + 5 + 40]
        l1.append(l)
        l = []
        txt_surface = data_font.render(data, True, (0, 0, 0))
        wn.blit(txt_surface, (x + counter + 5, y + 5 + 5))
        counter += 100


run = True

sy = 1

ty = 0

must_scroll = False

o_posY = 0

while run:
    pygame.time.delay(10)

    mouse = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and (800 <= mouse[0] <= 815 and sy <= mouse[1] <= sy + 100):
            o_posY = mouse[1] - sy
            must_scroll = True
        if event.type == pygame.MOUSEBUTTONUP:
            must_scroll = False

    if must_scroll and (mouse[1] < 400 or (0 <= sy < 400)):
        if mouse[1] - o_posY > 0:
            sy = mouse[1] - o_posY
        else:
            sy = 1

    ty = -sy
    
    wn.fill((0, 0, 40))
    for i in range(len(Table)):
        draw_columns(Table[i], 0, ty + (i * 50))

    pygame.draw.rect(wn, (150, 150, 150), (800, sy, 15, 100))

    pygame.display.update()
pygame.quit()
