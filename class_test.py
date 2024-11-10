import pgzrun
import random
from pgzhelper import *
# Pencerenin Çizimi
hucre = Actor("sinir")

#pgzero

WIDTH = 600 # Pencere Genişliği
HEIGHT = 300 # Pencere Yüksekliği

TITLE = "Uzaylı Yarışı" # Title for the game window
FPS = 30 # Saniyedeki Kare Sayısı

class Sprite(Actor):
    def __init__(self, normal):
        super().__init__(normal)
        self.health = 100
        self.attack = 5
        self.coordinates = (50, 50)
        self.normal = normal
    vx = 5
    vy = 5

    def update(self):
        # self.x += self.vx
        # self.y += self.vy
        # if self.right > WIDTH or self.left < 0:
        #     self.vx = -self.vx
        # if self.bottom > HEIGHT or self.top < 0:
        #     self.vy = -self.vy
        if keyboard.right or keyboard.d and self.x + hucre.width < WIDTH - hucre.width:
            self.x += 3
            #normal.image = 'karakter'
        elif keyboard.left or keyboard.a and self.x - hucre.width > hucre.width:
            self.x -= 3
            #karakter.image = 'sol'
        elif keyboard.down or keyboard.s and self.y + hucre.height < HEIGHT - hucre.height*2:
            self.y += 3
        elif keyboard.up or keyboard.w and self.y - hucre.height > hucre.height:
            self.y -= 3

    

# Nesneler
uzayli = Sprite('uzayli')
arkaplan = Sprite("arkaplan")
kutu = Sprite("kutu")

def draw():
    arkaplan.draw()
    uzayli.draw()
    kutu.draw()
       
def update(dt):
    # Kutunun Hareketi
    # if kutu.x > -20:
    #     kutu.x = kutu.x - 5
    #     kutu.angle = kutu.angle + 5        
    # else:
    #     kutu.x = WIDTH + 20
    uzayli.update()




    # import pgzrun
# import random
# from pgzhelper import *


# WIDTH = 600 # Pencere Genişliği
# HEIGHT = 300 # Pencere Yüksekliği

# TITLE = "Uzaylı Yarışı" # Title for the game window
# FPS = 30 # Saniyedeki Kare Sayısı

# arkaplan = Actor("arkaplan")
# alien = Actor('karakter')
# alien.images = ["karakter", "karakter_right_attack"]
# alien.fps = 10

# def update():
#   arkaplan.draw()
#   if keyboard.right:
#     alien.x += 3
#     alien.animate()

# def draw():
#   alien.draw()