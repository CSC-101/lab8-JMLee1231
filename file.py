import sys

def str_to_float(str1:str)->[float]:
    try:
        return float(str1)

    except ValueError:
        return None



#the purpose is to read a file in the command line input and converts two string float values to floats and prints their sum
if __name__ == '__main__':
    try:
        print(sys.argv)
        with open(sys.argv[1], "r") as file:
            count = 0
            for line in file:
                count += 1
                for i in range(len(line)):
                    if line[i] == " ":
                        x = str_to_float(line[0: i])
                        y = str_to_float(line[i+1:len(line)-1])
                        print("line: ", count, "||", "sum = ",x+y)
    except FileNotFoundError:
        print("Error: file not found")