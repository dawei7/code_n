# Read the input values


def solve():
    n, k = map(int, input().split())
    array = list(map(int, input().split()))

    # Initialize a flag to indicate if the element is found
    found = False

    # Use a for loop to search for the element in the array
    for element in array:
        if element == k:
            found = True
            break

    # Print the result
    if found:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    solve()
