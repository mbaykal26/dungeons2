import pgzrun
import random
from pgzhelper import *
# Pencerenin Çizimi
hucre = Actor("sinir")
hucre1 = Actor("zemin")
hucre2 = Actor("catlak")
hucre3 = Actor("kemikler")
carpi = Actor("carpi", (760, 30))
set_sound = Actor("bonus",(550, 250))
exit_the_game = Actor("bonus",(400, 420))
oyna = Actor("oyna",(250, 250))
ekran_g = 16 # Ekranın enindeki hücre sayısı
ekran_y = 17# Ekranın boyundaki hücre sayısı
hucre.width = 50
hucre.height = 50
WIDTH = hucre.width * ekran_g
HEIGHT = hucre.height * ekran_y

mod = "menu"
kazanmak = 0
attack = 0
puan = 0
dusman_numara = -1
TITLE = "Zindanlar" # Oyunun Adı
FPS = 30 # Saniyedeki Kare Sayısı
haritam = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1], 
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
    vx = 1
    vy = 1

    def update(self):
        self.x += self.vx
        self.y += self.vy
        if self.right > WIDTH or self.left < 0:
            self.vx = -self.vx
        if self.bottom > HEIGHT or self.top < 0:
            self.vy = -self.vy

ball = Sprite("alien")

def draw():
    screen.clear()
    ball.draw()

def update():
    ball.update()
    
# Başrol Karakteri
karakter = Actor('karakter')
karakter.health = 100
karakter.attack = 5
karakter.top = hucre.height
karakter.left = hucre.width

# Düşmanların Oluşturulması
dusmanlar = []
def form_dusmanlar():
    for i in range(5):
        x = random.randint(1, 10) * hucre.width
        y = random.randint(1, 10) * hucre.height
        dusman = Actor("dusman", topleft = (x, y))
        dusman.health = random.randint(10, 20)
        dusman.attack = random.randint(5, 10)
        dusman.bonus = random.randint(0, 2)
        dusman.direction = random.randint(-100, -80)
        dusmanlar.append(dusman)
form_dusmanlar()
# print(f"dusman.direction:{dusman.direction}")
# print(f"dusman.health:{dusman.direction}")
# print(f"dusman_numara:{dusman_numara}")
# Bonuses
kalpler = []
kiliclar = []


def harita_cizim_menu():
    for i in range(len(haritam)):
        for j in range(len(haritam[0])):
            hucre1.left = hucre.width*j
            hucre1.top = hucre.height*i
            hucre1.draw()

def harita_cizim():
    for i in range(len(haritam)):
        for j in range(len(haritam[0])):
            hucre1.left = hucre.width*j
            hucre1.top = hucre.height*i
            hucre1.draw()
# if mod == "menu":
#     sounds.level1.play(-1)
# elif mod == "oyun":
#     sounds.level2.play()                                                                                                                                                                                                                                                                                                                                                        


def draw():
    if mod == "menu":
        screen.fill("#2f3542")
        harita_cizim_menu()
        #sounds.thaelmines.play()
        #sounds.peacefuldays.play(1000)
        #sounds.sfx_sounds_interaction25.play()
        oyna.draw()
        set_sound.draw()
        screen.draw.text("Sound On/Off\n", center = (550, 265), color = "black", fontsize = 35) 
        exit_the_game.draw()
        screen.draw.text("Exit Game\n", center = (400, 435), color = "black", fontsize = 35) 
        screen.draw.text(str(karakter.pos) + "\n", center = (600, 600), color = "black", fontsize = 35)
        #print(oyna.pos, set_sound.pos)


    elif mod == "oyun": 
        if attack == 0:       
            sounds.thaelmines.play()
        screen.fill("#2f3542")
        harita_cizim()
        karakter.draw()
        screen.draw.text("Health:\n", center=(50, 835), color = 'black', fontsize = 37)
        screen.draw.text(str(karakter.health) + "\n", center=(130, 835), color = 'black', fontsize = 37)
        screen.draw.text("Attack:\n", center=(700, 835), color = 'black', fontsize = 37)
        screen.draw.text(str(karakter.attack) + "\n", center=(780, 835), color = 'black', fontsize = 37)
        screen.draw.text(str(karakter.pos) + "\n", center = (425, 835), color = "black", fontsize = 37)
        #screen.draw.text(str(dusman.health) + "\n", center = (760, 600), color = "black", fontsize = 37)
        for i in range(len(dusmanlar)):
            dusmanlar[i].draw()
        for i in range(len(kalpler)):
            kalpler[i].draw()
        for i in range(len(kiliclar)):
            kiliclar[i].draw()
        carpi.draw()



    elif mod == "off":        
        screen.fill("#2f3542")
        harita_cizim()
        karakter.draw()
        screen.draw.text("Health:\n", center=(35, 740), color = 'black', fontsize = 30)
        screen.draw.text(str(karakter.health) + "\n", center=(85, 740), color = 'black', fontsize = 30)
        screen.draw.text("Attack:\n", center=(700, 740), color = 'black', fontsize = 30)
        screen.draw.text(str(karakter.attack) + "\n", center=(825, 825), color = 'black', fontsize = 30)
        for i in range(len(dusmanlar)):
            dusmanlar[i].draw()
        for i in range(len(kalpler)):
            kalpler[i].draw()
        for i in range(len(kiliclar)):
            kiliclar[i].draw()
        sounds.thaelmines.stop()
            # sounds.level1.stop()
            # sounds.level2.stop()
        carpi.draw()
            
    elif mod == "son":
        screen.fill("#2f3542")
        if kazanmak == 1:
            sounds.thaelmines.stop()
            sounds.winning.play(1)
            screen.draw.text("wE GOTTA WINNER!\n", center=(WIDTH/2, HEIGHT/2), color = 'cyan', fontsize = 46)
            #screen.fill("red")
            # sounds.thaelmines.play()
            # sounds.militarybase.stop()
            # sounds.level1.stop()
            # sounds.level2.stop()

        else:
            sounds.winning.stop()
            sounds.loser.play(1)
            screen.fill("purple")
            screen.draw.text("You are such a LOSER!\n", center=(WIDTH/2, HEIGHT/2), color = 'cyan', fontsize = 46)
            # sounds.thaelmines.play()
            # sounds.militarybase.stop()
            # sounds.level1.stop()
            # sounds.level2.stop()
    
