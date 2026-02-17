import stringListFunctions
import Gods
import Item

def choiceInput():
    while True:
        try:
            x = int(input())
            return x
        except ValueError:
            print("Invalid input, please enter a number")




class Building:
    def __init__(self,name):
        self.name = name

class Temple(Building):
    def __init__(self,gods_worshipped):
        super().__init__(self)
        self.gods_worshipped = gods_worshipped

    def addDeity(self,new_god):
        self.gods_worshipped.append(new_god)


class Shop(Building):
    def __init__(self,name,storeGold,inventory):
        super().__init__(name)

        #int
        self.storeGold = storeGold

        #item list
        self.inventory = inventory

        #print "sprite" of store clerk
    def printSprite(self):
        print(r"""

                 ___________
                ///          \
                ///   ________)
                (x     (0 0)|  
                |  /_____U___\
                 \__________/
                /      x    \
                |__|______|_|

                 ___________________________ 
                |                           |
              "<  Hello, what're ya in for? |
                |___________________________|

        """)



    # print store inventory
    def printInventory(self):

       print(" _________________________________ ","\n")
       print("(_________________________________)","\n")
       stringListFunctions.printNumberedList(self.inventory)
       print(" _________________________________ ","\n")
       print("(_________________________________)","\n")


    #print every thing
    def printShop(self):

        self.printSprite()
        self.printInventory()

    # function to buy item
    def buyItem(self,soldItem, yourGold, yourBag):

        if yourGold < soldItem.price :
            print("$----------------------------------------------------------------$","\n")
            print("  It appears your a little short on cash, as you only have ", yourGold,"G.","\n")
            print("$----------------------------------------------------------------$","\n")
        else:
            yourBag.append(soldItem)
            print("You got a ", soldItem.name ,".","\n")
            yourGold -= soldItem.price
            self.storeGold += soldItem.price

    #function to set data to bought item
    def buyItem(self,soldItem, yourBag, yourGold):

        if yourGold < soldItem.price:

            print("$----------------------------------------------------------------$","\n")
            print("  It appears your a little short on cash, as you only have ", yourGold ,"G.","\n")
            print("$----------------------------------------------------------------$","\n")

        else:

            yourBag.apend(soldItem)
            print("You got a ", soldItem.name ,".","\n")
            yourGold -= soldItem.price
            self.storeGold += soldItem.price

    # function to sell item
    def sellItem(self, yourBag, yourGold):
        if len(yourBag)== 0 :
            print(" 0----------------------------------0","\n")
            print(" | You don't have anything to sell! |","\n")
            print(" 0----------------------------------0","\n")
        elif len(yourBag)== 1:
            print(" 0--------------------------------------------0","\n")
            print(" | You're gonna need something on your quest! |","\n")
            print(" 0--------------------------------------------0","\n")
        else:
            print(" v---------------v","\n")
            print(" | Pick an item. |","\n")
            print(" v---------------v","\n")
            stringListFunctions.printNumberedList(yourBag)

            sellChoice = choiceInput()
            yourGold += yourBag[sellChoice-1].price
            soldItem = yourBag[sellChoice-1]
            self.inventory.append(soldItem)
            yourBag.remove(yourBag[sellChoice-1])
            print(" $------------------------------------------$","\n")
            print("   You sold your item and now have ", yourGold, "G","\n")
            print(" $------------------------------------------$","\n")





class Bank(Building):

    def __init__(self,name,bankMoney,account):

        #string
        self.name = name

        #int
        self.bankMoney = bankMoney
        self.account = account

    def bankMenu(self,gold):

        bankChoice = -1
        print("///////////",end="")
        print("//  / \\ //",end="")
        print("// (.).) |",end="")
        print("///  7   |",end="")
        print("<x    -  |",end="")
        print("\\________/",end="")
        print(" ___|_|___",end="")
        print("|     %   |",end="")
        print("|__|____|_|",end="")
        print("  ___________________________________ ",end="")
        print(" |                                   |",end="")
        print("< Bank Owner: Hi, welcome to bank :) |",end="")
        print(" |___________________________________|",end="")
        print(f"You have {gold} G.", end="")
        print(f"You have {self.account} G in your account.",end="")

        print("O--------------O",end="")
        print("| 1 : Deposit  |",end="")
        print("| 2 : Withdraw |",end="")
        print("O--------------O",end="")
        print("")
        bank_choice = choiceInput()

        match bank_choice:

            case 1 :
                print("O-------------O",end="")
                print("| Enter Amount|",end="")
                print("O-------------O",end="")
                deposited_amount = choiceInput()
                if(gold>deposited_amount):
                    gold -= deposited_amount
                    self.account += self.bankMoney
                    self.account += deposited_amount
                else:
                    print("  ________ ",end="")
                    print(" |        |",end="")
                    print("< BO: >:( |",end="")
                    print(" |________|",end="")
                    print("You dont have enough gold to deposit")


            case 2 :
                print("O-------------O",end="")
                print("| Enter Amount|",end="")
                print("O-------------O",end="")
                withdrawn_amount = choiceInput()
                if(self.account>=withdrawn_amount):
                    gold += withdrawn_amount
                    self.account -= withdrawn_amount
                else:
                    print("  ________ ",end="")
                    print(" |        |",end="")
                    print("< BO: >:( |",end="")
                    print(" |________|",end="")
                    print("You dont have enough gold in your account to withdraw")







