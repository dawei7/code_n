# cook your dish here


def solve():
    for _ in range(int(input())):
        o, money = list(map(int, input().split()))
        lit = list(map(int, input().split()))

        lit.sort()

        Onwards = True

        buyable = 0

        while Onwards:
            if len(lit) == 0: 
                Onwards = False
                break
            elif lit[0] > money:
                if lit[0]/2 <= money: 
                    buyable += 1 
                Onwards = False
                break
            else:
                buyable += 1 
                money -= lit[0]
                lit.remove(lit[0])

        print(buyable)


if __name__ == "__main__":
    solve()
