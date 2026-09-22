class Item:
    def __init__(self,price,weight,name,attributes,description):

        #int
        self.price = price
        self.weight = weight

        #string
        self.name = name

        # string list
        self.attributes = attributes
        self.description = description

    def print_name(self):
        print(self.name)


class Weapon(Item):
    def __init__(self,price,weight, atk_multp, def_multp, name,attributes,handle_attributes,description):

        super().__init__(price,weight,name,attributes,description)

        #int
        self.atk_multp = atk_multp
        self.def_multp = def_multp

        # string list
        self.handle_attributes = handle_attributes

class Book(Item):
    def __init__(self,price,weight,name,attributes,coverAttributes,writing,description):

        super().__init__(price,weight,name,attributes,description)

        # string list
        self.coverAttributes = coverAttributes
        self.writing = writing


class Food(Item):
    def __init__(self,price,fullness,weight,name,attributes,description):

        super().__init__(price, weight, name, attributes, description)

        #int
        self.fullness = fullness


class Potion(Item):
    def __init__(self, price, fullness, weight, name, attributes, effects, description):
        super().__init__(price, weight, name, attributes, description)

        # int
        self.fullness = fullness

        # string list
        self.effects = effects


class Armor(Item):
    def __init__(self,price,weight,def_multp,name,attributes,description,body_part):

        super().__init__(price,weight,name,attributes,description)

        #int
        self.def_multp = def_multp

        #string
        self.body_part = body_part


