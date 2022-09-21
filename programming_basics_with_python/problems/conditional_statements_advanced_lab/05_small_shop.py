product = input()
town = input()
quantity = float(input())
price = 0

if town == 'Sofia' and product == 'coffee':
    price = 0.50
    print(quantity * price)
elif town == 'Sofia' and product == 'water':
    price = 0.80
    print(quantity * price)
elif town == 'Sofia' and product == 'beer':
    price = 1.20
    print(quantity * price)
elif town == 'Sofia' and product == 'sweets':
    price = 1.45
    print(quantity * 1.45)
elif town == 'Sofia' and product == 'peanuts':
    price = 1.60
    print(quantity * price)

if town == 'Plovdiv' and product == 'coffee':
    price = 0.40
    print(quantity * price)
elif town == 'Plovdiv' and product == 'water':
    price = 0.70
    print(quantity * price)
elif town == 'Plovdiv' and product == 'beer':
    price = 1.15
    print(quantity * price)
elif town == 'Plovdiv' and product == 'sweets':
    price = 1.30
    print(quantity * price)
elif town == 'Plovdiv' and product == 'peanuts':
    price = 1.50
    print(quantity * price)

if town == 'Varna' and product == 'coffee':
    price = 0.45
    print(quantity * price)
elif town == 'Varna' and product == 'water':
    price = 0.70
    print(quantity * price)
elif town == 'Varna' and product == 'beer':
    price = 1.10
    print(quantity * price)
elif town == 'Varna' and product == 'sweets':
    price = 1.35
    print(quantity * price)
elif town == 'Varna' and product == 'peanuts':
    price = 1.55
    print(quantity * price)

