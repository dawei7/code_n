## General

Let $n$ be the array length. If a partition exists, the number of groups is forced to be

$$
g=\frac{n}{k}.
$$

Therefore $n$ must be divisible by $k$. In addition, copies of one value cannot share a group. A value occurring $f$ times needs $f$ different groups, so every frequency must satisfy $f\le g$. These two conditions are necessary.

They are also sufficient. View each distinct value as needing one slot in each of $f$ different groups. There are $g$ groups with $k$ slots apiece, for exactly $gk=n$ slots overall. Sort the frequencies conceptually and distribute each value across different least-filled groups. No frequency exceeds $g$, so a value never needs the same group twice. Balanced distribution keeps the group loads within one of each other; after all $n$ occurrences are placed, every one of the $g$ groups therefore has exactly $k$ elements.

Equivalently, the placement is a zero-one incidence matrix whose value-row sums are the frequencies and whose $g$ group-column sums are all $k$. For any set of fewer than $k$ value rows, the total demand is at most $g$ times the number of rows because each frequency is at most $g$; for $k$ or more rows, demand is at most the total $gk$. Thus the capacity conditions hold for every subset.

Count frequencies once. After confirming divisibility, compare the largest count with $g$. If it is at most $g$, the sufficient construction exists; otherwise that value alone proves impossibility.

## Complexity detail

Let $n$ be the length of `nums` and $d$ the number of distinct values. Building the frequency table takes $O(n)$ expected time with hashing, and finding its maximum takes $O(d)$ time. Since $d\le n$, total expected time is $O(n)$. The table uses $O(d)$ auxiliary space.

The benchmark defines its size as $n$, uses distinct values and `k = 2`, and spans $256$ through $4096$ elements. Distinct values force a correct repeated-`count` alternative to scan the entire array once per occurrence, exposing quadratic growth, while the accepted frequency table performs one pass.

## Alternatives and edge cases

- **Sorting first:** Equal values become adjacent, allowing maximum-frequency detection in $O(n\log n)$ time and $O(1)$ or $O(n)$ implementation-dependent extra space.
- **Repeated `nums.count`:** This is simple and correct but may rescan all $n$ elements for every occurrence, taking $O(n^2)$ time.
- **Non-divisible length:** If $n\bmod k\ne0$, exact-size groups cannot consume every element.
- **Frequency exactly g:** A value appearing once in every group is valid; only frequencies strictly greater than $g$ fail.
- **k equals one:** Every occurrence can occupy its own singleton group, even when values repeat.
- **k equals n:** Only one group exists, so every array value must be distinct.
- **Repeated occurrences:** Equal values may appear in different groups; distinctness is required only within each individual group.
