# Athena Mestas

# An import that allows the user to exit while in the storyline or instruction sections
import sys

# ---------------------------------------------------------------------------------------------------------------
# Dictionary section.

# Main dictionary connecting directions, rooms, items, villain, and exit.
rooms = {
    'Living Room': {'name': 'Living Room', 'south': 'Office', 'west': 'Bathroom', 'north': 'Bedroom',
                    'east': 'Dining Room'},
    'Office': {'name': 'Office', 'north': 'Living Room', 'item': 'Nunchucks'},
    'Bathroom': {'name': 'Bathroom', 'east': 'Living Room', 'item': 'Spoiled Milk'},
    'Bedroom': {'name': 'Bedroom', 'south': 'Living Room', 'west': 'Closet', 'item': 'Truffle Oil'},
    'Dining Room': {'name': 'Dining Room', 'west': 'Living Room', 'north': 'Kitchen', 'item': 'Bobby Flays Cookbook'},
    'Closet': {'name': 'Closet', 'east': 'Bedroom', 'north': 'Attic', 'item': 'Sword'},
    'Attic': {'name': 'Attic', 'south': 'Closet', 'item': 'Illegal Stock-Trade Tips'},
    'Kitchen': {'name': 'Kitchen', 'villain': 'Martha Stewart'},
    'exit': {'name': 'exit', 'exit': 'Thank you for playing!'}
}


# Dictionary containing the beginning storyline.
def story_line():
    return (f'{boarder()}'
            '\n.   Martha Stewart has taken over your kitchen and will not let you get a snack '
            'because it would “ruin your dinner”.    .'
            '\n*   You need to get rid of Martha, but to do so, you will need to find a few items.                    '
            '                 *'
            '\n.   You will need grab Nunchucks from the office to protect yourself if she leaves the kitchen,        '
            '                 .'
            '\n*   spoiled milk from the bathroom to throw her off your scent, '
            'truffle oil from the bedroom to lure her later,         *'
            '\n.   a sword from the closet for obvious reasons,                                                       '
            '                 .'
            '\n*   and illegal stock trade tips to send her to prison... again.                                       '
            '                 *'
            f'\n{boarder()}')


# Dictionary outlining the instructions/available inputs.
def show_instructions():
    return (f'\n{boarder()}'
            '\n.   Be careful to not go into the kitchen until you have all of the items!                              '
            '                .'
            '\n*                                                                                                       '
            '                *'
            '\n.   The available commands that allow you to sneak around the house are: '
            'North, East, South, West                       .'
            '\n*                                                                                                       '
            '                *'
            '\n.   To add items to your inventory, in the Pick Up prompt, enter: (item name)                           '
            '                .'
            '\n*                                                                                                       '
            '                *'
            '\n.   If you wish to exit the game at any time, enter: exit                                               '
            '                .'
            f'\n{boarder()}')


# Dictionary for a boarder to separate game sections for a more organized user experience.
def boarder():
    return ('. * . * . * . * . * . * . * . * . * . * . * . * . * . * . * . * . * . * . * . * . * . * . * . * . * . * '
            '. * . * . * . * .')


# Dictionary to output when the user enters 'exit'.
def exit_output():
    return ('\n\n\n       . * . * . * . * . * . * . * .'
            '\n       .                           .'
            '\n       *    Thanks For Playing!    *'
            '\n       .                           .'
            '\n       . * . * . * . * . * . * . * .\n\n\n')


# Dictionary displaying the output if the user loses the game.
def losing_dialogue():
    return ('Martha Stewart caught you sneaking into the kitchen!!!\nEven though you fought '
            'hard with the items you had... it was not enough.\nShe ate your face.\n\nTry again...')


# Dictionary displaying the output if the user wins the game.
def winning_dialogue():
    return ('You walk into the kitchen waving around the spoiled milk to sneak around Martha...'
            '\nOnce you reach the pantry to hide, you drip a few drops of truffle oil onto '
            'Bobby Flays Cookbook and slide the book out from under the pantry door...'
            '\nThe book does not slide out far enough from the pantry, so you take out your sword, '
            'and maneuver it under the door to push the book out farther.'
            '\nThe smell of Truffle Oil intrigues her, and she walks over to inspect.'
            '\nOnce she sees her competitors book she roars and becomes flustered and enraged, looking around '
            'to see who did this...'
            '\nYou burst out of the pantry! You swing your Nunchucks at her, they completely miss her '
            'and swing back around, hitting you in the face, giving you a black eye!'
            '\nThe cops bust in... (apparently the neighbors filed a noise complaint)... '
            'They see you with a black eye and immediately assume she attacked you!'
            '\nWhile in questioning, you successfully convince the police that you had found her '
            'Illegal Stock-Trade Tips, and they send her back to prison!!!'
            '\n                                       .*.*.* You win!!! *.*.*.')


