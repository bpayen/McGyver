#! /usr/bin/env python3
# coding: utf-8

from pygame.locals import *
import pygame

from personnages import MacGyver, Guardian
from maze import Maze


class App:

	def __init__(self):

		# create graphics elements
		# Maybe not the best place for that....?!
		pygame.display.init()

		self._running = True

		# TRUE -> the game is actif and player may ... play
		self.contextGame = False

		self.initialisation()

		# Display mainn menu
		self.displayControlScreen("start")

	# Action needed to be run every new game
	def initialisation(self):

		self.MacGyver = MacGyver('ressources/MacGyver.png')

		self.MacGyver.initialisation()

		self.guardian = Guardian('ressources/Gardien.png')

		self.maze = Maze(self.MacGyver, self.guardian, self)

		self.maze.initialisation()

	def  on_execute(self):

		pygame.key.set_repeat(10,200)

		while( self._running ) :

			for event in pygame.event.get():
				if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
					self._running = False
					pygame.quit()

				if self.contextGame:
					# Maze is displayed....we are in playing context.... Hero can move into the maze

					if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
						self.maze.movePlayerDirection("UP")

					if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
						self.maze.movePlayerDirection("DOWN")

					if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
						self.maze.movePlayerDirection("LEFT")

					if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
						self.maze.movePlayerDirection("RIGHT")
				else:
					# Control screen is displayed .... 

					if event.type == pygame.KEYDOWN and event.key == pygame.K_n:
						self.contextGame = True
						self.maze.displayJeu()

					if event.type == pygame.KEYDOWN and event.key == pygame.K_f:
						# End the game, close the screen...
						self._running = False
						pygame.quit()


	# Display the control screen.
	def displayControlScreen(cls, context):

		cls.windowWidth = 300
		cls.windowHeight = 300

		# Display surface 
		cls.start_display_surf = pygame.display.set_mode((cls.windowWidth,cls.windowHeight))

		# we select the right picture depending on the program context
		if context == "start":
			# at the begenning of the game
			cls.image_base = pygame.image.load('ressources/StartScreen.png').convert()

		elif context == "win":
			# McGyver defeated the guardian 
			cls.image_base = pygame.image.load('ressources/WinScreen.png').convert()

			# guardian defeated McGyver
		elif context == "lose":
			cls.image_base = pygame.image.load('ressources/LoseScreen.png').convert()

		cls.start_display_surf.blit(cls.image_base, (0,0))
		
		pygame.display.update()

	# set program context (GAMING or CONTROL)
	def setProgramContext(self, context):
	
		if context == "GAMING" :
			self.contextGame = True
		else:
			self.contextGame = False

# ==================================================================================================
def main():
	app = App()
	app.on_execute()


if __name__ == "__main__":
	main()

