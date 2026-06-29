# cook your dish here


def solve():
    def check(num):
        if num[::-1] == num:
            return True
        return False

    for T in range(int(input())):
        N = input()
        print("wins" if check(N) else "loses")


if __name__ == "__main__":
    solve()
