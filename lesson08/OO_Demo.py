class Human:
    name = ''
    age = 0
    sex = ''

    def __str__(self):
        return self.name + ',' + str(self.age) + ',' + self.sex


h = Human()
h.name = 'Vincent'
h.age = 20
h.sex = '男'

print(h.name, h.age, h.sex)
print(h)
