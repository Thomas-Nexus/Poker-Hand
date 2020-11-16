import random
from collections import Counter

#-----------------------------------------------------------------------------------------------------------------------

class Card(object):
    def __init__(self, name, number, suit, shape):
        self.name = name
        self.number = number
        self.suit = suit
        self.shape = shape

    def __repr__(self):
        return f"{self.shape}"

#-----------------------------------------------------------------------------------------------------------------------

class Deck_Actions(object):
    def __init__(self):
        self.cards = None

    def shuffle(self):
        random.shuffle(self.cards)
        return self.cards

    def deal(self):
        return self.cards.pop(0)

#-----------------------------------------------------------------------------------------------------------------------

#DESIGN

def red(text):
    return "\033[95m {}\033[00m".format(text)

card_outline = red('|')
heart = red('♡')
diamond = red('♢')

#-----------------------------------------------------------------------------------------------------------------------

#DECK CONFIGURATION

class Deck(Deck_Actions):
    def __init__(self):
        self.cards = []
        suit = {'Heart': f'{heart}', 'Diamond': f'{diamond}', 'Club': "♧", 'Spades': "♤"}
        number = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7,
                  'Eight': 8, 'Nine': 9, 'Ten': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

        for each in number:
            for s in suit:
                shape = suit[s]
                if number[each] < 11:
                    ICON = f"{card_outline}{number[each]} {shape} {card_outline}"
                else:
                    ICON = f"{card_outline}{each[0]} {shape} {card_outline}"

                self.cards.append(Card(each, number[each], s, ICON))

#-----------------------------------------------------------------------------------------------------------------------

class Player(object):
    def __init__(self):
        self.cards = []

    def addCard(self, card):
        self.cards.append(card)

#------------------------------------------------------------------------------------------------------------------------

# HAND GRADING RULES - String Outputs Formatted To Be Centrally Aligned With Card Display

class Grading(object):
    def __init__(self, cards):
       self.cards = cards


    def pair(self):
        search = [each.number for each in self.cards]
        frequency = Counter(search).items()

        for Number in frequency:
            if Number[0] < 11 and Number[1] == 2:
                return f"                                                                           A PAIR OF {Number[0]}'s"
            elif Number[0] == 11 and Number[1] == 2:
                return '                                                              POCKET JACKS CAN BE DANGEROUS SOMETIMES'
            elif Number[0] == 12 and Number[1] == 2:
                return '                                                                          A PAIR OF QUEENS!'
            elif Number[0] == 13 and Number[1] == 2:
                return '                                                                          A PAIR OF KINGS!'
            elif Number[0] == 14 and Number[1] == 2:
                return '                                                                    POCKET ROCKETS YOU DAREDEVIL'


    def twoPair(self):
        test = []
        numbers = [check.number for check in self.cards]
        for number in numbers:
            if numbers.count(number) == 2 and number not in test:
                test.append(number)
        if len(test) == 2:
            return True


    def trips(self):
         search = [each.number for each in self.cards]
         frequency = Counter(search).items()

         for Number in frequency:
            if Number[1] == 3 and Number[0] < 11:
                return f"                                                                             TRIP {Number[0]}'s!"
            elif Number[1] == 3 and Number[0] == 11:
                return "                                                                        3 JACKS, REEL THEM IN"
            elif Number[1] == 3 and Number[0] == 12:
                return "                                                                     3 LADIES IS NEVER A BAD HAND"
            elif Number[1] == 3 and Number[0] == 13:
                return "                                                               THE KING OF KINGS. HOW'S THE POKER FACE?"
            elif Number[1] == 3 and Number[0] == 14:
                return "                                                                3 ROCKETS. HOUSTON, WE HAVE A PROBLEM!"


    def straight(self):
        numbers = [check.number for check in self.cards]
        numbers.sort()

        if not len(set(numbers)) == 5:
            return False

        # REQUIRED AS ACE CAN BE LOW OR HIGH
        if numbers[4] == 5 and numbers[3] == 4 and numbers[2] == 3 and numbers[1] == 2 and numbers[0] == 14:
            return '5 HIGH STRAIGHT'

        else:
            if not numbers[0] + 1 == numbers[1]:
                return False
            if not numbers[1] + 1 == numbers[2]:
                return False
            if not numbers[2] + 1 == numbers[3]:
                return False
            if not numbers[3] + 1 == numbers[4]:
                return False
        return True and numbers[4]
        #INDEX 4 USED FOR ROYAL FLUSH CLARIFICATION


    def flush(self):
        suits = [check.suit for check in self.cards]
        if len(set(suits)) == 1:
            return True


    def fullHouse(self):
        full = False
        boat = False
        numbers = [check.number for check in self.cards]
        for each in numbers:
            if numbers.count(each) == 3:
                full = True
            elif numbers.count(each) == 2:
                boat = True
            if full and boat:
                return True


    def fourOfAKind(self):
        numbers = [check.number for check in self.cards]
        for each in numbers:
            if numbers.count(each) == 4:
                return True

#-----------------------------------------------------------------------------------------------------------------------

# COLOR PALETTE

def red(color):
    return "\033[91m {}\033[00m" .format(color)
def green(color):
    return "\033[96m {}\033[00m" .format(color)
def yellow(color):
    return "\033[93m {}\033[00m".format(color)

Title = red("HOW'S YOUR LUCK?")
Poles = green("|||||||||||||||||||")
Dashes = red("---------------------------------------------------")
Points = yellow("POINTS: + ")

#-----------------------------------------------------------------------------------------------------------------------

# CONSOLE

def play():
    bank = 0
    deck = Deck()
    deck.shuffle()
    player = Player()

    print('')
    print(f'                                                                         {Title}')
    print(f'                                                                       {Poles}')
    print(f'                                                      {Dashes}')

    for each in range(5):
        player.addCard(deck.deal())

    print(f'                                                       {player.cards}')
    print(f'                                                      {Dashes}')
    print('')


    #GRADING
    score = Grading(player.cards)
    pair = score.pair()
    two_pair = score.twoPair()
    trips = score.trips()
    straight = score.straight()
    flush = score.flush()
    house = score.fullHouse()
    quads = score.fourOfAKind()


    if straight and flush and straight == 14:
        print('                                                                         !_____ROYAL FLUSH_____!')
        print("                                                       You don't realise how lucky this is. 0.00015% is the answer....")
        bank += 100000

    elif straight and flush:
        print('                                                                             STRAIGHT FLUSH')
        bank += 800

    elif quads:
        print('                                                                              4 OF KIND!')
        bank += 775

    elif house:
        print('                                                                             A FULL BOAT!')
        bank += 750

    elif flush:
        print('                                                               YOU LOOK FLUSHED. THERE MAY BE A REASON!')
        bank += 700

    elif straight:
        print('                                                                        CONNECT 5. A STRAIGHT!')
        bank += 650

    elif trips:
        print(trips)
        bank += 500

    elif two_pair:
        print('                                                                             TWO PAIR!')
        bank += 400

    elif pair:
        print(pair)
        bank += 150

    print('')
    print(f'                                                                          {Points}{bank}')

play()