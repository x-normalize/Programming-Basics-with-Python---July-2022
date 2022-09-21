budget = float(input())
season = input()
cost = 0


if budget <= 100:
    print('Somewhere in Bulgaria')
    if season == 'summer':
        cost = budget * 0.30
        print(f'Camp - {cost:.2f}')
    elif season == 'winter':
        cost = budget * 0.70
        print(f'Hotel - {cost:.2f}')

elif 100 <= budget <= 1000:
    print('Somewhere in Balkans')
    if season == 'summer':
        cost = budget * 0.40
        print(f'Camp - {cost:.2f}')
    elif season == 'winter':
        cost = budget * 0.80
        print(f'Hotel - {cost:.2f}')

elif budget > 1000:
    print('Somewhere in Europe')
    cost = budget * 0.90
    print(f'Hotel - {cost:.2f}')
