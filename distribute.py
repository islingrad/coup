from random import randint


deck = ["assassin", "assassin", "assassin", "duke", "duke", "duke", "abrar", "abrar", "abrar", "captain","captain","captain", "contessa", "contessa", "contessa"]

name = 0
class Player(object):
    def __init__(self, cards_in_hand = [], coins = 2):
        global name
        self.name = name
        self.cards = cards_in_hand
        self.coins = coins
        name = name + 1
    def __repr__(self):
        return "THIS IS Player {2}. They have {0} and {1} coins\n".format(self.cards, self.coins, self.name)
    def abrar_request(self, player_abrar):
        pass
    def assassin_request(self, player_assassin):
        pass
    def duke_request(self, player_duke):
        pass
    def captain_request(self, player_captain):
        pass
    def contessa_request(self, player_contessa):
        pass
        


def create_n_players(n):
    player_list = []
    while n > 0:
        new_player = Player([])
        player_list.append(new_player)
        n = n-1
    return player_list

n = int(input('NUMBER OF PLAYERS'))
p = create_n_players(n)

def alive_help(n):
    alive = []
    for i in range(0,n):
        alive += [i]
    return alive
alive = alive_help(n)



#function that distributes cards to players
def dis_help():
    butthole = randint(0,len(deck)-1)
    asshole = deck[butthole]
    deck.remove(deck[butthole])
    return asshole

def distribute(n):
    for i in range(0,n):
        p[i].cards.append(dis_help())
        p[i].cards.append(dis_help())

distribute(n)

print(p)
print("\n")


#play card
def play(player):
    print("Here is what you have: ", p[player].cards)
    card = input("Which card do you want to play?")
    while (not (card=="0" or card=="1")):
        card = input("Invalid input, choose a card to play")
    card = int(card)
    card = p[player].cards[card]
    print(alive)
    ind = alive.remove(p[player].name)
    print(ind)
    if (card == "captain"):
        tar = input("Choose to steal two coins from")
        while (not int(tar) in ind):
            tar = input("Invalid input, choose to steal from")
        tar = int(tar)    
        print("I steal two coins from player",p[tar].name)

#play(0)

print("Initial deck: ")
print(deck)
print("\n")

#Abrar: obtains two cards
player_abrar = int(input('WHO IS ABRAR?'))

def abrar1(player_abrar):
    p[player_abrar].cards.append(dis_help())
    p[player_abrar].cards.append(dis_help())
    print("Your cards now are ")
    print(p[player_abrar].cards)

abrar1(player_abrar)
   #input which player is an abrar

print("This is from the deck:")
print(deck)
#Abrar: discards two cards
def abrar2(player_abrar):
    d1 = input('CHOOSE FIRST CARD TO DROP')
    while (not (d1=="0" or d1=="1" or d1=="2" or d1=="3")):
        d1 = input("INVALID INPUT, CHOOSE FIRST CARD TO DROP AGAIN")
    d1 = int(d1)
    deck.append(p[player_abrar].cards[d1])
    d2 = input('CHOOSE SECOND CARD TO DROP')
    while (not ((d2=="0" or d2=="1" or d2=="2" or d2=="3") and not(str(d1)==d2))):
        d2 = input('INVALID INPUT, CHOOSE SECOND CARD TO DROP AGAIN')
    d2 = int(d2)
    deck.append(p[player_abrar].cards[d2])           
    d1 = p[player_abrar].cards[d1]
    d2 = p[player_abrar].cards[d2]
    p[player_abrar].cards.remove(d1)
    p[player_abrar].cards.remove(d2)
    print("Your cards now are ")
    print(p[player_abrar].cards)

         
    
abrar2(player_abrar)

print("Now the deck becomes")
print(deck)













