# Dictionary to determine if a user wins/loses, their current location, current inventory,
# and if it is appropriate to tell the user if there is an item in their current room.
def show_status():
    # Making the variable: room_item able to be accessed throughout the code.
    global room_item
    # Determining the user's win or loss.
    if current_room == rooms['Kitchen']:
        # Loosing branch.
        if (len(current_inventory)) < 6:
            print(losing_dialogue())
            return sys.exit()
        # Winning branch.
        else:
            print(winning_dialogue())
            return sys.exit()
    else:
        # Outputs the user's current location.
        print('You are in the: {}'.format(current_room['name']))
        # Outputs the user's current inventory.
        print('Inventory:', current_inventory)
        # Determines whether the player sees an item.
        if 'item' in current_room.keys():
            room_item = current_room['item']
            if room_item not in current_inventory:
                return f'You see: {room_item}\n\n\n\n'
            else:
                return '\n\n\n'
        else:
            return '\n\n\n'


# ------------------------------------------------------------------------------------------------------------------
# Assigning beginning variables and values.

# Sets the available commands to move.
directions = ['north', 'south', 'east', 'west']
# Sets the available items to pick up.
items = ['Nunchucks', 'Spoiled Milk', 'Truffle Oil', 'Bobby Flays Cookbook', 'Sword', 'Illegal Stock-Trade Tips']
# Assigns the input to exit.
exit_code = 'exit'
# Sets the beginning room to 'Living Room'.
current_room = rooms['Living Room']

# Sets the beginning value of the following variables to nothing/empty.
input_move = ()
current_inventory = []
room_item = ()
pick_item = ()

# ----------------------------------------------------------------------------------------------------------------
# Beginning sections of the game: storyline and instructions.

# Displays the story line of the game.
print(story_line())
# Prompts the user to enter 'okay' to move on to the instructions.
user_response_storyline = input('\n ~ Enter okay to continue, or exit to leave: ').lower().strip()
# Outlines what happens if the user inputs an invalid response.
while (user_response_storyline != 'okay') and (user_response_storyline != 'exit'):
    print('Invalid input, please try again...')
    user_response_storyline = input('\n ~ Enter okay to continue, or exit to leave: ').lower().strip()
# Allows the user to exit.
if exit_code in user_response_storyline:
    print(exit_output())
    sys.exit()

# Displays the instructions for the game.
print(show_instructions())
user_response_instructions = input('\n\n ~ Enter okay to continue, or exit to leave: ').lower().strip()
while (user_response_instructions != 'exit') and (user_response_instructions != 'okay'):
    print('Invalid input, please try again...')
    user_response_instructions = input('\n\n ~ Enter okay to continue, or exit to leave: ').lower().split()
# Allows the user to exit.
if exit_code in user_response_instructions:
    print(exit_output())
    sys.exit()

# -------------------------------------------------------------------------------------------------------------------
# Game loop.

while True:
    # Prints a boarder between each loop.
    print(f'\n{boarder()}')
    # Shows user's location, inventory, and if there is an available item.
    print(show_status())

    # Determines if user gets a 'Pick Up' prompt.
    if ('item' in current_room.keys()) and (room_item not in current_inventory):
        pick_item = input('\n ~ Pick Up: ').title()
        if exit_code in pick_item.lower():
            print(exit_output())
            break
        # Outlines what happens if the user enters an invalid response.
        elif (exit_code not in pick_item) and (pick_item not in items):
            while (pick_item not in items) or (pick_item not in current_room.values()):
                print('You cannot pick that up, please try again...')
                pick_item = input('\n ~ Pick Up: ').title()
        else:
            current_inventory.extend([pick_item])
            print(f'   - {pick_item} added to your inventory!')
    else:
        print()

    # Get user directional input.
    input_move = input('\n ~ Enter Direction: ').lower().strip()
    # Allows the user to exit through the 'Enter direction' prompt.
    if exit_code in input_move:
        print(exit_output())
        break
    # Outlines what happens if the user enters an invalid response
    elif (exit_code not in input_move) and (input_move not in directions):
        while (input_move not in current_room) or (input_move not in directions):
            print('You cannot go that way, please try again...')
            input_move = input('\n ~ Enter direction: ')
    # Changes the user's location based on their input.
    else:
        current_room = rooms[current_room[input_move]]

