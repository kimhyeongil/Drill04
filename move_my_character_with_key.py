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
        self.frame = 0
        self.dirH, self.dirV = 0, 0
    def draw(self):
        self.img.clip_draw(self.frame * 36,self.img.h - 36, 36, 36, self.x, self.y, self.w, self.h)
        self.x += self.dirH * 5
        self.y += self.dirV * 5
        self.frame = (self.frame + 1) % 6
my_character = character()

def animation_idle():
    clear_canvas()
    backGround.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    my_character.draw()
    update_canvas()
    delay(0.1)
def handle_events():
    global my_character
    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                my_character.dirH += 1
            if event.key == SDLK_LEFT:
                my_character.dirH -= 1
            if event.key == SDLK_UP:
                my_character.dirV += 1
            if event.key == SDLK_DOWN:
                my_character.dirV -= 1        
        if event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                my_character.dirH -= 1
            if event.key == SDLK_LEFT:
                my_character.dirH += 1
            if event.key == SDLK_UP:
                my_character.dirV -= 1
            if event.key == SDLK_DOWN:
                my_character.dirV += 1  
while True:
    handle_events()
    animation_idle()

delay(1)

close_canvas()
