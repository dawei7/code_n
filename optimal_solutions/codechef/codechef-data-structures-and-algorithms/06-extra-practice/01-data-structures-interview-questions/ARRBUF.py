# cook your dish here


def solve():
    def buf_order(A):
        B = 10**7
        buf = []
        while len(A)>0:
            e = A.pop()
            if e > B:
                return("No") 
            if len(buf) == 0 or buf[-1] <= e:
                buf.append(e)
            else:
                while len(buf) > 0:
                    B = buf.pop()
                if e > B:
                    return("No") 
                buf.append(e)
        return("Yes")
    T = int(input())
    for t in range(T):
        N = int(input())
        L = list(map(int,input().split()))
        print(buf_order(L))


if __name__ == "__main__":
    solve()
