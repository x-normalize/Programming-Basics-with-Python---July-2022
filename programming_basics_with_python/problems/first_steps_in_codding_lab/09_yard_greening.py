meters_that_will_be_landed = float(input())
price_for_one_meter = meters_that_will_be_landed * 7.61
discount = price_for_one_meter * 0.18
final_price = price_for_one_meter - discount

print(f'The final price is: {final_price} lv.')
print(f'The discount is: {discount} lv.')

