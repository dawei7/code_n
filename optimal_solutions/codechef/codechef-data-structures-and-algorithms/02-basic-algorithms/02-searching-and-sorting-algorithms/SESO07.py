


def solve():
    n = int(input())
    arr = list(map(int, input().split()))

    smallest = float('inf')
    largest = float('-inf')

    for num in arr:
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num

    print(smallest, largest)


if __name__ == "__main__":
    solve()
