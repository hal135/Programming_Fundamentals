factor = int(input())
count = int(input())
multiples_list = []

for i in range(count):
    multiple = factor * (i + 1)
    multiples_list.append(multiple)

print(multiples_list)
