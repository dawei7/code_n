## Description

A permutation is a linear arrangement of every member of an integer array. For `arr = [1, 2, 3]`, its permutations in lexicographic order are `[1, 2, 3]`, `[1, 3, 2]`, `[2, 1, 3]`, `[2, 3, 1]`, `[3, 1, 2]`, and `[3, 2, 1]`.

The next permutation is the immediately following arrangement in that lexicographic ordering. Thus `[1, 2, 3]` advances to `[1, 3, 2]`, and `[2, 3, 1]` advances to `[3, 1, 2]`. If the current arrangement is already the greatest one, such as `[3, 2, 1]`, wrap around to the lowest arrangement `[1, 2, 3]`.

Transform `nums` into its next permutation in place, using only constant extra memory.
