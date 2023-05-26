import pygame

pygame.init()
width = 1280
height = 400
screen = pygame.display.set_mode((width, height), flags=pygame.RESIZABLE)
clock = pygame.time.Clock()
running = True
map_imgs = [
    pygame.image.load("images/gflat.png"),
]
gg_imgs = [
    pygame.transform.scale_by(pygame.image.load("images/gg1.png").convert_alpha(), 4)
]
offset = [0, 0]
TILE_SIZE = 64
pygame.mouse.set_cursor(
    pygame.cursors.Cursor(
        (0, 0), pygame.transform.scale_by(pygame.image.load("images/cursormain.png"), 2)
    )
)
map = [
    [None, None, None, None, None, None, None, None, None, None],
    [0, None, None, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, None, 0, 0, 0, 0, 0, 0],
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
        self.rect = pygame.Rect(abs(self.x) - 36, abs(self.y) - 42, 72, 96)

    def draw(self):
        screen.blit(gg_imgs[0], (int(width / 2 - 36), int(height / 2 - 48)))
        self.rect = pygame.Rect(abs(self.x) - 36, abs(self.y) - 42, 72, 96)
        if DEBUG:
            pygame.draw.circle(
                screen,
                (255, 0, 0),
                (self.x, self.y),
                4,
            )
            pygame.draw.rect(
                screen,
                "yellow",
                (
                    abs(self.x) - 36,
                    abs(self.y) - 48,
                    72,
                    96,
                ),
                4,
            )

    def move(self):
        self.dy -= 0.4
        if keys[pygame.K_SPACE]:
            self.dy = 12
        if keys[pygame.K_a]:
            self.x += 4
        if keys[pygame.K_d]:
            self.x -= 4
        self.y += self.dy
        iftiles = []
        for tile in tiles:
            if tile.inframe and tile.img is not None:
                iftiles.append(tile)
        self.rect = pygame.Rect(abs(self.x) - 36, abs(self.y) - 42, 72, 96)
        colliding = True
        collided = False
        while colliding:
            collided = False
            for tile in iftiles:
                if (
                    self.rect.colliderect(tile.rect)
                    and abs(self.y) + TILE_SIZE > abs(tile.y)
                    and abs(self.y) != self.y
                    and abs(self.x) != self.x
                ):
                    print("Y")
                    self.y += 0.1
                    self.dy = 0
                    collided = True
                    self.rect = pygame.Rect(abs(self.x) - 36, abs(self.y) - 42, 72, 96)
            colliding = collided


class Tile:
    def __init__(self, x, y, img):
        self.x = x * TILE_SIZE
        self.y = y * TILE_SIZE
        self.img = img
        if img is not None and img < 128:
            self.rect = pygame.Rect(self.x, self.y, TILE_SIZE, TILE_SIZE)
        else:
            self.rect = pygame.Rect(self.x, self.y, 0, 0)
        self.inframe = False

    def draw(self):
        x = self.x + offset[0] + width / 2
        y = self.y + offset[1] + height / 2
        if (
            x > -TILE_SIZE
            and y > -TILE_SIZE
            and x < width
            and y < height
            and self.img is not None
        ):
            screen.blit(map_imgs[self.img], (x, y))
            self.inframe = True
            if DEBUG:
                pygame.draw.rect(screen, "red", self.rect, 4)
        else:
            self.inframe = False
        self.rect = pygame.Rect(self.x, self.y, TILE_SIZE, TILE_SIZE)


player = Player(0, 0)
tiles = []
for i in range(len(map)):
    for j in range(len(map[i])):
        tiles.append(Tile(j, i, map[i][j]))
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    screen.fill("purple")
    """
    for i in range(len(map)):
        for j in range(len(map[i])):
            x = i * TILE_SIZE + offset[0] + width / 2
            y = j * TILE_SIZE + offset[1] + height / 2
            if (
                x > -TILE_SIZE
                and y > -TILE_SIZE
                and x < width
                and y < height
                and map[j][i] is not None
            ):
                screen.blit(map_imgs[map[j][i]], (x, y))
                pygame.draw.rect(screen,"red",(x,y,TILE_SIZE,TILE_SIZE), 4)
    """
    for tile in tiles:
        tile.draw()
    width, height = pygame.display.get_surface().get_size()
    offset[0] = player.x
    offset[1] = player.y
    player.draw()
    player.move()

    clock.tick(60)
    pygame.display.flip()

pygame.quit()
