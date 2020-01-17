#! /usr/bin/env python3
# coding: utf-8

from pygame.locals import *
import pygame

from personnages import MacGyver, Guardian
from maze import Maze

""" The application aim to control the program flow.
It listen to the user's key strokes and dispatch them
to the right object.
It instantiate all program objects and initialise them when
needed.
"""
class App:
    def __init__(self):

        # create graphics elements
        # Maybe not the best place for that....?!
        pygame.display.init()

        self._running = True

        # TRUE -> the game is actif and player may ... play
        self._context_game = False

        self.initialisation()

        # Display main menu
        self.display_control_screen("start")

    """ Realizes actions needed to be run before every new game.
    """
    def initialisation(self):

        self._mac_gyver = MacGyver("ressources/MacGyver.png")

        self._mac_gyver.initialisation()

        self._guardian = Guardian("ressources/Gardien.png")

        self.maze = Maze(self._mac_gyver, self._guardian, self)

        self.maze.initialisation()

    """ Listenes to the user's keyboard input and dispatches 
    it to the right part of the program.
    """
    def on_execute(self):

        pygame.key.set_repeat(10, 200)

        while self._running:

            for event in pygame.event.get():

                if event.type == pygame.QUIT or (
                    event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
                ):
                    self._running = False
                    pygame.quit()

                if self._context_game:
                    # Maze is displayed....we are in playing context.... Hero can move into the maze

                    if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                        self.maze.move_player_direction("UP")

                    if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                        self.maze.move_player_direction("DOWN")

                    if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                        self.maze.move_player_direction("LEFT")

                    if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                        self.maze.move_player_direction("RIGHT")
                else:
                    # Control screen is displayed ....

                    if event.type == pygame.KEYDOWN and event.key == pygame.K_n:
                        self._context_game = True
                        self.maze.display_jeu()

                    if event.type == pygame.KEYDOWN and event.key == pygame.K_f:
                        # End the game, close the screen...
                        self._running = False
                        pygame.quit()

    """ Display the control screen.
    The control screen is used to ask the user if he wants to start a game,
    or if he wantes to stop the game.
    """
    def display_control_screen(self, context):

        self._window_width = 300
        self._window_height = 300

        # Display surface
        self.start_display_surf = pygame.display.set_mode(
            (self._window_width, self._window_height)
        )

        # we select the right picture depending on the program context
        if context == "start":
            # at the begenning of the game
            self.image_base = pygame.image.load("ressources/StartScreen.png").convert()

        elif context == "win":
            # McGyver defeated the guardian
            self.image_base = pygame.image.load("ressources/WinScreen.png").convert()

            # guardian defeated McGyver
        elif context == "lose":
            self.image_base = pygame.image.load("ressources/LoseScreen.png").convert()

        self.start_display_surf.blit(self.image_base, (0, 0))

        pygame.display.update()

    """ Toggle the program context in the right mode according to the function 
    parameter.
    """

    def set_program_context(self, context):

        if context == "GAMING":
            self._context_game = True
        else:
            self._context_game = False


# ============================================================================
def main():
    app = App()
    app.on_execute()


if __name__ == "__main__":
    main()
