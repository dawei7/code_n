## General

Count the letters of `s`. Build the longest possible prefix equal to `target` by consuming the matching letter at each position while it remains available. The desired answer should stay equal for as long as possible before becoming greater, because any earlier increase would produce a lexicographically larger result.

At the first position that cannot be matched—or after matching all of `target`—look for the smallest remaining letter strictly greater than the target letter at that position. If it exists, place it there and append every other remaining letter in ascending order. The first difference is then greater, and the sorted suffix is the smallest possible completion.

If no greater letter is available, restore the last matched prefix letter and move one position left. Repeating this backtracking examines candidate first-difference positions from right to left. The first successful position keeps the longest possible equal prefix; choosing its smallest greater letter and sorted suffix makes the completed permutation minimal. If even position zero cannot be increased, no qualifying permutation exists.

## Complexity detail

Let $n$ be the common string length and let the alphabet size be the fixed constant $A = 26$. Each prefix character is consumed and restored at most once, each position scans at most $A$ letters, and the suffix is emitted once. Time is $O(nA)$, which is $O(n)$ for lowercase English letters. Counts, prefix, and output construction use $O(n+A)$, or $O(n)$, auxiliary space.

## Alternatives and edge cases

- **Enumerate all permutations:** Generating and sorting permutations is factorial and becomes infeasible long before the maximum length.
- **Choose a greater letter too early:** The result is valid but may not be lexicographically smallest; the first differing position should be as far right as feasibility allows.
- **Unsorted suffix:** Once the result is already greater, any suffix order is valid, but ascending order is required for the smallest result.
- **Duplicate letters:** Frequency counts preserve multiplicity and avoid treating identical permutations as different choices.
- **Strict comparison:** A permutation equal to `target` does not qualify; a full equality match must backtrack.
- **Target below every permutation:** Increase at the first position and append the remaining letters in ascending order.
- **Target at or above the maximum permutation:** No position can be increased, so return `""`.
