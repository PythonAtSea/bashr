import pygame

pygame.init()
width = 1280
height = 400
screen = pygame.display.set_mode((width, height), flags=pygame.RESIZABLE)
clock = pygame.time.Clock()
running = True
imgs = [
    pygame.transform.scale_by(pygame.image.load("images/sand.png"), 4),
]
offset = [0, 0]
cursor = pygame.cursors.Cursor(
    (0, 0), pygame.transform.scale_by(pygame.image.load("images/cursormain.png"), 2)
)
TILE_SIZE = 64
pygame.mouse.set_cursor(cursor)
map = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("purple")
    for i in range(len(map)):
        for j in range(len(map[0])):
            x = i * TILE_SIZE + offset[0]
            y = j * TILE_SIZE + offset[1]
            if x > -TILE_SIZE and y > -TILE_SIZE and x < width and y < height:
                screen.blit(imgs[map[i][j]], (x, y))
    pygame.display.flip()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        offset[1] += 5
    if keys[pygame.K_s]:
        offset[1] -= 5
    if keys[pygame.K_a]:
        offset[0] += 5
    if keys[pygame.K_d]:
        offset[0] -= 5
    width, height = pygame.display.get_surface().get_size()
    clock.tick(60)

pygame.quit()
