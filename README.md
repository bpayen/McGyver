# McGyver

This projet displays a maze in wich MacGyver have to escape after grabing three objects on the ground, elaborates syring and made asleep the maze guardian.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Prerequisites

You need to set up Python 3 on your machine before cloning the project on it.
It's best to use virtual environments which into you can install modules necessary to run the project.

### Installing
Create repository on your machine, and go into it :

```
$ md MacGyver
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
Choose to start a new game, by strocking the "N" key.

Then a maze will apprears on the screen.
You can move MacGyver in the maze whit the four direction key UP/DOWN/RIGHT/LEFT.
You have to grab the three objects laying onto the maze's ground before going in face of the guardian.
Then you can move on the guardian box to fight against him, and WIN !
be careful : if you face the guardian without having grabed all the objects he will kill you .... and you LOSE the game

A screen will inform you if you WIN or LOOSE the game... From this screen you can decide to start a new game or not.



## Authors

* **Bertrand PAYEN**.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Olivier, my Mentor from OpenclassRooms :)
