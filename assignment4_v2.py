'''
    This file contains the template for Assignment4.  For testing it, I will place it
    in a different directory, call the function <first_second_third_mst>, and check its output.
    So, you can add/remove  whatever you want to/from this file.  But, don't change the name
    of the file or the name/signature of the following function.

    Also, I will use <python3> to run this code.
'''

global n
def printMST(parent):
    print( "Edge \tWeight")
    for i in range( 1 , n):
        print( parent[i], "-",i,"\t",c[i][parent[i]])

def first_second_third_mst(input_file_path, output_file_path):
    '''
    This function will contain your code, it will read the input from the file
    <input_file_path> and write to the file <output_file_path>.

    Params:
        input_file_path (str): full path of the input file.
        output_file_path (str): full path of the output file.
    '''
    #Take the input and process it
    global Array
    Array = []
    global maximum
    maximum = 0
    global x
    n = 0
    fp = open(input_file_path)
    line = fp.readline()
    n = int(line)
    print("n ", n)
    # print("n is", n)
    columns, rows = (n, n)
    c = []
    for x in range(n):
        if x == line:
            break
        #  print(line[0])
        line = fp.readline()
        line = line.rstrip('\n')
        line = line.split(",")
        c.append(line)
    print(c)
    for i in range( 0,len(c)):
        c[i] = list(map(int,c[i]))
    print(c)

    #Prepare for PrimMST
    #initiallize
    key = [float("inf")] * n
    parent = [0] * n

    key[0] = 0
    mstSet = [False] * n
    parent[0] = -1

    for cout in range(n):
        #minKey
        min = float("inf")
        for v in range(n):
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                min_index = v
        u = min_index
        #end
        mstSet[u] = 1
        for v in range(n):
            if c[u][v] > 0 and mstSet[v] == False and key[v] > c[u][v]:
                    key[v] = c[u][v]
                    parent[v] = u
        #print
        print("Edge \tWeight")
        add = 0
        for i in range(1, n):
            print(parent[i], "-", i, "\t", c[i][parent[i]])
            add = add + c[i][parent[i]]
        print("MST Best = ", add)
    pass

first_second_third_mst('input0.in', 'input0.out')
