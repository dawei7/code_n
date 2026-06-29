# cook your dish here


def solve():
    for _ in range(int(input())):
        s=input()
        o= s.split("0")
        print(len(o)-o.count(""))


if __name__ == "__main__":
    solve()
