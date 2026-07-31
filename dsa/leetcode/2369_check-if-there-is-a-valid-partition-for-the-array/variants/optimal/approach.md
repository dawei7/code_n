## General

Let `dp[i]` mean that the prefix containing the first `i` elements has a valid partition. The empty prefix is valid, so `dp[0] = true`; a one-element prefix is invalid because every permitted part has length two or three.

**Reduce every partition to its final part.** If the prefix ending just before a candidate final part is valid, then appending that part preserves validity. Conversely, every valid partition must end in one of the three allowed shapes. Thus a prefix of length `i` is valid precisely when either:

- `dp[i - 2]` is true and `nums[i - 2] == nums[i - 1]`; or
- `dp[i - 3]` is true and the last three values are all equal; or
- `dp[i - 3]` is true and the last three values increase consecutively by $1$.

These alternatives cover every legal final part and no illegal one. Inductively, a true state therefore describes an actual partition of its prefix, while any valid prefix makes at least one corresponding transition true.

**Keep only reachable prefix boundaries.** The transition for length `i` reads only `dp[i - 2]` and `dp[i - 3]`. Three rolling Boolean states are enough to retain those values as `i` advances; the full dynamic-programming table is unnecessary. The answer is the state for the complete array.

## Complexity detail

Let $n = \lvert\texttt{nums}\rvert$. Each prefix length performs a constant number of comparisons, so the running time is $O(n)$. The rolling state uses only a constant number of Boolean values, giving $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Full dynamic-programming table:** Storing every `dp[i]` gives the same $O(n)$ time and a straightforward reconstruction path, but it uses $O(n)$ auxiliary space when only the final decision is required.
- **Top-down memoization:** A recursive search with memoized prefix positions is also $O(n)$, but it adds recursion and memo storage and may exceed the language's recursion depth near the maximum input size.
- **Greedy block selection:** Always taking an available pair or triple is unsafe because a locally valid cut can leave an impossible suffix; prefix reachability keeps all relevant choices.
- **Exact lengths:** A valid part has length exactly two or exactly three. Longer runs must be decomposable into allowed parts rather than treated as one part.
- **Consecutive direction:** The third rule requires increasing adjacent differences of exactly $1$; decreasing triples and increasing triples with larger gaps are invalid.
- **Minimum input:** For two elements, equality is the only way to form a valid partition.
