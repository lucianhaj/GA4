'''
    This file contains the template for Assignment4.  For testing it, I will place it
    in a different directory, call the function <first_second_third_mst>, and check its output.
    So, you can add/remove  whatever you want to/from this file.  But, don't change the name
    of the file or the name/signature of the following function.

    Also, I will use <python3> to run this code.
'''


def first_second_third_mst(input_file_path, output_file_path):
    '''
    This function will contain your code, it will read the input from the file
    <input_file_path> and write to the file <output_file_path>.

    Params:
        input_file_path (str): full path of the input file.
        output_file_path (str): full path of the output file.
    '''

    global Array
    Array = []
    global maximum
    maximum = 0
    global x
    n = 0
    fp = open("test0.txt")
    # print('hello')
    line = fp.readline()
    n = int(line)
    print(line)
    print(n)
    # print("n is", n)
    columns, rows = (n, n)
    for x in range(n):
        if x == line:
            break
        #  print(line[0])
        line = fp.readline()
        line = line.rstrip('\n')
        line = line.split(",")

        #   print(line)
        '''
        for i in range(0, n):
            insert[i] = line[i]unt += 1
        '''
        line = [int(i) for i in line]
        Array.append(line)
    '''Array = [[0, 1, 2], [1, 0, 3], [2, 3, 0]]'''
    n = len(Array)
    global marked
    marked = [n]
    marked = [0 for i in range(n)]
    marked[0] = 0
    global bag
    global minimum
    global minIndex
    minIndex = 0
    minimum = 1000000
    bag = []
    global count
    count = 1
    global MST
    MST = 0
    bag = [100 for i in range(n)]
    global mst
    mst = 0
    bag[0] = 0
    print len(bag)
    minimum = 100
    minIndex = 0
    for y in range(0, n):
        print('iteration')
        minimum = 100
        for i in range(0, n):
            print('i is ', i)
            print('bag', bag[i])
            if bag[i] < minimum and marked[i] == 0:
                minIndex = i
                minimum = bag[i]
            marked[minIndex] = 1
            mst += 1
        for x in range(0, n):
            print('x')
            print(Array[minIndex][x])
            if Array[minIndex][x] != 0 and Array[minIndex][x] < bag[x] and marked[x] == 0:
                bag[x] = Array[minIndex][x]
        print('minimum:', MST)

    for i in range(0, n):
        MST += bag[i]
    print('minimum:', MST)


first_second_third_mst('test0.in', 'input0.out')
