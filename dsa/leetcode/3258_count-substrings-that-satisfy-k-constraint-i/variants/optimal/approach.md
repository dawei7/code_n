## General

Let $n$ be the string length.

**Negate the OR condition carefully**

A substring is valid when its zero count is at most $k$ OR its one count is at most $k$. By De Morgan's law, it is invalid only when both counts exceed $k$. This conjunction determines when a sliding window must shrink.

Maintain a window \`s[left:right+1]\` and counts for both bits. After adding \`s[right]\`, advance \`left\` while both counts are greater than $k$, removing each departed bit. When shrinking stops, the current window is valid and \`left\` is the earliest valid start for this ending position.

Every later start from \`left\` through \`right\` removes characters from a valid window, so it also satisfies at least one count bound. Every earlier start contains the invalid window that existed just before the final removal and therefore still has more than $k$ copies of both bits. Consequently exactly \`right - left + 1\` valid substrings end at \`right\`; add that number to the answer.

The bit counts always describe the maintained window. The shrink condition removes precisely the invalid state, and removing characters cannot turn a valid substring invalid. The earliest-start argument partitions all substrings ending at each index into an invalid prefix of starts and a valid suffix, so summing their suffix lengths counts every valid substring exactly once.

## Complexity detail

The right boundary visits each character once, and the left boundary also advances at most $n$ times over the complete scan. The total time is $O(n)$. Two counters, two indices, and the answer use $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Enumerate all substrings:** Maintaining counts in a nested-loop scan is correct but takes $O(n^2)$ time.
- **Recount each slice:** Calling count operations for every substring can take $O(n^3)$ time.
- **Shrink when either count exceeds $k$:** That implements an AND requirement and incorrectly rejects strings whose other bit remains within the limit.
- A homogeneous substring always satisfies the constraint because one bit count is zero.
- Every one-character substring is valid for positive $k$.
- When $k=n$, all $n(n+1)/2$ substrings are valid.
- Substrings with exactly $k$ occurrences of one bit satisfy that side of the condition.
- Identical substring text at different locations is counted separately.
