# cook your dish here


def solve():
    def linear_search(Arr, n, x):
        if(n==len(Arr)):
            return -1
        if(Arr[n]==x):
            return n
        return linear_search(Arr, n+1, x)

    n, x = map(int, input().split())
    Arr = list(map(int, input().split()))
    print(linear_search(Arr, 0, x))


if __name__ == "__main__":
    solve()
