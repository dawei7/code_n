# Read the number of test cases


def solve():
    t = int(input())

    # Process each test case
    for _ in range(t):
        # Read the size of the array
        n = int(input())

        # Read the array elements
        arr = [int(x) for x in input().split()]

        # Find the maximum element
        maximum = arr[0]
        for i in range(1, n):
            if arr[i] > maximum:
                maximum = arr[i]

        # Print the maximum element
        print(maximum)


if __name__ == "__main__":
    solve()
