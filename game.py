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
    [0, None, None, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
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
font=pygame.font.Font("fonts/Pixel.ttf",28)

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dy = 0
        self.rect = pygame.Rect(abs(self.x) - 36, abs(self.y) - 42, 72, 96)
        self.jumped=False
        self.dir=True
    def draw(self):
        if self.dir:
            screen.blit(gg_imgs[0], (int(width / 2 - 36), int(height / 2 - 42)))
        else:
            screen.blit(pygame.transform.flip(gg_imgs[0], True, False), (int(width / 2 - 36), int(height / 2 - 42)))
        self.rect = pygame.Rect(abs(self.x) - 36, abs(self.y) - 42, 72, 96)

    def move(self):
        self.dy -= 0.8
        if keys[pygame.K_SPACE] and not self.jumped:
            self.dy = 20
            self.jumped=True
        elif keys[pygame.K_SPACE]:
            self.jumped=True
        else:
            self.jumped=False
        if keys[pygame.K_a]:
            self.dir=False
            self.x += 4
        if keys[pygame.K_d]:
            self.dir=True
            self.x -= 4
        self.y += self.dy
        iftiles = []
        for tile in tiles:
            if tile.inframe and tile.img is not None:
                iftiles.append(tile)
        self.rect = pygame.Rect(abs(self.x) - 36, abs(self.y) - 42, 72, 96)
        colliding = True
        collided = False
        bounce=False
        origdy=self.dy
        while colliding:
            collided = False
            for tile in iftiles:
                if (
                    self.rect.colliderect(tile.rect)
                    and abs(self.y) + TILE_SIZE > abs(tile.y)
                    and abs(self.y) != self.y
                    and abs(self.x) != self.x
                    and self.dy <= 0
                ):
                    self.y += 0.1
                    self.dy = 0
                    collided = True
                    bounce=True
                    self.rect = pygame.Rect(abs(self.x) - 36, abs(self.y) - 42, 72, 96)
                    self.jumped=False
            colliding = collided
        if bounce:
            self.dy=abs(origdy)*0.45
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
        else:
            self.inframe = False
        self.rect = pygame.Rect(self.x, self.y, TILE_SIZE, TILE_SIZE)


player = Player(0, 0)
tiles = []
for i in range(len(map)):
    for j in range(len(map[i])):
        tiles.append(Tile(j, i, map[i][j]))
dt=0
while running:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or keys[pygame.K_q]:
            running = False
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

    dt=clock.tick(60)
    fps=clock.get_fps()
    screen.blit(font.render(str(round(fps))+" FPS", False, (255,255,255), ),(10,10))
    pygame.display.flip()

pygame.quit()
