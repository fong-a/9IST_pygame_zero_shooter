import pgzrun

WIDTH = 800
HEIGHT = 600

ship = Actor('playership1_red')
ship.x = 370
ship.y = 550

def update():
    if keyboard.left:
        ship.x = ship.x - 5
    if keyboard.right:
        ship.x = ship.x + 5

def draw():
    ship.draw()

pgzrun.go() # Must be last line