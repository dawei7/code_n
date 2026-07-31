## General

**Separate the difficulty levels**

A round cannot mix difficulty values, so choices for one difficulty never
affect another. Count how many times each value occurs, solve that frequency
independently, and add the resulting round counts.

**Minimize rounds for one frequency**

For a frequency $f$, groups of three are preferable because no round can
remove more than three tasks. If $f=1$, no legal group exists and the entire
schedule is impossible. Every $f\ge2$ can be formed from pairs and triples:

- if $f$ is divisible by three, use only triples;
- if the remainder is two, add one pair;
- if the remainder is one, replace one prospective triple plus the remaining
  task by two pairs.

These cases all use $\lceil f/3\rceil$, computed as `(f + 2) // 3`. This is
also a lower bound because each round completes at most three tasks, so the
construction is optimal. Summing these independent optima gives the global
minimum.

## Complexity detail

Let $n=\lvert\texttt{tasks}\rvert$ and let $u$ be the number of distinct
difficulty values. Building the frequency table takes $O(n)$ time, and
processing its $u$ counts takes $O(u)$ time, for $O(n)$ total. The frequency
table uses $O(u)$ space.

## Alternatives and edge cases

- **Sort and scan runs:** Sorting makes equal difficulties consecutive and is correct, but costs $O(n\log n)$ time.
- **Call `count` for every distinct value:** This avoids an explicit map but repeatedly scans the array and can take $O(n^2)$ time.
- **Dynamic programming per frequency:** A recurrence over pairs and triples works, but the closed-form count makes that extra work unnecessary.
- **Singleton frequency:** Any difficulty occurring exactly once makes the answer `-1`.
- **Remainder one:** For counts such as four or seven, use two pairs or one triple plus two pairs; never leave one task alone.
- **All tasks equal:** Apply the same formula once; no special scheduling interaction is needed.
- **Large difficulty values:** Only equality matters, so sparse values up to $10^9$ are ordinary hash-map keys.
