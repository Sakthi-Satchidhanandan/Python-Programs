n = int(input("Enter how many elements in the list: "))

numbers = []

for i in range(n):
    value = int(input(f"Enter element {i + 1}: "))
    numbers.append(value)

minimum = numbers[0]
maximum = numbers[0]

for num in numbers:
    if num < minimum:
        minimum = num
    if num > maximum:
        maximum = num

print("List:", numbers)
print("Minimum value:", minimum)
print("Maximum value:", maximum)
