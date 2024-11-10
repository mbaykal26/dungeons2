import pgzrun
import random
from pgzhelper import *

# print(pgzrun.__dict__)


mod = "menu"
winner = 0
attack = 0
puan = 0
enemy_list_index = -1
TITLE = "Zindanlar" # Oyunun Adı
FPS = 30 # Saniyedeki Kare Sayısı
map_list = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1], 
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1], 
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],  
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],  
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1], 
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],  
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1], 
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],  
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],  
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1], 
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],  
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1], 
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],  
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],  
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1], 
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],     
          ] # Hücüm Gücü ve Sağlık bilgisi


WIDTH = 500
HEIGHT = 500

class Sprite(Actor):
    def __init__(self, normal):
        super().__init__(normal)
        self.health = 100
        self.attack = 5
        self.normal = normal
        self.enemies = []
        self.pos = (50, 50)
        topleft = (50,50)
    vx = 5
    vy = 5
    def update(self):   
        if keyboard.right or keyboard.d and enemy.x + 50 < WIDTH - 50:
            enemy.x += 2
            #self.image = 'karakter'
        elif keyboard.left or keyboard.a and enemy.x - hucre.width > hucre.width:
            enemy.x -= 2
            #self.image = 'sol'
        elif keyboard.down or keyboard.s and enemy.y + 50 < HEIGHT - 50*2:
            enemy.y += 2
        elif keyboard.up or keyboard.w and enemy.y - 50 > 50:
            enemy.y -= 2

enemy = Sprite("dusman")
cell = Sprite("sinir")
cell1 = Sprite("zemin")
cell2 = Sprite("catlak")
cell3 = Sprite("kemikler")
cross = Sprite("carpi")
cross.pos = (760, 30)
set_sound = Sprite("bonus")
set_sound.pos = (550, 250)
exit_the_game = Sprite("bonus")
exit_the_game.pos = (400, 420)
play_the_game = Sprite("oyna")
play_the_game.pos = (250, 250)
screen_w = 16 # Ekranın enindeki hücre sayısı
height_h = 17# Ekranın boyundaki hücre sayısı
cell.width = 50
cell.height = 50
WIDTH = cell.width * screen_w
HEIGHT = cell.height * height_h 
    
# # Başrol Karakteri
# my_character = Sprite('karakter')
# my_character.health = 100
# my_character.attack = 5
# my_character.top = cell.height
# my_character.left = cell.width   

def map_sketch_menu():
    for i in range(len(map_list)):
        for j in range(len(map_list[0])):
            cell1.left = cell.width*j
            cell1.top = cell.height*i
            cell1.draw()

# # def draw():
# #     map_sketch_menu()
# #     my_character.draw()

# # def update(dt):
# #     my_character.move_forward(30)


# # Define the screen size
# # WIDTH = 800
# # HEIGHT = 600




# # Variable to keep track of the current image for walking animation
# walking_toggle = True
  
def draw():
    screen.clear()
    map_sketch_menu()
    enemy.draw()

def toggle_walking_image():
    global walking_toggle
    # Alternate between 'enemy_walk1' and 'enemy_walk2' to create a walking effect
    if walking_toggle:
        enemy.image = 'dusman_flipped'
    else:
        enemy.image = 'dusman'
    walking_toggle = not walking_toggle

def update():
# Schedule the image toggle every 0.5 seconds (500 milliseconds)
    enemy.update()
clock.schedule_interval(toggle_walking_image, 0.5)

# pgzrun.go()



# Define the screen size
# WIDTH = 800
# HEIGHT = 600

# # Create the character Actor with the initial image
# character = Actor('dusman', (400, 300))  # Use the uploaded image file name here

# # Variables to create the running effect
# bobbing_toggle = True
# base_y = character.y  # Store the original y position

# def draw():
#     screen.clear()
#     screen.fill("grey")
#     character.draw()

# def update():
#     # Simulate a running effect by slightly moving the character up and down
#     global bobbing_toggle
#     if keyboard.right:
#         character.x += 3
#         if bobbing_toggle:
#             character.y = base_y - 2  # Move up slightly
#         else:
#             character.y = base_y + 2  # Move down slightly
#         bobbing_toggle = not bobbing_toggle
#     if keyboard.left:
#         character.x -= 3
#         if bobbing_toggle:
#             character.y = base_y - 2  # Move up slightly
#         else:
#             character.y = base_y + 2  # Move down slightly
#         bobbing_toggle = not bobbing_toggle

#     # Schedule the bobbing effect every 0.1 seconds to create a quick "running" motion
# clock.schedule_interval(update, 0.1)

pgzrun.go()

