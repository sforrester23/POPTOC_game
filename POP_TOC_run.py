# We will need to import our functions
from POP_TOC_functions import *

# Run some POPTOC commands here

play_on = input('Press enter to start playing POPTOC! Or type exit to leave: ').upper()

while play_on != 'EXIT':
    count = 0
    number = int(input('What number would you like to play POPTOC with?: '))
    while count <= number:
        print(count, '--', POPTOC(count))
        count += 1
    play_on = input('Press enter to keep playing POPTOC! Or type exit to leave: ').upper()