def on_key_down(key):
    global attack, puan, dusmanlar, fuzeler, mod
    eski_x = karakter.x
    eski_y = karakter.y
    if keyboard.right or keyboard.d and karakter.x + hucre.width < WIDTH - hucre.width:
        karakter.x += hucre.width
        karakter.image = 'karakter'
    elif keyboard.left or keyboard.a and karakter.x - hucre.width > hucre.width:
        karakter.x -= hucre.width
        karakter.image = 'sol'
    elif keyboard.down or keyboard.s and karakter.y + hucre.height < HEIGHT - hucre.height*2:
        karakter.y += hucre.height
    elif keyboard.up or keyboard.w and karakter.y - hucre.height > hucre.height:
        karakter.y -= hucre.height

    
    dusman_numara = karakter.collidelist(dusmanlar)
    if dusman_numara != -1: #and karakter.image == "karakter":
        attack = 1
        sounds.thaelmines.stop()
        sounds.eating_effect.play()
        karakter.image = "karakter_attack65bg"
        karakter.x = eski_x
        karakter.y = eski_y
        dusman = dusmanlar[dusman_numara]
        dusman.health -= karakter.attack
        karakter.health -= dusman.attack
        if dusman.health <= 0:
            if dusman.bonus == 1:
                kalp = Actor('kalp')
                kalp.pos = dusman.pos
                kalpler.append(kalp)
            elif dusman.bonus == 2:
                kilic = Actor('kilic')
                kilic.pos = dusman.pos
                kiliclar.append(kilic)
            dusmanlar.pop(dusman_numara)
    elif dusman_numara != -1 and karakter.image == "sol":
        attack = 1
        sounds.thaelmines.stop()
        sounds.eating_effect.play()
        karakter.image = "karakter_sol_attack"
        karakter.x = eski_x
        karakter.y = eski_y
        dusman = dusmanlar[dusman_numara]
        dusman.health -= karakter.attack
        karakter.health -= dusman.attack
        if dusman.health <= 0:
            if dusman.bonus == 1:
                kalp = Actor('kalp')
                kalp.pos = dusman.pos
                kalpler.append(kalp)
            elif dusman.bonus == 2:
                kilic = Actor('kilic')
                kilic.pos = dusman.pos
                kiliclar.append(kilic)
        # if dusman.health <= 0:
            # if dusman.bonus == 1:
            #     kalp = Actor('kalp')
            #     kalp.pos = dusman.pos
            #     kalpler.append(kalp)
            # elif dusman.bonus == 2:
            #     kilic = Actor('kilic')
            #     kilic.pos = dusman.pos
            #     kiliclar.append(kilic)
            dusmanlar.pop(dusman_numara)
    else:
        attack = 0
        karakter.image = "karakter"
        sounds.eating_effect.stop()

    if mod == "son" and keyboard.space:
        mod = "menu"
        dusmanlar = []
        form_dusmanlar()
        karakter.health = 100
        karakter.attack = 5

            

def zafer():
    global mod, kazanmak
    if dusmanlar == [] and karakter.health > 0:
        mod = "son"
        kazanmak = 1
    elif karakter.health <= 0:
        mod = "son"
        kazanmak = -1

  # UPDATE FUNCTION PART      
def update(dt):
    global puan, dusmanlar, dusman_numara
    zafer()
    
    for i in range(len(kalpler)):
        if karakter.colliderect(kalpler[i]):
            sounds.winning.play()
            karakter.health += 5
            kalpler.pop(i)
            break
    for i in range(len(kiliclar)):
        if karakter.colliderect(kiliclar[i]):
            sounds.winning.play()
            karakter.attack += 5
            kiliclar.pop(i)
            break
    
    for dusman in dusmanlar:
        #print(alien.distance_to(hero)) 
        if dusman.distance_to(karakter) <= 100:
            dusman.point_towards(karakter)
            karakter.point_towards(dusman)
            dusman.move_towards(karakter, 1)
            # dusman.move_in_direction(2)
            # dusman.animate()
        


    # clock.schedule(dusmanlar_right, 2.0)   
    # def dusmanlar_left():        
    #     for i in range(len(dusmanlar)):
    #         dusmanlar[i].x = dusmanlar[i].x - hucre.width
    #         break


def on_mouse_down(button, pos):
    global mod
    if mouse.LEFT and mod == "menu":
        if oyna.collidepoint(pos):            
            mod = "oyun"
        elif set_sound.collidepoint(pos):
            mod = "off"
        elif exit_the_game.collidepoint(pos):
            exit()
    elif mouse.LEFT and mod == "oyun":
        if carpi.collidepoint(pos):
            mod = "menu"


pgzrun.go()