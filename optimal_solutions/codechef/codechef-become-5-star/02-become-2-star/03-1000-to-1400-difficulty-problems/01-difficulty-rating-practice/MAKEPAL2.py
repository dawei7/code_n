# cook your dish here


def solve():
    for T in range(int(input())):

        N = int(input())
        S = input().strip()

        count0 = S.count('0')
        count1 = S.count('1')

        if count1 > count0:
            print('1'*count1)
        else:
            print('0'*count0)


if __name__ == "__main__":
    solve()
