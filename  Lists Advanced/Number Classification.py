numbers = input().split(", ")
positive = [number for number in numbers if int(number) >= 0]
print(f"Positive: {', '.join(positive)}")
negative = [number for number in numbers if int(number) < 0]
print(f"Negative: {', '.join(negative)}")
even = [number for number in numbers if int(number) % 2 == 0]
print(f"Even: {', '.join(even)}")
odd = [number for number in numbers if int(number) % 2 != 0]
print(f"Odd: {', '.join(odd)}")