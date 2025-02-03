def find_max(numbers):
    max_num = numbers[0]  # Assume the first number is the largest
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num


print(find_max([3, 5, 7, 2, 8]))  # Output: 8

