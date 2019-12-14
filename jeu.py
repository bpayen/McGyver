#! /usr/bin/env python3
# coding: utf-8

from pygame.locals import *
import pygame
import sys
import random
import pandas as pd

class App:



	def __init__(self):

		self._running = True
		self.maze = Maze()

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
					self.maze.movePlayerDirection("UP")

				if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
					print("DOWN")
					self.maze.movePlayerDirection("DOWN")

				if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
					print("LEFT")
					self.maze.movePlayerDirection("LEFT")

				if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
					print("RIGHT")
					self.maze.movePlayerDirection("RIGHT")



class McGyver:

	alive = True

	objectList = []

	def move(self,x,y):
		pass



class Maze:

	# Window size 
	windowWidth = 15 * 20 
	windowHeight = 15 * 20

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

	pd_maze = None

	# coordonates of the entry point of (X / Y) maze plannar coordonate -> NOT in Matrice !
	maze_start_point = [2,0]

	# Free case for Objects positionning
	free_case = []

	# List of Object positionning in the maze
	objects_positions = []

	# List of object's names
	objects_list = ["Seringue", "tuyau","aiguille", "ether"]


	# player position 
	player_position = maze_start_point

	# Gauradian position 
	gardian_position = []


	def __init__(self):

		self.pd_maze  = pd.DataFrame(self.maze)
		# print(self.pd_maze)

		# print(self.pd_maze.iloc[0, 0:])
		# print(self.pd_maze.iloc[1])
		# print(self.pd_maze.iloc[2])


		#print( pd_maze.iloc[0, 1])
		# initialize Objects spreading in the Maze
		# Constraintes : every "floor" case must be recheable
		# from the main path .... 

		# Initialize Maze

		# Display Maze on screen

		pass
	
	# return object's name at the position
	# or retrun empty string
	def getObjectAt(cls, x, y):
		index = cls.objects_positions.index([x,y]) 
		if index >= 0:
			return cls.objects_list[index]
		else:
			return ""

	# Display the Maze and the objects...
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
		cls.objects_positions = random.sample(cls.free_case, k=len(cls.objects_list))

		# display objects on the screen...
		iol.append( pygame.transform.scale(pygame.image.load('ressources/aiguille.png').convert_alpha(), (20,20)))
		iol.append(pygame.transform.scale(pygame.image.load('ressources/ether.png').convert_alpha(), (20,20)))
		iol.append(pygame.transform.scale(pygame.image.load('ressources/seringue.png').convert_alpha(), (20,20)))
		iol.append(pygame.transform.scale(pygame.image.load('ressources/tube_plastique.png').convert_alpha(), (20,20)))

		for x in range(0,4):
			cls.display_surf.blit(iol[x], (cls.objects_positions[x][0] * 20 , cls.objects_positions[x][1] * 20  ) )

		pygame.display.update()

	# return TRUE if the posotion is not Wall
	def isXYPositionPossible(cls,x,y):
		# use of NOT as a wall is "1" and "floor" is "0"...the opisite 
		# af the question ...
		print("X :" + str(x) + " Y:" + str(y), end=" ")
		print(cls.pd_maze.iloc[ y , x ])
		print(cls.pd_maze.iloc[ y , 0: ] )


		if ( y < 0 ) :
			return False

		if ( y > len(Maze.maze) ) :
			return False

		if ( cls.pd_maze.iloc[ y , x ] == 0 ):
			return True

		if ( cls.pd_maze.iloc[ y , x ] == 1 ):
			return False

	# return TRUE if the guardian is at the position
	def isXYPositionIsGuardian(cls,x,y):	
		#return cls.gardian_position[x][y]
		pass

	# Moves Player in the Maze
	def movePlayerDirection(cls, direction):

		# print("Direction =" + direction )
		# print(cls.player_position)
		# print(cls.isPositionFree( cls.player_position[0] , cls.player_position[1] + 1 ))

		if direction == "UP" :
			if cls.isXYPositionPossible( cls.player_position[0], cls.player_position[1] - 1) :
				cls.player_position = [ cls.player_position[0], cls.player_position[1] - 1]
				print("Move UP", end=" ")
				print(cls.player_position)

		if direction == "DOWN" :
			if cls.isXYPositionPossible( cls.player_position[0], cls.player_position[1] + 1) :
				cls.player_position = [ cls.player_position[0], cls.player_position[1] + 1]
				print("Move DOWN", end=" ")
				print(cls.player_position)

		if direction == "RIGHT" :
			if cls.isXYPositionPossible( cls.player_position[0] + 1, cls.player_position[1]) :
				cls.player_position = [ cls.player_position[0] + 1, cls.player_position[1] ]
				print("Move RIGHT", end=" ")
				print(cls.player_position)

		if direction == "LEFT" :
			if cls.isXYPositionPossible( cls.player_position[0] - 1, cls.player_position[1]) :
				cls.player_position = [ cls.player_position[0] - 1, cls.player_position[1] ]
				print("Move LEFT", end=" ")
				print(cls.player_position)
	

def main():
	maze = Maze()
	maze.display()

	app = App()
	app.on_execute()


if __name__ == "__main__":
	main()

