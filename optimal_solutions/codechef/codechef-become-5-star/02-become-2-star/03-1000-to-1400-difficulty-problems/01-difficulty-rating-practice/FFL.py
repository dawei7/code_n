# cook your dish here


def solve():
    for i in range(int(input())):
        n,s=map(int,input().split())
        p=list(map(int,input().split()))
        q=list(map(int,input().split()))

        #n is the numbers of players to purchase
        #s is the sum of the prices of the players Chef has purchased already.
        # THE TOTAL PRICE SHOULD NOT EXCEED 100

        #p is a list containing the prices of those n players
        #q is a list where if,
                # q[i] == 0 => p[i] is a defender
                # q[i] == 1 => p[i] is a forward

        defender, forward = [],[]
        for i in range(n):
            if q[i]==0:
                defender.append(p[i])
            elif q[i]==1:
                forward.append(p[i])

        if len(defender)==0 or len(forward)==0:
            print('NO')
        else:
            if s+min(forward)+min(defender)<=100:
                print('YES')
            else:
                print('NO')


if __name__ == "__main__":
    solve()
