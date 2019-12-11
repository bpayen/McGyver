#! /usr/bin/env python3
# coding: utf-8

from pygame.locals import *
import pygame
import sys

class App:

	windowWidth = 800
	windowHeight = 800


	def __init__(self):
		
		pygame.display.init()

		self.display_surf = pygame.display.set_mode((self.windowWidth,self.windowHeight))

		self.image_surf = pygame.image.load('ressources/Gardien.png').convert()


		self.display_surf.blit(self.image_surf, (0, 0))

		pygame.display.update()

		self._running = True

	def  on_execute(self):

		while( self._running ) :
			pygame.event.pump()

			keys = pygame.key.get_pressed()
			for event in pygame.event.get():
				if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
					print("DDDDD")
					self._running = False
					pygame.quit()





class Maze:

	maze = [[1,0,1,1,1],
			[1,0,0,1,1],
			[1,1,0,1,1],
			[1,1,0,0,0],
			[1,1,1,1,1]]

	def __init__(self):

		# Initialize Maze

		# Display Maze on screen

		pass
	

	def display(cls):

		for i in range(len(cls.maze)):
			for j in range(len(cls.maze[i])):
				if cls.maze[i][j] :
					print("X", end=' ')
				elif not cls.maze[i][j] :
					print(" ", end=' ')

			print()


def main():
	#maze = Maze()
	#maze.display()

	app = App()
	app.on_execute()


if __name__ == "__main__":
	main()

