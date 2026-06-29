# cook your dish here


def solve():
    def reverse(arr, l, r):
        while l < r:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1

    for _ in range(int(input())):
        n = int(input())
        my_list = []
        for i in range(n):
            inner = []
            for j in range(n):
                inner.append((i+j)%n + 1)
            my_list.append(inner)

        reverse(my_list, 0, n-1)
        reverse(my_list, 0, n//2-1)
        reverse(my_list, n//2, n-1)
        for i in my_list:
            print(*i)


if __name__ == "__main__":
    solve()
