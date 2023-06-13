n1 = int(input())
n2 = int(input())
n3 = int(input())

if n3 >= 9:
    n3 = 0
    n2 += 1
    if n2 >= 9:
        n2 = 0
        n1 += 1

version = "".join([f"{n1}.{n2}.{n3}"])

print(version)

