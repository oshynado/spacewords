import pygame
from sys import exit
from random import randint,choice
from english_words import english_words_lower_alpha_set as all_words  

#this is a sprite of the main character
class SpaceShip(pygame.sprite.Sprite):
    #constructor of the main player class 
    def __init__(self):
        super(SpaceShip,self).__init__()
        #the image of the main character
        self.image= pygame.image.load("graphics/space_ship.png").convert_alpha()
        self.rect=self.image.get_rect(midbottom =(200,645))
        #variable for contain the number of hearts of the player 
        self.health=3

    #method for check if a letter pressed 
    def typing(self,key):
        if all_enemies_group:
            if key==pygame.K_a:
                all_enemies_group.sprites()[0].hit_enemy("a")
            elif key==pygame.K_b:
                all_enemies_group.sprites()[0].hit_enemy("b")
            elif key==pygame.K_c:
                all_enemies_group.sprites()[0].hit_enemy("c")
            elif key==pygame.K_d:
                all_enemies_group.sprites()[0].hit_enemy("d")
            elif key==pygame.K_e:
                all_enemies_group.sprites()[0].hit_enemy("e")
            elif key==pygame.K_f:
                all_enemies_group.sprites()[0].hit_enemy("f")
            elif key==pygame.K_g:
                all_enemies_group.sprites()[0].hit_enemy("g")
            elif key==pygame.K_h:
                all_enemies_group.sprites()[0].hit_enemy("h")
            elif key==pygame.K_i:
                all_enemies_group.sprites()[0].hit_enemy("i")
            elif key==pygame.K_j:
                all_enemies_group.sprites()[0].hit_enemy("j")
            elif key==pygame.K_k:
                all_enemies_group.sprites()[0].hit_enemy("k")
            elif key==pygame.K_l:
                all_enemies_group.sprites()[0].hit_enemy("l")
            elif key==pygame.K_m:
                all_enemies_group.sprites()[0].hit_enemy("m")
            elif key==pygame.K_n:
                all_enemies_group.sprites()[0].hit_enemy("n")
            elif key==pygame.K_o:
                all_enemies_group.sprites()[0].hit_enemy("o")
            elif key==pygame.K_p:
                all_enemies_group.sprites()[0].hit_enemy("p")
            elif key==pygame.K_q:
                all_enemies_group.sprites()[0].hit_enemy("q")
            elif key==pygame.K_r:
                all_enemies_group.sprites()[0].hit_enemy("r")
            elif key==pygame.K_s:
                all_enemies_group.sprites()[0].hit_enemy("s")
            elif key==pygame.K_t:
                all_enemies_group.sprites()[0].hit_enemy("t")
            elif key==pygame.K_u:
                all_enemies_group.sprites()[0].hit_enemy("u")
            elif key==pygame.K_v:
                all_enemies_group.sprites()[0].hit_enemy("v")
            elif key==pygame.K_w:
                all_enemies_group.sprites()[0].hit_enemy("w")
            elif key==pygame.K_x:
                all_enemies_group.sprites()[0].hit_enemy("x")
            elif key==pygame.K_y:
                all_enemies_group.sprites()[0].hit_enemy("y")
            elif key==pygame.K_z:
                all_enemies_group.sprites()[0].hit_enemy("z")
            
    #method to increment the number of hearts of the player 
    def addhealth(self):
        self.health += 1
    #method to decrement the number of hearts of the player 
    def damage(self):
        self.health -=1
        #check if number of hearts is less than or equal 0 will stop the game
        if self.health<=0:
            global run_game 
            run_game=False
    #method for show the health of player on screen
    def hp_bilt(self):
        hp_surf=score_font.render(f"HP:{self.health}",False,(220,220,220))
        hp_rect=hp_surf.get_rect(center=(80,620))
        screen.blit(hp_surf,hp_rect)
    #the update method of the sprite
    def update(self,health=0):
        if health==-1:
            self.damage()
        self.hp_bilt()

#this class of the words monsters which are enemies for player
class Enemies(pygame.sprite.Sprite):
    #the constructor
    #type is a parameter which define the difficult of the enemy
    def __init__(self, type):
        super(Enemies,self).__init__()
        if type=="easy":
            self.image= pygame.image.load("graphics/enemies/easy_enemy.png").convert_alpha()
            self.word=choice(easy_words)
        elif type=="mid":
            self.image= pygame.image.load("graphics/enemies/mid_enemy.png").convert_alpha()
            self.word=choice(mid_words)
        elif type=="hard":
            self.image= pygame.image.load("graphics/enemies/hard_enemy.png").convert_alpha()
            self.word=choice(hard_words)
        elif type=="health":
            self.image= pygame.image.load("graphics/enemies/health_enemy.png").convert_alpha()
            self.word=choice(health_words)
        self.type=type
        #position of the enemy respawn on the screen
        self.position=(randint(0,400),-30)
        self.rect = self.image.get_rect(center=self.position)
        self.word_text=words_font.render("    "+self.word,False,(200,200,200))
        self.word_rect=self.word_text.get_rect(bottomleft=self.position)
        self.position=pygame.math.Vector2(self.position)
        self.speed=1
    #method responsible for the movement of the enemy towards the player 
    def enemy_movement(self,player):
        player_position = player.rect.center
        direction = player_position - self.position
        velocity = direction.normalize() * self.speed

        self.position += velocity
        self.rect.center = self.position
        self.word_rect.bottomleft= self.position
    #method check if the pressed letter is in the correct order in the word of the closest enemy for the player 
    def hit_enemy(self,letter):
        global score
        global d_score
        if self.word[0]==letter:
            self.word=self.word[1:]
        #if the word of the monster is finished increment the score and the difficulty score by one 
        #and delete the empty monster
        if self.word=="":
            if self.type=="health":
                player.sprite.addhealth()
            score+=1
            d_score+=1
            self.kill()
    #the update method of the enemies sprites 
    def update(self,player):
        self.enemy_movement(player)

