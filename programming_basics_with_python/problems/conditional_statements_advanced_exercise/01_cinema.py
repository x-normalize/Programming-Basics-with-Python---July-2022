name_of_the_movie = input()
number_of_seats = int(input())
number_of_colons = int(input())
price = 0

if name_of_the_movie == 'Premiere':
    price = 12 * number_of_seats * number_of_colons
    print(f'{price:.2f}')

elif name_of_the_movie =='Normal':
    price = 7.50 * number_of_seats * number_of_colons
    print(f'{price:.2f}')

elif name_of_the_movie =='Discount':
    price = 5 * number_of_seats * number_of_colons
    print(f'{price:.2f}')



