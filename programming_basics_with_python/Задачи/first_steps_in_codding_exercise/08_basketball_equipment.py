year_tax_for_play_basketball = int(input())

price_for_shoes = year_tax_for_play_basketball - (year_tax_for_play_basketball * 0.40)
price_for_suit = price_for_shoes - (price_for_shoes * 0.20)
price_for_basketball_ball = price_for_suit / 4
price_for_accessories = price_for_basketball_ball / 5
total_price = year_tax_for_play_basketball + price_for_shoes + price_for_suit + price_for_basketball_ball + \
              price_for_accessories

print(total_price)

