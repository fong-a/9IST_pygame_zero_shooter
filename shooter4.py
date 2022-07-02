
import pgzrun

WIDTH = 800
HEIGHT = 600

ship = Actor('playership1_red')
ship.x = 370
ship.y = 550

gem = Actor('gemyellow')
gem.x = 350
gem.y = 0

def update():
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
def draw():
    screen.fill((80,0,70))
    ship.draw()
    gem.draw()

pgzrun.go() # Must be last line
