from pico2d import *


class Character:
    def __init__(self,sprite):
        self.x, self.y = get_canvas_width() // 2, get_canvas_height() // 2
        self.img = sprite
        self.sizeW, self.sizeH = 2, 2
        self.frame = 0
        self.dirH, self.dirV = 0, 0
        self.speed = 10
        
        self.lefts = list(range(0, 36 * 13 + 1, 36))
        self.bottoms = [sprite.h - 38 for i in range(len(self.lefts))]
        self.widths = [36 for i in range(len(self.lefts))]
        self.heights = [38 for i in range(len(self.lefts))]
        
        self.lefts += [108, 144, 180, 223, 271, 318, 360, 396, 432, 468, 504, 545, 596, 646, 688]
        self.widths += [36, 36, 43, 48, 47, 42, 36, 36, 36, 36, 41, 51, 50, 42, 36]
        self.bottoms += [sprite.h - 82 for i in range(15)]
        self.heights += [38 for i in range(15)]
        
        self.index, self.nFrame = 0, 13
        self.isLookLeft = True
    
    def draw(self):
        if (not self.isLookLeft):
            self.img.clip_composite_draw(self.lefts[self.frame + self.index], self.bottoms[self.frame + self.index], 
                           self.widths[self.frame + self.index], self.heights[self.frame + self.index],
                           0, 'h',
                           self.x + (self.widths[self.frame + self.index] - 36), self.y,
                           self.widths[self.frame + self.index] * self.sizeW, self.heights[self.frame + self.index] * self.sizeH)
        else:
            self.img.clip_draw(self.lefts[self.frame + self.index], self.bottoms[self.frame + self.index], 
                           self.widths[self.frame + self.index], self.heights[self.frame + self.index],
                           self.x - (self.widths[self.frame + self.index] - 36), self.y,
                           self.widths[self.frame + self.index] * self.sizeW, self.heights[self.frame + self.index] * self.sizeH)
        if (self.x + self.dirH * self.speed <= get_canvas_width() - 50 and self.x + self.dirH * self.speed >= 50):
            self.x += self.dirH * self.speed
        if (self.y + self.dirV * self.speed <= get_canvas_height() - 50 and self.y + self.dirV * self.speed >= 50):
            self.y += self.dirV * self.speed
        self.frame = ((self.frame + 1) % self.nFrame)
    
    def set_idle(self):
        self.nFrame, self.index = 14, 0
    
    def set_punch(self):
        self.nFrame, self.index = 15, 14
        
class GameManager:
    def __init__(self):
        open_canvas()
        self.sprite = load_image('sprite_sheet.png')
        self.backGround = load_image('TUK_GROUND.png')
        self.width, self.height = self.backGround.w, self.backGround.h
        resize_canvas(self.width, self.height)
        self.my_character = Character(self.sprite)   
    
    def render(self):
        clear_canvas()
        self.backGround.draw(self.width // 2, self.height // 2)
        self.my_character.draw()
        update_canvas()
        delay(0.15)
    

GM = GameManager()

while (True):
    GM.render()

delay(1)

close_canvas()
