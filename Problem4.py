placeholder = int()

for i in range(0, 999):
    for j in range(0,999):
        check = str(i*j)
        if check == check[::-1]:
            if i*j > placeholder:
                placeholder = i*j
                print(placeholder)