time = int(input())
day_of_the_week = input()

if 10 <= time <= 18 and day_of_the_week in 'Monday Tuesday Wednesday Thursday Friday Saturday':
    print('open')
else:
    print('closed')
