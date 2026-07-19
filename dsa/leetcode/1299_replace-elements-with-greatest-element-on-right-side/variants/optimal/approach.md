## General
**Carry the suffix maximum from right to left**

A left-to-right scan does not yet know which later value will be greatest. Scanning from the final index toward the beginning reverses that dependency: before replacing `arr[i]`, a variable `best` can already store the maximum of the original values strictly to the right of $i$.

Initialize `best = -1`, which is exactly the required replacement for the final element and is below every legal input value. At each index, first save the original current value, write `best` into that position, and then update `best` with the larger of its old value and the saved original value.

After the update at index $i$, `best` is the maximum of the original suffix beginning at $i$. Therefore, at the next index to the left, it is precisely the greatest original element strictly to that index's right. This establishes every replacement while retaining only one running value.

## Complexity detail
The reverse scan visits each of the $n$ positions once, taking $O(n)$ time. Apart from the returned input array, it stores only the current suffix maximum and loop state, so auxiliary space is $O(1)$.

## Alternatives and edge cases
- **Recompute each suffix maximum:** Calling `max` or scanning the suffix separately for every index is straightforward but takes $O(n^2)$ time.
- **Suffix-maximum array:** Precomputing all suffix maxima also takes $O(n)$ time, but requires $O(n)$ additional storage that the in-place reverse scan avoids.
- **Single element:** It is replaced directly by `-1`.
- **Strictly increasing input:** Every position except the last receives the original final value.
- **Strictly decreasing input:** Each position receives the original next value.
- **Repeated maxima:** Equal values cause no ambiguity; the required replacement is the greatest value, not its index.
