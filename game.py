import pygame
import random

from Shared import *
from Car import Car
from Stripes import Stripes


pygame.init()


# def check_collision(player_x, player_y, player_width, player_height, car_x, car_y, car_width, car_height):
#     if (player_x+player_width > car_x) and (player_x < car_x+car_width) and (player_y < car_y+car_height) and (player_y+player_height > car_y):
#         return True
#     else:
#         return False


# Set the width and height of the window [width, height]
size = (WINDOW_WIDTH, WINDOW_HIEGHT)
window = pygame.display.set_mode(size)

pygame.display.set_caption("RACING")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the window updates
clock = pygame.time.Clock()

# Create a player car object
player = Car(175, 475, 0, 0, 70, 130, RED)
player.load_image("car.png")

collision = True

# Store the score
# score = 0

# # Load the fonts
# font_40 = pygame.font.SysFont("Arial", 40, True, False)
# font_30 = pygame.font.SysFont("Arial", 30, True, False)
# text_title = font_40.render("Ride the Road", True, TEXT_COLOR)
# text_ins = font_30.render("Click to Play!", True, TEXT_COLOR)


# def draw_main_menu():
#     window.blit(text_title, [size[0] / 2 - 106, size[1] / 2 - 100])
#     score_text = font_40.render("Score: " + str(score), True, TEXT_COLOR)
#     window.blit(score_text, [size[0] / 2 - 70, size[1] / 2 - 30])
#     window.blit(text_ins, [size[0] / 2 - 85, size[1] / 2 + 40])
#     pygame.display.flip()


# Setup the enemy cars
# cars = []
# car_count = 2
# for i in range(car_count):
#     x = random.randrange(0, 340)
#     car = Car(x, random.randrange(-150, -50), 0, random.randint(5, 10), 60, 60, CAR_COLOR)
#     cars.append(car)


# Setup the stripes.
stripe_width = 20
stripe_x = WINDOW_WIDTH / 2 - stripe_width / 2
stripes = Stripes(x=stripe_x)
stripes.build()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        # Reset everything when the user starts the game.
        # if collision and event.type == pygame.MOUSEBUTTONDOWN:
        #     collision = False
            # for i in range(car_count):
            #     cars[i].y = random.randrange(-150, -50)
            #     cars[i].x = random.randrange(0, 350)
            # player.x = 175
            # player.dx = 0
            # score = 0
            # pygame.mouse.set_visible(False)

        # if not collision:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player.dx = 4
            elif event.key == pygame.K_LEFT:
                player.dx = -4
            elif event.key == pygame.K_UP:
                player.dy = -4
            elif event.key == pygame.K_DOWN:
                player.dy = 4

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.dx = 0
            elif event.key == pygame.K_RIGHT:
                player.dx = 0
            elif event.key == pygame.K_UP:
                player.dy = 0
            elif event.key == pygame.K_DOWN:
                player.dy = 0

    # --- Game logic should go here

    # --- window-clearing code goes here
    window.fill(GRAY)

    # --- Drawing code should go here
    # if not collision:
    # Draw the stripes

    for stripe in stripes.get():
        pygame.draw.rect(window, WHITE, stripe)
    
    stripes.move()
    player.draw_image(window)
    player.move_x()
    player.move_y()
    player.check_out_of_window()

    # # Check if the enemy cars move out of the window.
    # for i in range(car_count):
    #     cars[i].draw_rect()
    #     cars[i].y += cars[i].dy
    #     if cars[i].y > size[1]:
    #         score += 10
    #         cars[i].y = random.randrange(-150, -50)
    #         cars[i].x = random.randrange(0, 340)
    #         cars[i].dy = random.randint(4, 9)

    # # Check the collision of the player with the car
    # for i in range(car_count):
    #     if check_collision(player.x, player.y, player.width, player.height, cars[i].x, cars[i].y, cars[i].width, cars[i].height):
    #         collision = True
    #         pygame.mouse.set_visible(True)
    #         break

    # Draw the score.
    # txt_score = font_30.render("Score: "+str(score), True, WHITE)
    # window.blit(txt_score, [15, 15])

    pygame.display.flip()
    # else:
    #     draw_main_menu()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
