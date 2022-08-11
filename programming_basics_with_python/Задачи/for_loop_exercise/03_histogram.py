n = int(input())
count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
for c in range(1 , n + 1):
    number = int(input())
    if number < 200:
        count1 += 1
    elif 200 <= number <= 399:
        count2 += 1
    elif 400 <= number <= 599:
        count3 += 1
    elif 600 <= number <= 799:
        count4 += 1
    elif number > 799 :
        count5 += 1
first = count1 / n
second = count2 / n
third = count3 / n
forth = count4 / n
fifth = count5 / n
print(f'{first:.2%}')
print(f'{second:.2%}')
print(f'{third:.2%}')
print(f'{forth:.2%}')
print(f'{fifth:.2%}')