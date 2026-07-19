## General
**Track the required final comparison:** Let `up` be the length of the longest turbulent subarray ending at the current position whose final comparison is an increase. Let `down` mean the same when the final comparison is a decrease. Both start at one because a single element needs no comparison.

**Extend only the opposite state:** If `arr[i] > arr[i - 1]`, an increasing comparison can extend exactly a range whose previous final comparison was decreasing, so set `up = down + 1` and reset `down = 1`. If the current comparison decreases, apply the symmetric update `down = up + 1` and reset `up = 1`. Equality resets both states to one because neither strict sign is available.

Every turbulent range ending at `i` must have one of these two final signs. The alternating requirement uniquely determines which state at `i - 1` it may extend, so the recurrence neither misses a longer range nor accepts two identical consecutive signs. Taking the maximum state over the scan yields the global longest length.

## Complexity detail
The algorithm visits each of the $N$ elements once and performs constant work per adjacent comparison, giving $O(N)$ time. It stores only `up`, `down`, and the best length, so auxiliary space is $O(1)$.

## Alternatives and edge cases
- **Start a scan at every index:** Extending each candidate range independently is correct but takes $O(N^2)$ time on an array that remains turbulent throughout.
- **Comparison-array sliding window:** Converting adjacent pairs to signs and finding the longest alternating nonzero sign window also runs in $O(N)$ time, but explicitly storing all signs uses $O(N)$ space unnecessarily.
- **Equal neighbors:** Equality terminates every turbulent range crossing that pair and resets both state lengths to one.
- **Monotone arrays:** Any two unequal adjacent elements form a turbulent range of length two, but a second comparison with the same sign cannot extend it.
- **Single element:** With no adjacent comparison to violate the rule, the answer is one.
