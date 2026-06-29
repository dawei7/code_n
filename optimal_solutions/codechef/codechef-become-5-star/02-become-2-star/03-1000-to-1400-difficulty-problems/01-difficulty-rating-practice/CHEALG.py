# cook your dish here


def solve():
    t = int(input())
    for _ in range(t):
        a = input()
        z=1
        b=""
        a+=" "
        for i in range(len(a)-1):
            if a[i]==a[i+1]:
                z+=1
            else:
                b+=f"{a[i]}{z}"
                z=1

        print("YES" if len(b)<len(a)-1 else "NO")


if __name__ == "__main__":
    solve()
