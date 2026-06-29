# cook your dish here


def solve():
    for _ in range(int(input())):
        n,k = map(int,input().split())
        my_dict = dict()
        for i in range(n):
            s,f,p = map(int,input().split())
            if p in my_dict:
                my_dict[p].append([s,f])
            else:
                my_dict[p] = [[s,f]]
        result = 0
        for a in my_dict.values():
            a.sort(key=lambda x: (x[1], x[0]))
            m = len(a)
            present = 0
            for i in range(m):
                if a[i][0] >= present:
                    result += 1
                    present = a[i][1]
        print(result)


if __name__ == "__main__":
    solve()
