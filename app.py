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

class Refrigerator:
    def __init__(self):
        self.items = []
        self.capacity = 10

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

f = Refrigerator()
f.add(Apple())
    .add(Apple())
    .add(Chicken())
print(f.get('яблоко'))
print(f)