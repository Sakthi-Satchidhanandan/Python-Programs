numbers = [1, 2, 5, 8, 8, 1, 9, 9, 4, 2, 1, 7, 5, 2, 8, 6, 5, 4, 2, 9,
           3, 8, 2, 2, 9, 1, 6, 8, 7, 6, 5, 3, 0, 7, 6, 9, 7, 3, 5, 8,
           9, 6, 0, 8, 1, 6, 2, 7, 9, 1, 7, 6, 9, 8, 2, 3, 5, 6, 8,
           9, 2, 4, 3, 8, 2, 9, 4, 1, 5, 0, 3, 2, 0, 0, 1, 0, 7, 0,
           8, 2, 0, 0, 0, 2, 7, 9, 7, 5]
           
count_dict = {}

for num in numbers:
    if num in count_dict:
        count_dict[num] = count_dict[num] + 1
    else:
        count_dict[num] = 1
for key in sorted(count_dict):
    print(key, ":", count_dict[key])
