import sys

def hello():

    print "Welcome to Python!"
    # Write your code below!
    my_variable = 10

    # Set the variables to the values listed in the instructions!

    my_int = 7
    my_float = 1.23
    my_bool = True

    # my_int is set to 7 below. What do you think
    # will happen if we reset it to 3 and print the result?

    my_int = 7

    # Change the value of my_int to 3 on line 8!

    my_int = 3

    # Here's some code that will print my_int to the console:
    # The print keyword will be covered in detail soon!

    print my_int


def spam():
    eggs = 12
    return eggs

def main(n):
    res = fact(n)
    print(res)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(int(sys.argv[1]))