#class resource
import json

class Resource:
    def __init__(self,name,category,tech,biomes:list):

        #string
        self.name = name
        self.category = category
        self.tech = tech

        #dict
        self.biomes = biomes

    def __repr__(self):
        return f"Resource({self.name!r}, {self.category!r}, {self.tech!r}, {self.biomes})"

def load_resources(path):
    with open(path, encoding="utf-8") as f:
        return [Resource(**entry) for entry in json.load(f)]