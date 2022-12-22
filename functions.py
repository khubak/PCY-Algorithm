import numpy as np

def parser(test_file):
    r = open(test_file)
    input_file = []

    for line in r:
        try:
            row = line.rstrip().split()
            row = [int(i) for i in row]
            input_file.append(row)
        except:
            row = float(line.rstrip())
            input_file.append(row)

    return input_file

def parserNUMPY(test_file):
    r = open(test_file)
    num_lines = sum(1 for _ in r)
    input_file = np.empty(num_lines)
    i = 0
    for line in r:

        try:
            row = line.rstrip().split()
            input_file[i] = [int(i) for i in row]
        except:
            input_file[i] = float(line.rstrip())

        i += 1

    return input_file

def parser_sprut():
    input_file = []

    brKosara = int(input())
    s = float(input())
    brPretinaca = int(input())

    input_file.extend((brKosara, s, brPretinaca))

    for i in range (0, brKosara):
        row = input().rstrip().split()
        row = [int(j) for j in row]
        input_file.append(row)

    return input_file