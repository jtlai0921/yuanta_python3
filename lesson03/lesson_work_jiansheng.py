import random

range_start = 1
range_end = 99
ans = random.randint(range_start, range_end)

while True:
    inpu = int(input("%d~%d -> " % (range_start, range_end)))
    if(ans == inpu):
        print("OK")
        break
    elif(inpu > ans):
        range_end = inpu
    elif(inpu < ans):
        range_start = inpu