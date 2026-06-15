# Läsa och förstå kod

"""
Skriv ner vad du tror kommer skrivas ut. Skriv sedan in koden i din IDE, exakt
som den står, och kör den. Fick du samma resultat som du trodde? Om inte, varför?
"""

# Uppgift 1
#
# Svar: Anakonda Boaorm

"""
class SafeStorage:
    __data = None
    def get(self):
        return self.__data
    def put(self, data):
        self.__data = data

safe = SafeStorage()
safe.put("Anakonda")
x = safe.get()
safe.put("Boaorm")
y = safe.get()
print(x, y)

"""


# Uppgift 2
#
# Svar: Anakonda Boaorm
# Detta djur har vi inget ljud för. (Från superklass Animal)
# Mjau!
# Voff!
# Kuckeliku!
# Goddag Goddag!

"""
class Animal:
    def make_noise(self):
        print("Detta djur har vi inget ljud för.")

class Dog(Animal):
    def make_noise(self):
        print("Voff!")

class Cat(Animal):
    def make_noise(self):
        super().make_noise()
        print("Mjau!")

class Rooster(Animal):
    def make_noise(self):
        print("Kuckeliku!")
        
class Parrot(Animal):
    def make_noise(self):
        print("Goddag Goddag!!")

def sound_off(animals):
    for animal in animals:
        animal.make_noise()

c = Cat()
d = Dog()
h = Rooster()
p = Parrot()
sound_off([c, d, h, p)

"""




