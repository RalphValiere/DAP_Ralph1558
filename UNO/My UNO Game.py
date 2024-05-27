# -*- coding: utf-8 -*-
"""
Created on Fri May 24 16:42:14 2024

@author: Ralph Valery VALIERE
"""

# This is the code for the last UNO version. UNO is a game owned by Mattel and
# all rules, with some modifications, used in this script are coming from:
    # https://www.unorules.com/
# The version I coded is inspired by the latest Classic UNO version.
# But there exists more than a dozen of UNO version. Everytime you want 
# to know what version is being played, please refer to the rules coded here...
# UNO can be played with 2 and up to 10 players.
# YOU WILL NEED INTERNET TO RUN THE GAME. SOME FEATURES REQUIRES A CONNECTION!
# PLEASE! ENJOY!


# >>> Start runnning code here
pip install termcolor
# I found this cool package which allows me to print text in color in the 
# console. It needs to be run first, for the next codes to run.
# You need Internet connection to run it!
class MyUnoGame():
    def __init__(self, number_players, version='classic'):
        
        # Set up for number of players
        while number_players not in range(2,11):            
            print('##\nUNO can only be played with 2 or up to 10 players. ', 
                  'Please choose a integer between 2 and 10.\n')
            number_players = input('Choose the number of players for this game: ') 
            try:
                number_players = int(number_players)
            except ValueError:
                print('\n##\nYou can enter integers ONLY. There is no such thing',
                      ' as 0.5 player or a integer in string format.')                              
        self.number_players = number_players        
        print('##\n Understood!\n Now, each player will enter their username\n',
              'Look for the pop-up box that will appear on the screen.\n',
              'In case it does not appear automatically, check the IDE tab on the Taskbar or Dock,\n',
              'as the pop-up box might be automatically minimized or hidden.\n',
              'Check on your taksbar or Dock to see if the pop-up box has opened.\n')        
        input('Type anything after finishing reading this instruction, to start the process:')
        
        # Set up fo names or psuedo names for players        
        from tkinter import simpledialog
        
            # I learned how to use this package thanks to ChatGPT.
            # This will allow me have input from players when they play their cards.
            # https://chatgpt.com/share/1305c4c4-3329-48c1-93ee-5b17d9bc39fd               
        player_names = {}        
        for num_player in range(1, self.number_players+1):
            id_name = 'Player ' + str(num_player)
            box_text = [id_name,'\n',
                        f'An UNO game started with {self.number_players} other players.\n',
                        'Please enter the username you want to use.']
            user_name = simpledialog.askstring("Pass", ''.join(box_text))
            player_names[id_name] = user_name
        self.player_names = player_names
        
        # Set up for Wild Customizable Cards
        print('\n##\n WELL DONE!.\n',
              ' Before starting the game, please choose rule for "Wild Customizable Cards".\n',
              ' Wild Customizable Cards are all blank at the beginning of the game.\n',
              ' They are meant to select a rule from other available set of rules.\n',
              ' To start the game, each player will choose 1 rule from a set of 3 rules.\n',
              ' The rule with maximum vote will be the one applied to those cards.\n',
              ' If there is a tie, the computer will select randomly from the tied options.\n')        
        input('Type anything after finishing reading this instruction, to start the process:')
        
        self.rule_one = 'Next player hands is shown to you. But they reshufle 1 card.'
        self.rule_two = 'Player with least card pick 2 cards from Draw Pile (person playing this card excluded)'
        self.rule_three = 'Everyone but you will get 2 more cards'              
        
        wild_custom_choice = []
        for num in range(0, self.number_players):
            rule_options = ['Player ' + str(num+1) + ': ' + list(self.player_names.values())[num] + '\n',                            
                            'Please select the rule number you want for the Wild Customizable Cards.\n',
                            'Only insert the number of the rule you prefer.\n',
                            'Do not enter anything else other than a single number.\n',
                            'For example, if you want rule number 1, insert 1.\n\n',
                            'Choose your prefered rule:\n\n',
                            '1- ', self.rule_one, '\n',
                            '2- ', self.rule_two, '\n',
                            '3- ', self.rule_three] 
            rule_choice = simpledialog.askstring("Pass", ''.join(rule_options))            
            while rule_choice not in ['1', '2', '3']:
                print('##\nError: You need to insert a number from 1 to 3.\n')
                rule_choice = simpledialog.askstring("Pass", ''.join(rule_options))
            rule_choice = int(rule_choice)
            wild_custom_choice.append(rule_choice)
        
        import numpy as np
        from numpy import random
        # I have to say it's crazy that Python doesn't have a pre-built mode function
        freq_one = sum(np.array(wild_custom_choice) == 1)
        freq_two = sum(np.array(wild_custom_choice) == 2)
        freq_three = sum(np.array(wild_custom_choice) == 3)
        
        if freq_one > freq_two and freq_one > freq_three:
            wild_custom_rule = self.rule_one
        elif  freq_two > freq_one and freq_two > freq_three:
            wild_custom_rule = self.rule_two
        elif freq_three > freq_one and freq_three > freq_two:
            wild_custom_rule = self.rule_three
        elif freq_one == freq_two and freq_one > freq_three:
            wild_custom_rule = random.choice([self.rule_one, self.rule_two])
        elif freq_one == freq_three and freq_one > freq_two:
            wild_custom_rule = random.choice([self.rule_one, self.rule_three])
        elif freq_two == freq_three and freq_two > freq_one:
            wild_custom_rule = random.choice([self.rule_two, self.rule_three])
        elif freq_one == freq_two and freq_one == freq_three:
            wild_custom_rule = random.choice([self.rule_one, self.rule_two, self.rule_three])
        
        self.wild_custom_rule = wild_custom_rule
        
        # Set up for all other cards
        color_suit = ['red', 'yellow', 'green', 'blue']
        action_nowild = ['Skip', 'Draw Two', 'Reverse']
        ##
        suit_zero = ['0-red', '0-yellow', '0-green', '0-blue']
        suit_nonzero = [str(num)+'-'+col for num in range(1,10) for col in color_suit] * 2
        suit_nowild = [action+'-'+col for action in action_nowild for col in color_suit] * 2
        wild_cards = ['Wild Swap Hand',
                     'Wild Shuffle Hands',
                     'Wild Customizable', 'Wild Customizable', 'Wild Customizable',
                     'Wild', 'Wild', 'Wild', 'Wild',
                     'Wild Draw Four', 'Wild Draw Four', 'Wild Draw Four', 'Wild Draw Four']        
        self.all_card_names = suit_zero + suit_nonzero + suit_nowild + wild_cards
        assert len(self.all_card_names) == 113, 'The number of cards does not add up to 112.'
                
        print('\n AWESOME! You are all set now! You can start the game,\n',
              'by calling the method .play(). You will need to provide game mode.\n',
              'You can also change the max points to win the game. By default, it is 500 points.\n',
              'Depending on the game mode, the max points will be irrelevant.\n',
              'There are three game modes for this version of UNO.\n',
              'Please refer to the rules [using .rule()] to understand each game mode,\n',
              'or any other rules of the game, before you start playing')        
    
    def play(self, game_mode, max_points=500):        
        while game_mode not in ['with_score', 'no_score', 'until_last']:
            print(' ##\n',
                  'Please select a game mode from this list:\n',
                  '["with_score", "no_score", "until_last"]\n',
                  'Please refer to the rules, using .rule(), to understand each game mode.\n')
            game_mode = input('Choose your game mode: ')
        self.game_mode = game_mode
            
        while type(max_points) != int or max_points < 1:
            print(' ##\n',
                  'Please enter a non-zero max points. Accept only integers.\n')
            max_points = input(' Set the maximum points to win the game: ')
            try:
                max_points = int(max_points)
            except ValueError:
                print('\n##\n You can enter integers ONLY. Max points cannot be float/decimals')
        self.max_points = max_points
            
        from termcolor import colored
        pass
    
    def draw_pile(self):
        pass
    
    def discarded_pile(self):
        pass
    
    def score_board(self):
        pass
    
    def all_game_features(self):        
        self.features = ['List of attributes: \n',
                         'number_players\n',
                         'player_names\n',
                         'rule_one\n',
                         'rule_two\n',
                         'rule_three\n',
                         'wild_custom_rule\n',
                         'all_card_names',
                         'game_mode',
                         'max_points',
                         'features\n',
                         '\nList of methods\n',
                         'all_game_features\n',
                         'score_board\n',
                         'draw_pile\n',
                         'discarded_pile\n',
                         'play\n',
                         'rules\n']
        print('This is the list of attributes and methods you can call with an instance of this class:\n')
        print(*self.features)
    
    
    def rules(self):
        print(' ')
        pass


