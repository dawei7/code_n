## General
**Convert cumulative releases into individual durations.** Initialize the best pair from press 0, whose start time is fixed at zero. For each later index `i`, subtract the preceding release time from the current one. This local difference is exactly the interval during which `keysPressed[i]` was held.

**Compare duration before the tie-break key.** Replace the current answer when the new duration is greater. When durations are equal, replace it only if the new key is lexicographically larger. No comparison of key characters may override a strictly longer duration.

Every press is examined once and its exact duration is compared with the best of the preceding presses. After processing index `i`, the stored pair is therefore the required duration/key maximum for the prefix through `i`, including the specified tie rule. At the final index, that prefix is the entire test sequence.

## Complexity detail
The scan performs constant work for each of the $n$ presses, taking $O(n)$ time. It stores only the preceding release time and current best duration and key, so auxiliary space is $O(1)$.

## Alternatives and edge cases
- **Materialize and sort durations:** Sorting `(duration, key)` pairs gives the same answer in $O(n\log n)$ time and $O(n)$ space but does unnecessary work.
- **Compare every pair of presses:** Testing whether each press dominates all others is correct but takes $O(n^2)$ time.
- The first press starts at zero, so its duration is not a difference with another release time.
- Repeated occurrences of one key are separate presses and can have different durations.
- A tie is resolved by the key character, not by the earlier or later event position.
- Strictly increasing release times guarantee every duration is positive.
