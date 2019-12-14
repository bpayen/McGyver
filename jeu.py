#! /usr/bin/env python3
# coding: utf-8

from pygame.locals import *
import pygame
import sys
import random

class App:



	def __init__(self):

		self._running = True

	def  on_execute(self):

		while( self._running ) :
			pygame.event.pump()

			keys = pygame.key.get_pressed()
			for event in pygame.event.get():
				if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
					#print("DDDDD")
					self._running = False
					pygame.quit()

				if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
					print("UP")

				if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
					print("DOWN")

				if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
					print("LEFT")

				if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
					print("RIGHT")






class Maze:

	# Window size 
	windowWidth = 15 * 20 
	windowHeight = 15 * 20

	# Free case for Objects positionning
	free_case = []

	# List of Object positionning in the maze
	objects_positions = []

	# List of object's names
	objects_liste = ["Seringue", "tuyau","aiguille", "ether"]

	# Maze charte
	maze = [[1,1,0,1,1,1,1,1,1,1,1,1,1,1,1],
			[1,1,0,1,0,0,0,1,1,1,1,1,0,0,1],
			[1,1,0,0,0,1,1,0,0,0,0,0,0,1,1],
			[1,1,1,1,0,0,0,0,1,0,1,1,1,1,1],
			[1,0,0,1,0,1,1,1,1,0,0,0,0,1,1],
			[1,1,0,1,0,1,1,1,1,1,1,1,0,1,1],
			[1,0,0,0,0,0,0,0,1,0,0,0,0,0,1],
			[1,0,1,1,1,1,1,0,1,0,1,0,0,0,1],
			[1,0,0,0,0,1,1,0,1,1,1,1,0,1,1],
			[1,1,1,1,0,1,1,0,0,0,0,1,0,0,1],
			[1,0,0,0,0,1,1,0,1,1,0,1,0,1,1],
			[1,1,0,1,0,0,1,0,1,1,0,1,0,0,1],
			[1,0,0,1,1,0,1,0,0,1,0,0,0,1,1],
			[1,0,1,1,0,0,1,1,0,1,1,1,0,1,1],
			[1,1,1,1,1,1,1,1,1,1,1,1,0,1,1]]

	# coordonates of the entry point of maze
	maze_start_point = [2,0]


	def __init__(self):

		# initialize Objects spreading in the Maze
		# Constraintes : every "floor" case must be recheable
		# from the main path .... 

		# Initialize Maze

		# Display Maze on screen

		pass
	

	def display(cls):

		# coordonate of wall element in graphic file
		position_wall = ( (12 * 20, 0 ) , (20 , 20) )
		# coordonate of flor element in graphic file
		position_floor = ( (8 * 20, 40) , (20 , 20) )

		# Objects's images list
		iol = []

		# create graphics elements
		pygame.display.init()

		cls.display_surf = pygame.display.set_mode((cls.windowWidth,cls.windowHeight))

		cls.image_pavement = pygame.image.load('ressources/floor-tiles-20x20.png').convert()

		# fill Maze surface with right graphic elements
		for li in range(len(cls.maze)):
			for col in range(len(cls.maze[li])):
				if cls.maze[li][col] :
					# Wall
					cls.display_surf.blit(cls.image_pavement, (col * 20, li * 20),  position_wall )

				elif not cls.maze[li][col] :
					# Floor
					cls.display_surf.blit(cls.image_pavement, (col * 20, li * 20),  position_floor )

					# Appends the free case to le list of avelable cases for objects
					cls.free_case.append([col,li])


		# place objecys in Maze
		objects_positions = random.sample(cls.free_case, k=len(cls.objects_liste))

		# display objects on the screen...
		iol.append( pygame.transform.scale(pygame.image.load('ressources/aiguille.png').convert_alpha(), (20,20)))
		iol.append(pygame.transform.scale(pygame.image.load('ressources/ether.png').convert_alpha(), (20,20)))
		iol.append(pygame.transform.scale(pygame.image.load('ressources/seringue.png').convert_alpha(), (20,20)))
		iol.append(pygame.transform.scale(pygame.image.load('ressources/tube_plastique.png').convert_alpha(), (20,20)))

		for x in range(0,4):
			cls.display_surf.blit(iol[x], (objects_positions[x][0] * 20 , objects_positions[x][1] * 20  ) )

		pygame.display.update()


def main():
	maze = Maze()
	maze.display()

	app = App()
	app.on_execute()


if __name__ == "__main__":
	main()

