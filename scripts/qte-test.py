from AppKit import NSEvent

import pygame
import time
import sys

easy_meter = "[\033[91m||||\033[93m||||\033[92m||||\033[93m||||\033[91m||||\033[0m]"
med_meter = "[\033[91m|||||\033[93m||\033[92m||\033[93m||\033[91m|||||\033[0m]"
hard_meter = "[\033[91m|||||\033[93m|||\033[92m|\033[93m|||\033[91m|||||\033[0m]"


def qte_easy(speed):
    # Initialize Pygame
    pygame.init()

    # Set the width and height of the screen (doesn't matter for keyboard input)
    screen = pygame.display.set_mode((100, 100))

    # Variable to keep track of whether space key is pressed
    space_pressed = False

    # Set up a clock to control the frame rate
    clock = pygame.time.Clock()

    # Set initial time
    last_print_time = time.time()
    start_time = time.time()
    print(easy_meter)
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
        if current_time - start_time >= 22*speed:
            print("\nYou missed.")
            break

        # If space key is pressed, break out of the loop
        if space_pressed:
            print("|\n")
            if amount_printed < 4:
                return "red"
            elif amount_printed < 8:
                return "yellow"
            elif amount_printed < 12:
                return "green"
            elif amount_printed < 16:
                return "yellow"
            else:
                return "red"

        # Control the frame rate
        clock.tick(60)

    # Quit Pygame
    pygame.quit()


def qte_med(speed):
    # Initialize Pygame
    pygame.init()

    # Set the width and height of the screen (doesn't matter for keyboard input)
    screen = pygame.display.set_mode((100, 100))

    # Variable to keep track of whether space key is pressed
    space_pressed = False

    # Set up a clock to control the frame rate
    clock = pygame.time.Clock()

    # Set initial time
    last_print_time = time.time()
    start_time = time.time()
    print(med_meter)
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
        if current_time - start_time >= 17*speed:
            print("\nYou missed.")
            break

        # If space key is pressed, break out of the loop
        if space_pressed:
            print("|\n")
            if amount_printed < 5:
                return "red"
            elif amount_printed < 7:
                return "yellow"
            elif amount_printed < 9:
                return "green"
            elif amount_printed < 11:
                return "yellow"
            else:
                return "red"

        # Control the frame rate
        clock.tick(60)

    # Quit Pygame
    pygame.quit()


def qte_hard(speed):
    # Initialize Pygame
    pygame.init()

    # Set the width and height of the screen (doesn't matter for keyboard input)
    screen = pygame.display.set_mode((100, 100))

    # Variable to keep track of whether space key is pressed
    space_pressed = False

    # Set up a clock to control the frame rate
    clock = pygame.time.Clock()

    # Set initial time
    last_print_time = time.time()
    start_time = time.time()
    print(hard_meter)
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
        if current_time - start_time >= 22*speed:
            print("\nYou missed.")
            break

        # If space key is pressed, break out of the loop
        if space_pressed:
            print("|\n")
            if amount_printed < 5:
                return "red"
            elif amount_printed < 8:
                return "yellow"
            elif amount_printed < 9:
                return "green"
            elif amount_printed < 12:
                return "yellow"
            else:
                return "red"

        # Control the frame rate
        clock.tick(60)

    # Quit Pygame
    pygame.quit()


# Call the function to start monitoring the keyboard
print(qte_med(0.1))
