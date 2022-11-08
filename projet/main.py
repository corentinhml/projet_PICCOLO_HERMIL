from pygame.math import Vector2
import core


def setup():
    print("Setup START---------")
    core.fps = 30
    core.WINDOW_SIZE = [800, 700]

    core.memory("position", Vector2(400, 350))
    core.memory("vitesse", Vector2(0, -1))
    core.memory("accélération", Vector2(0, 0))
    core.memory("p1", Vector2())
    core.memory("p2", Vector2())
    core.memory("p3", Vector2())
    core.memory("score", 0)
    core.memory("life", 3)

    print("Setup END-----------")


def spaceshipcontrol():

    if core.getKeyPressList("z"):
        core.memory("vitesse").scale_to_length(core.memory("vitesse").length() + 0.1)
        # core.memory("accélération", core.memory("accélération") + (1, 0))
    if core.getKeyPressList("s"):
        core.memory("vitesse").scale_to_length(core.memory("vitesse").length() - 0.1)
        # core.memory("accélération", core.memory("accélération") + (-1, 0))
    if core.getKeyPressList("d"):
        core.memory("vitesse", core.memory("vitesse").rotate(5))
        # core.memory("accélération", core.memory("accélération") + (0, +1))
    if core.getKeyPressList("q"):
        core.memory("vitesse", core.memory("vitesse").rotate(-5))
        # core.memory("accélération", core.memory("accélération") + (0, -1))


def spaceship():

    core.memory("position", core.memory("position") + core.memory("vitesse"))

    p1 = core.memory("vitesse")
    p1 = p1.rotate(90)
    p1.scale_to_length(5)
    p1bis = p1 + core.memory("position")
    core.memory("p1", p1bis)

    p2 = core.memory("vitesse")
    p2.scale_to_length(20)
    p2bis = p2 + core.memory("position")
    core.memory("p2", p2bis)

    p3 = core.memory("vitesse")
    p3 = p3.rotate(-90)
    p3.scale_to_length(5)
    p3bis = p3 + core.memory("position")
    core.memory("p3", p3bis)


def drawspaceship():

    core.Draw.polygon((255, 0, 0), (core.memory("p1"), core.memory("p2"), core.memory("p3")))


def bord():
    if core.memory("position").x < 0:
        core.memory("position").x = core.WINDOW_SIZE[1]
    if core.memory("position").x > core.WINDOW_SIZE[1]:
        core.memory("position").x = 0
    if core.memory("position").y < 0:
        core.memory("position").y = core.WINDOW_SIZE[1]
    if core.memory("position").y > core.WINDOW_SIZE[1]:
        core.memory("position").y = 0


def scorelife():
    core.Draw.text((255, 255, 255), " score : " + str(core.memory("score")), (0, 0), 15)
    core.Draw.text((255, 255, 255), " life : " + str(core.memory("life")), (0, 35), 15)


def run():
    # core.memory("accélération", Vector2(0,0))
    core.cleanScreen()

    spaceshipcontrol()
    spaceship()
    drawspaceship()
    bord()
    scorelife()


core.main(setup, run)
