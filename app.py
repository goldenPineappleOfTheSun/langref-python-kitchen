class Food:
    def __init__(self, name, state, emoji):
        self.name = name
        self.state = state
        self.emoji = emoji

    def __str__(self):
        return f'{self.emoji}:{self.name}:{self.state}'

    def fry(self):
        self.state = 'жареный'
        return self

class Chicken(Food):
    def __init__(self):
        super().__init__('курица', 'хороший', '🍗')

class Apple(Food):
    def __init__(self):
        super().__init__('яблоко', 'хороший', '🍎')

class Omelete(Food):
    def __init__(self):
        super().__init__('яишница', 'хороший', '🍳')

    def fry(self):
        pass
        
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

f = Refrigerator(10, 10)
stove = Stove()
f.add(Apple()).add(Apple()).addToFreezer(Chicken())
apple = f.get('яблоко')
stove.fry(apple)
fe = Omelete()
print(fe)
print(stove.fry(fe))
