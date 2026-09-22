#class element
class Element:
    def __init__(self,name,weakness,strength):
        self.name = name
        self.weakness = weakness
        self.strength = strength


#class for spell
class Spell:
    def __init__(self,element,attack,effects,status,status_percent=0,hp_absorb=0,mp_absorb=0):

        #Element
        self.element = element

        #Status
        self.status = status

        #int
        self.attack = attack
        self.status_percent = status_percent
        self.hp_absorb = hp_absorb
        self.mp_absorb = mp_absorb

        #Effects
        self.effects = effects


class Status:
    def __init__(self, name, element, hp_loss, sleep):

        #string
        self.name = name

        #Element
        self.element = element

        #int
        self.hp_loss = hp_loss

        #bool
        self.sleep = sleep