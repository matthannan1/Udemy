import glob2, datetime

files = glob2.glob('*.txt')

with open("glob_test.txt", "a+") as output:
    for file in files:
        with open(file,"r") as input:
            content = input.read()
            output.write(content+"\n")