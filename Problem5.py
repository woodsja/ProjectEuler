stop = False
remainder = 0

iterable = 1

#I don't know the upper limit a priori so maybe while is the right tool?
while not stop:
    print("new number is {}".format(iterable))

    for i in range(1, 20):
        remainder = iterable % i + remainder
        # holy shit, this takes forever
        # could speed it up by limiting to prime factorization of range integers
        # unfortunately, i realized this after I started running the program
        # alternatively could  throw an exit flag as soon as remainder > 0
        # prime factorization's probably faster...

        #print("i is currently {} and the remainder is currently {}".format(i, remainder))

    if remainder == 0:
        print(iterable)
        stop = True
    else:
        iterable = iterable + 1
        remainder = 0