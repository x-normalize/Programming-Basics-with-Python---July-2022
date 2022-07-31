budget = int(input())
season = input()
number_of_fishers = int(input())
cost = 0

if season == 'Summer' or season == 'Autumn':
    cost = 4200

if season == 'Spring':
    cost = 3000

if season == 'Winter':
    cost = 2600

if number_of_fishers <= 6:
    cost -= cost * 0.10
elif 7 <= number_of_fishers <= 11:
    cost -= cost * 0.15
elif number_of_fishers > 11:
    cost -= cost * 0.25

if number_of_fishers % 2 == 0 and season != 'Autumn':
    cost -= cost * 0.05

diff = abs(budget - cost)

if budget >= cost:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {diff:.2f} leva.")


