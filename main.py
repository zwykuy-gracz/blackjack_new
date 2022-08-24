import random

FIRST_ROUND = True

card_values = {
    'A': 11, 
    '2': 2, 
    '3': 3, 
    '4': 4, 
    '5': 5, 
    '6': 6, 
    '7': 7, 
    '8': 8, 
    '9': 9, 
    'T': 10, 
    'J': 10, 
    'Q': 10, 
    'K': 10,
}

def creating_deck():
    card_values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
    card_suits = ['D', 'H', 'S', 'C']

    deck = []
    for i in range(len(card_values)):
        for j in range(len(card_suits)):
            deck.append(card_values[i] + card_suits[j])
    random.shuffle(deck)
    return deck

def first_round(deck):
    players_hand = ''
    computers_hand = ''
    players_hand += deck[0] + deck[1]
    computers_hand += deck[2]
    return players_hand, computers_hand

def display_hand(players_hand, computers_hand):
    print("computer's hand: ", computers_hand)
    print('Your hand: ', players_hand)

def counting_hand_value(hand):
    hand_value = 0
    for i in range(0, len(hand), 2):
        hand_value += card_values[hand[i]]
    return hand_value

def pulling_card(deck):
    pass

def game_start():
    return starting_hands

def game_play():
    deck = creating_deck()
    starting_hands = first_round(deck)
    current_hand = starting_hands[0]
    computers_hand = starting_hands[1]
    displaying_hands = display_hand
    hand_value = counting_hand_value(starting_hands[0])
    computers_value = counting_hand_value(starting_hands[1])

    user_play = True
    game_on = True
    pulled_cards = 3

    while game_on:

        if user_play:
            displaying_hands(current_hand, computers_hand)
            print('Your hand value:', hand_value)
            if current_hand[0] == current_hand[2] == 'A' or hand_value == 21:
                print('Nice hand!')
                user_play = False
            elif hand_value >= 21:
                print('Too much. You lose!')
                break
            else:
                players_game_choise = input("[H]it me! or [P]ass? ").lower()
                if players_game_choise == 'h':
                    current_hand += deck[pulled_cards]
                    hand_value = counting_hand_value(current_hand)
                    pulled_cards += 1
                elif players_game_choise == 'p':
                    user_play = False

        else: # computer's turn
            if computers_value < hand_value:
                computers_hand += deck[pulled_cards]
                computers_value = counting_hand_value(computers_hand)
                pulled_cards += 1
            elif computers_hand[0] == current_hand[2] == 'A':
                if computers_value == hand_value:
                    print('DRAW!')
                else: print('You lose!')
                displaying_hands(current_hand, computers_hand)
                print("Computer's hand value: ", computers_value)
                game_on = False 
            else:
                if computers_value > 21:
                    print('you won!')
                elif computers_value == current_hand:
                    print('Draw')
                elif computers_value > current_hand:
                    print('You lose!')
                displaying_hands(current_hand, computers_hand)
                print("Computer's hand value: ", computers_value)
                game_on = False 

game_play()