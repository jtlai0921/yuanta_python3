import random
poker = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10'
         , 'J', 'Q']
# poker = poker + poker
# poker = poker * 4
print(poker)
print(poker[2], poker[-2])
print(poker[1:4])
print(poker.count('A'))
poker.append('K')
print(poker)
poker.reverse()
print(poker)
poker.sort()
print(poker)
random.shuffle(poker)
print(poker)

