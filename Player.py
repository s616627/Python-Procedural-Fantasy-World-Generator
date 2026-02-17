import random
import Item

import RacesAndCreatures
from stringListFunctions import printNumberedList

#random.randrange(0,len(secondHalf))

class Player(RacesAndCreatures.Creature):

    def __init__(self,name, sprite, attack, defense, speed, size, magicAttack, magicDefense, maxHP, attributes, sapient, bodyParts):

        super().__init__(name, sprite, attack, defense, speed, size, magicAttack, magicDefense, maxHP, attributes, sapient, bodyParts)

        #bool
        self.sapient = True

        #int
        self.bankAccount = 0
        self.gold = 0
        self.xCoord = 0
        self.yCoord = 0
        self.exp = 0

        #bag
        self.bag = []
        self.nextBagSpace = -1

        #list of creatures of the party
        self.party = []



    def printParty(self):

        printNumberedList(self.party)


    #function for enemy encounter with the creature 'badguy'
    def enemyEncounter(self,badguy):
        """
        line = ""
        personalities = []
        ifstream file("personalityTraits.txt")
        int total_lines=0;

        while(getline(file,line)):

        total_lines++;
        personalities.push_back(line);

        file.close();

        int random_number = rand()%total_lines;

        for(int i=0;i<3;i++){
         badguy.personality.push_back(personalities[random_number]);
         cout << personalities[random_number] << endl;
        random_number = rand()%total_lines;
        """

        battle(badguy)



    def buyItem(self,soldItem):

        if self.gold < soldItem.maxPrice :

            print("$----------------------------------------------------------------$","\n")
            print("  It appears your a little short on cash, as you only have ", self.gold,"G.","\n")
            print("$----------------------------------------------------------------$","\n")

        else:

            self.bag.append(soldItem)
            print("You got a ", soldItem.name, ".","\n")
            self.gold -= soldItem.maxPrice
            #storeGold += soldItem.maxPrice;


    def printBag(self):

        print(" You have ", gold, "G","\n")
        printNumberedList(self.bag)


    def printStats(self):

        print("\n")
        print(" (((((((((())))  ","\n")
        print("  )))))  ^  ^|   " , " <----------------------->","\n")
        print(" ((((   (@  @)   " , "   HP: " , self.maxHP,"\n")
        print("  ))       > |   " , "   Speed: " , self.speed,"\n")
        print(" (x     ______\\  " , "   Attack(Physical): " , self.attack,"\n")
        print("   \\________/    " , "   Attack(Magic): " , self.magicAttack,"\n")
        print("  ____|_|____    " , "   Defense(Physical): " , self.defense,"\n")
        print(" (      X    )   " , "   Defense(Magic): " , self.magicDefense,"\n")
        print("  )_|___X__|(    " , " <----------------------->","\n")


    def addItem(self,newItem):
        self.bag.append(newItem)
        print( "You got a " , newItem.name , ".","\n" )


    def removeItem(self,index):
        self.bag.remove(index)


    def setStats(self):

        #srand((unsigned)time(0))
        self.attack = random.randrange(5,11)
        self.defense = random.randrange(5,11)
        self.speed = random.randrange(5,11)
        self.magicAttack = random.randrange(5,11)
        self.magicDefense = random.randrange(5,11)
        self.maxHP = random.randrange(30,41)
        self.gold = random.randrange(50,61)
        self.currentHP = self.maxHP


    def levelUp(self):

        expPerLevel = [0]*100
        levelThreshold = 40

        for i in expPerLevel:

            i = levelThreshold
            levelThreshold *= 2


        while self.exp >= expPerLevel[self.level] :

            print("(!)--------(!)","\n")
            print(" | LEVEL UP |","\n")
            print("(!)--------(!)","\n")


            print("\n")
            print(" (((((((((())))  ","\n")
            print("  ))))) ^  ^|    " , " <----------------------->","\n")
            print(" ((((  (@  @)    " ,"   HP: ", self.maxHP ,"\n")
            print("  ))      > |    " , "   Speed: ", self.speed ,"\n")
            print(" (x       U |    " , "   Attack(Physical): ", self.attack ,"\n")
            print("   \\________|    " , "   Attack(Magic): ", self.magicAttack ,"\n")
            print("  ____|_|____    " , "   Defense(Physical): ", self.defense ,"\n")
            print(" (      X    )   " , "   Defense(Magic): ", self.magicDefense ,"\n")
            print("  )_|___X__|(    " , " <---------___----------->" ,"\n")

            #srand((unsigned)time(0));
            self.attack += random.randrange(0,3)
            self.defense += random.randrange(0,3)
            self.speed += random.randrange(0,3)
            self.magicAttack += random.randrange(0,3)
            self.magicDefense += random.randrange(0,3)
            self.maxHP += random.randrange(1,4)

            print("                            \\ /" ,"\n")
            print("                  <----------v------------>" ,"\n")
            print("                    HP: " , self.maxHP ,"\n")
            print("                    Speed: " , self.speed ,"\n")
            print("                    Attack(Physical): ", self.attack ,"\n")
            print("                    Attack(Magic): " , self.magicAttack ,"\n")
            print("                    Defense(Physical): ", self.defense ,"\n")
            print("                    Defense(Magic): ", self.magicDefense ,"\n")
            print("                  <----------------------->","\n")

            self.level = self.level + 1
            print("LEVEL",self.level)

    def noCash(self):

        print("$-----------------------------------------------------------------$","\n")
        print("  It appears your a little short on cash, as you only have ", self.gold , "G." ,"\n")
        print("$-----------------------------------------------------------------$","\n")



    def buyItem(self,item):

        if self.gold < item.price :

            self.noCash()

        else:

            self.bag.append(item)
            print("You got a " , item.name , ".","\n")
            self.gold -= item.price

    def craftSword(self):


        self.printBag()
        print("0) Use Blade material")
        hiltChoice = input("Choose your hilt.")

        if hiltChoice > self.bag.size():
            hiltChoice = self.bag.size()

        if hiltChoice < 1:
            hiltChoice = 1

        hilt = self.bag[hiltChoice - 1]
        newSword = Item.Weapon(hilt.price,hilt.weight, hilt.atkMltp, hilt.defMltp, hilt.name,hilt.attributes,hilt.attributes,hilt.description)


        for i in hilt.attributes.size():
            newSword.handleTraits.push_back(hilt.handleTraits[i])

        self.printBag()
        bladeChoice = int(input("Choose your blade."))


        if bladeChoice > self.bag.size():
            bladeChoice = self.bag.size()

        if bladeChoice < 1:
            bladeChoice = 1

        if bladeChoice == hiltChoice:
            bladeChoice = 1

        blade = self.bag[bladeChoice - 1]
        newSword.maxPrice += blade.maxPrice
        newSword.atkMltp = blade.atkMltp
        newSword.element = blade.element
        newSword.defMltp += blade.defMltp
        newSword.healAmount = blade.healAmount
        newSword.attributes = blade.attributes

        for x in blade.handleTraits:
            newSword.attributes.append(x)


        bag.erase(bag.begin() + hiltChoice - 1)

        bag.erase(bag.begin() + bladeChoice - 1)

        string
        swordName;
        cout << " Name your sword" << endl;
        cout << "X------------------------X" << endl;
        cout << "Attack bonus: " << newSword.atkMltp << endl;

        if (newSword.defMltp != 0)
            cout << " Defense bonus: " << newSword.defMltp << endl;

        if (newSword.element != swordName)
            cout << " Element: " << newSword.element << endl;

        cout << " Value: " << newSword.maxPrice << endl;

        if (newSword.healAmount != 0)
            cout << " Healing: " << newSword.healAmount << endl;
        cout << "X------------------------X" << endl;

        cin >> swordName
        newSword.name = swordName
        bag.push_back(newSword)

    def craftBook():

        printBag()
        int
        coverChoice;
        cout << "Pick an item to make the cover" << endl;
        cin >> coverChoice;

        printBag();
        int
        paperChoice;
        cout << "Pick an item to make the pages" << endl;
        cin >> paperChoice;

        vector < string > book;
        string
        line;

        cout << "Type in the contents and press enter for a new line. Type and enter 'THE END' in all uppercase to end writing" << endl;

        while (line != "THE END"){

            getline(cin, line);
            book.push_back(line);
        // cout << line << endl;
        }

        string bookName;
        cout << "What is the title of this ";

        if (book.size() < 10):
            cout << "passage?" << endl
        else if (book.size() >= 10 & & book.size() < 50):
            cout << "letter?" << endl
        else:
            cout << "novel?" << endl

        getline(cin, bookName);

        Item work;

        bookName = bookName + " [B]"

        work.writing = book
        work.name = bookName

        for (int i = 0;i < bag[coverChoice-1].attributes.size();i++):
            work.handleTraits.push_back(bag[coverChoice-1].attributes[i])


        for (int j = 0;j < bag[paperChoice-1].attributes.size();j++):
            work.attributes.push_back(bag[paperChoice-1].attributes[j])


        work.maxPrice = book.size() * 5

        bag.push_back(work)

    def battle(enemy):
        int battleChoice;
        int equipChoice;
        int equipChoice2;

        vector <Item> floor;

        cout << "X-------------------------------------------------------------------------X" << endl;
        cout << "  You encountered a " << enemy.name << ". Equip your weapon!" << endl;
        cout << "X-------------------------------------------------------------------------X" << endl;
        cout << endl;

        printBag();

        cin >> equipChoice;
        //printGoblin();
        cout << "X------------------------------------X" << endl;
        cout << "  Equip an item in your second hand!" << endl;
        cout << "X------------------------------------X" << endl;
        cout << endl;

        printBag();

        cin >> equipChoice2;
        //system("cls");

        double xtraAtk = 1;
        double xtraDef = 1;

        int damageMultiplier = attack * bag[equipChoice-1].atkMltp * xtraAtk;
        int defenseMultiplier = defense * bag[equipChoice2-1].defMltp * xtraDef;

        int r;
        r = (rand()%5);

        bool battleMode = true;
        while(enemy.currentHP > 0 && battleMode)
        {
            //printGoblin();
            //system("cls");
            cout << endl;
            cout << "X---------------------X" << endl;
            cout << "| 1 : Fight 2 : Talk  |" << endl;
            cout << "| 3 : Run   4 : Items |" << endl;
            cout << "X---------------------X" << endl;

            cin >> battleChoice;
            switch(battleChoice)
            {
            case 1: #fight

            if(speed > enemy.speed){
                cout << endl;
                cout << "X-----------------------------------X" << endl
                cout << "  You attack the enemy." << endl
                int critChance = rand()%16

                if(critChance == 1){ # 1/16 chance for critical hit
                    damageMultiplier = damageMultiplier*2;
                }
                enemy.currentHP -= (((level)*0.4 + 2)*(damageMultiplier+r)/(enemy.defense))/25;
                if(enemy.currentHP < 0){
                    enemy.currentHP = 0;
                    battleMode = false;
                }

                if(critChance == 1){//crit hit mentioned and damage multiplier returns to normal
                    cout << "  A CRITICAL HIT!" << endl;
                    damageMultiplier = damageMultiplier/2;
                }

                cout << "  The enemy attacks you." << endl;
                currentHP -= (((enemy.level)*0.4 + 2)*(attack*r)/(defenseMultiplier))/25;
                if(currentHP < 0){
                    currentHP = 0
                    battleMode = false
                }
                cout << " " << endl;
                cout << "  The enemy has " << enemy.currentHP << " HP left." << endl;
                cout << "  You have " << currentHP << " HP left." << endl;
                cout << "X-----------------------------------X" << endl;
                r = (rand()%5);
            }else{
                cout << endl;
                cout << "X-----------------------------------X" << endl;
                cout << "  The enemy attacks you." << endl;
                cout << "  You attack the enemy." << endl;
                int critChance = rand()%16 ;

                if(critChance == 1){// 1/16 chance for critical hit
                    damageMultiplier = damageMultiplier*2;
                }
                currentHP -= (((enemy.level)*0.4 + 2)*(enemy.attack*r)/(defense))/25;
                if(currentHP < 0){
                    currentHP = 0;
                    battleMode = false;
                }
                enemy.currentHP -= (((level)*0.4 + 2)*(damageMultiplier*r)/(enemy.defense))/25;
                if(enemy.currentHP < 0){
                    enemy.currentHP = 0;
                     battleMode = false;
                }
                cout << endl;
                cout << "  You have " << currentHP << " HP left." << endl;
                cout << "  The enemy has " << enemy.currentHP << " HP left." << endl;
                cout << "X-----------------------------------X" << endl;
                cout << endl;
                r = (rand()%5);
                }
            break;

            case 2://talk
                cout << "X------------------------------------------------------X" << endl;
                cout << "  You try to converse with the enemy." << endl;
                cout << endl;
                cout << "  " << enemy.name << ": ";

                if(checkForString("Feral",enemy.personality)){
                    cout << "GGRRRRRAAAAAAAAAAAWWWWWWWWWWWWWHHH!!!!!!!!" << endl;
                    cout << endl;
                    cout <<"  It seems like it isn't going anywhere." << endl;
                break;
                }else if(checkForString("Greedy",enemy.personality)){

                    cout << "Oh so you've given up huh? Hmmm, I suppose I could let" << endl;
                    cout << " you go for a small fee." << endl;
                    cout << endl;
                    cout << " 1: Pay 10G" << endl;
                    cout << " 2: Refuse" << endl;
                    cout << endl;
                    cin >> battleChoice;
                    switch (battleChoice){

                    case 1:
                    if(gold < 10)
                        cout << " " << enemy.name << ": WHAT! You can't even scrape together 10G? I suppose i'll have to settle." << endl;

                    gold -= 10;

                    if(gold<0)
                    gold = 0;

                    battleMode = false;
                    break;

                    default:

                    cout << " " << enemy.name << ": Lets see how courageous you are without your spleen!" << endl;
                    break;
                    }


                }else{

                    cout << "Alright, fine whatever." << endl;
                    cout << endl;
                    cout << "  The enemy has decided to leave you alone." << endl;

                    battleMode = false;
                }
            cout << "X------------------------------------------------------X" << endl;
            break;

            case 3://run
                cout << "X------------------------------------------------------X" << endl;
                cout << "  You try to escape,";
                if(speed > enemy.speed){
                    cout << " and you escaped the enemy." << endl;
                    cout << "X------------------------------------------------------X" << endl;
                    battleMode = false;
                break;
                }else{
                    cout << " but you fail" << endl;
                    cout << "X------------------------------------------------------X" << endl;
                }
            break;

            case 4:

                int chooseItem;
                cout << "What item?" << endl;
                cout << endl;
                printBag();
                cin >> chooseItem;
                chooseItem--;
                if(chooseItem > bag.size() || chooseItem < 0){
                cout << "X------------------------------X" << endl;
                cout << "  You don't have that right now!" << endl;
                cout << "X------------------------------X" << endl;
                }else if(bag[chooseItem].name[name.size()-2] == 'H'){
                    currentHP += bag[chooseItem].healAmount;

                cout << "X----------------------------X" << endl;
                cout << "  You healed " << bag[chooseItem].healAmount << " HP" << endl;
                cout << "  You now have " << currentHP << " HP" << endl;
                cout << "X----------------------------X" << endl;
                bag.erase(bag.begin()+chooseItem);

                }else{
                cout << "X------------------------------X" << endl;
                cout << "  You can't use that right now!" << endl;
                cout << "X------------------------------X" << endl;
                }

            break;

        }
        //waitForUser();
    }       if(enemy.currentHP < 1){
            cout << "You have defeated the enemy." << endl;
            gold += enemy.level*2;
            cout << "You have earned " << enemy.level*2 << "G." << endl;
            exp += enemy.level*5;
            cout << "You have earned " << enemy.level*5 << " XP." << endl;
            levelUp();
            //waitForUser();
            //system("cls");
    }else if(currentHP < 1){
        cout << "Thou art boned" << endl;
    }
    }

    void yebuMenu()
    {
    cout << "O----------------------------------------------O" << endl;
    cout << "| Your quest begins in the small town of Yebo. |" << endl;
    cout << "O----------------------------------------------O" << endl;

    cout << endl;
    cout << "O----------------------------O" << endl;
    cout << "| What would you like to do? |"<<endl;
    cout << "O----------------------------O" << endl;

    int choice;
    cout<<endl;
    cout << "O-----------O" << endl;
    cout << "| 1 : Store |" << endl;
    cout << "| 2 : Bank  |" << endl;
    cout << "| 3 : Bar   |" << endl;
    cout << "| 4 : Embark|" << endl;
    cout << "| 5 : Inven.|" << endl;
    cout << "| 6 : Write |" << endl;
    cout << "O-----------O" << endl;
    cin>>choice;
    switch(choice){
case 1 :
    storeMenu();
    break;
case 2 :
    bankMenu();
    break;
case 3 :
    barMenu();
    break;
case 4 :
    embark();
    break;
case 5 :
    printBag();
    break;
case 6 :
    craftBook();
    break;
case 7 :
    craftSword();
    break;
default:
    embark();
    break;
    }


    }




    void barMenu()
{
        //system("cls");
        cout<<"/////\\\\\\\\\\\\\\\\\\\\"<<endl;
        cout<<"///         | "<<endl;
        cout<<"///   <|><|>| "<<endl;
        cout<<"///  \\   [  / "<<endl;
        cout<<"<x   |   V | "<<endl;
        cout<<" |   | ____\\ " << endl;
        cout<<" |__________| "<<endl;
        cout<<"     |_|    "<<endl;
        cout<<" ____|O|____"<<endl;
        cout<<"|     O|    |"<<endl;
        cout<<"|__|___|__|_|"<<endl;
    cout << "  _______________ " << endl;
    cout << " |               |" << endl;
    cout << "< Bartender: ... |" << endl;
    cout << " |_______________|" << endl;
    cout << endl;
    cout << "O-----------O" << endl;
    cout << "| 1 : Buy   |" << endl;
    cout << "| 2 : Gamble|" << endl;
    cout << "O-----------O" << endl;
    int buyDrink;
    cin >> buyDrink;

    switch(buyDrink)
    {
        case 1:
            int buyChoice;
            int amount;
            cout << endl;
            cout << "O----------------------O" << endl;
            cout << "| 1 : Beer(2G)         |" << endl;
            cout << "| 2 : Cheeseburger(5G) |" << endl;
            cout << "| 3 : Roast(15G)       |" << endl;
            cout << "O----------------------O" << endl;
            cout << "You have " << gold << "G." << endl;
            cin >> buyChoice;


            switch(buyChoice){

            case 1 :
                        buyItem(2,0,0,0,10,"Beer [H]","None");
            break;

            case 2 :
                        buyItem(5,0,0,0,15,"Cheeseburger [H]","None");
            break;

            case 3 :
                        buyItem(15,0,0,0,20,"Roast [H]","None");
            break;

            default:
                cout << "Wait" << endl;
            break;

                }

            break;

            case 2:
                cardGame();
            break;

            case 3:
                fuseMenu();
            break;



    }
        //waitForUser();
        //system("cls");
}

    void fuseMenu(){

        cout<<" __________ "<<endl;
        cout<<"///        ) "<<endl;
        cout<<"///_ <i><I> "<<endl;
        cout<<"Co |   ^^( "<<endl;
        cout<<" | |__nnnnn" << endl;
        cout<<" |_________) "<<endl;
        cout<<"  // .|.|"<<endl;
        cout<<" |_ooo__ooo"<<endl;
        cout << "  _______________ " << endl;
        cout << " |               |" << endl;
        cout << "< Bominatio: :)  |" << endl;
        cout << " |_______________|" << endl;
        cout << endl;
        cout << "O-----------O" << endl;
        cout << "| 1 : Fuse  |" << endl;
        cout << "| 2 : Leave |" << endl;
        cout << "O-----------O" << endl;
        int choice;
        cin >> choice;

        switch(choice){

    case 1:
        if(party.size() < 2){
        cout << "  _______________ " << endl;
        cout << " |               |" << endl;
        cout << "< Bominatio: >:( |" << endl;
        cout << " |_______________|" << endl;
        cout << "You have less than two 'subjects' for fusion" << endl;
        cout << "You leave" << endl;
        break;
        }
        Enemy fused;

        Enemy first;

        Enemy second;

        printParty();
        cout << "Pick the first one to fuse." << endl;
        cin >> choice;

        if(choice < 1)
            choice = 1;

        if(choice>party.size())
            choice = party.size();

        int firstIndex = choice - 1;

        first = party[firstIndex];

        printParty();
        cout << "Pick the second one to fuse." << endl;
        cin >> choice;

        if(choice < 1)
            choice = 1;

        if(choice>party.size())
            choice = party.size();

        int secondIndex = choice - 1;

        second = party[secondIndex];

        fused.attack = (first.attack + second.attack)/2 + 1;
        fused.defense = (first.defense + second.defense)/2 + 1;
        fused.currentHP = (first.currentHP + second.currentHP)/2 + 1;
        fused.level = (first.level + second.level)/2 + 1;
        fused.maxHP = (first.maxHP + second.maxHP)/2 + 1;
        fused.currentHP = maxHP;
        fused.magicAttack = (first.magicAttack + second.magicAttack)/2 + 1;
        fused.magicDefense = (first.magicDefense + second.magicDefense)/2 + 1;
        fused.name = first.name.substr(0,first.name.size()/2) + second.name.substr(second.name.size()/2,second.name.size());


        if(first.species == second.species){
            fused.species = first.species;
        }else{

        fused.species = first.species + "-" + second.species;
        }

        fused.speed =  (first.speed + second.speed)/2 + 1;
        fused.personality = first.personality;

        for(int i = 0;i<second.personality.size();i++){

            if(!checkForString(second.personality[i],fused.personality))
                fused.personality.push_back(second.personality[i]);

        }

        fused.sprite = first.sprite;

        for(int j = 0;j<fused.sprite.size();j++){

            cout << fused.sprite[j] << endl;
        }

        cout << " <---------------------------------->" << endl;
        cout << "   " << fused.name << "(" << fused.species << ")" << endl;
        cout << "   HP: " << fused.maxHP << endl;
        cout << "   Speed: " << fused.speed << endl;
        cout << "   Attack(Physical): " << fused.attack << endl;
        cout << "   Attack(Magic): " << fused.magicAttack << endl;
        cout << "   Defense(Physical): " << fused.defense << endl;
        cout << "   Defense(Magic): " << fused.magicDefense << endl;
        cout << " <---------------------------------->" << endl;

        cout << endl;
        cout << "O---------------O" << endl;
        cout << "| 1: Accept     |" << endl;
        cout << "| 2: Never mind |" << endl;
        cout << "O---------------O" << endl;

        cin >> choice;

        if(choice == 1){
            cout << endl;
            cout << fused.name << endl;
            cout << fused.species << endl;
        cout << "O----------------O" << endl;
        cout << "| 1: Change name |" << endl;
        cout << "| 2: Continue    |" << endl;
        cout << "O----------------O" << endl;
        cin >> choice;
            if(choice == 1){

                string newName;
                cout << " Enter new name" << endl;
                getline(cin,newName);
                fused.name = newName;

            }

            party.push_back(fused);
            party.erase(party.begin()+firstIndex);

            if(firstIndex<secondIndex)
                secondIndex--;

            party.erase(party.begin()+secondIndex);
        }

        }




    }

    void embark()
    {
        //system("cls");
        int embarkChoice;
        cout << "              _____________________" << endl;
        cout << "             /                    /)" << endl;
        cout << "            /                    /" << endl;
        cout << "            |Where shall you go?|" << endl;
        cout << "            |                   |" << endl;
        cout << "            |    (1)North ^     |" << endl;
        cout << "            |             |     |" << endl;
        cout << "            |<-(2)West (3)East->|_" << endl;
        cout << "            |              |    | \\" << endl;
        cout << "            |     (4)South v   C__/\\" << endl;
        cout << "           /                    |\\  \\" << endl;
        cout << "          /                    / " << endl;
        cout << "       _____________________  /" << endl;
        cout << "      (____________________(_/" << endl;

        cin >> embarkChoice;

        switch(embarkChoice)
        {
        case 1:
            yCoord++;
        break;

        case 2:
            xCoord--;
        break;

        case 3:
            xCoord++;
        break;

        case 4:
            yCoord--;
        break;
        }
    }

        void beggar(){

        //system("cls");
      cout << "   //\\\\\\\\     " << endl;
      cout << "  ((. .\\\\\\    " << endl;
      cout << "   )<  (3))   " << endl;
      cout << "   //\\\\\\((    " << endl;
      cout << "  (__  ___)   " << endl;
      cout << "  /  \\\\\\   \\  " << endl;
      cout << " /    )))   \\ " << endl;
      cout << "(____(((_____)" << endl;
      cout << endl;
      cout << "?------------------?" << endl;
      cout << "  You see a beggar  " << endl;
      cout << "?------------------?" << endl;
    int choice;
    cout << "?-------------?" << endl;
    cout << " 1 : Give 5G   "<<endl;
    cout << " 2 : Give 100G "<<endl;
    cout << " 3 : Spit      "<<endl;
    cout << "?-------------?" << endl;
    cin >> choice;
//system("cls");
     switch(choice){

            case 1:

                gold -= 5;
                if(gold < 0)
                    gold = 0;

      cout << "   //\\\\\\\\     " << endl;
      cout << "  ((^ ^\\\\\\    " << endl;
      cout << "   )<  (3))   " << endl;
      cout << "   //\\\\\\((    " << endl;
      cout << "  (__  ___)   " << endl;
      cout << "  /  \\\\\\   \\  " << endl;
      cout << " /    )))   \\ " << endl;
      cout << "(____(((_____)" << endl;
      cout << endl;

            break;

            case 2:

                gold -= 100;
                if(gold < 0)
                    gold = 0;

      cout << "   //\\\\\\\\     " << endl;
      cout << "  ((O O\\\\\\    " << endl;
      cout << "   )<  (3))   " << endl;
      cout << "   //\\\\\\((    " << endl;
      cout << "  (__  ___)   " << endl;
      cout << "  /  \\\\\\   \\  " << endl;
      cout << " /    )))   \\ " << endl;
      cout << "(____(((_____)" << endl;
      cout << endl;
            break;

            case 3:

      cout << "   //\\\\\\\\     " << endl;
      cout << "  ((-V-\\\\\\    " << endl;
      cout << "   )<  (3))   " << endl;
      cout << "   //\\\\\\((    " << endl;
      cout << "  (__  ___)   " << endl;
      cout << "  /  \\\\\\   \\  " << endl;
      cout << " /    )))   \\ " << endl;
      cout << "(____(((_____)" << endl;
      cout << endl;
            break;

                }

        //waitForUser();

    }

    void treeTraveler(){

            //system("cls");

    Enemy treeFolk = Enemy(rand()%10+1,rand()%20+10,rand()%10+1,rand()%10+1,rand()%10+1,"Terry");
    srand(time(0));

    treeFolk.species = "Treant";
      cout << "  OOOOOO  " << endl;
      cout << " OOOOOOOO " << endl;
      cout << "  OOOOOO  " << endl;
      cout << "   O|||   " << endl;
      cout << "   |o|o ^ " << endl;
      cout << "   ||^| | " << endl;
      cout << " (X)|v|-8 " << endl;
      cout << "   |||| | " << endl;
      cout << "  ^^^^^^  " << endl;

      vector <string> treeImage ={"  OOOOOO  ",
                                  " OOOOOOOO ",
                                  "  OOOOOO  ",
                                  "   O|||   ",
                                  "   |o|o ^ ",
                                  "   ||^| | ",
                                  " (X)|v|-8 ",
                                  "   |||| | ",
                                  "  ^^^^^^  "};

        treeFolk.sprite = treeImage;

      cout << "?-----------------------------------------------------------------?" << endl;
      cout << "  You see a Treefolk.  " << endl;
      cout << endl;
      cout << "  Treefolk: Hail traveler! My name is " << treeFolk.name << "." << endl;
      cout << "  Ive come to see the mighty adventurer himself with my own eyes!"  << endl;
      cout << endl;
      cout << "?-----------------------------------------------------------------?" << endl;
    int choice;
    cout << "?----------------?" << endl;
    cout << " 1 : Ask to join "<<endl;
    cout << " 2 : Attack "<<endl;
    cout << " 3 : Run "<<endl;
    cout << "?-------------?" << endl;
    cin >> choice;

    switch(choice){

    case(1):

      cout << endl;
      cout << "?-----------------------------------------------------------------?" << endl;
      cout << "  " << treeFolk.name << ": You mean it! It would be an honor to" << endl;
      cout << "  fight side by side with the great adventurer himself!" << endl;
      cout << "?-----------------------------------------------------------------?" << endl;
        party.push_back(treeFolk);
    break;

case(2):
      cout << "  OOOOOO  " << endl;
      cout << " OOOOOOOO " << endl;
      cout << "  OOOOOO  " << endl;
      cout << "   O\\|/   " << endl;
      cout << "   |o|o ^ " << endl;
      cout << "   ||^| | " << endl;
      cout << " (X)|-|-8 " << endl;
      cout << "   |||| | " << endl;
      cout << "  ^^^^^^  " << endl;
      cout << endl;
        battle(treeFolk);
break;

default:
      cout << "  OOOOOO  " << endl;
      cout << " OOOOOOOO " << endl;
      cout << "  OOOOOO  " << endl;
      cout << "   OOO|   " << endl;
      cout << "   |||o ^ " << endl;
      cout << "   |||| |" << endl;
      cout << "___||||-8______*___ " << endl;
      cout << "  (((|| | " << endl;
      cout << "  ^^^^^^  " << endl;
      cout << endl;

    }

    }

