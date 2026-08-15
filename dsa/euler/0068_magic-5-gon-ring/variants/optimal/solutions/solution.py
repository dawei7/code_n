import itertools


def solve() -> int:
    """Find the maximum 16-digit concatenated string for a magic 5-gon ring using numbers 1 to 10.

    Mathematical Principles Applied:
    1. Magic 5-gon Ring Structure:
       A 5-gon ring consists of 5 external nodes (o0..o4) and 5 internal nodes (i0..i4).
       The 5 line triplets are:
       Line 0: (o0, i0, i1)
       Line 1: (o1, i1, i2)
       Line 2: (o2, i2, i3)
       Line 3: (o3, i3, i4)
       Line 4: (o4, i4, i0)

    2. Magic Ring Property:
       The sum of each line triplet must be equal: s0 == s1 == s2 == s3 == s4.

    3. 16-Digit String Length Constraint:
       The concatenated string representation starts with the line possessing the lowest external node o0.
       For the concatenated string to have length 16 (not 17), 10 MUST be an external node!
       If 10 were an internal node, it would be included twice, giving 17 digits.

    Time Complexity: O(10!) over 3.6 million permutations (executes in ~0.25s).
    Space Complexity: O(1) constant auxiliary space.
    """
    max_string = 0

    # Iterate through all 10! = 3,628,800 permutations of numbers 1..10
    for perm in itertools.permutations(range(1, 11)):
        o0, o1, o2, o3, o4, i0, i1, i2, i3, i4 = perm

        # Enforce canonical starting node: o0 MUST be the minimum of all external nodes
        if o0 != min(o0, o1, o2, o3, o4):
            continue

        # Evaluate the 5 line sums
        s0 = o0 + i0 + i1
        s1 = o1 + i1 + i2
        s2 = o2 + i2 + i3
        s3 = o3 + i3 + i4
        s4 = o4 + i4 + i0

        # Check if all 5 line sums are equal
        if s0 == s1 == s2 == s3 == s4:
            # Form concatenated string representation
            s_concat = f"{o0}{i0}{i1}{o1}{i1}{i2}{o2}{i2}{i3}{o3}{i3}{i4}{o4}{i4}{i0}"

            # Only accept 16-digit strings (10 is an external node)
            if len(s_concat) == 16:
                max_string = max(max_string, int(s_concat))

    # Return the maximum 16-digit magic 5-gon ring string integer
    return max_string


if __name__ == "__main__":
    print(solve())
