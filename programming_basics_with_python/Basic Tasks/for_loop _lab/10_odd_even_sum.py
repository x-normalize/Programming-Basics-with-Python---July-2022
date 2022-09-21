n = int(input())

even = 0
odd = 0

for k in range(1, n + 1):
    current_num = int(input())

    if k % 2 == 0:
        even += current_num
    else:
        odd += current_num

diff = abs(even - odd)
if even == odd:
    print(f'Yes')
    print(f'Sum = {even}')
else:
    print(f'No')
    print(f'Diff = {diff}')
