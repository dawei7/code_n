## General

Store every distinct array value in a hash set. A positive value $k$ is valid exactly when `-k in values`; no information about positions or multiplicities is needed.

Inspect the distinct positive values and keep the largest one whose negation is present. Initializing the result through `max(..., default=-1)` also handles the case where the candidate collection is empty. Restricting candidates to positive values matters: the task asks for positive $k$, and the input guarantee already excludes zero.

The set contains precisely the values that occur in the array, so a reported candidate always has both required signs. Conversely, every valid $k$ is in the set and its negative passes the membership test, so the maximum cannot be missed.

## Complexity detail

Let $n=\lvert\texttt{nums}\rvert$. Building and scanning the set takes $O(n)$ expected time under standard hash-table behavior. The set holds at most $n$ distinct values, so it uses $O(n)$ space.

The bounded value range also permits a fixed-size presence table, but the manifest describes the general hash-set implementation.

## Alternatives and edge cases

- **Sort with two pointers:** Sorting allows opposite signs to be matched in $O(n\log n)$ time and can use less auxiliary space when in-place mutation is acceptable.
- **Check every pair:** Comparing all index pairs is straightforward but costs $O(n^2)$ time.
- **Fixed presence table:** Because values lie from -1000 through 1000, a boolean array supports deterministic $O(n)$ time and $O(1)$ bounded-domain space.
- **No qualifying pair:** Return `-1`, not the largest negative value.
- **Multiple pairs:** Choose the greatest positive candidate, regardless of input order.
- **Duplicates:** Repeated copies do not affect membership or the answer.
- **Boundary magnitude:** Both `-1000` and `1000` may occur, making 1000 a valid result.
- **No zero:** The contract excludes zero, so it can never be treated as its own negative pair.
