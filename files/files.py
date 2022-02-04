with open('demo.txt', mode='r') as f:  # auto close file after with statement
    # f.write("Add this content!\n")
    # file_content = f.readlines()
    # f.close()
    #
    # for line in file_content:
    #     print(line[:-1])

    line = f.readline()
    while line:
        print(line)
        line = f.readline()

print('Done!')

