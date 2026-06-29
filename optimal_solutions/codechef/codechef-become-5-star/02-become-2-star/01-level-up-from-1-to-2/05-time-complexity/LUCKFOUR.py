# We have populated the solutions for the 10 easiest problems for your support.
# Click on the SUBMIT button to make a submission to this problem.

#Note that it's python3 Code. Here, we are using input() instead of raw_input().
#You can check on your local machine the version of python by typing "python --version" in the terminal.

from collections import Counter


def solve():
    t = int(input())
    for i in range(t):
        fours = 0
        num = int(input())
        ls=[int(x) for x in str(num)]
        l=Counter(ls)
        if 4 in l:
            print(l[4])
        else:
            print("0")


if __name__ == "__main__":
    solve()
