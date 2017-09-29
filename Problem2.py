#initialize a variable that we will update later in a for loop iterating over ints
dummy_sum = 0

upper_limit = 4000000

def fib(n):
    a,b = 1,1
    for i in range(n-1):
        a,b = b,a+b
    return a

for n in range(0,40):
    temp = fib(n)
    print(temp)
    if temp > upper_limit:
        break
    elif temp % 2 == 0:
        dummy_sum = temp + dummy_sum

        print(dummy_sum)




print(dummy_sum)
