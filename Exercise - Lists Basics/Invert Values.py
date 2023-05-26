numbers = input()
number_list = numbers.split()
opposite_list = []


for number in number_list:
    number = -int(number)
    opposite_list.append(number)

print(opposite_list)

