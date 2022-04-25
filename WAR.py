import random

# deck of cards
frontOfCard = []

suits = ["Hearts", "Diamonds", "Clubs", "Spades"]

ranks = ["Ace", "Jack", "Queen", "King"]

oldDeck = []


for numbers in range(2,11):
  frontOfCard.append(str(numbers))

for rank in range(4):
  frontOfCard.append(ranks[rank])

for suit in range(4):
  for card in range(13):
    cards = (frontOfCard[card] + " of " + suits[suit])
    oldDeck.append(cards)

#create players
def nameOfPlayers():
  print("Welcome to the Game of WAR! " + playerOne + " and " + playerTwo)
  
#explanation of game of war
def explanation():
  print("Here are the rules!")
  print("The deck is divided evenly to each player, with each player receiving 26 cards.")
  print()
  print("The cards will be flipped for the playeres and the player with the higher card takes both cards.")
  print()
  print("If the cards are the same rank, it is WAR.  Each player turns up one card face down and one card face up.  The player with the higher card takes both piles, if they are the same rank,each players places another card face down and turns the other face down card up, continue until the winner of that pile is determined.")

#Deal out cards
#Fix code to go into war if cards are the same
def dealWar():
    random.shuffle(oldDeck)
    hand1 = oldDeck[0:int(len(oldDeck)/2)]
    hand2 = oldDeck[int(len(oldDeck)/2):len(oldDeck)]
    for i in range(0, int(len(oldDeck)/2)):
        handOne = hand1.pop()
        handTwo = hand2.pop()
        print(playerOne + " has played: " + handOne + "  |  " + playerTwo + " has played: " + handTwo)
        one=handOne.split(" ")
        a=one[0]
        #print(a)
        #print(one)
        two=handTwo.split(" ")
        b=two[0]
        #print(b)
        #print(two)
        if a > b:
            print(playerOne + " Wins!")
            print()
        elif a == b:
            print("                      !!!!!WARRR!!!!! ")
            print(" ")
            
        else:
          print(playerTwo + " Wins!")
          print()
# fix to count every word that says player name and wins
def finalScore():
    playerOneScore = len(playerOne + " Wins!")
    playerTwoScore = len(playerTwo + " Wins!")
    if playerOneScore > playerTwoScore:
        print(playerOne + " ! ")
    elif playerOneScore == playerTwoScore:
        print("NO ONE, the game ended as a DRAW! ")
    else:
        print(playerTwo + " ! ")
#CODE

playerOne = input("What is your name? ")
playerTwo = input("What is your name? ")
print()

nameOfPlayers()

print()

explanation()
print()

userInput = input("Are both players ready to start? (y/n): ")
print()

if userInput == "y":
    print("Here we go! ")
    print()
elif userInput == "n":
  print("Too bad we're starting anyways")
else:
  print("Wrong Input, Try Again!")

print()

dealWar()

print("The winner is...........")
finalScore()
print()
