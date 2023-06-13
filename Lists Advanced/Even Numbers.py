def find_even_indices(numbers_str):
    numbers = numbers_str.split(", ")
    even_indices = []

    for i, num in enumerate(numbers):
        if int(num) % 2 == 0:
            even_indices.append(i)

    return even_indices



input_str = input()
indices = find_even_indices(input_str)
print(indices)