pygame.init()
#fonts declaration
words_font=pygame.font.Font('font/Jersey10-Regular.ttf',25)
score_font=pygame.font.Font('font/Jersey10-Regular.ttf',50)
#generate the lists of english words with different lengths
easy_words=[i for i in all_words if len(i) >=3 and len(i) <=5]
mid_words=[i for i in all_words if len(i) >=6 and len(i) <=8]
hard_words=[i for i in all_words if len(i) >=9 and len(i) <=13]
health_words=[i for i in all_words if len(i) >=7 and len(i) <=11]
#declare the main screen of the game
screen=pygame.display.set_mode((400,650))
pygame.display.set_caption('Space Words')
pygame.display.set_icon(pygame.image.load("graphics/logo.jpg").convert_alpha())
#declare a clock to control the framerate 
clock = pygame.time.Clock()
#make a single group for the sprite of the player 
player=pygame.sprite.GroupSingle()
player.add(SpaceShip())

#declare a sprite group for all enemies
all_enemies_group=pygame.sprite.Group()
#declare a sprite group for enemies make damage
enemies_group=pygame.sprite.Group()
#declare a sprite group for health bonus enemies 
health_group=pygame.sprite.Group()
#declare a list to hold the probability of spawning different difficulty enemies 
difficult_list=["easy"]*10

#function for check the collide between the player and any enemies
def collision_sprite():
    if pygame.sprite.spritecollide(player.sprite,enemies_group,True):
       player.update(-1)
    else:
        player.update()
    pygame.sprite.spritecollide(player.sprite,health_group,True)

#a score counter
score=0
#a score difficulty counter
d_score=0
#function for displaying the score 
def scoring():
    score_surf=score_font.render(f"score:{score}",False,(220,220,220))
    score_rect=score_surf.get_rect(midtop=(200,5))
    screen.blit(score_surf,score_rect)

#background declaration
background_surf1=pygame.image.load("graphics/background.jpg").convert()
background_rect1=background_surf1.get_rect(bottomleft=(0,650))
background_surf2=pygame.image.load("graphics/background.jpg").convert()
background_rect2=background_surf2.get_rect(bottomleft=(0,-650))

#declare start screen
start_screen=pygame.image.load("graphics/start_screen.png")
start_screen_rect=start_screen.get_rect(center=(200,325))

#declare game over screen
game_over_surf=score_font.render("Game Over",False,(255,255,255))
game_over_rect=game_over_surf.get_rect(center=(200,325))
game_over_surf2=words_font.render("press any key to play again",False,(255,255,255))
game_over_rect2=game_over_surf2.get_rect(center=(200,370))
start=True

#timer of the spawning regular enemies 
spawning_timer= pygame.USEREVENT + 1
pygame.time.set_timer(spawning_timer,5000)
#timer of the spawning health enemies
spawning_health=pygame.USEREVENT + 2
pygame.time.set_timer(spawning_health,62000)

#bool for know if the game is running or not
run_game=False

while True:
    #event check
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()    
        if run_game:
            if event.type==spawning_timer:
                enemy=Enemies(choice(difficult_list))
                enemies_group.add(enemy)
                all_enemies_group.add(enemy)
            if event.type==spawning_health:
                enemy=Enemies("health")
                health_group.add(enemy)
                all_enemies_group.add(enemy)
            if event.type==pygame.KEYDOWN:
                player.sprite.typing(event.key)
        else:
            if event.type==pygame.KEYDOWN:
                if start:
                    start=False
                score=0
                d_score=0
                run_game=True 
                player.sprite.health=3   
                for enemy in all_enemies_group.sprites():
                    enemy.kill()
                for enemy in enemies_group.sprites():
                    enemy.kill()
                for enemy in health_group.sprites():
                    enemy.kill()
                difficult_list=["easy"]*10
    if run_game:
        screen.blit(background_surf1,background_rect1)
        screen.blit(background_surf2,background_rect2)
        background_rect1.y +=1
        background_rect2.y +=1

        if background_rect1.bottom>=2600:background_rect1.bottom=0
        if background_rect2.bottom>=2600:background_rect2.bottom=0

        player.draw(screen)

        for enemy in all_enemies_group:
            if enemy==all_enemies_group.sprites()[0]:
                enemy.word_text=words_font.render("    "+enemy.word,False,(255,128,0))

            pygame.draw.rect(screen,(88,88,88),enemy.word_rect)
            screen.blit(enemy.word_text,enemy.word_rect)
        all_enemies_group.draw(screen)
        all_enemies_group.update(player.sprite)

        scoring()    

        collision_sprite()

        if d_score>=2 and score<=20:
            difficult_list.append("mid")
            difficult_list=difficult_list[1:]
            d_score=0
        if d_score>=2 and score>=20:
            difficult_list.append("hard")
            difficult_list=difficult_list[1:]
            d_score=0
    elif run_game==False and start==True:
        screen.fill((42,47,125))
        screen.blit(start_screen,start_screen_rect)
    else:
        screen.fill((42,47,125))
        screen.blit(game_over_surf,game_over_rect)
        screen.blit(game_over_surf2,game_over_rect2)

    pygame.display.update()
    clock.tick(60) 