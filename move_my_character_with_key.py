from pico2d import *
TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

sprite = load_image('sprite_sheet.png')
backGround = load_image('TUK_GROUND.png')

class character:
    def __init__(self):
        self.x, self.y = TUK_WIDTH // 2, TUK_HEIGHT // 2
        self.img = sprite
        self.w, self.h = 100, 100
    def draw(self):
        self.img.clip_draw(0, self.img.h - 36, 36, 36, self.x, self.y, self.w, self.h)
my_character = character()

clear_canvas()
backGround.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
my_character.draw()
update_canvas()



delay(1)

close_canvas()
