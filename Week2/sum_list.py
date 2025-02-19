import random
num_list =[]

for x in range (0,9):
    num = random.randint(0,4)
    num_list.append(num)


def sum():
    prv = 0
    for num in num_list:
        new = num
        total = prv + new
        prv = total
    print(f'the total sum is {total}')

sum()
