#! /usr/bin/env python3
# coding: utf-8

from pygame.locals import *
import pygame
import sys
import random
import pandas as pd
import json


class App:



	def __init__(self):


		# create graphics elements
		# Move... later....
		pygame.display.init()

		self._running = True

		# TRUE -> the game is actif and player may ... play
		self.contextGame = False

		self.initialisation()

		#Self.maze.displayJeu()

		self.displayControlScreen("start")


	def initialisation(self):

		self.MacGyver = MacGyver('ressources/MacGyver.png')

		self.MacGyver.initialisation()

		self.guardian = Guardian('ressources/Gardien.png')

		# self.EcranBase = MacGyver('ressources/EcranBase.png')

		# self.EcranGagne = MacGyver('ressources/EcranGagne.png')

		# self.EcranPerdu = MacGyver('ressources/EcranPerdu.png')

		self.maze = Maze(self.MacGyver, self.guardian, self)

		self.maze.initialisation()




	def  on_execute(self):

		while( self._running ) :
			pygame.event.pump()

			keys = pygame.key.get_pressed()
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




	# Display the start screen 
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

		# if context == "start"
		# 	cls.image_base = pygame.image.load('ressources/EcranBase.png').convert()

		cls.start_display_surf.blit(cls.image_base, (0,0))
		
		pygame.display.update()


	# set program context (GAMING or CONTROL)
	def setProgramContext(self, context):
	
		if context == "GAMING" :
			self.contextGame = True
		else:
			self.contextGame = False



class Personnage:

	position = None

	photoPath = None

	def __init__(cls, photoPath ):
		cls.photoPath = photoPath

	def getPhotoPath(cls):
		return cls.photoPath


class MacGyver(Personnage):

	alive = True

	objectList = []

	#photoPath = 'ressources/MacGyver.png'

	def __init__(cls, photoPath):
		super().__init__( photoPath )
		cls.initialisation()

	def addObjectToList(cls, objectName):
		if (  objectName is not None and objectName != "") :
			cls.objectList.append(objectName)

	def getObjectNumber(cls):
		return len(cls.objectList)

	def initialisation(cls):
		cls.objectList = []

	def killMacGyver(cls):
		cls.alive = False


class Guardian(Personnage):

	#photoPath = 'ressources/MacGyver.png'

	def __init__(cls, photoPath):
		super().__init__(photoPath)


