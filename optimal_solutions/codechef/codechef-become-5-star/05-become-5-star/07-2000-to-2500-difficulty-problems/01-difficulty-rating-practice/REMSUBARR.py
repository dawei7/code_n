


def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int,input().split()))
        if sorted(arr)==arr:
            print(n-1)
        else:
            l = 0
            r = n - 1
            size = 0
            maxi = 0
            while l<r:
                a,b = arr[l],arr[r]
                if a<b:
                    maxi = max(maxi,a)
                    l += 1
                else:
                    maxi = max(maxi,b)
                    r -= 1
                size += 1
                if size==maxi:
                    break
            print(n-size)


if __name__ == "__main__":
    solve()
