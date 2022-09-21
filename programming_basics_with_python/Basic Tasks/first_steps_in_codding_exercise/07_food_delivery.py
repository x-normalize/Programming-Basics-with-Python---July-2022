chicken_menus_number = int(input())
fish_menus_number = int(input())
vegans_menus_number = int(input())

price_for_chicken_menus = chicken_menus_number * 10.35
price_for_fish_menus = fish_menus_number * 12.40
price_for_vegans_menus = vegans_menus_number * 8.15
price_for_all = price_for_chicken_menus + price_for_fish_menus + price_for_vegans_menus
price_for_desert = price_for_all * 0.20
price_for_delivery = 2.50
final_price = price_for_all + price_for_desert + price_for_delivery
print(final_price)

