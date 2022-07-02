
import pgzrun

WIDTH = 800
HEIGHT = 600

ship = Actor('playership1_red')
ship.x = 370
ship.y = 550

def update():
    if keyboard.left:
        if ship.x < 0:
            ship.x = 800
        ship.x = ship.x - 5
    if keyboard.right:
        if ship.x > 800:
            ship.x = 0
        ship.x = ship.x + 5

def draw():
    screen.fill((80,0,70))
    ship.draw()

pgzrun.go() # Must be last line
