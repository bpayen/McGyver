import sys
import random

import pygame
import pandas as pd
import json

""" THE MAZE... this class modelizes the maze into wich MacGyver will crawl.
The maze is charged from a file. 
Maze's structure can be modified directly into the maze.def file.
"""
class Maze:
    # Window size
    _window_width = 15 * 20
    _window_height = (15 * 20) + 20  # One line to list objects grabed
    # Maze scheme
    _maze = None
    # Maze in Pandas (cartesian...) coordinates...
    _pd_maze = None
    # coordinates of the entry/ending point of (X / Y) maze plannar 
    # coordinates -> NOT Matrice Coordinates !
    _maze_start_point = []
    _maze_end_point = []
    # Floor case for Objects positionning
    _free_case = []
    # List of Object positionning in the maze
    _objects_positions = []
    # List of object's names
    _number_of_initial_objects_list = 0
    # List of object's names
    _available_objects_list = []
    # list of grabed object
    _grabed_objects_list = []
    # player .... him-self
    _player = None
    # player position
    _player_position = None
    # player picture
    _player_picture = None
    # guardina .... him-self
    _guardian = None
    # guardian position
    _guardian_picture = None
    # Guaradian position
    _guardian_position = []
    # Maze Backgroung, to restore picture part after player move
    _background_display_surf = None
    # Object's pictures
    _aiguille_picture = None
    _ether_picture = None
    _tube_plast_picture = None
    _seringue_picture = None
    # object's names
    _TUYAU = "tuyau"
    _AIGUILLE = "aiguille"
    _ETHER = "ether"
    # Bottom line into wich the objects grabbed by MacGuyver will be displayed.
    _bottom_line_rect = ((0, 15 * 20), (15 * 20, 20))

    def __init__(self, player, guardian, application):
        # Player ....
        self._player = player
        # Guardian ....
        self._guardian = guardian
        self.application = application
        # Load the Maze's scheme from the file
        self._maze = read_values_from_json("ressources/maze.def", "maze")
        # Construct Pandas structure (easier to use with cartesian coordinates...)
        self._pd_maze = pd.DataFrame(self._maze)

    """ Initialisation of variables that
    needs to be set at every new game starting.
    """
    def initialisation(self):
        """ Picture's name order in the object list is importante for pictures of
         grabed objects at bottom line screen
        """
        self._available_objects_list = [self._AIGUILLE, self._ETHER, self._TUYAU]
        self._number_of_initial_objects_list = len(self._available_objects_list)
        self._grabed_objects_list = []

    """ return object's name at the position
    or retrun empty string if the box is empty.
    """
    def get_object_at(self, x_y):

        try:
            index = self._objects_positions.index(x_y)
            # OK.... there is an object at position....
            # Remove it from le liste before returning it
            # to caller...
            self._objects_positions.remove(x_y)
            object_to_return = self._available_objects_list[index]
            del self._available_objects_list[index]
            self.display_grabed_objects(object_to_return)
            return object_to_return
        except ValueError:
            return ""

    """
    Displays, in the bottom line, the objects MacGyver have grabbed. 
    The line color depends on the number of object MacGyver have grabbed.
	"""
    def display_grabed_objects(self, object_name):
        # inc object grabed list
        self._grabed_objects_list.append(object_name)
        actual_number_of_objects = len(self._grabed_objects_list)
        # rect = ( ( 0 , 15 * 20 ) , ( 15 * 20, 20 ) )
        if self._number_of_initial_objects_list == actual_number_of_objects:
            # all objects have been grabed
            self.display_surf.fill((0, 128, 0), self._bottom_line_rect)
            self.display_surf.blit(self._seringue_picture, (0, 15 * 20))
        else:
            # New object grabed.... display it at bottom line
            if actual_number_of_objects == 1:
                self.display_surf.fill((255, 69, 0), self._bottom_line_rect)

            if object_name == self._ETHER:
                self.display_surf.blit(
                    self._ether_picture, ((actual_number_of_objects - 1) * 20, 15 * 20)
                )
            elif object_name == self._TUYAU:
                self.display_surf.blit(
                    self._tube_plast_picture,
                    ((actual_number_of_objects - 1) * 20, 15 * 20),
                )
            elif object_name == self._AIGUILLE:
                self.display_surf.blit(
                    self._aiguille_picture,
                    ((actual_number_of_objects - 1) * 20, 15 * 20),
                )
        pygame.display.update()

    """ Display on the screen the Maze and the objects...
    """
    def display_jeu(self):
        # coordonate of wall element in graphic file
        position_wall = ((12 * 20, 0), (20, 20))
        # coordonate of flor element in graphic file
        position_floor = ((8 * 20, 40), (20, 20))
        # Objects's images list
        iol = []
        # Display surface
        self.display_surf = pygame.display.set_mode((self._window_width, self._window_height))
        # Background Surface de sauvegarde, pour les restaurations
        # après mouvement du player
        self._background_display_surf = pygame.Surface(
            (self._window_width, self._window_height)
        )
        self.image_pavement = pygame.image.load(
            "ressources/floor-tiles-20x20.png"
        ).convert()
        # fill Maze surface with right graphic elements
        for li in range(len(self._maze)):
            for col in range(len(self._maze[li])):
                # Automatic detection of coordinates of START/END  in the maze...
                if self._maze[li][col] == "S":
                    # START point ....
                    self._maze_start_point = [col, li]
                    self._player_position = self._maze_start_point
                    self._background_display_surf.blit(
                        self.image_pavement, (col * 20, li * 20), position_floor
                    )
                    continue
                if self._maze[li][col] == "E":
                    # END point ....
                    self._maze_end_point = [col, li]
                    self._guardian_position = self._maze_end_point
                    self._background_display_surf.blit(
                        self.image_pavement, (col * 20, li * 20), position_floor
                    )
                    continue
                if self._maze[li][col]:
                    # Wall
                    self._background_display_surf.blit(
                        self.image_pavement, (col * 20, li * 20), position_wall
                    )
                elif not self._maze[li][col]:
                    # Floor
                    self._background_display_surf.blit(
                        self.image_pavement, (col * 20, li * 20), position_floor
                    )
                    # Appends the free case to le list of avelable cases for objects
                    self._free_case.append([col, li])

        self.display_surf.blit(self._background_display_surf, (0, 0))

        self.display_surf.fill((139, 0, 0), self._bottom_line_rect)

        # Removes the maze's start point from the list of 
        # available boxe for objects to grab.
        try:
            self._free_case.remove(
                self._maze_start_point
            )  # No object on Maze's starting point
        except:
            pass # Bad idea ... maskes errors 

        # Removes the maze's end point from the list of 
        # available boxe for objects to grab.
        try:
            self._free_case.remove(self._maze_end_point)  # No object on Maze's ending point
        except:
            pass # Bad idea ... maskes errors 

        # get enought free floor coordinate, where will be put onto the objects
        self._objects_positions = random.sample(
            self._free_case, k=len(self._available_objects_list)
        )

        # display objects on the screen...
        self._aiguille_picture = pygame.transform.scale(
            pygame.image.load("ressources/aiguille.png").convert(), (20, 20)
        )
        self._ether_picture = pygame.transform.scale(
            pygame.image.load("ressources/ether.png").convert_alpha(), (20, 20)
        )
        self._tube_plast_picture = pygame.transform.scale(
            pygame.image.load("ressources/tube_plastique.png").convert_alpha(), (20, 20)
        )
        self._seringue_picture = pygame.transform.scale(
            pygame.image.load("ressources/seringue.png").convert_alpha(), (20, 20)
        )

        iol.append(self._aiguille_picture)
        iol.append(self._ether_picture)
        iol.append(self._tube_plast_picture)

        # Dispatches objects in the maze's boxes.
        for x in range(0, 3):
            self.display_surf.blit(
                iol[x],
                (self._objects_positions[x][0] * 20, self._objects_positions[x][1] * 20),
            )

        # Display McGyver in le Lab, with right size image
        self._player_photo_path = self._player.get_photo_path()
        self._player_picture = pygame.transform.scale(
            pygame.image.load(self._player_photo_path).convert_alpha(), (20, 20)
        )
        self.display_surf.blit(
            self._player_picture,
            (self._player_position[0] * 20, self._player_position[1] * 20),
        )

        # Display Guardian in le Lab, with right size image
        self._guardian_photoPath = self._guardian.get_photo_path()
        self._guardian_picture = pygame.transform.scale(
            pygame.image.load(self._guardian_photoPath).convert_alpha(), (20, 20)
        )
        self.display_surf.blit(
            self._guardian_picture,
            (self._guardian_position[0] * 20, self._guardian_position[1] * 20),
        )

        pygame.display.update()

    """ Restores the background picture from the saved one
    at the specified coordinates.
    """
    def restore_background(self, coordinates, size_x=20, size_y=20):

        rect = ((coordinates[0] * size_x, coordinates[1] * size_y), (size_x, size_y))

        self.display_surf.fill((0, 0, 0), rect)

        self.display_surf.blit(
            self._background_display_surf,
            (coordinates[0] * size_x, coordinates[1] * size_y),
            rect,
        )

        pygame.display.update(rect)

    """ return TRUE if the boxe's position is not a Wall.
    Memento : wall is modelized by "1" and "floor" is "0".
    """
    def is_xy_position_possible(self, x, y):
        if x < 0 or y < 0:
            return False

        if x >= len(self._maze[0]) or y >= len(self._maze):
            return False

        if self._pd_maze.iloc[y, x] == 1:
            return False
        else:
            return True

    """ return TRUE if the guardian is at the boxe's position.
    """
    def is_xy_position_is_guardian(self, x_y):
        if self._guardian_position == x_y:
            return True
        else:
            return False

    """ Return TRUE if Player win against Guardian.
    """
    def is_player_win_over_guardian(self):

        if self._player.get_object_number() == self._number_of_initial_objects_list:
            return True
        else:
            self._player.kill_mac_gyver()
            return False

    """ Moves Player in the Maze according to the 
    keyboard key received by the application.
    """
    def move_player_direction(self, direction):

        if direction == "UP":
            if self.is_xy_position_possible(
                self._player_position[0], self._player_position[1] - 1
            ):
                self.restore_background(self._player_position)
                self._player_position = [
                    self._player_position[0],
                    self._player_position[1] - 1,
                ]
                self.strock_key_systematic_actions(self._player_position)

        if direction == "DOWN":
            if self.is_xy_position_possible(
                self._player_position[0], self._player_position[1] + 1
            ):
                self.restore_background(self._player_position)
                self._player_position = [
                    self._player_position[0],
                    self._player_position[1] + 1,
                ]
                self.strock_key_systematic_actions(self._player_position)

        if direction == "RIGHT":
            if self.is_xy_position_possible(
                self._player_position[0] + 1, self._player_position[1]
            ):
                self.restore_background(self._player_position)
                self._player_position = [
                    self._player_position[0] + 1,
                    self._player_position[1],
                ]
                self.strock_key_systematic_actions(self._player_position)

        if direction == "LEFT":
            if self.is_xy_position_possible(
                self._player_position[0] - 1, self._player_position[1]
            ):
                self.restore_background(self._player_position)
                self._player_position = [
                    self._player_position[0] - 1,
                    self._player_position[1],
                ]
                self.strock_key_systematic_actions(self._player_position)

    """ We group actions that are executed every time a direction key is 
    stroked. This simplify methods coding.
    """
    def strock_key_systematic_actions(self, player_position):

        self._player.add_object_to_list(self.get_object_at(player_position))

        self.display_player(player_position)

        if self.is_xy_position_is_guardian(player_position):
            
            self.application.set_program_context("CONTROL")
            
            if self.is_player_win_over_guardian():
                self.application.display_control_screen("win")
            else:
                self.application.display_control_screen("lose")

            self.application.initialisation()

    """ Displays the player at the specifized coordinate on the Maze....
    """
    def display_player(self, coordinates, size_x=20, size_y=20):

        rect = ((coordinates[0] * size_x, coordinates[1] * size_y), (size_x, size_y))

        self.display_surf.blit(
            self._player_picture, (coordinates[0] * 20, coordinates[1] * 20)
        )

        pygame.display.update(rect)

""" Return the informations associated to the KEY from within 
the file specified.
"""
def read_values_from_json(file_into_search, key):
    values = []
    with open(file_into_search) as f:
        data = json.load(f)
        values = data[key]

    return values