class Maze:

	# Window size 
	windowWidth = 15 * 20 
	windowHeight = 15 * 20

	# Maze scheme
	#maze = None
	maze = [
			[1,1,'S',1,1,1,1,1,1,1,1,1,1,1,1],
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
			[1,1,1,1,1,1,1,1,1,1,1,1,'E',1,1]
			]

	# Maze in Pandas (cartesian...) coordinates... 
	pd_maze = None

	# coordinates of the entry/ending point of (X / Y) maze plannar coordinates -> NOT Matrice Coordinates !
	# maze_start_point = [2,0]
	# maze_end_point = [12,14]
	maze_start_point = []
	maze_end_point = []

	# Floor case for Objects positionning
	free_case = []

	# List of Object positionning in the maze
	objects_positions = []

	# List of object's names
	number_of_initial_objects_list = 0

	# List of object's names
	#available_objects_list = ["seringue", "tuyau", "aiguille", "ether"] 
	available_objects_list = [] 

	# player .... him-self
	player = None

	# player position 
	player_position = None

	# player picture
	player_picture = None

	# guardina .... him-self
	guardian = None

	# guardian position 
	guardian_picture = None

	# Guaradian position 
	guardian_position = []

	# Maze Backgroung, to restore picture part after player move
	background_display_surf = None


	def __init__(self, player, guardian, application ):

		# Construct Pandas structure (easier to use with cartesian coordinates...)
		self.pd_maze = pd.DataFrame(self.maze)

		# Player ....
		self.player = player
		#self.player_position = self.maze_start_point

		# Guardian ....
		self.guardian = guardian
		#self.guardian_position = self.maze_end_point

		#self.number_of_initial_objects_list = len ( self.available_objects_list )

		self.application = application

		#self.initialisation()

		#print(self.guardian_position) # DEBUG

		# Load the Maze's scheme...
		#self.maze = self.loadMazeScheme()

		# initialize Objects spreading in the Maze
		# Constraintes : every "floor" case must be recheable
		# from the main path .... 

		# Initialize Maze

		# Display Maze on screen

	# Initialisation of variables that
	# needs to be set at every new game starting.
	def initialisation(self):
		self.available_objects_list = ["seringue", "tuyau", "aiguille", "ether"] 
		self.number_of_initial_objects_list = len ( self.available_objects_list )
	

	# Load Maze structure definition file
	def loadMazeScheme(self):
		 
		# return [
		# 	[1,1,0,1,1,1,1,1,1,1,1,1,1,1,1],
		# 	[1,1,0,1,0,0,0,1,1,1,1,1,0,0,1],
		# 	[1,1,0,0,0,1,1,0,0,0,0,0,0,1,1],
		# 	[1,1,1,1,0,0,0,0,1,0,1,1,1,1,1],
		# 	[1,0,0,1,0,1,1,1,1,0,0,0,0,1,1],
		# 	[1,1,0,1,0,1,1,1,1,1,1,1,0,1,1],
		# 	[1,0,0,0,0,0,0,0,1,0,0,0,0,0,1],
		# 	[1,0,1,1,1,1,1,0,1,0,1,0,0,0,1],
		# 	[1,0,0,0,0,1,1,0,1,1,1,1,0,1,1],
		# 	[1,1,1,1,0,1,1,0,0,0,0,1,0,0,1],
		# 	[1,0,0,0,0,1,1,0,1,1,0,1,0,1,1],
		# 	[1,1,0,1,0,0,1,0,1,1,0,1,0,0,1],
		# 	[1,0,0,1,1,0,1,0,0,1,0,0,0,1,1],
		# 	[1,0,1,1,0,0,1,1,0,1,1,1,0,1,1],
		# 	[1,1,1,1,1,1,1,1,1,1,1,1,0,1,1]
		# 	]
		pass

	# return object's name at the position
	# or retrun empty string
	def getObjectAt(cls, x_y): 
		try:
			index = cls.objects_positions.index( x_y ) 
			# OK.... there is an object at position....
			# Remove it from le liste before returning it 
			# to caller...
			cls.objects_positions.remove( x_y ) 
			object_to_return = cls.available_objects_list[index]
			del cls.available_objects_list[index]
			return object_to_return
		except ValueError:
			return ""

	# Display the Maze and the objects...
	def displayJeu(cls):

		# coordonate of wall element in graphic file
		position_wall = ( (12 * 20, 0 ) , (20 , 20) )
		# coordonate of flor element in graphic file
		position_floor = ( (8 * 20, 40) , (20 , 20) )

		# Objects's images list
		iol = []

		# create graphics elements
		#pygame.display.init()

		# Display surface 
		cls.display_surf = pygame.display.set_mode((cls.windowWidth,cls.windowHeight))
		
		# Background Surface de sauvegarde, pour les restaurations
		# après mouvement du player
		cls.background_display_surf = pygame.Surface((cls.windowWidth,cls.windowHeight))

		cls.image_pavement = pygame.image.load('ressources/floor-tiles-20x20.png').convert()

		# fill Maze surface with right graphic elements
		for li in range(len(cls.maze)):
			for col in range(len(cls.maze[li])):
				
				#Automatic detection of START/END of maze...
				if cls.maze[li][col] == 'S':
					cls.maze_start_point = [col,li]
					cls.player_position = cls.maze_start_point
					cls.background_display_surf.blit(cls.image_pavement, (col * 20, li * 20),  position_floor )
					continue

				if cls.maze[li][col] == 'E':
					cls.maze_end_point = [col,li]
					cls.guardian_position = cls.maze_end_point
					cls.background_display_surf.blit(cls.image_pavement, (col * 20, li * 20),  position_floor )
					continue		

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
		try:
			cls.free_case.remove( cls.maze_start_point ) # No object on Maze's starting point 
		except:
			pass

		try:
			cls.free_case.remove( cls.maze_end_point ) # No object on Maze's ending point 
		except:
			pass

		cls.objects_positions = random.sample(cls.free_case, k=len(cls.available_objects_list))

		# display objects on the screen...
		iol.append(pygame.transform.scale(pygame.image.load('ressources/aiguille.png').convert(), (20,20)))
		iol.append(pygame.transform.scale(pygame.image.load('ressources/ether.png').convert_alpha(), (20,20)))
		iol.append(pygame.transform.scale(pygame.image.load('ressources/seringue.png').convert_alpha(), (20,20)))
		iol.append(pygame.transform.scale(pygame.image.load('ressources/tube_plastique.png').convert_alpha(), (20,20)))

		for x in range(0,4):
			cls.display_surf.blit(iol[x], ( cls.objects_positions[x][0] * 20 , cls.objects_positions[x][1] * 20  ) )

		# Display McGyver in le Lab, with right size image
		cls.player_photo_path = cls.player.getPhotoPath()
		cls.player_picture = pygame.transform.scale( pygame.image.load( cls.player_photo_path  ).convert_alpha(), (20,20) )
		cls.display_surf.blit( cls.player_picture , ( cls.player_position[0] * 20 , cls.player_position[1] * 20  ) ) 


		# Display Guardian in le Lab, with right size image
		cls.guardian_photoPath = cls.guardian.getPhotoPath()
		cls.guardian_picture = pygame.transform.scale( pygame.image.load( cls.guardian_photoPath  ).convert_alpha(), (20,20) )
		cls.display_surf.blit( cls.guardian_picture , ( cls.guardian_position[0] * 20 , cls.guardian_position[1] * 20  ) ) 
		
		pygame.display.update()

	# Restore the background picture from the saved one
	def restoreBackground(cls, coordinates, sizeX = 20, sizeY = 20 ):
		rect = ( ( coordinates[0] * sizeX, coordinates[1] * sizeY ) , (sizeX ,sizeY ) ) 
		cls.display_surf.fill((0,0,0), rect )
		cls.display_surf.blit( cls.background_display_surf,  ( coordinates[0] * sizeX, coordinates[1] * sizeY ), rect )
		pygame.display.update( rect )

	# return TRUE if the position is not Wall
	def isXYPositionPossible(cls, x, y ):
		# use of NOT as a wall is "1" and "floor" is "0"...the oposite 
		# af the question ...

		if ( x < 0 or y < 0 ) :
			return False

		if ( x >= len( cls.maze[0] ) or y >= len(cls.maze) ) :
			return False

		# if ( cls.pd_maze.iloc[ y , x ] == 0 ):
		# 	return True

		if ( cls.pd_maze.iloc[ y , x ] == 1 ):
			return False
		else :
			return True


	# return TRUE if the guardian is at the position
	def isXYPositionIsGuardian(cls,XY):	
		if ( cls.guardian_position == XY ): 
			return True
		else:
			return False

	# return TRUE if Player win against Guardian
	#def isPlayerWinOverGuardian(cls,XY):	
	def isPlayerWinOverGuardian(cls):

		#if cls.isXYPositionIsGuardian(XY):
		if ( cls.player.getObjectNumber() ==  cls.number_of_initial_objects_list ) :
			return True
		else:
			cls.player.killMacGyver()
			return False



	# Moves Player in the Maze
	def movePlayerDirection(cls, direction):

		if direction == "UP" :
			if cls.isXYPositionPossible( cls.player_position[0], cls.player_position[1] - 1 ) :
				cls.restoreBackground( cls.player_position )
				cls.player_position = [ cls.player_position[0], cls.player_position[1] - 1 ]
				cls.player.addObjectToList( cls.getObjectAt( cls.player_position ) )
				cls.displayPlayer( cls.player_position )
				if cls.isXYPositionIsGuardian(cls.player_position):
					cls.application.setProgramContext("CONTROL")					
					if cls.isPlayerWinOverGuardian():
						cls.application.displayControlScreen("win")
					else:
						cls.application.displayControlScreen("lose")
					cls.application.initialisation()


		if direction == "DOWN" :
			if cls.isXYPositionPossible( cls.player_position[0], cls.player_position[1] + 1 ) :
				cls.restoreBackground( cls.player_position )
				cls.player_position = [ cls.player_position[0], cls.player_position[1] + 1 ]
				cls.player.addObjectToList( cls.getObjectAt( cls.player_position ) )
				cls.displayPlayer( cls.player_position )
				if cls.isXYPositionIsGuardian(cls.player_position):
					cls.application.setProgramContext("CONTROL")
					if cls.isPlayerWinOverGuardian():
						cls.application.displayControlScreen("win")
					else:
						cls.application.displayControlScreen("lose")
					cls.application.initialisation()

		if direction == "RIGHT" :
			if cls.isXYPositionPossible( cls.player_position[0] + 1, cls.player_position[1] ) :
				cls.restoreBackground( cls.player_position )
				cls.player_position = [ cls.player_position[0] + 1, cls.player_position[1] ]
				cls.player.addObjectToList( cls.getObjectAt( cls.player_position ) )
				cls.displayPlayer( cls.player_position )
				if cls.isXYPositionIsGuardian(cls.player_position):
					cls.application.setProgramContext("CONTROL")
					if cls.isPlayerWinOverGuardian():
						cls.application.displayControlScreen("win")
					else:
						cls.application.displayControlScreen("lose")
					cls.application.initialisation()

		if direction == "LEFT" :
			if cls.isXYPositionPossible( cls.player_position[0] - 1, cls.player_position[1] ) :
				cls.restoreBackground( cls.player_position )
				cls.player_position = [ cls.player_position[0] - 1, cls.player_position[1] ]
				cls.player.addObjectToList( cls.getObjectAt( cls.player_position ) )
				cls.displayPlayer( cls.player_position )
				if cls.isXYPositionIsGuardian(cls.player_position):
					cls.application.setProgramContext("CONTROL")
					if cls.isPlayerWinOverGuardian():
						cls.application.displayControlScreen("win")
					else:
						cls.application.displayControlScreen("lose")
					cls.application.initialisation()

	# Display the player at the right place on the Maze....
	def displayPlayer(cls, coordinates, sizeX = 20, sizeY = 20 ):

		rect = ( ( coordinates[0] * sizeX, coordinates[1] * sizeY ) , ( sizeX ,sizeY ) ) 

		cls.display_surf.blit( cls.player_picture , ( coordinates[0] * 20 , coordinates[1] * 20 ) ) 

		pygame.display.update( rect )


def read_values_from_json(file, key):
	values = []
	with open(file) as f:
		data = json.load(f)
		for entry in data:
			values.append(entry[key])

	print(values) # DEBUG
	
	return values

def main():



	app = App()
	app.on_execute()


if __name__ == "__main__":
	main()

