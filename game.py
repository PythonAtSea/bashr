import pygame

pygame.init()
width = 1280
height = 400
screen = pygame.display.set_mode((width, height), flags=pygame.RESIZABLE)
clock = pygame.time.Clock()
running = True
imgs = [
    pygame.image.load("images/gflat.png"),
]
offset = [0, 0]
TILE_SIZE = 64
pygame.mouse.set_cursor(
    pygame.cursors.Cursor(
        (0, 0), pygame.transform.scale_by(pygame.image.load("images/cursormain.png"), 2)
    )
)
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
DEBUG = True

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dy = 0

    def draw(self):
        if DEBUG:
            pygame.draw.circle(
                screen,
                (255, 0, 0),
                (self.x - offset[0] + width / 2, self.y - offset[1] + height / 2),
                50,
            )
            pygame.draw.rect(screen, "yellow", (width / 2 - 36, height / 2 - 48, 72, 96))

    def move(self):
        if keys[pygame.K_SPACE]:
            self.dy = 12
        if keys[pygame.K_s]:
            self.y -= 4
        if keys[pygame.K_a]:
            self.x += 4
        if keys[pygame.K_d]:
            self.x -= 4
        self.dy -= 0.4
        self.y += self.dy


player = Player(0, 0)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    screen.fill("purple")
    for i in range(len(map)):
        for j in range(len(map[0])):
            x = i * TILE_SIZE + offset[0] + width / 2
            y = j * TILE_SIZE + offset[1] + height / 2
            if x > -TILE_SIZE and y > -TILE_SIZE and x < width and y < height:
                screen.blit(imgs[map[i][j]], (x, y))
    width, height = pygame.display.get_surface().get_size()
    offset[0] = player.x
    offset[1] = player.y
    player.draw()
    player.move()

    clock.tick(60)
    pygame.display.flip()

pygame.quit()
