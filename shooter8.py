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

def on_mouse_move(pos):
    ship.angle = ship.angle_to(pos) - 90

def update():
    global score
    
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
    
    gem.y = gem.y + 4
    if gem.y > 600:
        gem.y = -35
    if gem.colliderect(ship):
        gem.y = 0
        gem.x = random.randint(20, 780)
        score = score + 10
        
def draw():
    screen.fill((80,0,70))
    ship.draw()
    gem.draw()
    screen.draw.text('Score: ' + str(score), (15,10), color=(255,255,255), fontsize=30)

pgzrun.go() # Must be last line
