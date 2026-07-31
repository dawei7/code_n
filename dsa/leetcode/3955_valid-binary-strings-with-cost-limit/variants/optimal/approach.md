## General

Build each string from left to right. At index `i`, appending `'0'` is always legal and does not change the cost. Appending `'1'` is legal only when the previous character was not `'1'` and the new cost `cost + i` remains at most `k`. These two facts let the search reject an invalid branch at the first position where it becomes impossible.

Maintain a mutable path, the next index, the accumulated cost, and whether the previous bit is one. When the path reaches length `n`, every earlier choice already satisfies both restrictions, so join the path and add that string to the result. Backtracking then restores the path before trying the other bit.

Every emitted string has length `n`, respects the adjacency restriction at each one-branch, and never exceeds the cost bound. Conversely, take any valid target string. At each position, its zero choice is explored unconditionally, while its one choice passes both guards by validity; therefore the recursion follows that target through to a leaf. Each choice sequence is unique, so the result contains every valid string exactly once.

## Complexity detail

Let $R$ be the number of returned strings. Every visited prefix can be extended with zeros to at least one valid result, and a result has $n + 1$ prefixes, so there are $O(nR)$ visited states. Joining the $R$ completed paths also costs $O(nR)$, giving $O(nR)$ total time. The recursion stack and mutable path use $O(n)$ auxiliary space. The required returned strings themselves occupy $O(nR)$ space and are excluded from the auxiliary-space bound.

## Alternatives and edge cases

- **Enumerate all bitmasks:** Generating all $2^n$ strings and filtering afterward is simple under the small bound, but it explores adjacency and cost violations that backtracking can reject early.
- **Memoized counting DP:** A state such as `(index, remaining_cost, previous_one)` can count valid completions, but counts alone cannot replace the output work required to materialize every string.
- **Index zero:** Placing `'1'` at index `0` adds zero cost, so a zero budget does not force the all-zero string.
- **Maximum budget:** Even when `k` permits every possible index sum, strings containing `"11"` remain invalid.
- **Output order:** The contract permits any order, and validation compares the returned strings as an unordered list.
