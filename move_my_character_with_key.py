from pico2d import *
TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

sprite = load_image('sprite_sheet.png')
backGround = load_image('TUK_GROUND.png')

class character:
    pass

my_character = character()
print(type(my_character))

clear_canvas()
backGround.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
update_canvas()
delay(1)

close_canvas()
