# cook your dish here


def solve():
    for _ in range(int(input())):
        n = int(input())
        s=list(input())
        a = set(s)
        if n%2==1:
            print('no')
        else:
            flag = False
            for i in a:
                if s.count(i)%2==1:
                    flag = True
                    break
            if flag:
                print('no')
            else:
                print('yes')


if __name__ == "__main__":
    solve()