x = [1, 2] + [4, 5]

len(x)

x.append(*[3, 4])

str(0) + '-red'

[1, 2] * 2

print(colored('Manman', 'red'))

abc = MyUnoGame(2)
abc.play('no_score', max_points=0)

type(abc.player_names.values())
abc.player_names.values()
list(abc.player_names.values())[0]

'0-red' * 2
player_names = {}
for num_player in range(1, 11):
    id_game = 'Player ' + str(num_player)
    print(id_game)

x = [1, 2, 2]

x[x == max(x)]

import numpy as np
x = np.array(x)
x[x == max(x)]

sum(x == 1)
def ():    
    root = tk.Tk()
    root.withdraw()
    passw = simpledialog.askstring("Pass", "Enter password")
    return passw

# Rules for the Wild Card Custom

# Every players chooses from a set of 3 options
# The options chosen by the majority (50%+) will be selected as the rule
# If there is a tie between first two options, then computer will select
# randomly from those two options...
# Players will be prompt to accept the random process or reload the entire class


'Every player starts with seven cards.\n~,

'For instance, if the Discard Pile has a red card displayed that is an 8, Player must place either a red card or a card with an 8 on it. '
 sa'
Rest of the cards are in the Draw Pile.
Each card played are placed in the Discard Pile. 
The top card will be displayed (and placed in the Discard Pile) and the game begins!


        
'Every player starts with seven cards, and they are dealt face down. The rest of the 


