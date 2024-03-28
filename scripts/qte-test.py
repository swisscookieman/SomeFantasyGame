import pygame
import time
import sys


def qte(speed, red1, yellow1, green, yellow2, red2):
    # Initialize Pygame
    pygame.init()

    # Set the width and height of the screen (doesn't matter for keyboard input)
    screen = pygame.display.set_mode((100, 100))

    # Variable to keep track of whether space key is pressed
    space_pressed = False

    # Set up a clock to control the frame rate
    clock = pygame.time.Clock()

    meter = "["
    for i in range(red1):
        meter += "\033[91m|"
    for i in range(yellow1):
        meter += "\033[93m|"
    for i in range(green):
        meter += "\033[92m|"
    for i in range(yellow2):
        meter += "\033[93m|"
    for i in range(red1):
        meter += "\033[91m|"
    meter += "\033[0m]"

    # Set initial time
    last_print_time = time.time()
    start_time = time.time()
    print(meter)
    print(" ", end="")
    # Main loop
    running = True
    amount_printed = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Check if space key is pressed
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            space_pressed = True

        # Check if a second has elapsed since last message and print if so
        current_time = time.time()
        if current_time - last_print_time >= speed:
            print(">", end="")
            amount_printed += 1
            sys.stdout.flush()
            last_print_time = current_time
        if current_time - start_time >= (red1+yellow1+green+yellow2+red2+1)*speed:
            print("\nYou missed.")
            break

        # If space key is pressed, break out of the loop
        if space_pressed:
            print("|\n")
            if amount_printed < red1:
                return "red"
            elif amount_printed < red1+yellow1:
                return "yellow"
            elif amount_printed < red1+yellow1+green:
                return "green"
            elif amount_printed < red1+yellow1+green+yellow2:
                return "yellow"
            else:
                return "red"

        # Control the frame rate
        clock.tick(60)

    # Quit Pygame
    pygame.quit()


# Call the function to start monitoring the keyboard
print(qte(0.1, 6, 2, 2, 2, 6))
