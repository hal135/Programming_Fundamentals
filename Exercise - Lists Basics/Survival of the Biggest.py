numbers = list(map(int, input().split()))
n = int(input())
new_numbers = sorted(numbers)[n:]
new_numbers_string = ', '.join(map(str, new_numbers))
print(new_numbers_string)
