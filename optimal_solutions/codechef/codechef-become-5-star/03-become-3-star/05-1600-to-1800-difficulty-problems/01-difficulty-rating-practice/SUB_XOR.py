# www.codechef.com/problems/SUB_XOR


def solve():
    T = int(input())
    for _ in range(T):
        N = int(input())
        bstr = input().strip()
        incl = True 
        val = 0
        res = 0
        for b in bstr:
            if incl and b == "1":
                    val = 1 - val
            res = (res * 2 + val)% 998244353
            incl = not incl
        print(res)


if __name__ == "__main__":
    solve()
