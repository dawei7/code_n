## General

**Count choices by value group.** Let one distinct value occur `count` times. Imagine its group placed between all value groups already processed and all groups still unprocessed. If `left` positions belong to earlier groups and `right` positions belong to later groups, choosing one position from each side and one from the current group creates `left * count * right` triplets with three distinct values.

The actual order of the value groups is arbitrary. Every unordered choice of three distinct values has exactly one group that is processed between the other two, so its product of frequencies is added exactly once. Index ordering requires no extra factor: after choosing three positions, sorting their indices determines the unique valid ordering $i < j < k$.

Build a frequency map, initialize `right` to the array length, and process each frequency. Remove the current group from `right`, add its contribution, and then add it to `left`. This avoids enumerating either index triplets or triples of distinct values.

## Complexity detail

Let $n = \lvert\texttt{nums}\rvert$ and let $u$ be the number of distinct values. Building the frequency map takes $O(n)$ time, and processing its $u$ counts takes $O(u)$ time. Since $u \le n$, the total is $O(n)$ time and $O(u)$ auxiliary space.

## Alternatives and edge cases

- **Three index loops:** Directly testing all $\binom{n}{3}$ position triples is correct but requires $O(n^3)$ time.
- **Three frequency-group loops:** Multiplying every triple of distinct-value frequencies reduces dependence on duplicates but still costs $O(u^3)$ time.
- **Sorting equal groups:** Sorting permits a similar left-group-right count in $O(n\log n)$ time with no hash map, but it is slower asymptotically and may mutate the input.
- **Fewer than three distinct values:** No valid triplet exists, and every group contribution has either `left = 0` or `right = 0`.
- **All values distinct:** Every choice of three indices qualifies, producing $\binom{n}{3}$.
