#class element
class Element:
    def __init__(self,name,weakness,strength):
        self.name = name
        self.weakness = weakness
        self.strength = strength


#class for spell
class Spell:
    def __init__(self,element,attack,hpAbsorb,mpAbsorb,effects):
        self.element = element
        self.attack = attack
        self.hpAbsorb = hpAbsorb
        self.mpAbsorb = mpAbsorb
        self.effects = effects


class Status:
    def __init__(self, name, element, hpLoss, sleep):
        self.name = name
        self.element = element
        self.hpLoss = hpLoss
        self.sleep = sleep