void bees(){



    cout << " /| _" << endl;
    cout << " ||/|  ." << endl;
    cout << " | /O .  ." << endl;
    cout << " ||" << endl;
    cout << " ||    ." << endl;
    cout << "/__\\________" << endl;

      cout << endl;
      cout << "?-------------------?" << endl;
      cout << "  You see a beehive  " << endl;
      cout << "?-------------------?" << endl;
    int choice;
    cout << endl;
    cout << "?-------------?" << endl;
    cout << " 1 : Hit   "<<endl;
    cout << " 2 : Leave     "<<endl;
    cout << "?-------------?" << endl;
    cin >> choice;
//system("cls");
     switch(choice){

            case 1:

                currentHP -= 10;
                if(currentHP < 0)
                    currentHP = 0;

      cout << "  \\ \\ \\ | /  /  " << endl;
      cout << " \\  .   .    .  /" << endl;
      cout << "     * .  * . * " << endl;
      cout << " -  .    . *     -" << endl;
      cout << "  .  *  .  . * " << endl;
      cout << "  /    .  .   * \\" << endl;
      cout << "   / / / | \\ \\  " << endl;
      cout << endl;
      cout << "?--------------------------------?" << endl;
      cout << " What did you think would happen? "<<endl;
      cout << endl;
      cout << "             -10 HP               "<<endl;
      cout << "?--------------------------------?" << endl;

            break;


            default:

            break;

                }

        //waitForUser();
}

