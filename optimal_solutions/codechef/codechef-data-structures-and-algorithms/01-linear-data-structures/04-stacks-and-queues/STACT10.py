


def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    stack = []

    # Initialize the NGE array
    nge = [-1] * n

    # Iterating the array from right to left
    for i in range(n-1, -1, -1):

        # Pop till the top element is smaller than current
        while stack and stack[-1] < arr[i]:
            stack.pop()

        if stack:
            nge[i] = stack[-1]
        else:
            nge[i] = -1

        # Push the current element to stack
        stack.append(arr[i])

    print(*nge)


if __name__ == "__main__":
    solve()
