class Chicken:
    def __init__(self):
        self.name = 'курица'

    def __str__(self):
        return '🍗'

class Apple:
    def __init__(self):
        self.name = 'яблоко'

    def __str__(self):
        return '🍎'

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

f = Refrigerator(10, 10)
f.add(Apple()).add(Apple()).addToFreezer(Chicken())
print(f.get('яблоко'))
print(f)