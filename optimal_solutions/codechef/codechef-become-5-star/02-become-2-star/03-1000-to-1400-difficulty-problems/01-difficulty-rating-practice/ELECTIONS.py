


def solve():
    parties = ('A', 'B', 'C')
    for i in range(int(input())):
        votes = list(map(int, input().split()))
        for i in range(3):
            if votes[i] > 50:
                print(parties[i])
                break
        else:
            print("NOTA")


if __name__ == "__main__":
    solve()
