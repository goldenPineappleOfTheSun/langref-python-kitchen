from enum import Enum
import logging

logging.basicConfig(filename='app.log', filemode='w', format='[%(asctime)s: %(levelname)s] %(message)s')

class FoodStates(Enum):
    good = 'хороший'
    bad = 'испорченый'
    used = '[использован!]'
    fried = 'жареный'
    boiled = 'варёный'
    steamed = 'тушёный'

book_of_receipts = {
    'бутерброд': (('хлеб', FoodStates.good), ('кура', FoodStates.good))
}

class Food:
    def __init__(self, name, state, emoji):
        self.name = name
        self.state = state
        self.emoji = emoji


    def __str__(self):
        return f'{self.emoji}:{self.name}:{self.state.value}'

    def fry(self):
        if self.state == FoodStates.used:
            logging.warning(f'Невозможно снова использовать: {self.name}')
            return self
        self.state = FoodStates.fried
        return self

    def boil(self):
        if self.state == FoodStates.used:
            logging.warning(f'Невозможно снова использовать: {self.name}')
            return self
        self.state = FoodStates.boiled
        return self

    def steam(self):
        if self.state == FoodStates.used:
            logging.warning(f'Невозможно снова использовать: {self.name}')
            return self
        self.state = FoodStates.steamed
        return self

    def used(self):
        self.state = FoodStates.used
        return self

class Bread(Food):
    def __init__(self):
        super().__init__('хлеб', FoodStates.good, '🍞')

class Chicken(Food):
    def __init__(self):
        super().__init__('кура', FoodStates.good, '🍗')

class Apple(Food):
    def __init__(self):
        super().__init__('яблоко', FoodStates.good, '🍎')

class Omelete(Food):
    def __init__(self):
        super().__init__('яишница', FoodStates.good, '🍳')

    def fry(self):
        pass

class Sandwich(Food):
    def __init__(self):
        super().__init__('бутерброд', FoodStates.good, '🥪')

class Storage:
    def __init__(self, capacity = 10):
        self.items = []
        self.capacity = capacity

    def add(self, product):
        if (len(self.items) < self.capacity):
            self.items.append(product)
        return self

    def get(self, name):
        for item in self.items:
            if item.name == name:
                self.items.remove(item)
                return item

    def __str__(self):
        return str([str(x) for x in self.items])

class Refrigerator(Storage):
    def __init__(self, capacity, freezerCapacity):
        super().__init__(capacity)
        self.freezer = Freezer(freezerCapacity)

    def get(self, name):
        return super().get(name) or self.freezer.get(name)

    def addToFreezer(self, item):
        self.freezer.add(item)
        return self

    def __str__(self):
        return str((str([str(x) for x in self.items]), self.freezer.__str__()))

class Freezer(Storage):
    pass

class Shelve(Storage):
    pass

class Stove:
    def __init__(self):
        pass

    def fry(self, obj):
        return obj.fry()

    def steam(self, obj):
        return obj.steam()

    def boil(self, obj):
        return obj.boil()

class Receipt:
    def __init__(self, type, products):
        self.type = type
        self.products = products

book_of_receipts = {
    'бутерброд': Receipt(Sandwich, (('хлеб', 'хороший'), ('кура', 'хороший'))),
}

def mix(*arr):
    arr = set(arr)
    for k in book_of_receipts:
        r = book_of_receipts[k]
        match_count = 0
        for a in r.products:
            found = False
            for b in arr:
                if (b.name, b.state.value) == a:
                    found = True
            if found:
                match_count += 1
        if match_count == len(r.products):
            for item in arr:
                item.used()
            return r.type()
    return None

f = Refrigerator(10, 10)
stove = Stove()
f.add(Apple()).add(Apple()).addToFreezer(Chicken())
apple = f.get('яблоко')
stove.fry(apple)
fe = Omelete()
chicken = Chicken()
bread = Bread()
print(mix(chicken, bread))
print(mix(chicken, bread))
print(chicken)
chicken.fry()
