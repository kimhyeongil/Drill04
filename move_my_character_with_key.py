from pico2d import *
TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

sprite = load_image('sprite_sheet.png')
backGround = load_image('TUK_GROUND.png')

class character:
    def __init__(self):
        self.x, self.y = TUK_WIDTH // 2, TUK_HEIGHT // 2
        self.img = sprite
        self.sizeW, self.sizeH = 100, 100
        self.frame = 0
        self.dirH, self.dirV = 0, 0
        self.speed = 10
        self.width, self.height = 36, 36
        self.left, self.bottom = 0, self.img.h - 36
        self.nFrame = 6
    
    def draw(self):
        self.img.clip_draw(self.left + self.frame * self.width,self.bottom, 36, 36, self.x, self.y, self.sizeW, self.sizeH)
        if (self.x + self.dirH * self.speed <= TUK_WIDTH - self.sizeW // 2 and self.x + self.dirH * self.speed >= self.sizeW // 2):
            self.x += self.dirH * self.speed
        if (self.y + self.dirV * self.speed <= TUK_HEIGHT - self.sizeH // 2 and self.y + self.dirV * self.speed >= self.sizeH // 2):
            self.y += self.dirV * self.speed
        self.frame = (self.frame + 1) % self.nFrame

    def set_idle(self):
        self.width, self.height = 36, 36
        self.left, self.bottom = 0, self.img.h - 36
        self.nFrame = 6
    
    def set_punch(self):
        self.width, self.height = 36, 36
        self.left, self.bottom = 108, self.img.h - 36
        self.nFrame = 12        
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
    if (my_character.dirH == 0 and my_character.dirV == 0):
        my_character.set_idle()

while True:
    handle_events()
    animation_idle()

delay(1)

close_canvas()
