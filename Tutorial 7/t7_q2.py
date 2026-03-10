def readData(filename, n):
    my_file = open(filename, "r")
    for line in my_file:
        if line % n == 0:
            word = line.strip()
            word = line.split()
    my_file.close()

def main():
    for i in range(4):
        print(readData("animals.txt", i))

if __name__ == "__main__":    main()