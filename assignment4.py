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

        '''for i in range(0, n):
            insert[i] = line[i]unt += 1
        '''
        line = [int(i) for i in line]
        Array.append(line)

    global marked
    marked = [n]
    for i in range(0, n):
        marked[i] = 0
    global bag
    global minimum
    global minIndex
    minimum = 1000000
    bag = [n]
    global count
    count = 1
    global MST
    MST = 0
    bag[0] = Array[0][0]
    while len(bag) != 0:
        for i in range(0, n):
            if bag[i] < min:
                minIndex = i
                minimum = bag[i]
        bag.pop(minimumIndex)
        count -= 1
        if marked[minIndex] == 0:
            marked[minIndex] = 1
            for x in range(0, n):
                if Array[minIndex][x] != 0:
                    MST += 1
                    bag[count] = Array[minIndex][x]
                    count += 1
    print('minimum:', MST)


first_second_third_mst('test0.in', 'input0.out')
