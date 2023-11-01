'''
Program that plays rock paper scissors
plays until the user types 'I quit'

'''

import random

#Global constants
HAND_DICT = {
    'rock' : {'beats' : 'scissors', 
              'beaten_by' : 'paper'},  
    'paper' : {'beats' : 'rock', 
               'beaten_by' : 'scissors'},
    'scissors' : {'beats' : 'paper', 
                  'beaten_by': 'rock'}
}

HANDS = ['rock', 'paper', 'scissors']

def rand_hand() -> str:
    comp_play = random.randint(0, 2)
    for i, hand in enumerate(HANDS):
        comp_play = str(comp_play).replace(str(i), hand)
    return comp_play

def get_user_hand() -> str:
    valid = False
    while valid == False:
        valid = True
        user_play = input('What is your play? (rock / paper / scissors / "I quit" ')
        if user_play.lower() not in HANDS and user_play.lower() != 'i quit':
            print('Invalid input, try again')
            valid = False
    return user_play.lower()


def determine_outcome(user_hand: str, comp_hand: str) -> str:
    # win
    if comp_hand == HAND_DICT[user_hand]['beats']:
        return 'You WIN'
    # lose
    elif comp_hand == HAND_DICT[user_hand]['beaten_by']:
        return 'You LOSE'
    # draw
    elif comp_hand == user_hand.lower():
        return 'Game tied'

def play_game():
    while True:
        # choose hands
        comp_play = rand_hand()
        user_play = get_user_hand()

        # check for exit
        if user_play == 'i quit':
            break
        
        # evaluate
        result = determine_outcome(user_play, comp_play)
        print(result)
    print('Thank you for playing')

if __name__ == '__main__':
    play_game()