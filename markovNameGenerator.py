import random
import sys

#this program was based off of this https://www.roguebasin.com/index.php/Markov_chains_name_generator_in_Python

#class for a list of strings(prefix) and the letters that come after(suffix)
class MarkovDictionary:

    #init function that includes a python dictionary datatype
    def __init__(self):
        self.dict = {}

    def __getitem__(self, key):
        if key in self.dict:
            return self.dict[key]
        else:
            raise KeyError(key)

    def add_key(self, prefix, suffix):
        if prefix in self.dict:
            self.dict[prefix].append(suffix)
        else:
            self.dict[prefix] = [suffix]

    def get_suffix(self, prefix):
        return random.choice(self[prefix])


class MarkovName:

    def __init__(self,name_list,chainlen=2):

        self.name_list = name_list

        if chainlen > 10 or chainlen < 1:
            print("Chain Length Must Be 1-10 in Length")
            sys.exit(0)

        self.markovDict = MarkovDictionary()
        oldnames = []
        self.chainlen = chainlen

        for name in name_list:
            name = name.strip()
            s = " " * chainlen + name
            oldnames.append(name)
            for n in range(0,len(name)):
                self.markovDict.add_key(s[n:n+chainlen], s[n+chainlen])
            self.markovDict.add_key(s[len(name):len(name)+chainlen],"\n")

    #generate new name using the markov chain
    def New(self,maxLength=10):
        prefix = " "*self.chainlen
        newName = ""
        suffix = ""

        while True:
            suffix = self.markovDict.get_suffix(prefix)
            if suffix == "\n" or len(newName) >= maxLength:
                break
            else:
                newName = newName + suffix
                prefix = prefix[1:] + suffix

            while newName.lower() in set(self.name_list):
                newName = self.New(maxLength)


        new_name_split = newName.split(' ')

        new_name_capitalized = ""

        for x in new_name_split:

            last_string = "**"

            if x is new_name_split[0]:
                new_name_capitalized = new_name_capitalized + x.capitalize()
            elif len(x) == 1:
                new_name_capitalized = new_name_capitalized + x
            else:
                new_name_capitalized = new_name_capitalized + ' ' + x.capitalize()

            last_string = x

        return new_name_capitalized





