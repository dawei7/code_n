


def solve():
    t = int(input())


    while t > 0:
        n = int(input())


        if n%2 == 0:
            for i in range(1,n+1,2):
                print(i+1,i,end=" ")

        else:
            print(1,end=" ")
            for i in range(2,n+1,2):
                print(i+1,i,end=" ")
        print()

        t -= 1


if __name__ == "__main__":
    solve()
