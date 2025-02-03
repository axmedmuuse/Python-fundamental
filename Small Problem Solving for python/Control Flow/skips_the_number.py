def skip_five():
    for i in range(1, 11):
        if i == 5:
            continue
        print(i)

# Test the function
skip_five()
# Output:
# 1
# 2
# 3
# 4
# 6
# 7
# 8
# 9
# 10