# Напишете програма, която да пресмята резултата от игра. Първо получавате число,
# което показва колко хода ще продължи играта.
# После за всеки ход на играта ще получавате по едно ново число.
# Според интервала в който попада числото се прибавят точки. Ако числото е отрицателно или по-голямо 50,
# тогава то е невалидно. В началото на играта резултата е 0 и на всеки ход се прибавят точки по следният
# начин:
#
# •	От 0 до 9  20 % от числото
# •	От 10 до 19  30 % от числото
# •	От 20 до 29  40 % от числото
# •	От 30 до 39  50 точки
# •	От 40 до 50  100 точки
# •	Невалидно число  резултата се дели на 2
# Освен резултата програмата трябва да изкарва статистика за проценти числа в дадените интервали.
# Вход
# Входът се чете от конзолата:
# Първи ред - колко хода ще има по време на играта – цяло число в интервала [1...100]
# За всеки ход – числата, които се проверяват в кой интервал са – цели числа в интервала [-100...100]
# Изход
# Да се отпечата на конзолата 7 реда:
# •	1ви ред: "{Краен резултат}"
# •	2ри ред: "From 0 to 9: {процент в интервала}%"
# •	3ти ред: "From 10 to 19: {процент в интервала}%"
# •	4ти ред: "From 20 to 29: {процент в интервала}%"
# •	5ти ред: "From 30 to 39: {процент в интервала}%"
# •	6ти ред: "From 40 to 50: {процент в интервала}%"
# •	7ми ред: "Invalid numbers: {процент в интервала}%"
# Всички числа трябва да са форматирана до вторият знак след запетаята.
n = int(input())
bonus = 0
fr_1_to_10 = 0
fr_1_to_9 = 0
fr_20_to_29 = 0
fr_10_to_19 = 0
fr_30_to_39 = 0
fr_40_to_49 = 0
fr_else = 0
moves = int()
for moves in range(1, n + 1):
    move = int(input())
    if 0 <= move <= 9:
        bonus += 0.2 * move
        fr_1_to_9 += 1
    elif 10 <= move <= 19:
        fr_10_to_19 += 1
        bonus += 0.3 * move
    elif 20 <= move <= 29:
        bonus += 0.4 * move
        fr_20_to_29 += 1
    elif 30 <= move <= 39:
        bonus += 50
        fr_30_to_39 += 1
    elif 40 <= move <= 50:
        bonus += 100
        fr_40_to_49 += 1
    else:
        bonus /= 2
        fr_else += 1
print(f'{bonus:.2f}')
print(f'From 0 to 9: {(fr_1_to_9 / n):.2%}')
print(f'From 10 to 19: {(fr_10_to_19 / n):.2%}')
print(f'From 20 to 29: {(fr_20_to_29 / n):.2%}')
print(f'From 30 to 39: {(fr_30_to_39 / n):.2%}')
print(f'From 40 to 50: {(fr_40_to_49 / n):.2%}')
print(f'Invalid numbers: {(fr_else / n):.2%}')


