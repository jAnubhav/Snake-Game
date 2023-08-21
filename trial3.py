import pygame
from pygame import display, draw, event, time
from random import randrange

pygame.init()

win = display.set_mode((404, 504))
win.fill("white")
display.set_caption("Snake Game")

change = [0, 0]
snake = [[randrange(2, 400, 25), randrange(2, 500, 25)]]
while True:
    food = [randrange(2, 400, 25), randrange(2, 500, 25)]
    if food not in snake:
        break

status = True
while status:
    draw.rect(win, "black", pygame.Rect(2, 2, 400, 500))
    draw.rect(win, "dark green", pygame.Rect(snake[-1][0], snake[-1][1], 25, 25))
    draw.rect(win, "green", pygame.Rect(snake[-1][0]+4, snake[-1][1]+4, 17, 17))
    for i in range(len(snake)-1):
        draw.rect(win, "blue", pygame.Rect(snake[i][0]+1, snake[i][1]+1, 23, 23), border_radius=3)
        draw.rect(win, "cyan", pygame.Rect(snake[i][0]+4, snake[i][1]+4, 17, 17), border_radius=3)

    draw.rect(win, "orange", pygame.Rect(food[0], food[1], 25, 25))
    draw.rect(win, "yellow", pygame.Rect(food[0]+4, food[1]+4, 17, 17))
    display.update()

    for events in event.get():
        if events.type == pygame.QUIT:
            status = False
        if events.type == pygame.KEYDOWN:
            if events.key == pygame.K_UP:
                if change != [0, 25]:
                    change[0], change[1] = 0, -25
            if events.key == pygame.K_DOWN:
                if change != [0, -25]:
                    change[0], change[1] = 0, 25
            if events.key == pygame.K_LEFT:
                if change != [25, 0]:
                    change[0], change[1] = -25, 0
            if events.key == pygame.K_RIGHT:
                if change != [-25, 0]:
                    change[0], change[1] = 25, 0
    
    if food in snake:
        snake.insert(0, snake[0])
        while True:
            food = [randrange(2, 400, 25), randrange(2, 500, 25)]
            if food not in snake:
                break

    snake.append([snake[-1][0]+change[0], snake[-1][1]+change[1]])
    del snake[0]

    if snake[-1][0] > 400 or snake[-1][0] < 0 or snake[-1][1] > 500 or snake[-1][1] < 0 or snake[-1] in snake[0:len(snake)-1]:
        status = False

    time.delay(250)
pygame.quit()