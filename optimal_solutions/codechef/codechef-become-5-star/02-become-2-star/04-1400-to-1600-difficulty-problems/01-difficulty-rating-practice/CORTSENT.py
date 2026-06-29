import re

# Regular expressions for both languages


def solve():
    first_lang_pattern = re.compile('^[a-m]+$')
    second_lang_pattern = re.compile('^[N-Z]+$')

    T = int(input())  # Number of test cases

    for _ in range(T):
        # Read the input and split it into words
        words = input().split()[1:]

        valid = True  # Flag to check if the sentence is valid or not

        for word in words:
            # Check if the word matches one of the two regex patterns
            if not (first_lang_pattern.match(word) or second_lang_pattern.match(word)):
                valid = False
                break

        # Print the result
        print("YES" if valid else "NO")


if __name__ == "__main__":
    solve()
