number_list = input().split()

round_value = []

for num in number_list:
    round_value.append(round(float(num)))

print(round_value)