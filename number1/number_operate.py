import random
i = 0
while i < 10:
    print(random.randint(0, 100))
    i = i + 1

test = ['123', '345', '1233']
i = 0
str1 = ''
while i < 5:
    str1 = str1 + test[random.randint(0, len(test)-1)]
    i = i + 1
print(str1)
