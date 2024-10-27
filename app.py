rows = int(input("Enter the number of rows: "))


print("For rows =", rows)
# Upper half and the middle line
for i in range(1, rows + 1):
    print(' ' * (rows - i) + '*' * (2 * i - 1))

# Lower half
for i in range(rows - 1, 0, -1):
    print(' ' * (rows - i) + '*' * (2 * i - 1))