number_as_digits = [int(number) for number in input().split()]
result = [number for number in number_as_digits if number % 2 == 0]
print(result)