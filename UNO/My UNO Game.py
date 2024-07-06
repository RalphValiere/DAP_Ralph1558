# -*- coding: utf-8 -*-
"""
Created on Fri May 24 16:42:14 2024

@author: Ralph Valery VALIERE
"""

# This is my code for the last UNO game version. UNO is a game owned by Mattel and
# all rules, with some modifications, used in this script are coming from:
    # https://www.unorules.com/
# The version I coded is inspired by the latest Classic UNO version.
# But there exists more than a dozen of UNO version. Everytime you want 
# to know what version is being played, please refer to the rules coded here...
# UNO can be played with 2 and up to 10 players.
# YOU WILL NEED INTERNET TO LAUNCH THE GAME THE FIRST TIME.
# SOME FEATURES REQUIRES A CONNECTION!
# PLEASE! ENJOY! AND DON'T FORGET TO SEND ANY COMMENTS!!!!


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
        input('Type anything after finishing reading this instruction, to start the process: ')
        
        # Set up fo names or psuedo names for players        
        from tkinter import simpledialog
        
            # I learned how to use this package thanks to ChatGPT.
            # This will allow me have input from players when they play their cards.
            # https://chatgpt.com/share/1305c4c4-3329-48c1-93ee-5b17d9bc39fd               
        player_names = {}        
        taken_names = []
        for num_player in range(1, self.number_players+1):
            id_name = 'Player ' + str(num_player)
            box_text = [id_name,'\n',
                        f'An UNO game started with {self.number_players} other players.\n',
                        'Please enter the username you want to use.']
            user_name = simpledialog.askstring("Pass", ''.join(box_text))
            while user_name in taken_names:
                print('##\n##\nThis username is already taken by another player. Choose another one!\n')
                user_name = simpledialog.askstring("Pass", ''.join(box_text))
            taken_names.append(user_name)
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
        input('Type anything after finishing reading this instruction, to start the process: ')
        
        self.rule_one = 'Next player hands is shown to you. But they reshufle 1 card.'
        self.rule_two = 'Player with least card pick 2 cards from Draw Pile (person playing this card excluded)'
        self.rule_three = 'Everyone but you will get 2 more cards'              
        
        wild_custom_choice = []
        for num in range(0, self.number_players):
            rule_options = ['Player ' + list(self.player_names.values())[num] + '\n',                            
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
              'or any other rules of the game, before you start playing.\n')        
    
    def play(self, game_mode, max_points=500):
        from tkinter import simpledialog
        
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
        
        # Distributing cards to players...        
        import random
        from termcolor import colored
        self.pile = self.all_card_names.copy()
        self.discard = []
        players_cards = {}
        for num in range(0, self.number_players):
            user_name = list(self.player_names.values())[num]           
            user_cards = list(random.sample(self.pile, 7))
            players_cards[user_name] = user_cards
            [self.pile.pop(self.pile.index(cards)) for cards in user_cards]
        input('Seven cards distributed to each player. Type anything to continue: ')
        
        # Revealing first top card
        first_card = random.sample(self.pile, 1)
        while first_card[0] == 'Wild Draw Four':
            first_card = random.sample(self.pile, 1)            
        self.pile.pop(self.pile.index(first_card[0]))
        self.discard.append(first_card[0])
        if first_card[0].endswith('-red'):
            print('\nThe first card is ', colored(first_card[0], 'black', on_color='on_red'), '\n')
        elif first_card[0].endswith('-yellow'):
            print('\nThe first card is ', colored(first_card[0], 'black', on_color='on_magenta'), '\n')
        elif first_card[0].endswith('-blue'):
            print('\nThe first card is ', colored(first_card[0], 'black', on_color='on_cyan'), '\n')
        elif first_card[0].endswith('-green'):
            print('\nThe first card is ', colored(first_card[0], 'black', on_color='on_green'), '\n')
        else:
            print('\nThe first card is a: ', first_card[0], )
        
        first_card[0] = 'Wild Shuffle Hands'
        if first_card[0] in ['Wild Swap Hand', 'Wild Shuffle Hands',
                             'Wild Customizable', 'Wild']:
            first_is_wild = True # Initializing condition showing if first card displayed is a wild card"
        else:
            first_is_wild = False # Initializing condition showing if first card displayed is a wild card"
        self.discard.append('Wild Shuffle Hands')

        # Creating a function to put back the discarded cards into the pile, when there is less
        # than 11 cards left in the pile...
        
        def reshuffle_discarded():
            container_reshuffle = []
            if len(self.pile) >= 11:
                pass
            elif len(self.pile) < 11:
                print(f'\nThe pile has less than 10 cards left (only {len(self.pile)} left).\n'
                      'The discarded cards will be reshuffled into the pile,'
                      'except the last displayed card on th discarded pile.\n')
                for position in range(len(self.discard)-1):
                    container_reshuffle.append(self.discard[position])
                    self.pile.append(self.discard[position])
                for card in container_reshuffle:
                    self.discard.pop(self.discard.index(card))
            
        # Creating a function that will ask players to set the color
        # when a wild card is played.
        
        def set_wild_color(wild):
            if wild in ['Wild Swap Hand', 'Wild Shuffle Hands', 'Wild Customizable',
             'Wild', 'Wild Draw Four']:
                wild_color_message = ['Player ' + list(self.player_names.values())[num].upper() + '\n',
                                      'Please select a color for the wild card played or displayed.\n',
                                      'Do not enter anything else other than a single number.\n',
                                      'For example, if you want the color option 1, insert 1, not the color.\n\n',
                                      'Choose your prefered color for the game to continue:\n\n',
                                      '1- red\n',
                                      '2- blue\n',
                                      '3- green\n',
                                      '4- yellow']                                  
                wild_color_chosen = simpledialog.askstring("Pass", ''.join(wild_color_message))
                while wild_color_chosen not in ['1', '2', '3', '4']:
                    print('##\nError: You need to insert a number from the list available.\n')
                    wild_color_chosen = simpledialog.askstring("Pass", ''.join(wild_color_message))
                if wild_color_chosen == '1':
                    color_set = '-red'
                elif wild_color_chosen == '2':
                    color_set = '-blue'
                elif wild_color_chosen == '3':
                    color_set = '-green'
                elif wild_color_chosen == '4':
                    color_set = '-yellow'
            else:
                print('##\nThere might a big bug in the game.\n')
                color_set = 'No color - Game bug'
                
            if color_set == '-red':
                print('\nThe new color called by Player', list(players_cards.keys())[num].upper(), 'is',
                      colored(color_set.upper(), 'black', on_color='on_red'))
            elif color_set == '-blue':
                print('\nThe new color called by Player', list(players_cards.keys())[num].upper(), 'is',
                      colored(color_set.upper(), 'black', on_color='on_cyan'))
            elif color_set == '-green':
                print('\nThe new color called by Player', list(players_cards.keys())[num].upper(), 'is',
                      colored(color_set.upper(), 'black', on_color='on_green'))
            elif color_set == '-yellow':
                print('\nThe new color called by Player', list(players_cards.keys())[num].upper(), 'is',
                      colored(color_set.upper(), 'black', on_color='on_magenta'))
            elif color_set == 'No color - Game bug':
                print('\nThere is bug in the game! Game will exit! Developers will fix it!')
                import sys
                sys.exit()
            return color_set
        
        # Crating a function that analyze card value and determine all possible
        # illegal moves a player can make
        
        def ismove_legal(played):
            if ((self.discard[-1] == ('Draw Two-red') and (not played.endswith('-red') and
                                                           (not played.startswith('W') and
                                                            not played.startswith('Draw Two')))) or
                (self.discard[-1] == ('Draw Two-blue') and (not played.endswith('-blue') and 
                                                            (not played.startswith('W') and
                                                             not played.startswith('Draw Two')))) or
                (self.discard[-1] == ('Draw Two-green') and (not played.endswith('-green') and 
                                                             (not played.startswith('W') and
                                                              not played.startswith('Draw Two')))) or
                (self.discard[-1] == ('Draw Two-yellow') and (not played.endswith('-yellow') and 
                                                              (not played.startswith('W') and
                                                               not played.startswith('Draw Two'))))):
                legality_message = 'Illegal Move'
            elif (((self.discard[-1].startswith('Skip') and self.discard[-1].endswith('-red')) and 
                   (not played.endswith('-red') and (not played.startswith('W') and not played.startswith('Skip')))) or 
                  ((self.discard[-1].startswith('Skip') and self.discard[-1].endswith('-blue')) and 
                   (not played.endswith('-blue') and (not played.startswith('W') and not played.startswith('Skip')))) or 
                  ((self.discard[-1].startswith('Skip') and self.discard[-1].endswith('-green')) and 
                   (not played.endswith('-green') and (not played.startswith('W') and not played.startswith('Skip')))) or 
                  ((self.discard[-1].startswith('Skip') and self.discard[-1].endswith('-yellow')) and 
                    (not played.endswith('-yellow') and (not played.startswith('W') and not played.startswith('Skip'))))):                
                legality_message = 'Illegal Move'
            elif (((self.discard[-1].startswith('Reverse') and self.discard[-1].endswith('-red')) and 
                   (not played.endswith('-red') and (not played.startswith('W') and not played.startswith('Reverse')))) or 
                  ((self.discard[-1].startswith('Reverse') and self.discard[-1].endswith('-blue')) and 
                   (not played.endswith('-blue') and (not played.startswith('W') and not played.startswith('Reverse')))) or 
                  ((self.discard[-1].startswith('Reverse') and self.discard[-1].endswith('-green')) and 
                   (not played.endswith('-green') and (not played.startswith('W') and not played.startswith('Reverse')))) or 
                  ((self.discard[-1].startswith('Reverse') and self.discard[-1].endswith('-yellow')) and 
                    (not played.endswith('-yellow') and (not played.startswith('W') and not played.startswith('Reverse'))))):
                legality_message = 'Illegal Move'
            elif ((self.discard[-1].startswith('W') and self.wild_color == '-red') and
                  (not played.endswith('-red') and not played.startswith('W'))):
                legality_message = 'Illegal Move'
            elif ((self.discard[-1].startswith('W') and self.wild_color == '-blue') and
                  (not played.endswith('-blue') and not played.startswith('W'))):
                legality_message = 'Illegal Move'
            elif ((self.discard[-1].startswith('W') and self.wild_color == '-green') and
                  (not played.endswith('-green') and not played.startswith('W'))):
                legality_message = 'Illegal Move'
            elif ((self.discard[-1].startswith('W') and self.wild_color == '-yellow') and
                  (not played.endswith('-yellow') and not played.startswith('W'))):
                legality_message = 'Illegal Move'
            elif ((self.discard[-1].endswith('-red') and not played.endswith('-red') or
                   self.discard[-1].endswith('-blue') and not played.endswith('-blue') or
                   self.discard[-1].endswith('-green') and not played.endswith('-green') or
                   self.discard[-1].endswith('-yellow') and not played.endswith('-yellow'))
                  and
                  ((self.discard[-1][0].isdigit() and (not played[0].isdigit() and not played.startswith('W'))) or
                  (not self.discard[-1][0].isdigit() and played[0].isdigit()) or
                  ((self.discard[-1][0].isdigit() and played[0].isdigit()) and
                   self.discard[-1][0] != played[0]))):
                legality_message = 'Illegal Move'
            else:
                legality_message = 'Legal Move'                
            return legality_message
        
        # Now, Players plays until end of game
        quantity_players = self.number_players
        skip_next_player = True
        draw_two_skip = True
        draw_four_skip = True
        self.wild_color = '' # Initializing color for Wild cards
        self.show_card = '' # Initializing the command to show a player's card
        while all(len(hand) != 0 for hand in players_cards.values()):
            while quantity_players > 1:
                self.number_players_left = 0
                player_who_left = []
                for num in range(0, quantity_players):
                    # Initializing player's turn
                    displayed_hand = []
                    number_card = len(list(players_cards.values())[num])
                    number_options = []
                    for position in range(0, number_card):
                        card_face = list(players_cards.values())[num][position]
                        card_list = ''.join([str(position+1), ') ',
                                             str(card_face), '\n'])
                        displayed_hand.append(card_list)
                        number_options.append(str(position+1))                    
                    displayed_hand = ''.join(displayed_hand)
                    number_options.append('888')
                    number_options.append('999')
                    number_options.append('000')
                    options_message = [list(players_cards.keys())[num].upper(), '\n',
                                      'Your turn!\n', 'Please choose the card you want to play.\n',
                                      'Here is your hand: \n\n',
                                      displayed_hand,
                                      '888) Pass (or Draw cards if required)\n',
                                      '999) Concede the game']
                    draw_two_message = [list(players_cards.keys())[num].upper(), '\n',
                                      'A Draw Two card has been played! You can draw two cards or\n',
                                      'quit the game: \n\n',
                                      '888) Pass (or Draw cards if required)\n',
                                      '999) Concede the game']
                    wild_four_message = [list(players_cards.keys())[num].upper(), '\n\n',
                                      'A Wild Draw Four card has been played! You can draw four cards or\n',
                                      'challenge (refer to rules for challenge) or quit the game: \n\n',
                                      '888) Pass (or Draw cards if required)\n',
                                      '999) Concede the game\n',
                                      '000) Challenge the Wild Draw Four']
                    
                    swap_hand_message = ['Choose the player you want to swap hands with:\n\n',
                                         ''.join([str(list(players_cards.keys()).index(player)+1) + '- ' + player.upper() +
                                                  ' has ' + str(len(qt)) +
                                                  ' cards\n' for player, qt in players_cards.items()]),
                                         '888- No swap (choose color only)']
                    
                    # Create a function to run validity and legality test when card is
                    # played by players
                    
                    def test_validity():
                        validity_condition = False # Condition for validity of option chosen
                        legality_condition = False # Condition for legality of option chosen
                        while not (legality_condition and validity_condition):
                            option_chosen = simpledialog.askstring("Pass", ''.join(options_message))
                            legality_result = ''
                            try:
                                       if option_chosen == '888' or option_chosen == '999':
                                           card_face_played = []
                                           legality_result = 'Legal Move'
                                       else:
                                           card_face_played = list(players_cards.values())[num][int(option_chosen)-1]
                                           legality_result = ismove_legal(card_face_played)
                            except IndexError:
                                print('##\nError: You need to insert a number from the list available.\n')
                            if option_chosen not in number_options and legality_result != 'Legal Move':
                                validity_condition = False
                                legality_condition = False
                            elif option_chosen in number_options and legality_result != 'Legal Move':
                                validity_condition = True
                                legality_condition = False
                                print('##\nIllegal Move: Choose another card. Refer to rules to see legal moves.\n')
                            elif option_chosen not in number_options and legality_result == 'Legal Move':
                                validity_condition = False
                                legality_condition = True                            
                            elif option_chosen in number_options and legality_result == 'Legal Move':
                                validity_condition = True
                                legality_condition = True
                        return option_chosen
                    
                    # Create another function to run validity and legality test when card is
                    # played by players, but specifically for Draw Two cases
                    
                    def test_validity_dt():
                        validity_condition = False # Condition for validity of option chosen
                        legality_condition = False # Condition for legality of option chosen
                        while not (legality_condition and validity_condition):
                            option_chosen = simpledialog.askstring("Pass", ''.join(draw_two_message))
                            legality_result = ''
                            try:
                                       if option_chosen == '888' or option_chosen == '999':
                                           card_face_played = []
                                           legality_result = 'Legal Move'
                                       else:
                                           legality_result = 'Illegal Move'
                            except IndexError:
                                print('##\nError: You need to insert a number from the list available.\n')
                            if option_chosen not in number_options and legality_result != 'Legal Move':
                                validity_condition = False
                                legality_condition = False
                            elif option_chosen in number_options and legality_result != 'Legal Move':
                                validity_condition = True
                                legality_condition = False
                                print('##\nIllegal option: Choose another option.\n')
                            elif option_chosen not in number_options and legality_result == 'Legal Move':
                                validity_condition = False
                                legality_condition = True                            
                            elif option_chosen in number_options and legality_result == 'Legal Move':
                                validity_condition = True
                                legality_condition = True
                        return option_chosen
                    
                    # Create a third function to run validity and legality test when card is
                    # played by players, but specifically for Wild Draw Four cases
                    
                    def test_validity_wdf():
                        validity_condition = False # Condition for validity of option chosen
                        legality_condition = False # Condition for legality of option chosen
                        while not (legality_condition and validity_condition):
                            option_chosen = simpledialog.askstring("Pass", ''.join(wild_four_message))
                            legality_result = ''
                            try:
                                       if (option_chosen == '888' or
                                           option_chosen == '999' or
                                           option_chosen == '000'):
                                           card_face_played = []
                                           legality_result = 'Legal Move'
                                       else:
                                           legality_result = 'Illegal Move'
                            except IndexError:
                                print('##\nError: You need to insert a number from the list available.\n')
                            if option_chosen not in number_options and legality_result != 'Legal Move':
                                validity_condition = False
                                legality_condition = False
                            elif option_chosen in number_options and legality_result != 'Legal Move':
                                validity_condition = True
                                legality_condition = False
                                print('##\nIllegal option: Choose another option.\n')
                            elif option_chosen not in number_options and legality_result == 'Legal Move':
                                validity_condition = False
                                legality_condition = True                            
                            elif option_chosen in number_options and legality_result == 'Legal Move':
                                validity_condition = True
                                legality_condition = True
                        return option_chosen
                    
                    # Creating a function to swap hands when wild card ask to do that
                    
                    def swap_hands():
                        swap_validity_condition = False # Condition for validity of player chosen for swap
                        while not swap_validity_condition:
                            player_chosen = simpledialog.askstring('Pass', ''.join(swap_hand_message))
                            try:
                                if int(player_chosen) == num+1:
                                    print('You cannot choose your own hand. If you do not want to swap hand,',
                                          'please select option 888.\n')
                                elif int(player_chosen) != num+1 and int(player_chosen) in range(1, quantity_players+1):
                                    hand_player_swapping = list(players_cards.values())[num]
                                    hand_player_swapped = list(players_cards.values())[int(player_chosen)-1]
                                    players_cards[list(players_cards.keys())[num]] = hand_player_swapped
                                    players_cards[list(players_cards.keys())[int(player_chosen)-1]] = hand_player_swapping
                                    print('Player', list(players_cards.keys())[num].upper(), 'has swapped hands with',
                                          'Player', list(players_cards.keys())[int(player_chosen)-1].upper(), '\n')
                                    swap_validity_condition = True
                                elif player_chosen == '888':
                                    print('Player', list(players_cards.keys())[num].upper(), 'decided not to',
                                          'swap hands with any player. Player will pick color.\n')
                                    swap_validity_condition = True
                                elif player_chosen != '888' and int(player_chosen) not in range(1, quantity_players+1):
                                    print('##\nError: You need to insert a number from the list available.\n')
                            except IndexError:
                                print('##\nError: You need to insert a number from the list available.\n')
                            except ValueError:
                                print('##\nError: You need to insert a number from the list available.\n')
                    
                    # Creating a function to shuffle all cards in players' hands
                    
                    def shuffle_hands():
                        shuffle_container = []
                        [shuffle_container.append(card) for hand in list(players_cards.values()) for card in hand]
                        for player in list(players_cards.keys()):
                            players_cards[player] = []
                        position_next_player = num+1
                        while shuffle_container != []:
                            while position_next_player < quantity_players:
                                try:
                                    card_redistributed = random.choice(shuffle_container)
                                    player_targeted = list(players_cards.keys())[position_next_player]
                                    players_cards[player_targeted].append(card_redistributed)
                                    shuffle_container.pop(shuffle_container.index(card_redistributed))
                                    position_next_player += 1
                                except IndexError:
                                    print('No more card to distribute')
                                    break
                            position_next_player = 0
                    
                    # Creating a function to analyze action when 1 or more players abandon the game
                    
                    def player_quit():
                        if quantity_players > 2:
                            player_who_left.append(list(players_cards.keys())[num])
                            print('\nPlayer', list(players_cards.keys())[num].upper(), 'has left the game.\n')
                            self.number_players_left += 1
                        elif quantity_players < 3:
                            del players_cards[list(players_cards.keys())[num]]
                            print('\n', '#######', list(players_cards.keys())[0].upper(), 'has won the game. #######\n')
                            input('Type anything to exit the game: ')
                            print(' ')
                            import sys
                            sys.exit()
                    
                    # Creating a function to trigger the action- play a card
                    
                    def play_acard():
                        card_played = list(players_cards.values())[num][int(option_chosen)-1]
                        index_card = players_cards[list(players_cards.keys())[num]].index(card_played)
                        players_cards[list(players_cards.keys())[num]].pop(index_card)
                        self.discard.append(card_played)
                        if card_played.startswith('W') and card_played == 'Wild Swap Hand':
                            print('Player', list(players_cards.keys())[num].upper(), 'has played: ', card_played, '\n')
                            swap_hands()
                            print('The new displayed card is a: ', self.discard[-1], '\n')
                            self.wild_color = set_wild_color(card_played)
                        elif card_played.startswith('W') and card_played == 'Wild Shuffle Hands':
                            print('Player', list(players_cards.keys())[num].upper(), 'has played a Wild Shuffle Hands.\n',
                                  'All card in players hand will be collected and shuffled.\n',
                                  'Then, cards will be dealt evenly to all the players,\n',
                                  'starting with the next player after the one who played the "Wild Shuffle Hands".\n')
                            shuffle_hands()
                            print('All reshuffled cards have been distributed.\n')
                            for player in list(players_cards.keys()):
                                print('Player', player, 'received', len(players_cards[player]), 'cards.\n')
                            input('Type anything to continue: ')
                        elif card_played.startswith('W') and card_played not in ['Wild Swap Hand', 'Wild Shuffle Hands']:
                            self.wild_color = set_wild_color(card_played)
                            print('Player', list(players_cards.keys())[num].upper(), 'has played: ', card_played, '\n')
                            print('The new displayed card is a: ', self.discard[-1], '\n')
                        else:
                            print('Player', list(players_cards.keys())[num].upper(), 'has played: ', card_played, '\n')
                            if self.discard[-1].endswith('-red'):
                                print('The new displayed card is ', colored(self.discard[-1], 'black', on_color='on_red'), '\n')
                            elif self.discard[-1].endswith('-yellow'):
                                print('The new displayed is ', colored(self.discard[-1], 'black', on_color='on_magenta'), '\n')
                            elif self.discard[-1].endswith('-blue'):
                                print('The new displayed is ', colored(self.discard[-1], 'black', on_color='on_cyan'), '\n')
                            elif self.discard[-1].endswith('-green'):
                                print('The new displayed is ', colored(self.discard[-1], 'black', on_color='on_green'), '\n')
                            else:
                                print('\nThe new displayed card is a: ', self.discard[-1])
                    
                    # Creating a function that displayed previous or next player's card
                    
                    def show_player_card():
                        if self.show_card == 'Next':
                            if num == quantity_players - 1:
                                print('Player ', list(players_cards.keys())[0].upper(), 'cards will be displayed.\n')
                                print(list(players_cards.keys())[0].upper(), 'hand is: ')
                                print(list(players_cards.values())[0])
                                self.show_card = ''
                                pass
                            else:
                                print('Player ', list(players_cards.keys())[num+1].upper(), 'cards will be displayed.\n')
                                print(list(players_cards.keys())[num+1].upper(), 'hand is: ')
                                print(list(players_cards.values())[num+1])
                                self.show_card = ''
                        elif self.show_card == 'Prev':
                            if num == 0:
                                print('Player ', list(players_cards.keys())[quantity_players - 1].upper(), 'cards will be displayed.\n')
                                print(list(players_cards.keys())[quantity_players - 1].upper(), 'hand is: ')
                                print(list(players_cards.values())[quantity_players - 1])
                                self.show_card = ''
                                pass
                            else:
                                print('Player ', list(players_cards.keys())[num-1].upper(), 'cards will be displayed.\n')
                                print(list(players_cards.keys())[num-1].upper(), 'hand is: ')
                                print(list(players_cards.values())[num-1])
                                self.show_card = '' 
                            
                    # Analyzing displayed discarded card and determining action for player
                    ## When there is a Draw Two displayed
                    if self.discard[-1].startswith('Draw Two'):
                        if draw_two_skip == True:
                            draw_two_skip = False
                            option_chosen = test_validity_dt()
                            if option_chosen == '888':
                                reshuffle_discarded()
                                get_two_cards = list(random.sample(self.pile, 2))
                                players_cards[list(players_cards.keys())[num]].append(get_two_cards[0])
                                players_cards[list(players_cards.keys())[num]].append(get_two_cards[1])
                                self.pile.pop(self.pile.index(get_two_cards[0]))
                                self.pile.pop(self.pile.index(get_two_cards[1]))
                                print('\nPlayer', list(players_cards.keys())[num].upper(), 'has picked two more cards.\n')
                            elif option_chosen == '999':
                                player_quit()
                        elif draw_two_skip == False:
                            option_chosen = test_validity()
                            if option_chosen == '888':
                                reshuffle_discarded()
                                get_one_card = list(random.sample(self.pile, 1))
                                players_cards[list(players_cards.keys())[num]].append(get_one_card[0])
                                self.pile.pop(self.pile.index(get_one_card[0]))
                            elif option_chosen == '999':
                                player_quit()
                            else:
                                draw_two_skip = True
                                play_acard()
                                
                    ## When there is a Skip displayed
                    elif self.discard[-1].startswith('Skip'):
                        if skip_next_player == True:
                            skip_next_player = False
                            print('\nPlayer', list(players_cards.keys())[num].upper(), 'has been skipped.')
                            continue
                        elif skip_next_player == False:
                            option_chosen = test_validity()
                            if option_chosen == '888':
                                reshuffle_discarded()
                                get_one_card = list(random.sample(self.pile, 1))
                                players_cards[list(players_cards.keys())[num]].append(get_one_card[0])
                                self.pile.pop(self.pile.index(get_one_card[0]))
                            elif option_chosen == '999':
                                player_quit()
                            else:
                                skip_next_player = True
                                play_acard()
                                
                    ## When there is a Reverse displayed
                    elif self.discard[-1].startswith('Reverse'):
                        pass
                    
                    ## When there is a Wild displayed
                    elif self.discard[-1] == 'Wild':
                        if first_is_wild:
                            print('The first card is a Wild.\n',
                                  'Please choose the color before you can start playing.\n')
                            self.wild_color = set_wild_color(self.discard[-1])
                            option_chosen = test_validity()
                            if option_chosen == '888':
                                reshuffle_discarded()
                                get_one_card = list(random.sample(self.pile, 1))
                                players_cards[list(players_cards.keys())[num]].append(get_one_card[0])
                                self.pile.pop(self.pile.index(get_one_card[0]))
                            elif option_chosen == '999':
                                player_quit()
                            else:
                                play_acard()
                            first_is_wild = False
                        elif not first_is_wild:
                            option_chosen = test_validity()
                            if option_chosen == '888':
                                reshuffle_discarded()
                                get_one_card = list(random.sample(self.pile, 1))
                                players_cards[list(players_cards.keys())[num]].append(get_one_card[0])
                                self.pile.pop(self.pile.index(get_one_card[0]))
                            elif option_chosen == '999':
                                player_quit()
                            else:
                                play_acard()
                    
                    ## When there is a Wild Draw Four displayed
                    elif self.discard[-1] == 'Wild Draw Four':
                        if draw_four_skip == True:
                            draw_four_skip = False
                            option_chosen = test_validity_wdf()
                            if option_chosen == '888':
                                reshuffle_discarded()
                                get_four_cards = list(random.sample(self.pile, 4))
                                players_cards[list(players_cards.keys())[num]].append(get_four_cards[0])
                                players_cards[list(players_cards.keys())[num]].append(get_four_cards[1])
                                players_cards[list(players_cards.keys())[num]].append(get_four_cards[2])
                                players_cards[list(players_cards.keys())[num]].append(get_four_cards[3])
                                self.pile.pop(self.pile.index(get_four_cards[0]))
                                self.pile.pop(self.pile.index(get_four_cards[1]))
                                self.pile.pop(self.pile.index(get_four_cards[2]))
                                self.pile.pop(self.pile.index(get_four_cards[3]))
                                print('\nPlayer', list(players_cards.keys())[num].upper(),
                                      'has picked four more cards')
                            elif option_chosen == '999':
                                player_quit()
                            elif option_chosen == '000':
                                self.show_card = 'Prev'
                                print('\nPlayer', list(players_cards.keys())[num].upper(),
                                      'has challenged the "Wild Draw Four".\n')
                                show_player_card()
                                if num == 0:
                                    number_valid_move = 0
                                    for card in list(players_cards.values())[quantity_players - 1]:
                                        if card == 'Wild Draw Four':
                                            pass
                                        elif ismove_legal(card) == 'Illegal Move':
                                            number_valid_move += 0
                                        elif ismove_legal(card) == 'Legal Move':
                                            number_valid_move += 1
                                    if number_valid_move > 0:
                                        print('Challenge succesful!!!\n',
                                              'Player', list(players_cards.keys())[quantity_players - 1].upper(),
                                              'made an illegal move and will pick the four cards instead.\n')
                                        reshuffle_discarded()
                                        get_four_cards = list(random.sample(self.pile, 4))
                                        players_cards[list(players_cards.keys())[quantity_players - 1]].append(get_four_cards[0])
                                        players_cards[list(players_cards.keys())[quantity_players - 1]].append(get_four_cards[1])
                                        players_cards[list(players_cards.keys())[quantity_players - 1]].append(get_four_cards[2])
                                        players_cards[list(players_cards.keys())[quantity_players - 1]].append(get_four_cards[3])
                                        self.pile.pop(self.pile.index(get_four_cards[0]))
                                        self.pile.pop(self.pile.index(get_four_cards[1]))
                                        self.pile.pop(self.pile.index(get_four_cards[2]))
                                        self.pile.pop(self.pile.index(get_four_cards[3]))
                                        print('\nPlayer', list(players_cards.keys())[quantity_players - 1].upper(),
                                              'has picked four more cards.\n')
                                        option_chosen = test_validity()
                                        play_acard()
                                    elif number_valid_move == 0:
                                        print('Challenge failed!!!\n',
                                              'Player', list(players_cards.keys())[quantity_players - 1].upper(),
                                              'made an legal move.\n',
                                              'Player', list(players_cards.keys())[num].upper(),
                                              'will pick 6 cards instead.\n')
                                        reshuffle_discarded()
                                        get_six_cards = list(random.sample(self.pile, 6))
                                        players_cards[list(players_cards.keys())[num]].append(get_six_cards[0])
                                        players_cards[list(players_cards.keys())[num]].append(get_six_cards[1])
                                        players_cards[list(players_cards.keys())[num]].append(get_six_cards[2])
                                        players_cards[list(players_cards.keys())[num]].append(get_six_cards[3])
                                        players_cards[list(players_cards.keys())[num]].append(get_six_cards[4])
                                        players_cards[list(players_cards.keys())[num]].append(get_six_cards[5])
                                        self.pile.pop(self.pile.index(get_six_cards[0]))
                                        self.pile.pop(self.pile.index(get_six_cards[1]))
                                        self.pile.pop(self.pile.index(get_six_cards[2]))
                                        self.pile.pop(self.pile.index(get_six_cards[3]))
                                        self.pile.pop(self.pile.index(get_six_cards[4]))
                                        self.pile.pop(self.pile.index(get_six_cards[5]))
                                        print('\nPlayer', list(players_cards.keys())[num].upper(),
                                              'has picked six more cards.\n')
                                else:
                                    number_valid_move = 0
                                    for card in list(players_cards.values())[num-1]:
                                        if card == 'Wild Draw Four':
                                            pass
                                        elif ismove_legal(card) == 'Illegal Move':
                                            number_valid_move += 0
                                        elif ismove_legal(card) == 'Legal Move':
                                            number_valid_move += 1
                                    if number_valid_move > 0:
                                        print('\nChallenge succesful!!!\n',
                                              'Player', list(players_cards.keys())[num-1].upper(),
                                              'made an illegal move and will pick the four cards instead.\n')
                                        reshuffle_discarded()
                                        get_four_cards = list(random.sample(self.pile, 4))
                                        players_cards[list(players_cards.keys())[num-1]].append(get_four_cards[0])
                                        players_cards[list(players_cards.keys())[num-1]].append(get_four_cards[1])
                                        players_cards[list(players_cards.keys())[num-1]].append(get_four_cards[2])
                                        players_cards[list(players_cards.keys())[num-1]].append(get_four_cards[3])
                                        self.pile.pop(self.pile.index(get_four_cards[0]))
                                        self.pile.pop(self.pile.index(get_four_cards[1]))
                                        self.pile.pop(self.pile.index(get_four_cards[2]))
                                        self.pile.pop(self.pile.index(get_four_cards[3]))
                                        print('\nPlayer', list(players_cards.keys())[num-1].upper(),
                                              'has picked four more cards.\n')
                                        option_chosen = test_validity()
                                        play_acard()
                                    elif number_valid_move == 0:
                                        print('\nChallenge failed!!!\n',
                                              'Player', list(players_cards.keys())[num-1].upper(),
                                              'made an legal move.\n',
                                              'Player', list(players_cards.keys())[num].upper(),
                                              'will pick 6 cards instead.\n')
                                        reshuffle_discarded()
                                        get_six_cards = list(random.sample(self.pile, 6))
                                        players_cards[list(players_cards.keys())[num]].append(get_six_cards[0])
                                        players_cards[list(players_cards.keys())[num]].append(get_six_cards[1])
                                        players_cards[list(players_cards.keys())[num]].append(get_six_cards[2])
                                        players_cards[list(players_cards.keys())[num]].append(get_six_cards[3])
                                        players_cards[list(players_cards.keys())[num]].append(get_six_cards[4])
                                        players_cards[list(players_cards.keys())[num]].append(get_six_cards[5])
                                        self.pile.pop(self.pile.index(get_six_cards[0]))
                                        self.pile.pop(self.pile.index(get_six_cards[1]))
                                        self.pile.pop(self.pile.index(get_six_cards[2]))
                                        self.pile.pop(self.pile.index(get_six_cards[3]))
                                        self.pile.pop(self.pile.index(get_six_cards[4]))
                                        self.pile.pop(self.pile.index(get_six_cards[5]))
                                        print('\nPlayer', list(players_cards.keys())[num].upper(),
                                              'has picked six more cards.\n')
                        elif draw_four_skip == False:
                            option_chosen = test_validity()
                            if option_chosen == '888':
                                reshuffle_discarded()
                                get_one_card = list(random.sample(self.pile, 1))
                                players_cards[list(players_cards.keys())[num]].append(get_one_card[0])
                                self.pile.pop(self.pile.index(get_one_card[0]))
                            elif option_chosen == '999':
                                player_quit()
                            else:
                                play_acard()
                                draw_four_skip = True
                    
                    ## When there is a Wild Swap Hand displayed
                    elif self.discard[-1] == 'Wild Swap Hand':
                        if first_is_wild:
                            print('The first card is a Wild Swap Hands. You can swap hand with one player',
                                  'and just choose a color.\nOr you can decide to not swap and choose the color only.\n')
                            swap_hands()
                            set_wild_color('Wild Swap Hand')
                            option_chosen = test_validity()
                            if option_chosen == '888':
                                reshuffle_discarded()
                                get_one_card = list(random.sample(self.pile, 1))
                                players_cards[list(players_cards.keys())[num]].append(get_one_card[0])
                                self.pile.pop(self.pile.index(get_one_card[0]))
                            elif option_chosen == '999':
                                player_quit()
                            else:
                                play_acard()
                            first_is_wild = False
                        elif not first_is_wild:
                            option_chosen = test_validity()
                            if option_chosen == '888':
                                reshuffle_discarded()
                                get_one_card = list(random.sample(self.pile, 1))
                                players_cards[list(players_cards.keys())[num]].append(get_one_card[0])
                                self.pile.pop(self.pile.index(get_one_card[0]))
                            elif option_chosen == '999':
                                player_quit()
                            else:
                                play_acard()
                    
                    ## When there is a Wild Shuffle Hand
                    elif self.discard[-1] == 'Wild Shuffle Hands':
                        if first_is_wild:
                            print('The first card is a Wild Shuffle Hands.\n',
                                  'Please choose the color before you can start playing.\n')
                            self.wild_color = set_wild_color(self.discard[-1])
                            option_chosen = test_validity()
                            if option_chosen == '888':
                                reshuffle_discarded()
                                get_one_card = list(random.sample(self.pile, 1))
                                players_cards[list(players_cards.keys())[num]].append(get_one_card[0])
                                self.pile.pop(self.pile.index(get_one_card[0]))
                            elif option_chosen == '999':
                                player_quit()
                            else:
                                play_acard()
                            first_is_wild = False
                        elif not first_is_wild:
                            option_chosen = test_validity()
                            if option_chosen == '888':
                                reshuffle_discarded()
                                get_one_card = list(random.sample(self.pile, 1))
                                players_cards[list(players_cards.keys())[num]].append(get_one_card[0])
                                self.pile.pop(self.pile.index(get_one_card[0]))
                            elif option_chosen == '999':
                                player_quit()
                            else:
                                play_acard()
                    
                    ## When there is a Wild Customizable
                    elif self.discard[-1] == 'Wild Customizable':
                    
                    
                # Compiling iteration and actions and reset turns
                quantity_players -= self.number_players_left
                if self.number_players_left == 0:
                    pass
                elif self.number_players_left > 0:
                    if quantity_players == 1:
                        for left in player_who_left:
                            del players_cards[left]
                        print('\n', '#######', list(players_cards.keys())[0], 'has won the game. #######\n')
                        input('Type anything to exit the system: ')
                        import sys
                        sys.exit()
                    elif quantity_players > 1:
                        [self.pile.append(cards) for left in player_who_left for cards in players_cards[left]]
                        for left in player_who_left:
                            del players_cards[left]
                            
                # Validating Card choice
                
                # Compiling
                # Compiling discarded cards and reseting
                
                            
    def draw_pile(self):
        print(self.pile)
    
    def discarded_pile(self):
        print(self.discard)
        print(self.discard[-1], ' is the card at the top of the discarded pile.')
    
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
                         'all_card_names\n',
                         'game_mode\n',
                         'max_points\n',
                         'features\n',
                         'pile\n',
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


