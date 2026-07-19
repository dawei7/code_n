## General
**The version predicate changes only once**

Maintain an inclusive interval containing the first bad version. If the midpoint is bad, keep it and search left; otherwise discard it and everything earlier.

The first bad version always lies in `[left, right]`. A bad midpoint makes `[left, mid]` the only relevant half; a good midpoint makes `[mid + 1, right]` the only relevant half.

**Keeping a bad midpoint preserves the boundary candidate**

If the midpoint is good, monotonicity proves every earlier version is good and the boundary must be to its right. If it is bad, the midpoint might itself be the first bad version, so the search retains it while discarding only later candidates. Each update preserves the transition point until the interval contains one version, which must be the answer.

## Complexity detail
Each API call halves the remaining interval, so there are $O(\log n)$ calls and only constant local state.

## Alternatives and edge cases
- **Scan from version one:** may make $O(n)$ API calls.
- The first or only version may already be bad; overflow-safe midpoint arithmetic avoids fixed-width issues.
