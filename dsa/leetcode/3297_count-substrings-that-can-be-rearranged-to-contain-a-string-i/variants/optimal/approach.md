## General

Rearranging a substring can place `word2` first exactly when the substring contains at least the required frequency of every letter. Record those requirements in a 26-entry `deficit` array and let `missing` be the total number of required character occurrences not yet supplied by the current window.

Move the right boundary through `word1`. Adding a character reduces `missing` only while that letter still has a positive deficit; extra copies make its deficit negative but do not improve an already satisfied requirement. Whenever `missing` becomes zero, advance the left boundary until removing one character makes the window invalid again. Thus, after shrinking, every start before `left` forms a valid substring ending at the current right boundary, while `left` itself does not. Adding `left` counts exactly those endings without enumerating their substrings.

Both boundaries move only forward. The deficit array always equals the required counts minus the counts in the current post-shrink window, so the validity test and the number of counted starts remain correct after every update.

## Complexity detail

Let $n=\lvert word1\rvert$ and $m=\lvert word2\rvert$. Initializing the requirements takes $O(m)$ time. Each character of `word1` enters the window once and leaves it at most once, taking $O(n)$ additional time. The total is $O(n+m)$. The 26-entry array and scalar counters use $O(1)$ auxiliary space because the alphabet is fixed.

## Alternatives and edge cases

- **Prefix frequencies plus binary search:** A frequency vector for every prefix can test a chosen range, and binary search can find the first valid end for each start, but this costs $O(26n\log n)$ time and $O(26n)$ space.
- **Enumerating all substrings:** Updating counts for every start and end requires $O(n^2)$ time, which is too slow when `word1` has length $10^5$.
- **Repeated required letters:** `missing` counts occurrences rather than distinct characters, so a requirement such as three copies of `a` is enforced exactly.
- **Extra characters:** Letters absent from `word2` and surplus required letters may stay in a valid substring; their deficits become non-positive and never falsely increase `missing`.
- **Impossible requirement:** If `word1` lacks enough copies of any required letter, `missing` never reaches zero and the answer remains zero.
