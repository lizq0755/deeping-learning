class Man:
    def __init__(self, name):
        self.name = name
        print('Initialized!')

    def hello(self):
        print('Hello ' + self.name + '!')

    def goodbye(self):
        print('Good-bye ' + self.name + '!')

m = Man('Kayden')
m.hello()
m.goodbye()

print(type(m))