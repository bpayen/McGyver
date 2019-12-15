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

		self.MacGyver = MacGyver()

		self.maze = Maze(self.MacGyver)

		self.maze.display()


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


class MacGyver:

	alive = True

	objectList = []

	photoPath = 'ressources/MacGyver.png'

	def __init__(cls):

	# def move(self,x,y):
		pass

	def getPhotoPath(cls):
		return cls.photoPath

	def addObjectToList(cls, objectName):
		objectList.append(objectName)

	def getObjectNumber(self):
		return len(objectList)


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

	# coordonates of the entry point of (X / Y) maze plannar coordonate -> NOT Matrice Coordinate !
	maze_start_point = [2,0]

	# Floor case for Objects positionning
	free_case = []

	# List of Object positionning in the maze
	objects_positions = []

	# List of object's names
	objects_list = ["Seringue", "tuyau","aiguille", "ether"]

	# player position 
	player_position = None

	# Gauradian position 
	gardian_position = []

	# Maze Backgroung, to restore picture part after player move
	background_display_surf = None


	def __init__(self, mcGyver):

		self.pd_maze = pd.DataFrame(self.maze)

		self.player_position = self.maze_start_point

		self.McGyver = mcGyver

		# print(self.pd_maze)

		# print(self.pd_maze.iloc[0, 0:])
		# print(self.pd_maze.iloc[1])
		# print(self.pd_maze.iloc[2])


		# print( pd_maze.iloc[0, 1] )
		# initialize Objects spreading in the Maze
		# Constraintes : every "floor" case must be recheable
		# from the main path .... 

		# Initialize Maze

		# Display Maze on screen
	
	# return object's name at the position
	# or retrun empty string
	def getObjectAt(cls, x_y):
		index = cls.objects_positions.index() 
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

		# Surafce de travail
		cls.display_surf = pygame.display.set_mode((cls.windowWidth,cls.windowHeight))
		
		# Surface Background de sauvegarde, pour les restaurations
		# après mouvement du player
		cls.background_display_surf = pygame.Surface((cls.windowWidth,cls.windowHeight))

		cls.image_pavement = pygame.image.load('ressources/floor-tiles-20x20.png').convert()

		# fill Maze surface with right graphic elements
		for li in range(len(cls.maze)):
			for col in range(len(cls.maze[li])):
				if cls.maze[li][col] :
					# Wall
					cls.background_display_surf.blit(cls.image_pavement, (col * 20, li * 20),  position_wall )

				elif not cls.maze[li][col] :
					# Floor
					cls.background_display_surf.blit(cls.image_pavement, (col * 20, li * 20),  position_floor )

					# Appends the free case to le list of avelable cases for objects
					cls.free_case.append([col,li])

		
		cls.display_surf.blit(cls.background_display_surf, (0,0))

		# get randoms objects list
		cls.objects_positions = random.sample(cls.free_case, k=len(cls.objects_list))

		# display objects on the screen...
		iol.append(pygame.transform.scale(pygame.image.load('ressources/aiguille.png').convert(), (20,20)))
		iol.append(pygame.transform.scale(pygame.image.load('ressources/ether.png').convert_alpha(), (20,20)))
		iol.append(pygame.transform.scale(pygame.image.load('ressources/seringue.png').convert_alpha(), (20,20)))
		iol.append(pygame.transform.scale(pygame.image.load('ressources/tube_plastique.png').convert_alpha(), (20,20)))

		for x in range(0,4):
			cls.display_surf.blit(iol[x], (cls.objects_positions[x][0] * 20 , cls.objects_positions[x][1] * 20  ) )

		# Display McGyver in le Lab, with right size image
		cls.photoPath = cls.McGyver.getPhotoPath()
		cls.PlayerPicture = pygame.transform.scale( pygame.image.load( cls.photoPath  ).convert_alpha(), (20,20))
		cls.display_surf.blit( cls.PlayerPicture , (cls.player_position[0] * 20 , cls.player_position[1] * 20  ) ) 
		
		pygame.display.update()

	def restoreBackground(cls):
		cls.display_surf.blit( cls.background_display_surf, (0,0) )
		pygame.display.update()


	# return TRUE if the posotion is not Wall
	def isXYPositionPossible(cls,x,y):
		# use of NOT as a wall is "1" and "floor" is "0"...the opisite 
		# af the question ...
		print("X :" + str(x) + " Y:" + str(y), end=" ") # DEBUG
		print(cls.pd_maze.iloc[ y , x ])  # DEBUG
		print(cls.pd_maze.iloc[ y , 0: ] ) # DEBUG

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

		if direction == "UP" :
			if cls.isXYPositionPossible( cls.player_position[0], cls.player_position[1] - 1) :
				cls.player_position = [ cls.player_position[0], cls.player_position[1] - 1]
				#getObjectAt(cls.player_position)
				print("Move UP", end=" ") # DEBUG
				print(cls.player_position) # DEBUG

		if direction == "DOWN" :
			if cls.isXYPositionPossible( cls.player_position[0], cls.player_position[1] + 1) :
				cls.player_position = [ cls.player_position[0], cls.player_position[1] + 1]
				print("Move DOWN", end=" ") # DEBUG
				print(cls.player_position) # DEBUG

		if direction == "RIGHT" :
			if cls.isXYPositionPossible( cls.player_position[0] + 1, cls.player_position[1]) :
				cls.player_position = [ cls.player_position[0] + 1, cls.player_position[1] ]
				print("Move RIGHT", end=" ") # DEBUG
				print(cls.player_position) # DEBUG

		if direction == "LEFT" :
			if cls.isXYPositionPossible( cls.player_position[0] - 1, cls.player_position[1]) :
				cls.player_position = [ cls.player_position[0] - 1, cls.player_position[1] ]
				print("Move LEFT", end=" ") # DEBUG
				print(cls.player_position) # DEBUG

	

def main():
	# maze = Maze()
	# maze.display()

	app = App()
	app.on_execute()



if __name__ == "__main__":
	main()

