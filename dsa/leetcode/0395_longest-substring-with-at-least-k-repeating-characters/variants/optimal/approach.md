## General
**Make the sliding-window condition monotone**

The requirement “every present character occurs at least `k` times” is not directly monotone: expanding a valid window with one new character makes it invalid. Fix a target number of distinct characters instead. For that target, shrink whenever the window contains too many distinct characters, which is a monotone boundary rule.

**Track distinct and sufficiently frequent characters separately**

For each target from one through the number of distinct letters in `s`, scan with a frequency array. `unique` counts positive frequencies, while `qualified` counts frequencies at least `k`. Adding or removing one character updates these counters exactly when its count crosses zero or `k`.

**Recognize a valid window without rescanning it**

After each right expansion and any required left contractions, the window is valid for this target precisely when `unique = target = qualified`. Then every present character has met the threshold, so update the best length.

**Why enumerating targets finds the optimum**

Any valid substring contains some number `u` of distinct lowercase letters. During the pass whose target is `u`, the two-pointer scan considers the maximal windows constrained to at most `u` distinct letters and detects that substring when all `u` counts qualify. Thus the best across all targets includes the global optimum.

## Complexity detail
For one target, each endpoint moves forward at most `n` times, so the pass is $O(n)$. There are at most 26 targets, a fixed alphabet constant, making total time $O(n)$. The 26 counters and scalar state use $O(1)$ space.

## Alternatives and edge cases
- **Divide at globally under-frequent characters:** recursively solves segments because such a character cannot belong to any valid answer; it is elegant but repeated counting can have less direct worst-case behavior.
- **Enumerate every substring with incremental counts:** is correct but examines $O(n^2)$ windows.
- **Brute-force recount each substring:** adds another scan and can take $O(n^3)$ time.
- With $k = 1$, the whole string is valid.
- If `k > len(s)`, no nonempty substring can qualify.
- A valid optimum may exclude a rare separator character.
- Repeated groups can make the optimum begin and end inside the full string.
