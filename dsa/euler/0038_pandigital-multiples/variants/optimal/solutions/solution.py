def solve() -> int:
    """Find the largest 1 to 9 9-digit pandigital number formed as concatenated product of integer x with (1, 2, ..., n) for n > 1.

    Mathematical Principles Applied:
    1. Base Candidate Bounds:
       For x = 9, n = 5: 9*1 = 9, 9*2 = 18, 9*3 = 27, 9*4 = 36, 9*5 = 45.
       Concatenated: 918273645 (9 digits, 1..9 pandigital).
       Any larger pandigital MUST start with digit 9, so x MUST start with 9!

    2. Candidate Digit Length Analysis:
       - 2-digit x (e.g. 91): n = 3 gives 2+3+3 = 8 digits; n = 4 gives 2+3+3+3 = 11 digits (cannot be 9).
       - 3-digit x (e.g. 912): n = 2 gives 3+4 = 7 digits; n = 3 gives 3+4+4 = 11 digits (cannot be 9).
       - 4-digit x starting with 9: n = 2 gives 4 + 5 = 9 digits! (x in range 9876 down to 9214).

    3. Search Range for 4-digit x:
       x in range 9876 down to 9214 with n = 2.
       Concatenated product s = str(x) + str(2*x).

    Time Complexity: O(1) over ~660 iterations (executes in ~0.0001s).
    Space Complexity: O(1) constant auxiliary space.
    """
    target = set("123456789")

    # Base candidate from x = 9, n = 5
    max_pandigital = 918273645

    # Iterate 4-digit x starting with 9 in descending order (n = 2 yields 4 + 5 = 9 digits)
    for x in range(9876, 9213, -1):
        # Concatenate x and 2*x
        s = f"{x}{x * 2}"

        # Test if s is 9 digits long and contains digits 1-9 exactly once
        if len(s) == 9 and set(s) == target:
            val = int(s)
            if val > max_pandigital:
                max_pandigital = val
                # Descending order guarantees first match > max_pandigital is the maximum
                break

    # Return the largest 9-digit 1..9 pandigital number
    return max_pandigital


if __name__ == "__main__":
    print(solve())
