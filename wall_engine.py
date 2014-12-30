import os.path, sys, getpass
from collections import OrderedDict
import cPickle as pickle
from users import User


class Wall():
    """
    Creates a new wall engine that will handle data
    """
    def __init__(self):
        """
        Instantiate all defaults for the instance. A new ordered dict word list
        is created that will hold all words the user enters. A new User instance
        from our User class will create a new player. The user list will hold
        all the users who use this program. File open objects will also be
        created to handle the file objects that will be being read to and
        written to during program execution
        """
        self.word_list = OrderedDict()
        self.player = User()
        self.user_list = []
        self.fo_ul = ''
        self.fo_wl = ''

    def display_menu(self):
        """
        Displays the menu for the use
        """
        print 57 * '#'
        print '#           WELCOME TO THE PYTHON/WEBDEV WALL           #'
        print '#     ----------------------------------------------    #'
        print '#     Here, we will dial in on your python skills by    #'
        print '#     providing an interactive and fun way to really    #'
        print '#     understand how this language functions.           #'
        print 57 * '#'
        print ''

    def old_user(self, u_name, u_pword):
        """
        Checks to see if the log in information that the user enters has the
        right credentials. Username and password are taken as parameters. Return
        true if the player is in the dB, false otherwise
        """
        for i in self.user_list:
            if i.username == u_name and i.psswrd == u_pword:
                self.player = i
                return True
        print 'Password/Username did not match.'
        return False

    def new_user(self):
        """
        Creates a new user. Make a temporary list of the current usernames. Get
        the desired username of the player and if the username is not currently
        taken, save the desired password for the user. There is a confirmation
        check for password. Once username and password have been created, add
        the user to the userlist, create a wordlist text for them, generate a
        user id for them, and save the user list.
        """
        t_list = [name.username for name in self.user_list]
        self.player.username = raw_input('Enter your desired username: ')
        if self.player.username not in t_list:
            self.player.psswrd = getpass.getpass('Enter in your password: ')
            usr_pwd_conf = getpass.getpass('Confirm your password: ')
            if self.player.psswrd != usr_pwd_conf:
                print 'Passwords did not match. Please try again.'
            else:
                print '%s was added to the database.' % self.player.username
                self.player.genIdNum()
                self.player.f_name = self.player.username + '_wordlist.txt'
                self.user_list.append(self.player)
                if self.fo_ul.closed:
                    self.fo_ul = open('user_list.txt', 'wb')
                pickle.dump(self.user_list, self.fo_ul)
                self.fo_ul.close()
                return True
        else:
            print 'User name is already taken. Please choose a different name.'
            return False

    def display_words(self):
        """
        Print all the words in the users wordlist with all the definitions. If
        the word list is empty, notify the user.
        """
        if len(self.word_list) == 0:
            print 'The word list is already empty.'
        else:
            print ''
            print '%s\'s word list:' % self.player.username
            print len(self.player.username) * '-' + '-------------'
            for word, meaning in self.word_list.items():
                print '\t%s: \t%s' % (word, meaning)

    def enter_word(self, new_word):
        """
        Function to add a new word to the users word list. The new word along with
        the definition is taken as a parameter. The new word is split into a
        length 2 tuple (word and definition). If the length of the new word is
        more than 2 (meaning there was incorrect input), the user will be
        prompted the input was incorrect. Next we check if the index of the
        tuple (word) is in the word list and if its not, add it to the word list.
        """
        if len(new_word) > 2:
            print 'Too many colons in your input.'
        elif new_word[0] not in self.word_list:
            try:
                self.word_list[new_word[0].strip()] = new_word[1].strip()
                print 'Your word \'%s\' was successfully added to the wall' % (new_word[0])
            except:
                print 'Invalid input. Please try again later.'
        else:
            print 'Sorry but \'%s\' is already in the word list.' % (new_word[0])

    def modify_word(self, word):
        """
        Function that modifies a word or definition in the list
        """
        if word not in self.word_list:
            print 'The word list does not contain that word.'
        else:
            which = raw_input('Would you like to modify the word or definition? ')
            if which == 'word':
                mod_word = raw_input('Enter your new word: ')
                self.word_list[mod_word] = self.word_list.pop(word)
                print 'Your word \'%s\' was updated successfully.' % (mod_word)
            elif which == 'definition':
                mod_def = raw_input('Enter your new definition for \'%s\': ' % word)
                self.word_list[word] = mod_def
                print 'The definition for \'%s\' has been successfully.' % word
            else:
                print 'Invalid input, please try again.'

    def load_user_list(self):
        """
        Load the current user list that exists or does not exist on the HD
        """
        if os.path.exists('user_list.txt'):
            self.fo_ul = open('user_list.txt', 'r')
            self.user_list = pickle.load(self.fo_ul)
            self.fo_ul.close()
        else:
            self.fo_ul = open('user_list.txt', 'wb')

    def player_word_list_load_r(self):
        """
        Load the users word list by pickling an already made list
        """
        fo_wl = open(self.player.f_name, 'r')
        self.word_list = pickle.load(fo_wl)
        fo_wl.close()

    def open_player_word_list_w(self):
        """
        Open the players word list for writing to
        """
        self.fo_wl = open(self.player.f_name, 'wb')

    def save_instance(self):
        """
        Before the program ends, save the word list by pickle dumping the
        contents of 'word_list' into the open word list file object.
        """
        pickle.dump(self.word_list, self.fo_wl)
        self.fo_wl.close()
