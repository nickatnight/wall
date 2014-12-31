from wall_engine import Wall
import getpass

choices = ['d', 'e', 'm', 'q', 'r', '1', '2', '3', '4', '5']
py_wall = Wall()

py_wall.load_user_list()

py_wall.display_menu()

user_check = raw_input('Greetings! Are you a registered user?(yes/no) ')

while True:
    if user_check == 'yes':
        while True:
            name = raw_input('Username: ')
            pword = getpass.getpass('Password: ')
            if py_wall.old_user(name, pword):
                py_wall.player_word_list_load_r()
                break
        break
    elif user_check == 'no':
        while True:
            if py_wall.new_user():
                break
        break
    else:
        print 'Could not understand user input.'

py_wall.open_player_word_list_w()

while True:
    print ''
    print '\t1. (D)isplay all words/meanings'
    print '\t2. (E)nter a new word/meaning'
    print '\t3. (M)odify a word/meaning'
    print '\t4. (R)emove word'
    print '\t5. (Q)uit'
    print ''

    user_input = raw_input('What would you like to do? ').lower()

    while user_input not in choices:
        user_input = raw_input('Please enter a valid value: ').lower()

    if user_input == 'd' or user_input == '1':
        py_wall.display_words()
    elif user_input == 'e' or user_input == '2':
        new_word = raw_input('Enter your word, followed by a \':\', followed by its definition: ').split(':')
        new_word = [i.strip() for i in new_word]
        py_wall.enter_word(new_word)
    elif user_input == 'm' or user_input == '3':
        mod_word = raw_input('Enter the word you would like to modify: ')
        py_wall.modify_word(mod_word)
    elif user_input == 'r' or user_input == '4':
        del_word = raw_input('Enter the word you would like to remove: ')
        py_wall.delete_word(del_word)
    elif user_input == 'q' or user_input == '5':
        print 'Thank you come again.'
        py_wall.save_instance()
        break
