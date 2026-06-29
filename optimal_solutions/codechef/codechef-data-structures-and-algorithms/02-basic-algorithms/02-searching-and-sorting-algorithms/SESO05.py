# Read the number of pairs


def solve():
    n = int(input())

    # Read the pairs
    pairs = []
    for _ in range(n):
        pair = tuple(map(int, input().split()))
        pairs.append(pair)

    # Read the integers a and b
    a, b = map(int, input().split())

    # Initialize a flag to indicate if the pair is found
    found = False

    # Check each pair
    for x, y in pairs:
        if (x == a and y == b) or (x == b and y == a):
            found = True
            break

    # Print the result
    if found:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    solve()
