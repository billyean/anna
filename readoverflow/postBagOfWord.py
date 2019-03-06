import sys

def main(argv):
    with open(argv[1]) as csvf:
        for line in csvf:
            cols = line.split(",")
            print(cols)


if __name__ == "__main__":
    main(sys.argv)
