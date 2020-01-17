""" Base class for Player and Guardian.
"""
class Person:
    _position = None
    _photo_path = None

    def __init__(cls, photo_path):
        cls._photo_path = photo_path

    """ Return the path to the photo associated to the Personnage
    """
    def get_photo_path(cls):
        return cls._photo_path


""" MacGyver  
"""
class MacGyver(Person):

    alive = True

    _object_list = []

    def __init__(self, photo_path):
        super().__init__(photo_path)
        self.initialisation()

    """ Add object name to yhe list of objects picked-up by Mc Gyver
    """
    def add_object_to_list(self, object_name):
        if object_name is not None and object_name != "":
            self._object_list.append(object_name)

    """  Return the number of objects picked-up by MacGyver since
    the game beginning.
    """
    def get_object_number(self):
        return len(self._object_list)

    """ Initialisation needed by the MacGyver object at every new game.
    """
    def initialisation(self):
        self._object_list = []

    """ This methode change the MacGyver to "killed" state ....
    """
    def kill_mac_gyver(self):
        self.alive = False


""" The guardian ...  
"""
class Guardian(Person):
    def __init__(self, photo_path):
        super().__init__(photo_path)
