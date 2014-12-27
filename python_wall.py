import os.path, sys, getpass
from collections import OrderedDict
import cPickle as pickle
from users import User



def displayMenu():
    print 57 * '#'
    print '#           WELCOME TO THE PYTHON/WEBDEV WALL           #'
    print '#     ----------------------------------------------    #'
    print '#     Here, we will dial in on your python skills by    #'
    print '#     providing an interactive and fun way to really    #'
    print '#     understand how this language functions.           #'
    print 57 * '#'
    print ''


def oldUser():
    while True:
        usr_name = raw_input('Username: ')
        usr_pwd = getpass.getpass('Password: ')
        for i in usr_list:
            if i.username == usr_name and i.psswrd == usr_pwd:
                return i
            else:
                print 'Password and user name did not match.'

def newUser():
    t_list = [name.username for name in usr_list]
    while True:
        usr_name = raw_input('Enter your desired username: ')
        while True:
            if usr_name not in t_list:
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
                print 'User name is already taken. Please choose a different name.'
                break

def displayWords():
    if len(words) == 0:
        print 'The word list is already empty.'
    else:
        print ''
        print 'Current word list:'
        print '------------------'
        for word, meaning in words.items():
            print '\t%s: \t%s' % (word, meaning)

def enterWord(new_word):
    if len(new_word) > 2:
        print 'Too many colons in your input.'
    elif new_word[0] not in words:
        try:
            words[new_word[0]] = new_word[1]
            new_word[1].lstrip()
            print 'Your word \'%s\' was successfully added to the wall' % (new_word[0])
        except:
            print 'Invalid input. Please try again later.'
    else:
        print 'Sorry but \'%s\' is already in the word list.' % (new_word[0])

def modifyWord(word):
    if word not in words:
        print 'The word list does not contain that word.'
    else:
        which = raw_input('Would you like to modify the word or definition? ')
        if  which == 'word':
            mod_word = raw_input('Enter your new word: ')
            words[mod_word] = words.pop(word)
            print 'Your word \'%s\' was updated successfully.' % (mod_word)
        elif which == 'definition':
            mod_def = raw_input('Enter your new definition for \'%s\': ' % (word))
            words[word] = mod_def
            print 'The definition for \'%s\' has been successfully.' % (word)
        else:
            print 'Invalid input, please try again.'

usr_list = [ ]
words = OrderedDict()

if os.path.exists('user_list.txt'):
    fo_ul = open('user_list.txt', 'r')
    usr_list = pickle.load(fo_ul)
    fo_ul.close()

else:
    fo_ul = open('user_list.txt', 'wb')

choices = ['d','e','m','q','1','2','3','4']

displayMenu()
usr_check = raw_input('Greetings! Are you a registered user?(yes/no) ')

while True:
    if usr_check == 'yes':
        player = oldUser()
        fo_wl = open(player.f_name, 'r')
        words = pickle.load(fo_wl)
        fo_wl.close()
        print 'Welcome back %s!' % (player.username)
        break
    elif usr_check == 'no':
        player = newUser()
        usr_list.append(player)
        fo_ul = open('user_list.txt', 'wb')
        pickle.dump(usr_list, fo_ul)
        fo_ul.close()
        break
    else:
        print 'Could not understand that input. Please try again.'

fo_wl = open(player.f_name, 'wb')

while True:
    print ''
    print '\t1. (D)isplay all words/meanings'
    print '\t2. (E)nter a new word/meaning'
    print '\t3. (M)odify a word/meaning'
    print '\t4. (Q)uit'
    print ''

    usr_input = raw_input('What would you like to do? ',).lower()
    while usr_input not in choices:
        usr_input = raw_input('Please enter a valid value: ')

    if usr_input == 'd' or usr_input == '1':
        displayWords()
    elif usr_input == 'e' or usr_input == '2':
        new_word = raw_input('Enter your word, followed by a \':\', followed by its definition: ').split(':')
        enterWord(new_word)
    elif usr_input == 'm' or usr_input == '3':
        mod_word = raw_input('Enter the word you like to modify: ')
        modifyWord(mod_word)
    elif usr_input == 'q' or usr_input == '4':
        print 'Thank you my lord. Please come again.'
        pickle.dump(words, fo_wl)
        fo_wl.close()
        break
