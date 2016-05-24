verbose = True

def example1():
    if verbose:
        print('Running example1')

example1()

been_called = False

def example2():
    global been_called
    been_called = True
    print(been_called)

example2()