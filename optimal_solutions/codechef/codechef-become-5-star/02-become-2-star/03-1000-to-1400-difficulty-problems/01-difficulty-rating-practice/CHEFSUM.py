# Read the number of test cases


def solve():
    T = int(input())

    for _ in range(T):
        # Read the number of integers in the array
        n = int(input())

        # Read the array of integers
        arr = list(map(int, input().split()))

        # Initialize minimum value and index
        mn = float('inf')
        where = -1

        # Find the minimum value and its index
        for i in range(n):
            x = arr[i]
            if x < mn:
                mn = x
                where = i + 1  # Store 1-based index

        # Output the index of the minimum value
        print(where)


if __name__ == "__main__":
    solve()
