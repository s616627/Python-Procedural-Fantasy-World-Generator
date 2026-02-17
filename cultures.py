
class Culture:

    def __init__(self,name,biome,buildings=[],attributes = []):

        #string
        self.name = name
        self.biome = biome

        #building array (buildings that can be built)
        self.buildings = buildings

        #attributes about culture
        self.attributes = attributes

