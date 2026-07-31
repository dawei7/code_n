## General

Only pairs touching an endpoint need to be considered. For any valid pair $(i,j)$, replacing its left endpoint by position `0` cannot shorten its span. That replacement is valid whenever `words[0] != words[j]`. If it is not valid, then `words[0] == words[j]`; because the original pair is valid, `words[i] != words[j]`, so positions `i` and `n - 1` form a valid pair whenever the final word equals the first. If the two array endpoints already differ, they themselves give the unbeatable distance $n$.

**Farthest word from the first position.** Scan from right to left until finding the largest index `right` whose word differs from `words[0]`. The inclusive distance of that pair is `right + 1`. Stopping at the first match is safe because every later candidate has already been ruled out.

**Farthest word from the last position.** Independently scan from left to right for the smallest index `left` whose word differs from `words[-1]`. This pair has distance `n - left`.

Take the larger of those two distances. The endpoint argument shows that at least one of these candidates is as long as every valid interior pair. If both scans find nothing, all words are equal and the initialized answer `0` is required.

## Complexity detail

Let $n=\lvert\texttt{words}\rvert$. The two scans inspect at most $2n-2$ entries, so the running time is $O(n)$. Apart from the input and returned integer, the algorithm keeps only indices and the best distance, using $O(1)$ auxiliary space.

## Alternatives and edge cases

- **All index pairs:** Comparing every $(i,j)$ is direct but uses $O(n^2)$ time, which is unnecessary at the maximum array length.
- **Store first and last occurrence per word:** An occurrence map can recover the answer, but it stores up to $O(n)$ distinct strings when endpoint comparisons need only constant extra space.
- **Unequal array endpoints:** Positions `0` and `n - 1` immediately establish the maximum possible distance $n$.
- **Matching array endpoints:** Both endpoint scans matter; an interior unequal word may be farther from the last position than from the first, or vice versa.
- **One word or all words equal:** Neither scan finds an unequal endpoint partner, so the result remains `0`.
- **Inclusive distance:** Adjacent positions contribute `2` because the contract uses $j-i+1$ rather than the index gap $j-i$.
