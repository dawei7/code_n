# cook your dish here


def solve():
    for _ in range(int(input())):
        n,k = map(int,input().split())
        s = input()
        pres = s[0]
        diff = 0
        for i in s[1:]:
            if i != pres:
                pres = i 
                diff += 1
        if diff < k:
            print(-1)
        else:
            print(s.rfind(('1' if s[0] == '0' else '0') if k%2 == 1 else s[0]) + 1)


if __name__ == "__main__":
    solve()