abc = MyUnoGame(3)
abc.play('with_score', max_points=500)
len(abc.pile)

['sasa' +
 'Papa']

#########
x = [1, "2", 'a', 4, "5", "6", 7]

from numpy import random
import random
random.choice(x)
random.sample(x, 1)

type(x[0])
y = [2 * a for a in x]
str()
x.index(4)
[a + b for a,b in xy]




import numpy
numpy.array(x) * 2



print(f'length of x is {len(x)}')
w = []
w.append(x[0])

for i in range(len(x)-1):
    w.append(x[i])

for a in w:
    x.pop(x.index(a))
#######

y = {'a':[1, 2], 'b':[4, 6], 'c':[9, 7]}

len(y['a'])

[a**2 for p in list(y.values()) for a in p]

y['a'] = [10, 11]

str(list(y.keys()).index('c'))


ya = ['Bon. Banm test\n', ''.join(yax)]
yax = ['- ' + player.upper() + ' has ' + 
 str(len(qt)) + ' cards\n' for player, qt in y.items()]

print(''.join(ya))

y['b'].pop(y['b'].index(6))

def test():
    print('Papa')

test()

test = False

if test == False:
    print('ajsa')

import random
y = list(random.sample(x, 2))
type(random.sample(x, 2))
y.append(3)
print(random.sample(x, 2).append(3))

x = 5
x += -2
x
def test():
    x = 3
    return x
print(test())
x = test()


y = [[1, 2], [3, 6]]
[a-1 for a in x for x in y]


mydict = {'a':[1, 2], 'b':[3, 4]}
mydict[list(mydict.keys())[1]]
abc = [a for a in mydict[list(mydict.keys())[1]]]
abc
print(colored('first_card', 'black', on_color = 'on_green'))





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
' You can not play a Draw Two over another Draw two. I am sorry. That is the rule.\n',
' See this funny video of Trevor Noah, confirming it:\n',
' https://www.youtube.com/shorts/s3BRHS_JjD8 \n',
' You cannot play a Draw Four on a Draw Two to make the next player draw 6 cards.\n',
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
' You cannot play a Draw Four over a Draw Four to make next player draw 8 card.\n',
' You cannot play a Draw Two on a Draw Four to make the next player draw 6 cards.\n',
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