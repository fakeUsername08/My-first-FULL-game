import pygame,sys,random,time,subprocess

pygame.init()

# varable
size = (600,800)
white = (255,255,255)
orange = (255,165,0)
enemy_list = []
clock = pygame.time.Clock()
fps = 60
player_x = 240
flag = True
speed = 10
sccore = 0
font = pygame.font.Font("DS-DIGI.TTF",30)
font_end = pygame.font.Font("DS-DIGI.TTF",60)

# game
win = pygame.display.set_mode(size)
pygame.display.set_caption("Space Runner")

# back ground
back = pygame.image.load("pictrue/back.png")
back_new = pygame.transform.scale(back,(1200,800))

# player
player = pygame.image.load("pictrue/player.png")
player_new = pygame.transform.scale(player,(80,80))

# dead player
player_crack = pygame.image.load("pictrue/player_crack.png")
player_crack_new = pygame.transform.scale(player_crack,(80,80))

# enemy (rock)
enemy = pygame.image.load("pictrue/rock.png")
enemy_new = pygame.transform.scale(enemy,(80,80))



# function
def make_enemy():
    spawn = random.randint(1,50)
    if len(enemy_list) < 10 and spawn == 1:
        enemy_x = random.randint(0,520)
        enemy_pos = [enemy_x,30]
        enemy_list.append(enemy_pos)
        # print(enemy_list)

def spawn_enemy():
    for enemy_xy in enemy_list:
        win.blit(enemy_new,(enemy_xy[0],enemy_xy[1]))

def update_enemy():
    for index,enemy_xy in enumerate(enemy_list):
        enemy_xy[1] += speed/3
        if enemy_xy[1] > 800:
            enemy_list.pop(index)
            return True

def game_over():
    for enemy_xy in enemy_list:
        if (player_x <= enemy_xy[0]+80 and player_x+80 >= enemy_xy[0] and 700 <= enemy_xy[1]+80):
            return True

def waiting():
    for i in range(3,0,-1):
        font = pygame.font.Font("DS-DIGI.TTF",100)
        i_new = str(i)
        text_wait = font.render(i_new,True,orange)
        win.blit(back_new,(-300,0))
        win.blit(text_wait,(250,350))
        pygame.display.update()
        time.sleep(1)

# loop
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and player_x < 520:
                player_x += speed
                # print(player_x)
            if (event.key == pygame.K_LEFT or event.key == pygame.K_a) and player_x > 0:
                player_x -= speed
                # print(player_x)

    text = (f"sccore: {sccore}")
    text_show = font.render(text,False,white)
    clock.tick(fps)
    make_enemy()
    win.blit(back_new,(-300,0))
    if flag:
        flag = False
        waiting()
    win.blit(text_show,(0,0))
    spawn_enemy()
    point = update_enemy()
    if point:
        sccore +=1
    end = game_over()
    if end:
        win.blit(back_new,(-300,0))
        spawn_enemy()
        win.blit(player_crack_new,(player_x,700))
        pygame.display.update()
        time.sleep(2)
        for i in range(5,0,-1):
            end_screen = font_end.render("Game Over",False,orange)
            end_sccore = font_end.render(f"sccore: {sccore}",False,orange)
            end_wait = font_end.render(str(i),False,orange)
            win.blit(back_new,(-300,0))
            win.blit(end_screen,(200,350))
            win.blit(end_sccore,(200,400))
            win.blit(end_wait,(200,450))
            pygame.display.update()
            time.sleep(1)
        break
    win.blit(player_new,(player_x,700))
    pygame.display.update()
pygame.quit()
subprocess.run(["python", "menu.py"])
sys.exit()