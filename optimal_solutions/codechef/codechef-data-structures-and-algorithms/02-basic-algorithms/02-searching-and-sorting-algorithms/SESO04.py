# Read the input string


def solve():
    input_string = input()

    # Read the character to search for
    search_char = input()

    # Initialize a variable to store the position of the character
    position = -1

    # Use a for loop to search for the character in the string
    for i in range(len(input_string)):
        if input_string[i] == search_char:
            position = i
            break

    # Print the result
    print(position)


if __name__ == "__main__":
    solve()
