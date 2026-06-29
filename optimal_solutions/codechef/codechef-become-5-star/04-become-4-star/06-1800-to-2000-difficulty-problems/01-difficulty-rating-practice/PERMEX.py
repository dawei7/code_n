# cook your dish here


def solve():
    for _ in range(int(input())):
        n = int(input())
        a = input()
        if a[0] == '0' or a[1] == '0' or a[-1] == '0':
            print("NO")
        else:
            result = [0]
            mylist = []
            for i in range(1,n+1):
                if a[i] == '1':
                    if mylist:
                        result.extend(mylist[::-1])
                    mylist = [i]
                else:
                    mylist.append(i)
            print("YES")
            print(*result)


if __name__ == "__main__":
    solve()
