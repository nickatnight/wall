# user class
import random

class User():
    """
    Defines a user that will be using the wall program
    """
    def __init__(self, username=None, psswrd=None):
        """
        Instantiates a new User object with the password and username set.
        The id is generated randomly and the file name is the user name plus
        wordlist.txt.
        """
        self.username = username
        self.psswrd = psswrd
        self.id_num = 0
        self.f_name = ''

    def __str__(self):
        """
        Return a formated string value which contains the users info
        """
        return 'User: {0}, Password: {1}, I.D.: {2}, Word List: {3}'.format(self.username, self.psswrd, self.id_num, self.f_name)

    def genIdNum(self):
        """
        Generate random number for the user
        """
        self.id_num = random.randrange(40000,90000) % 300
