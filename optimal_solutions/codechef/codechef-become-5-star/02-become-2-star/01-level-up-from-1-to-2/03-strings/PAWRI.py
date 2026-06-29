# cook your dish here
import re


def solve():
    for _ in range(int(input())):
        string = input()
        string = string.replace("party","pawri")
        print(string)

        #Using Regex
        # string = re.sub('party','pawri',string)
        # print(string)


if __name__ == "__main__":
    solve()
