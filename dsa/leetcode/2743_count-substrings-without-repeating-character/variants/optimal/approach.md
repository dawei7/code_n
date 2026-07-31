## General

Maintain a sliding window `[left, right]` whose characters are all distinct. For each lowercase letter, store the most recent index where it appeared. When the character at `right` was previously seen inside the current window, move `left` to one position after that occurrence. Taking the maximum with the existing boundary prevents `left` from moving backward.

**Count substrings by their right endpoint.** After adjusting the window, every substring ending at `right` and starting at any index from `left` through `right` contains no repetition. A start before `left` includes the repeated occurrence that forced the boundary forward, so it is invalid. Therefore exactly `right - left + 1` new special substrings end at this position; add that quantity to the answer.

The window invariant holds initially and is restored whenever the new character duplicates one inside it. The endpoint argument partitions all substrings by their unique ending index and counts precisely the valid starts for each, so every special substring is counted once and no invalid substring is included.

## Complexity detail

Let $n$ be the string length. The right endpoint advances once per character and the left boundary never retreats, so the algorithm takes $O(n)$ time. The last-seen array has exactly 26 entries for the fixed lowercase alphabet, giving $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Enumerate every substring:** Building or checking all $O(n^2)$ contiguous segments is correct but too slow for $n=10^5$.
- **Restart a set from each start:** Because only 26 letters exist, stopping at the first duplicate limits each scan to 26 characters and is asymptotically linear here, though with a larger alphabet-dependent constant.
- **Frequency-map window:** Incrementing and decrementing counts while shrinking from the left is also linear, but last-seen indices jump directly past a duplicate.
- A one-character string contributes exactly one special substring.
- A run of one repeated letter contributes only its length, from the one-character substrings.
- When all characters are distinct, a length-$n$ string contributes $n(n+1)/2$ substrings.
- A previous occurrence before `left` must not move the boundary backward; use `max(left, previous + 1)`.
- Equal substring text at different positions is counted separately.
