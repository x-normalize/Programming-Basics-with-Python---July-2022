days_to_stay = int(input())
room_type = input()
rating = input()
cost = 0
days_to_stay = days_to_stay - 1

if room_type == 'room for one person':
    cost = 18 * days_to_stay


elif room_type == 'apartment':
    cost = 25 * days_to_stay
    if days_to_stay < 10:
        cost -= cost * 0.30
    elif 10 <= days_to_stay <= 15:
        cost -= cost * 0.35
    elif days_to_stay > 15:
        cost -= cost * 0.50

elif room_type == 'president apartment':
    cost = 35 * days_to_stay
    if days_to_stay < 10:
        cost -= cost * 0.10
    elif 10 <= days_to_stay <= 15:
        cost -= cost * 0.15
    elif days_to_stay > 15:
        cost -= cost * 0.20

if rating == 'positive':
    cost += cost * 0.25
elif rating == 'negative':
    cost -= cost * 0.10

print(f'{cost:.2f}')
