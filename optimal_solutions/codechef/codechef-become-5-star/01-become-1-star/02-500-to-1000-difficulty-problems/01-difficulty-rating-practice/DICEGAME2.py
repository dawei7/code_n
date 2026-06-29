


def solve():
    t = int(input())

    for i in range(t):
        l = list(map(int,input().split()))
        alice = l[0:3]
        bob = l[3:6]
        alice.sort()
        bob.sort()
        if(alice[1] + alice[2] > bob[1] + bob[2]):
            print("Alice")
        elif(alice[1] + alice[2] < bob[1] + bob[2]):
            print("Bob")
        else:
            print("Tie")


if __name__ == "__main__":
    solve()
