


def solve():
    T = int(input())

    for _ in range(T):
        N = int(input())
        Q = list(map(int,input().split()))
        change = True
        swaplist = []
        ei = len(Q)
        while change:
            change = False
            for i in range(1,ei):
                if Q[i-1] > Q[i]:
                    swaplist.append(str(i) + " " + str(i+1))
                    Q[i-1], Q[i] = Q[i], Q[i-1]
                    change = True
                    ei = i
        print(len(swaplist))
        for s in swaplist:
            print(s)


if __name__ == "__main__":
    solve()
