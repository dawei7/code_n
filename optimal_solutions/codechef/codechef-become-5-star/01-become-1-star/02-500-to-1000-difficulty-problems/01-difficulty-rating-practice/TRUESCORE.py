# cook your dish here


def solve():
    for i in range(int(input())):
        a,b = map(int, input().split(" "))
        c,d = map(int, input().split(" "))
        if(c>=a and d>=b):
            print("Possible")
        else:
            print("Impossible")


if __name__ == "__main__":
    solve()
