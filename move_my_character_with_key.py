from pico2d import *
TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

sprite = load_image('sprite_sheet.png')
backGround = load_image('TUK_GROUND.png')

backGround.draw_now(TUK_WIDTH // 2, TUK_HEIGHT // 2)
delay(1)

close_canvas()
