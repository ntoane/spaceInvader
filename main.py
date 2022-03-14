import pygame
import random

# Initialize the pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption("Space Invaders")
# 32 Pixel PNG image recommended
icon = pygame.image.load("images/icon.png")
pygame.display.set_icon(icon)

# Add the player image and position it on the screen
playerImg = pygame.image.load("images/player.png")
playerX = 370
playerY = 480
playerX_change = 0

# Enemy image
enemyImg = pygame.image.load("images/enemy.png")
enemyX = random.randint(0, 736)
enemyY = random.randint(50, 150)
enemyX_change = 0


# Function to draw (using blit function) image on the screen
def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y):
    screen.blit(enemyImg, (enemyX, enemyY))


def playerBoundary():
    global playerX
    global playerY
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:  # Cater for size of the player image
        playerX = 736


# Loop of the Game, main logic
windowRunning = True
while windowRunning:  # we can access QUIT event when the window is running
    # Background colour
    screen.fill((0, 0, 0))

    # Access a QUIT event and close the window when it is clicked
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Change the boolean to false so that the while loop can stop
            windowRunning = False

        # If keystroke is pressed check whether it is left or right keystroke
        if event.type == pygame.KEYDOWN:  # if any keystroke is pressed down
            if event.key == pygame.K_LEFT:  # then if the key is LEFT arrow, move player to Left by 0.1
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:  # then if the key is RIGHT arrow, move player to Right by 0.1
                playerX_change = 0.3

        if event.type == pygame.KEYUP:  # if any keystroke pressed is released
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                # When either Left or Right key released, stop the X coordinate and maintain that position
                playerX_change = 0

    # After filling the screen with background color, draw the player image
    playerX += playerX_change  # Change the X coordinate
    playerBoundary()  # Apply boundaries accordingly
    player(playerX, playerY)
    enemy(enemyX, enemyY)

    pygame.display.update()

    # Ended at 53:00 minutes
