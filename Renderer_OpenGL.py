from pickle import TRUE
import pygame
from pygame.locals import *

from shaders import *

from gl import Renderer, Model

from math import cos, sin, radians

width = 960
height = 540

deltaTime = 0.0

pygame.init()

screen = pygame.display.set_mode((width, height), pygame.OPENGL | pygame.DOUBLEBUF)
clock = pygame.time.Clock()

rend = Renderer(screen)

rend.setShaders(vertex_shader, fragment_shader)


rend.target.z = -16

face = Model("heli.obj", "Skull.bmp")

face.position.z -= 13
face.scale.x = 0.1
face.scale.y = 0.1
face.scale.z = 0.1


rend.scene.append( face )


isRunning = True

while isRunning:

    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                isRunning = False

            elif event.key == pygame.K_z:
                rend.filledMode()
            elif event.key == pygame.K_x:
                rend.wireframeMode()
            elif event.key == pygame.K_1:
                rend.setShaders(still_shader, toonshader)
            elif event.key == pygame.K_2:
                rend.setShaders(still_shader, funBlue_shader)
            elif event.key == pygame.K_3:
                rend.setShaders(vertex_shader, colorExplotion_shader)

    if keys[K_q]:
        if rend.camDistance > 2:
            rend.camDistance -= 2 * deltaTime
    elif keys[K_e]:
        if rend.camDistance < 10:
            rend.camDistance += 2 * deltaTime

    if keys[K_a]:
        rend.angle -= 30 * deltaTime
    elif keys[K_d]:
        rend.angle += 30 * deltaTime


    if keys[K_w]:
        if rend.camPosition.y < 2:
            rend.camPosition.y += 5 * deltaTime
    elif keys[K_s]:
        if rend.camPosition.y > -2:
            rend.camPosition.y -= 5 * deltaTime


    rend.target.y = rend.camPosition.y

    rend.camPosition.x = rend.target.x + sin(radians(rend.angle)) * rend.camDistance
    rend.camPosition.z = rend.target.z + cos(radians(rend.angle)) * rend.camDistance
    
    if keys[K_LEFT]:
        rend.pointLight.x -= 10 * deltaTime
    elif keys[K_RIGHT]:
        rend.pointLight.x += 10 * deltaTime
    elif keys[K_UP]:
        rend.pointLight.y += 10 * deltaTime
    elif keys[K_DOWN]:
        rend.pointLight.y -= 10 * deltaTime


    deltaTime = clock.tick(60) / 1000
    rend.time += deltaTime

    rend.update()
    rend.render()
    pygame.display.flip()

pygame.quit()
