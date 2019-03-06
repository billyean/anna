import sys
from bs4 import BeautifulSoup

def main(argv):
    with open(argv[1], "rt") as csvf:
        count = 0
    # with open("10000\stackoverflow_posts.csv", "wt") as csvf:
        for line in csvf:
            cols = line.split(",")
            print("javascipt" in cols[18].lower())
            soup = BeautifulSoup(cols[2], 'html.parser')
            # print(soup.get_text())
            if count > 1000:
                break
            count += 1


if __name__ == "__main__":
    main(sys.argv)
