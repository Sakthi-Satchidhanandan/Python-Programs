numbers = [2, 1, 6, 1, 9]

while True:
    print("\nCurrent list:", numbers)
    choice = input("Add a number? (yes/no): ")
    if choice.lower() == "yes":
        value = int(input("Number to add: "))
        numbers.append(value)
        order = input("Enter sorting order (asc/des): ")
        if order.lower() == "asc":
            numbers.sort()
        elif order.lower() == "des":
            numbers.sort(reverse=True)
        else:
            print("Invalid choice! Sorting in ascending order.")
            numbers.sort()
    else:
        break
