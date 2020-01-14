# McGyver

This projet displays a maze in wich MacGyver have to escape after grabing three objects on the ground, elaborates syring and made asleep the maze's guardian.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for playing.

### Prerequisites

You need to set up Python 3 on your machine before cloning the project on it.
It's best to use virtual environment which into you can install modules necessary to run the project.

### Installing
Create repository on your machine, and go into it :

```
$ mkdir MacGyver
$ cd MacGyver
```

Clone the project :
```
$ git clone https://github.com/bpayen/McGyver.git
```

Once you have cloned the repository into your machine and started the virtual environment you need to install the modules required by the application.

```
$ pip install -r requirements.txt
```
 
 This command will install all required modules.

## Running

To run the game you have to type in the command :
```
$ python3 jeu.py
```

## Playing 

Once started the application displays a screen asking what you want to do.
Choose to start a new game by hitting the "N" key.

Then a maze will apprears on the screen.
You can move MacGyver in the maze with the four direction keys UP/DOWN/RIGHT/LEFT (or ESC to quitt).
You have to grab the three objects laying onto the maze's ground before going in face of the guardian.
Then you can move on the guardian box to fight against him, and WIN !
be careful : if you face the guardian without having grabed all the objects he will kill you .... and you LOOSE the game

A screen will inform you if you WIN or LOOSE the game... From this screen you can decide to start a new game or not.

## Configuration
You can change the maze layout easily. 
The maze structure is stored in the maze.def file, in the ressources folder.
The size of the maze is fix. 
Use "0" to place a "path" on the maze's ground, and "1" to put a wall.
You specifie the maze entry with a "S" letter, and the exit point with a "E" letter.
Be carful : each part of the maze path must be reachable from the start point. If not : some objects could be put by the application in points where MacGyver can't go, so he would be impossible for him to grab every objects needed to win against the guardian....
Be sure to draw a free path that allow MacGyver to reach the exit point !

Layout example : 
{ "maze" : [
			[1,1,"S",1,1,1,1,1,1,1,1,1,1,1,1],
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
			[1,1,1,1,1,1,1,1,1,1,1,1,"E",1,1]
			]
}


## Authors

* **Bertrand PAYEN**.

## License

You can freely use and modify this program.... 

## Acknowledgments

* Olivier.E, my Mentor from OpenclassRooms :)
