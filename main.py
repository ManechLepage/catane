import pygame, random, math

pygame.init()

screen = pygame.display.set_mode((1600, 900))


class Tile(pygame.sprite.Sprite):
    def __init__(self, type, x, y):
        self.tile_image = pygame.image.load("assets/tiles/" + type + ".PNG")
        self.type = type
        super().__init__(self.tile_image, (x, y))



all_sprites = pygame.sprite.Group()

tile_list = ['desert']
tile_list += ['sheep'] * 4
tile_list += ['wood'] * 4
tile_list += ['brick'] * 3
tile_list += ['wheat'] * 4
tile_list += ['ore'] * 3


x_len = [3, 4, 5, 4, 3]

tiles = []
for x in range(5):
    for y in range(x_len[x]):
        if x_len[x] in [4, 5]:
            tile = Tile(random.choice(tile_list), x, y)
        else:
            tile = Tile(random.choice(tile_list), x + 1, y)
        print(tile.type)
        tiles.append(tile)
        tile.add(all_sprites)



while True:

    all_sprites.draw(screen)

    if pygame.event.get(pygame.QUIT):
        break



