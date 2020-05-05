#Pong game from Skillshare using pyGame

from pygame import *

SCREENHEIGHT = 600
SCREENWIDTH = 900
screen = display.set_mode((SCREENWIDTH, SCREENHEIGHT))

white = (255, 255, 255)
black = (0,0,0)

player1_Y = 250
player2_Y = 250
paddle_width = 25
paddle_height = 100

ball_x = 450
ball_y = 300

ball_dx = 4
ball_dy = 3

running = True
myClock = time.Clock()
while running:
    for evt in event.get():
        if evt.type == QUIT:
            running = False
    player1_paddle = Rect(30, player1_Y, paddle_width, paddle_height)
    player2_paddle = Rect(850, player2_Y, paddle_width, paddle_height)
    ball = Rect(ball_x, ball_y, 15, 15)

    keys = key.get_pressed()

    if (keys[K_w] and player1_Y > 0):
        player1_Y -= 10
    elif (keys[K_s] and player1_Y+paddle_height < SCREENHEIGHT ):
        player1_Y += 10
    if (keys[K_UP] and player2_Y > 0):
        player2_Y -= 10
    elif (keys[K_DOWN] and player2_Y+paddle_height < SCREENHEIGHT ):
        player2_Y += 10

    ball_x += ball_dx
    ball_y += ball_dy
    if (ball.colliderect(player1_paddle)):
        ball_dx = abs(ball_dx)
    elif (ball.colliderect(player2_paddle)):
        ball_dx = abs(ball_dx) * -1
    elif (ball_y <= 0):
        ball_dy = abs(ball_dy)
    elif (ball_y >= SCREENHEIGHT):
        ball_dy = abs(ball_dy) * -1

    screen.fill(black)
    draw.circle(screen, white, (ball_x, ball_y), 10, 1)
    draw.rect(screen,white, ball)
    draw.rect(screen, white, player1_paddle)
    draw.rect(screen, white, player2_paddle)
    display.flip()
    myClock.tick(60)

quit()
