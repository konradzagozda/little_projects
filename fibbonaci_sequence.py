#TODO: Fibonacci Sequence - Enter a number and have the program generate the Fibonacci sequence to that number or to the Nth number.
#TODO: I WANT two versions of my program, when I can choose the parameter.
#TODO: Either I want the number N ( the number's counter of items ) or the maximum number the function will generate ( max ) and won't stop until reached.


def fibonacci(n=0,max=0):
    first = 0
    second = 1
    while max > 0 and first <= max:     # max case
        yield first
        first, second = second, first + second
    else:
        for x in range(n):      # n case
            yield first
            first, second = second, first + second


print(list(fibonacci(max=1597)))