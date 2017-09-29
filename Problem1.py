#initialize a variable that we will update later in a for loop iterating over ints
dummy_sum = 0

upper_limit = 1000

naturals = range(0,upper_limit)

for n in range(0,upper_limit):
    if n % 3 == 0:
        dummy_sum = n + dummy_sum
        print(dummy_sum)
        #input("enter to continue")

    elif n % 5 == 0:
        dummy_sum = n + dummy_sum
        print(dummy_sum)
        #input("enter to continue")

print(dummy_sum)
