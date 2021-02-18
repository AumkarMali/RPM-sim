import pygame as py

py.display.set_caption('RPM sim')

WIDTH = 800
HEIGHT = 600
FPS = 60

YELLOW = (224, 221, 38)
RED = (224, 57, 38)
BLACK = (0, 0, 0)

py.init()
screen = py.display.set_mode((WIDTH, HEIGHT))
clock = py.time.Clock()

rot = 0
rot_speed = 0.1
RPM = 0

image_orig = py.Surface((10, 200))
image_orig.set_colorkey(YELLOW)
image_orig.fill(RED)
image = image_orig.copy()
image.set_colorkey(YELLOW)
rect = image.get_rect()
rect.center = (WIDTH // 2, HEIGHT // 2)

running = True
while running:
    clock.tick(FPS)
    screen.fill(YELLOW)

    for event in py.event.get():
        if event.type == py.QUIT:
            running = False

        elif event.type == py.KEYDOWN:

            if event.key == py.K_1:
                rot_speed += 0.1
            if event.key == py.K_2:
                rot_speed += 0.2
            if event.key == py.K_3:
                rot_speed += 0.3
            if event.key == py.K_4:
                rot_speed += 0.4
            if event.key == py.K_5:
                rot_speed += 0.5
            if event.key == py.K_6:
                rot_speed += 0.6
            if event.key == py.K_7:
                rot_speed += 0.7
            if event.key == py.K_8:
                rot_speed += 0.8
            if event.key == py.K_9:
                rot_speed += 0.9

            if event.key == py.K_DOWN:
                rot_speed -= 0.1

    RPM = round(rot_speed / 0.1)

    speed = py.font.SysFont('Ariel', 38)
    vel = speed.render("RPM = " + str(RPM), True, BLACK)
    speedRect = vel.get_rect()
    speedRect.center = (WIDTH // 2, 30)
    screen.blit(vel, speedRect)

    old_center = rect.center
    rot = (rot + rot_speed) % 360

    new_image = py.transform.rotate(image_orig, rot)
    rect = new_image.get_rect()
    rect.center = old_center

    screen.blit(new_image, rect)
    py.display.flip()

py.quit()