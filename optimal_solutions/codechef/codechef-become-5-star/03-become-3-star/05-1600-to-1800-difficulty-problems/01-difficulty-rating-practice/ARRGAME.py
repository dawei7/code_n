# cook your dish here


def solve():
    for _ in range(int(input())):
        n = int(input())
        a = input().split() + ['1']
        big1 = 0
        big2 = 0
        current = 0
        for i in a:
            if i == '0':
                current += 1
            elif current > big1:
                big2 = big1
                big1 = current
                current = 0
            elif current > big2:
                big2 = current
                current = 0
            else:
                current = 0
        if big1%2 == 1 and big2*2 < big1:
            print('Yes')
        else:
            print('No')


if __name__ == "__main__":
    solve()
