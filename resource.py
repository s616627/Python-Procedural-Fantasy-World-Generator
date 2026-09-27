#class resource
class Resource:
    def __init__(self,name,category,tech,biomes):

        #string
        self.name = name
        self.category = category
        self.tech = tech

        #dict
        self.biomes = biomes
