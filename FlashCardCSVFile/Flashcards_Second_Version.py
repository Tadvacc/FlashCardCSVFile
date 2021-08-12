#Flashcards_Second_Version.py
"""This flashcard program allows the user to ask for a glossary entry from a CSV file.
In response, the program will create a dictionary and randomly picks a entry from all glossary entries.
It shows the entry.
After the user presses return, the program shows the definition of that particular entry.
The user can repeatedly ask for an entry and also has the option to quit the program."""

from random import *
import csv

def show_flashcard():
    """ Show the user a random key and ask them
        to define it. Show the definition
        when the user presses return.    
    """
    random_key = choice(list(glossary))
    print('Define: ', random_key)
    input('Press return to see the definition')
    print(glossary[random_key])

def file_to_dictionary ( filename ):
    """Return a dictionary with the contents of a file"""

    file = open( filename, 'r' )
    reader = csv.reader( file )
    dictionary = {}
    for row in reader:
        dictionary [ row [ 0 ] ] = row [ 1 ]
    return dictionary

# Set up the glossary

glossary = file_to_dictionary ( 'Glossary.txt' )

# The interactive loop

exit = False
while not exit:
    user_input = input('Enter s to show a flashcard and q to quit: ')
    if user_input == 'q':
        exit = True
    elif user_input == 's':
        show_flashcard()
    else:
        print('You need to enter either q or s.')
