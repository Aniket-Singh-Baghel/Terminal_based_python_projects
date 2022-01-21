import random

suits = ('heart', 'diamond', 'clubs', 'spades')

cards = ('two', 'three', 'four', 'five', 'six', 'seven',
         'eight', 'nine', 'jack', 'queen', 'king', 'ace')

face_value = {'two': 2, 'three': 3, 'four': 4,  'five': 5, 'six': 6, 'seven': 7,
              'eight': 8, 'nine': 9, 'jack': 10, 'queen': 10, 'king': 10, 'ace': 11}

# creating deck 

deck = []

def card_deck():
    for suit in suits:
        for card in cards:
            deck.append(card + ' of ' + suit)


# take_bet

total_chips = 100

def take_bet():
    while 1:
        try:
            bet = int(input("Enter your bet"))
        except Exception as m:
            print(m.__class__.__name__)
            print("Invalid Input")
            continue
        if bet > total_chips:
            print('You dont have enough chips')
            continue
        elif bet==0:
            print("Enter the valid amount of chip")
            continue
        else:
            return bet

# player cards
def show_player_card():
    print('\nthese are players card\n')
    for i in players_cards:
        print(i)
    print('\nthese are dealers card\n')
    for j in dealers_cards:
        if dealers_cards.index(j) == 0:
            print('one card is hidden')
        else:
            print(j)
#player score
ace_count = {}
def calculate_player_score():
    global player_score
    # player_score = 0

    for i in players_cards:
        if i not in ps:
            player_score += face_value[i.split()[0]]
            if i.split()[0] == 'ace':
                if i not in ace_count:
                    ace_count[i] = 1
            ps.append(i)
    if player_score>21:
        for i in ace_count:
            if ace_count[i] == 1:
                player_score -=10
                ace_count[i] = 0       
#dealer score
def calculate_dealer_score():
    global dealer_score
    dealer_score = 0

    for i in dealers_cards:
        s = i.split()[0]
        fv = face_value[s]
        dealer_score += fv

class WrongPassword(Exception):
            def __init__(self, msg):
                self.msg = msg
def hit_stand():
    global player_playing
    while True:        
        a = input('Enter hit or stand\n')
        try:
            if a[0] == 'h' or a[0] == 's':
                print("Welcome")
            else:
                raise WrongPassword("Inavlid Input")
        if a[0] == 'h':
            players_cards.append(deck.pop())
        elif a[0] == 's':
            player_playing = False
        else:
            continue
        break

def show_all_card():
    print('\nthese are players card\n')
    for i in players_cards:
        print(i)
    print('\nthese are dealers card\n')
    for j in dealers_cards:
        print(j)
    print("Player's score is", player_score)
    print("Dealer's score is", dealer_score)


# game starts
while True:
    card_deck()
    random.shuffle(deck)

    bet = take_bet()

    players_cards = []
    dealers_cards = []
    player_score = 0
    dealer_score = 0
    ps = []

    players_cards.append(deck.pop())
    players_cards.append(deck.pop())
    dealers_cards.append(deck.pop())
    dealers_cards.append(deck.pop())

    # player_playing
    calculate_player_score()
    print(player_score)
    player_playing = True
    while player_playing:
        show_player_card()
        calculate_player_score()
        print("Player's score is", player_score)
        if player_score == 21:
            print('hurray yor hit the blackjack')
            break
        elif player_score > 21:
            print('oops !! You are burst. Dealer wins')
            break
        else:
            hit_stand()

    # dealers_turn
    if player_score < 21:
        calculate_dealer_score()
        show_all_card()

        while dealer_score < 17:
            dealers_cards.append(deck.pop())
            show_all_card()
            calculate_dealer_score()
        if dealer_score == 21:
            print("Dealer hits the blackjack. You lose.")
            total_chips -= bet
        elif dealer_score > 21:
            print("Dealer burst . You Won")
            total_chips += bet
        elif dealer_score > player_score:
            print("Dealer wins")
            total_chips -= bet
        elif dealer_score == player_score:
            print("tie")
        else:
            print("You won")
            total_chips += bet
    print("Press any key to continue and NO to exit game.")        
    v = input()
    if v[0] == 'n':
        break
    else:
        continue
