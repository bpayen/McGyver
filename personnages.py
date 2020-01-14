# Base class for Player and Guardian
class Personnage:

	position = None

	photoPath = None

	def __init__(cls, photoPath ):
		cls.photoPath = photoPath

	def getPhotoPath(cls):
		return cls.photoPath

# Specialized class ..... 
class MacGyver(Personnage):

	alive = True

	objectList = []

	def __init__(cls, photoPath):
		super().__init__( photoPath )
		cls.initialisation()

	# Add object name to yhe list of objects picked-up
	# by Mc Gyver 
	def addObjectToList(cls, objectName):
		if (  objectName is not None and objectName != "") :
			cls.objectList.append(objectName)

	# Return the number of objects in of objects
	# picked-up by MacGyver 
	def getObjectNumber(cls):
		return len(cls.objectList)

	# Initialisation needed for every 
	# new game 
	def initialisation(cls):
		cls.objectList = []

	def killMacGyver(cls):
		cls.alive = False

# Specialized class ..... 
class Guardian(Personnage):

	def __init__(cls, photoPath):
		super().__init__(photoPath)