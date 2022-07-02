import pgzrun
import random


WIDTH = 800
HEIGHT = 600

ship = Actor('playership1_red')
ship.x = 370
ship.y = 550
ship.angle = 0

gem = Actor('gemyellow')
gem.x = 350
gem.y = 0
score = 0
gemCount = 0 
starActivate = False

star = Actor('star')
star.x = random.randint(20, 780) 
star.y = -35

enemies = []
bullets = []
bullet_delay = 0

music.play('music')

game_over = Actor('game-over')
game_over.x = 400
game_over.y = 300

game_state = 1

def on_mouse_move(pos):
    ship.angle = ship.angle_to(pos) - 90

def update():
    global score
    global lives
    global gemCount
    global starActivate
    global bullet_delay
    global game_state

    if keyboard.left:
        if ship.x <= 15: #detects if ship has reached left side of screen
            ship.x = 15
        ship.x = ship.x - 5
    if keyboard.right:
        if ship.x >= 785: #detects if ship has reached right side of screen
            ship.x = 785
        ship.x = ship.x + 5
    if keyboard.up:
        if ship.y <= 0: #detects if ship has reached the top of screen
            ship.y = 15
        ship.y = ship.y - 5
    if keyboard.down:
        if ship.y >= 600: #detects if ship has reached the bottom of screen
            ship.y = 600
        ship.y = ship.y + 5

    if keyboard.space and bullet_delay == 0:
        sounds.sfx_sounds_interaction25.play()
        bullet_delay = 5
        bullet = Actor('player_bullet')
        bullet.x = ship.x
        bullet.y = ship.y
        bullets.append(bullet)

    if bullet_delay > 0:
        bullet_delay -= 1
    
    for bullet in bullets:
        bullet.y = bullet.y - 6
        if bullet.y < 0:
            bullets.remove(bullet)
            
    # Deals with gems and stars
    
    gem.y = gem.y + 5 
    
    if gem.y > 600:
        gem.y = -35
        gem.x = random.randint(20, 780)
        
    if gem.colliderect(ship):
        gemCount = gemCount + 1
        gem.y = 0
        gem.x = random.randint(20, 780)
        score = score + 10
        if gemCount % 10 == 0:
            starActivate = True
            
    if starActivate == True:
        star.y = star.y + 10
        if star.y > 600:
            star.y = -35
            star.x = random.randint(20, 780)
            starActivate = False
    else:
        star.y = -35
            
    if star.colliderect(ship):
        score = score + 50
        starActivate = False
    
    # deals with spawning enemies
    
    if random.randint(0, 1000) > 990: # this can be adjusted to spawn less/more enemies
        enemy_images = ['ufored', 'ufogreen', 'ufoblue', 'ufoyellow']
        enemy = Actor(enemy_images[random.randint(0,3)]) # chooses a random image from the list above
        enemies.append(enemy) 
        enemy.y = -5
        enemy.x = random.randint(100, 700)
        enemy.direction = random.randint(-100, -80)
        enemies.append(enemy)
        
    # deals with enemy movement
    
    for enemy in enemies:
        enemy.y = enemy.y + 4
        if enemy.y > 700:
            enemies.remove(enemy)
  
    # destroys bullet and enemy when collision occurs
    
    for bullet in bullets:
        hit = bullet.collidelist(enemies)
        if hit != -1:
            bullets.remove(bullet)
            enemies.remove(enemies[hit])
            score = score + 20
  
    # deals with game over screen
    
    if ship.collidelist(enemies) != -1:
        game_state = 2
  
def draw():
    screen.fill((80,0,70))
    if game_state == 1:
        ship.draw()
    gem.draw()
    star.draw()
    screen.draw.text('Score: ' + str(score), (15,10), color=(255,255,255), fontname = 'righteous-regular', fontsize=40)

    for enemy in enemies:
        enemy.draw()
    for bullet in bullets:
        bullet.draw()
    
    if game_state == 2:
        game_over.draw()
        
pgzrun.go() # Must be last line
