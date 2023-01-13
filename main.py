import arcade, random, math

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "CATANE"

TILE_SIZE = 50


def size_to_scale(sprite_size, target_size):
    return target_size / sprite_size


class Tile(arcade.Sprite):
    def __init__(self, type, x, y):
        self.set_texture(arcade.load_texture(f"assets/tiles/{type}.PNG"))
        self.scale = size_to_scale(self.texture.size[0], TILE_SIZE)
        self.set_position(math.sqrt(3) * TILE_SIZE * x, 3/2 * TILE_SIZE * y)







class MyGame(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color((51, 51, 51))

    def setup(self):
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

    def on_draw(self):
        self.clear()

        for tile in tiles:
            tile.draw()

    def on_update(self, delta_time):
        pass

    def on_key_press(self, key, key_modifiers):
        pass

    def on_key_release(self, key, key_modifiers):
        pass

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        pass

    def on_mouse_press(self, x, y, button, key_modifiers):
        pass

    def on_mouse_release(self, x, y, button, key_modifiers):
        pass


def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
