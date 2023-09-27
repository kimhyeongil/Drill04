from pico2d import *
TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

sprite = load_image('sprite_sheet.png')
backGround = load_image('TUK_GROUND.png')

class character:
    def __init__(self):
        self.x, self.y = TUK_WIDTH // 2, TUK_HEIGHT // 2
        self.img = sprite
        self.sizeW, self.sizeH = 2, 2
        self.frame = 0
        self.dirH, self.dirV = 0, 0
        self.speed = 10
        
        self.lefts = list(range(0, 36 * 14 + 1, 36))
        self.bottoms = [sprite.h - 41 for i in range(len(self.lefts))]
        self.widths = [36 for i in range(len(self.lefts))]
        self.heights = [41 for i in range(len(self.lefts))]
        
        self.lefts += [108, 144, 180, 224, 272, 320, 360, 396, 432, 468, 504, 545, 596, 647, 688]
        self.widths += [36, 36, 44, 48, 48, 40, 36, 36, 36, 36, 41, 51, 51, 41, 36]
        self.bottoms += [sprite.h - 82 for i in range(15)]
        self.heights += [41 for i in range(15)]
        
        self.index = 0
    def draw(self):
        self.img.clip_draw(self.lefts[self.frame + self.index], self.bottoms[self.frame + self.index], 
                           self.widths[self.frame + self.index], self.heights[self.frame + self.index],
                           self.x - (self.widths[self.frame + self.index] - 36) // 2, self.y,
                           self.widths[self.frame + self.index] * self.sizeW, self.heights[self.frame + self.index] * self.sizeH)
        if (self.x + self.dirH * self.speed <= TUK_WIDTH - self.sizeW // 2 and self.x + self.dirH * self.speed >= self.sizeW // 2):
            self.x += self.dirH * self.speed
        if (self.y + self.dirV * self.speed <= TUK_HEIGHT - self.sizeH // 2 and self.y + self.dirV * self.speed >= self.sizeH // 2):
            self.y += self.dirV * self.speed
        self.frame = ((self.frame + 1) % self.nFrame)
    
    def set_idle(self):
        self.nFrame, self.index = 15, 0
    
    def set_punch(self):
        self.nFrame, self.index = 15, 15
        

my_character = character()

def animation():
    clear_canvas()
    backGround.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    my_character.draw()
    update_canvas()
    delay(0.15)

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
    else:
        my_character.set_punch()

while True:
    handle_events()
    animation()
    
delay(1)

close_canvas()