void goblinEncounter()
    {
        Enemy goblin = Enemy(rand()%10+1,rand()%10+1,rand()%10+1,rand()%10+5,10,"cabolin");
        printGoblin();
        battle(goblin);
    }

void mimicEncounter()
    {
   vector <string> mimicSprite={"       ___________   ",
                                "      /(,\\/,)    /\\\\ ",
                                "     /__________/\\\\\\\\",
                                "     \\V        V\\\\\\\\/",
                                "     _\\__________\\O/ ",
                                "    |     //  |    | ",
                                "    | /     / | // | ",
                                "    |_________|____| "};



        Enemy mimic = Enemy(rand()%10+1,rand()%10+1,rand()%10+1,rand()%10+5,10,"mimic");

        //mimicSprite = furrification(mimicSprite);
        for(int i = 0;i<=7;i++){

            cout << mimicSprite[i] << endl;

        }



                string line;
        vector<string> personalities;
        ifstream file("personalityTraits.txt");
        int total_lines=0;

        while(getline(file,line))
        {
        total_lines++;
        personalities.push_back(line);
        }

        int random_number = rand()%total_lines;

        for(int i=0;i<3;i++){
         mimic.personality.push_back(personalities[random_number]);
         cout << personalities[random_number] << endl;
        random_number = rand()%total_lines;
        }

        battle(mimic);
    }

    void randomEvent(){
    srand(time(0));
    int ladyLuck = rand()%5;

    switch(ladyLuck){

    case 1:
        goblinEncounter();
    break;

    case 2:
        beggar();
    break;

    case 3:
        mimicEncounter();
    break;

    default:
        treeTraveler();
    }

    char cont;
    cout << "O-----------------------------O" << endl;
    cout << "|You traverse to the next area|" << endl;
    cout << "| 1: Continue                 |" << endl;
    cout << "O-----------------------------O" << endl;
    cin >> cont;


}
/*
    def enemyEncounter(int atk, int def, int spd, int hp, int lvl,string name)

        Enemy badguy = Enemy(atk,def,spd,hp,lvl,name);

        string line;
        vector<string> personalities;
        ifstream file("personalityTraits.txt");
        int total_lines=0;

        while(getline(file,line))
        {
        total_lines++;
        personalities.push_back(line);
        }

        int random_number = rand()%total_lines;

        for(int i=0;i<3;i++){
         badguy.personality.push_back(personalities[random_number]);
         cout << personalities[random_number] << endl;
        random_number = rand()%total_lines;
        }

        battle(badguy)

*/
};