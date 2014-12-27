# user class
import random

class User():
    """
    Defines a user that will be using the wall program
    """
    def __init__(self, username, psswrd):
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
        return 'User: {0}, Password: {1}, I.D.: {2}, Word List: {3}'.format(self.username, self.psswrd, self.id_num, self.f_name)

    def genIdNum(self):
        self.id_num = random.randrange(40000,90000) % 300
    """
    def oldUser(self):
        while True:
            usr_name = raw_input('Username: ')
            usr_pwd = getpass.getpass('Password: ')
            for i in usr_list:
                if i.username == usr_name and i.psswrd == usr_pwd:
                    return i
                else:
                    print 'Password and user name did not match. Please Try again.'

    def newUser(self):
        while True:
            usr_name = raw_input('Enter your desired username: ')
            while True:
                if usr_name not in usr_list:
                    usr_pwd = getpass.getpass('Enter in your password: ')
                    usr_pwd_conf = getpass.getpass('Confirm your password: ')
                    if usr_pwd != usr_pwd_conf:
                        print 'Passwords did not match. Please try again.'
                    else:
                        print '%s was added to the database.' % (usr_name)
                        player = User(usr_name,usr_pwd)
                        player.genIdNum()
                        player.f_name = player.username + '_wordlist.txt'
                        return player
                else:
                    print 'User name is already taken. Please choose another name.'
    """
