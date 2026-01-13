def log(filename):
    def wrapper(func):








@log(filename="mylog.txt")
def my_function(x, y):
    return x + y

my_function(1, 2)