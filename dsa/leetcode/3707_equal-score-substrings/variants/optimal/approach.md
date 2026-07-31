## General

Every legal split divides the fixed total score into a prefix score and the remaining suffix score. If `total` is the score of all of `s` and `left` is the score through a candidate index, then the right score is `total - left`. Equality therefore reduces to `left == total - left`, or equivalently `2 * left == total`.

Compute `total` once. Then scan every character except the last, adding its alphabet value to `left` before testing the equality. Excluding the final character is essential: a split after it would leave an empty right substring.

The running prefix score is exact for the current split, while subtraction from `total` gives the exact suffix score without rescanning it. Thus the method returns `true` precisely when the current split is balanced. If the scan ends without equality, every legal split has been tested and the answer is `false`.

## Complexity detail

Let $n=\lvert s\rvert$. Computing the total and scanning the prefix each take $O(n)$ time, for $O(n)$ overall. The algorithm stores only two integer scores and the current character, so it uses $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Recompute both substring scores:** Summing the prefix and suffix separately at every split is straightforward but can take $O(n^2)$ time.
- **Prefix-sum array:** Precomputing every prefix score also supports constant-time split checks, but it uses $O(n)$ extra space when one running sum is sufficient.
- **Odd total score:** Two integer substring scores cannot both equal half of an odd total, so such a string can never balance; the equality test naturally handles this case.
- **Two-character string:** There is exactly one legal split, between the two characters.
- **Non-empty requirement:** The scan deliberately stops before the last character so it never accepts an empty suffix.
- **Alphabet values are one-based:** `a` contributes `1`, not `0`; using zero-based character offsets without adding one changes the result.
