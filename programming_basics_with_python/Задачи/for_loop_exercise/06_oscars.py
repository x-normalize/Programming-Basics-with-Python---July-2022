name_actor = input()
init_points = float(input())
number_judge = int(input())
copy_points = init_points

for i in range(1, number_judge + 1):
    name_judge = input()
    judge_points = float(input())

    copy_points = copy_points + (len(name_judge) * judge_points) / 2

    if copy_points >= 1250.5:
        break

final_points = 1250.5 - copy_points

if copy_points < 1250.5:
    print(f'Sorry, {name_actor} you need {final_points:.1f} more!')
else:
    print(f'Congratulations, {name_actor} got a nominee for leading role with {copy_points:.1f}!')


