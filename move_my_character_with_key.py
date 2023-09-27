from pico2d import *
open_canvas()

sprite = load_image('sprite_sheet.png')
backGround = load_image('TUK_GROUND.png')

backGround.draw_now(400,400)
delay(1)

close_canvas()
