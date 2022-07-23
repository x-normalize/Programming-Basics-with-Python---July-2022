from math import floor, ceil
name_for_the_movie = input()
time_for_movie = int(input())
break_time = int(input())

time_for_lunch = break_time * 1/8
time_for_break = break_time * 1/4
rest_time = break_time - time_for_lunch - time_for_break
diff = abs(rest_time - time_for_movie)

if rest_time >= time_for_movie:
    print(f'You have enough time to watch {name_for_the_movie} and left with {ceil(diff)} minutes free time.')
elif rest_time < time_for_movie:
    print(f"You don't have enough time to watch {name_for_the_movie}, you need {ceil(diff)} more minutes.")
