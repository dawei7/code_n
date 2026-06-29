


def solve():
    t = int(input())

    while t > 0:

        n,k,l = map(int,input().split())

        arr = list(map(int,input().split()))
        if n == 1:
            print("Yes")
        else:
            sp = arr[len(arr)-1]
            del arr[len(arr)-1]
            # print(arr)
            mx = max(arr)

            if mx < sp:
                print("Yes")

            elif (k <= 0 and mx >= sp):
                print("No")

            else:
                sp += (l-1)*k

                if mx < sp:
                    print("Yes")
                else:
                    print("No")
        t -= 1


if __name__ == "__main__":
    solve()