# I learned how to use this chunk of code thanks to ChatGPT, which allowed me to 
#hide the strings that are input by each players when they start played their cards.
    # https://chatgpt.com/share/1305c4c4-3329-48c1-93ee-5b17d9bc39fd
    
    
import tkinter as tk
from tkinter import simpledialog

def get_pass():
    text = ['The game is about to start.\n',
            'Please enter.\n',
            'We will not tolerate failure on this matter because you suck']
    passw = simpledialog.askstring("Pass", ''.join(text))
    return passw

get_pass()

text = ['The game is about to start.\n',
        'Please enter your password.']

print(''.join(text))



def get_pass():    
    root = tk.Tk()
    root.withdraw()
    passw = simpledialog.askstring("Pass", "Enter password")
    return passw

print(' ### VERSION: CLASSIC\n',
' ##\n',
' ## SET UP\n',
' Every player starts with seven cards.\n', 
' Rest of the cards are in the Draw Pile.\n',
' Each card played are placed in the Discard Pile.\n',
' The top card will be displayed (and placed in the Discard Pile) and the game begins!\n',
' ##\n',
' ## GAME PLAY\n',
' Each player views their cards when they are starting to play.\n',
' Player tries to match the displayed card in the Discard Pile.\n',
' Player must match either by the number, color, or the Symbol/Action.\n',
' For instance, if the Discard Pile has a red card displayed that is an 8,\n',
' Player must place either a red card or a card with an 8 on it.\n',
' Players can also play a Wild card (which can alter current color in play).\n',
' ##\n',
' ##\n',
' If Player has no matches or chooses not to play any of their cards even though\n',
' they might have a match, they must draw a card from the Draw pile.\n',
' If that card can be played, Player must play it. Otherwise, Player keeps the\n',
' card and the game moves on to the next player in turn.\n',
' You can also play a Wild card, or a Wild Draw Four card on your turn.\n',
' ##\n',
' ##\n',
' If first card displayed is an Action card, the Action from that card applies and\n',
' must be carried out by the first player.\n',
' The exceptions are if a Wild or Wild Draw Four card is turned up.:\n',
' - If it is a Wild card, first Player to start can choose whatever color to begin play.\n', 
' - If the first card is a Wild Draw Four card – another card will be displayed.\n', 
' ##\n',
' ##\n',
' Take note that Player can only play one card at a time.\n',
' Player cannot play a Draw Two when a Wild Four is displayed.\n',
' But Player can play a Draw Two when a Draw Two is displayed\n',
' or play a Wild Four when a Wild Four is displayed.\n',
' ##\n',
' ##\n',
' Game continues until a player has one card left. The moment a player has just\n', 
' one card, it will be displayed to all others players that this player is “UNO!”.\n',
' Assuming that Player is unable to play their last card and needs to draw, but after drawing\n',
' is then able to play/discard that penultimate card, the same "UNO" message will b displayed\n',
' Once a player has no cards remaining, the game round is over,\n', 
' points are scored, and the game begins over again.\n',
' The first player to achieve 500 points wins the game.\n',
' ##\n',
' ## CARDS\n',
' This UNO game consists of 113 cards: 25 in each of four color suits (red, yellow, green, blue).\n',
' Each color suit has:\n',
' 	- One zero\n',
' 	- Two each of 1 through 9\n',
' 	- Two each of the action/symbol cards "Skip", "Draw Two", and "Reverse"\n', 
' The deck also contains other action/symbol cards:\n',
'	- Four "Wild" cards\n',
'	- Four "Wild Draw Four"\n', 
'	- One "Wild Swap Hand\n',
'	- One "Wild Shuffle Hands\n',
'	- Three "Wild Customizable"\n',
' ##\n',
' ## ACTION CARDS\n',
' This is how to use the action/symbol cards:\n',
' [Reverse] - The game direction is reversed. If Player 4 plays that card, Player 3 will play, then Player 2,\n',
' and so, instead of having Player 5 then Player 6 and so on.\n',
' Reverse can an only be played on a card that matches by color, or on another Reverse card.\n', 
' If displayed at the beginning of play, game direction is automatically reversed.\n',
' If there is only two Players, Reverse works like Skip\n',
' #\n',
' [Skip] - The next player turn is skipped their turn.\n',
' It can only be played on a card that matches by color, or on another Skip card.\n',
' If displayed at the beginning of play, first player loses turn. The next player starts the game.\n',
' [Draw Two] – Next player gets two more cards and skip their turn.\n',
' #\n',
' It can only be played on a card that matches by color, or on another Draw Two.\n',
' If displayed at the beginning of play, the first player gets two more cards and skip their turn.\n',
' If there is only two Players, If a Player plays a "Draw Two", the next player will get two more cards,\n',
' and then play immediately resumes back on the player who played the "Draw Two" turn.\n',
' #\n',
' [Wild] – This card represents all four colors, and can be played on any card.\n',
' The player has to state which color it will represent for the next player.\n',
' It can be played regardless of whether another card is available.\n',
' If displayed at the beginning of play, first player chooses what color to play.\n',
' #\n',
' [Wild Draw Four] – This acts just like the wild card except that the next player\n',
' also has to get four more cards and skip their turn.\n',
' To play a "Wild Draw Four", Player must have NO other alternative cards to play.\n',
' If played illegally, targeted player may challenge the player who played the "Wild Draw Four".\n',
' If a challenge is called, the hand of the player who played the card will be revealed.\n',
' If guilty, the Player who played the "Wild Draw Four" need to draw 4 cards.\n',
' If not, the challenger needs to draw 6 cards instead.\n',
' A "Wild Draw Four will never be displayed at the beginning of play.\n'
' If there is only two Players, If a Player plays a "Wild Draw Four", the next player will get four more cards,\n',
' (unless there is a challenge) and then play immediately resumes back on the player who played the "Wild Draw Four" turn.\n',
' #\n',
' [Wild Swap Hands Card] – Powerful card that enables you to swap the cards in your hand with any player once.\n',
' Being a Wild card, Player who plays will also choose the color of play for next player.\n', 
' After players swap hands, the turn of Player who played the card will end. It will be the next player turn.\n',
' Ideally, Player will swap hand with the player who has the least number of cards!\n',
' If displayed at the beginning of the game, first player to start gets to choose the color\n',
' and also swap hands with another player.\n',
' #\n',
' [Wild Shuffle Hands Card] – This powerful card reset the game!\n',
' All card in players hand will be collected and shuffled. Then, cards will be dealt evenly to all the players,\n',
' starting with the player next after the person who played the "Wild Shuffle Hands card".\n',
' This means some players may end up with either more or less cards than what they had before.\n',
' Also, person who played the "Wild Shuffle Hands" gets to choose what color to resume play.\n',
' If displayed at the start of the game, first player only chooses the color that begins play.\n',
' #\n',
' [Wild Customizable Card] – They are all blank at the beginning of the game.\n',
' These are meant to select from other available set of rules.\n',
' Before starting the game, every player will choose 1 rule from a set of 3 rules.\n',
' The rule with maximum vote will be the one applied to those cards.\n',
' If there is a tie, the computer will select randomly from the tied options.\n',
' The person who play a "Wild Customized Card" also chooses the color of play.\n',
' After playing this card, the turn of Player who played it will end. It will be the next player turn.\n',
' If displayed at the start, first player only chooses the color of play. Rule does not apply.\n',
' ##\n',
' ## SPECIAL RULES\n',
' If a player last card is a "Wild Swap Hands" or "Wild Shuffle Hands card", the card will be treated\n',
' like a normal "Wild card". Player will play it to end the game. No further action is required.\n',
' if the last card is an Action card, such as a "Draw Two" or a "Wild Draw Four",\n',
' the next player must draw the required cards, even if a player is winning.\n',
' ##\n',
' ## SCORING AND WINNING\n',
' When a player no longer has any cards and the game ends, this player receives points.\n',
' All opponents’ cards are collected and points are counted from those cards.\n',
' The first player to attain 500 points (it could after several games) is the winner.\n',
' The scoring for the cards is as follows:\n',
' 	- Numbered cards (0-9) –> Points = Face value of the card\n',
'	- Draw Two/Skip/Reverse –> 20 points each\n',
'	- Wild Card/Wild Draw Four – 50 points each\n',
'	- Wild Swap Hands/Wild Shuffle Hans/Wild Customizable Cards – 40 points each\n',
' ##\n',
' ## SCORING AND WINNING SPECIAL RULES\n',
' MODE "no_score": Players can also decide to not score and restart the game. The first player who no longer\n',
' has any card left, wins the game. Players can start another game.\n',
' MODE "until_last": Players can decide to keep playing even after another player no longer has any card left.\n',
' Players with no card will slowly be removed from the game until two are left.\n',
' The final two players then challenge each other (under Two Player rules) until one no longer has any card left.\n',
' Players can choose the game mode when launching the play.')