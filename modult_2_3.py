my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
result = []
i = 0
while i < len(my_list):
    i += 1
    if my_list[i-1] < 0:
        break
    if my_list[i-1] == 0:
        continue
    print(my_list[i-1])
