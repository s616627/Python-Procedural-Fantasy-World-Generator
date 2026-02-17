#functions for card game and printing a card based on the number(not implemented).
#It checks for a number in the text file and prints the ascii art that comes after
import random

def printCard(cardNumber):
    totalLines = 9
    cardSprite = []
    with open("cards.txt") as file:
        for line in file:
            line = line.strip()

            if totalLines == -1:
                totalLines = 9

            if line.isdigit():
                if int(line) == cardNumber:
                    cardSprite.append(line)
                    totalLines = totalLines-1

            if totalLines < 9:
                cardSprite.append(line)
                totalLines = totalLines - 1



    file.close()

    cardSprite.pop(1)
    cardSprite.pop(0)

    for strip in cardSprite:
        print(strip)

def cardGame(gold):

        bet = 0
        print("\n")
        print("O---------------[THE RULES]---------------O")
        print("| Draw cards that add up to a number.     |")
        print("| If your sum is higher that 21, you lose.|")
        print("| The dealer does the same and if their   |")
        print("| sum is closer to 21, you lose the game. |")
        print("O-----------------------------------------O")
        print("\n")
        print("O----------------------------------O")
        print("| How much are you willing to bet? |")
        print("O----------------------------------O")
        print("You have ", gold, "G.")

        while bet <= 0 or bet > gold :

            try:
                bet = int(input("Enter Your Bet: "))
            except ValueError:
                print("Please Enter a Number")
                print(bet)

            if bet > gold or bet <= 0 :
                print("O---------------------------------------O")
                print("| Bet must be greater than zero &       |")
                print("| less than the amount of gold you have.|")
                print("| Please re-enter your bet amount.      |")
                print("O---------------------------------------O")

        cardOne = random.randrange(1,11)
        cardTwo = random.randrange(1,11)
        cardSum = cardOne + cardTwo

        printCard(cardOne)
        printCard(cardTwo)

        print("*--------------------*")
        print("  You draw two cards. ")
        print("  They add up to ", cardSum,".")
        print("*--------------------*")
        print("\n")

        playingGame = True
        while playingGame:
            print("O------------------------O")
            print("| 1:Draw another card    |")
            print("| 2:Stay with your cards |")
            print("O------------------------O")


            cardChoice = int(input())

            if cardChoice == 1 :
                #srand(time(0))
                newCard = random.randrange(1,10)
                printCard(newCard)
                cardSum += newCard
                print("*--------------------*")
                print("  Your sum is ", cardSum)
                print("*--------------------*")

                if cardSum >= 21 :
                    playingGame = False

            else:

                print("*--------------------*")
                print("  Your sum is ", cardSum)
                print("*--------------------*")

                playingGame = False



        if cardSum > 21 :
            print("\n")
            print("* ----------------------------------------------*")
            print("  Your sum is above 21 so you gave ", bet ,"G to the dealer")
            gold -= bet
            print("  You now have ", gold, "G.")
            print("*-----------------------------------------------*")

        elif cardSum == 21 :

            print("* ------------------------------------------------------------*")
            print("  Your sum equals 21 so you get ", bet, "G from the dealer ")
            gold += bet
            print("  You now have ", gold, "G.")
            print("*-------------------------------------------------------------*")



        else:

            dealerOne = random.randrange(1,10)
            dealerTwo = random.randrange(1,10)

            printCard(dealerOne)
            printCard(dealerTwo)

            dealSum = dealerOne + dealerTwo

            print("*---------------------------*")
            print("  The dealer draw two cards. ")
            print("  They add up to ", dealSum, ".")
            print("*---------------------------*")
            print("\n")
            print("O------------O")
            print("| 1:Continue |")
            print("O------------O")

            dealChoice = input()

            while dealSum < cardSum and dealSum < 21 :

                newDealCrd = random.randrange(1,10)
                printCard(newDealCrd)
                dealSum += newDealCrd;
                print("*-------------------------*")
                print("  The dealer draws a card. ")
                print(f"  Their sum is now {dealSum}")
                print("*-------------------------*")
                print("\n")
                print("O------------O")
                print("| 1:Continue |")
                print("O------------O")

                dealChoice = input()


            if dealSum > cardSum and dealSum <= 21 :

                print("* ------------------------------------*")
                print(f"  You gave {bet} G to the dealer")
                print("*-------------------------------------*")

                gold -= bet

            else:

                print("*---------------------------------------*","\n")
                print(f"  You get {bet} G from the dealer ","\n")
                print("*---------------------------------------*","\n")

                gold += bet




