## General
**Translate an answer into a group size**

A rabbit answering `y` belongs to a color group containing exactly $y + 1$ rabbits. Only rabbits with the same answer can share such a group, because every member of one color sees the same number of same-colored companions.

**Pack equal answers into full groups**

If answer $y$ appears $c$ times, at most $y+1$ of those respondents can occupy one color group. The minimum number of required groups is therefore $\lceil c/(y+1)\rceil$. Each group contributes its entire size, including any same-colored rabbits that were not surveyed.

Summing `ceil(count / group_size) * group_size` over distinct answers is feasible: partition each frequency into groups of capacity `group_size`, with only the final group possibly containing unreported members. Fewer groups cannot hold all respondents, while these packed groups satisfy every report, so the sum is minimal.

## Complexity detail
Counting all `n` responses and then visiting each distinct answer takes $O(n)$ time. The frequency table stores `u` distinct answers, using $O(u)$ auxiliary space.

## Alternatives and edge cases
- **Track remaining group capacity:** While scanning, start a new group when an answer has no open slots and consume a slot otherwise; this also takes $O(n)$ time and $O(u)$ space.
- **Sort equal answers together:** Grouping runs after sorting is correct but takes $O(n \log n)$ time.
- **Rescan for every distinct answer:** Repeatedly counting occurrences in the original list can degrade to $O(n^2)$ time.
- **Empty survey:** Return zero because there are no constraints to satisfy.
- **Zero answers:** Each such rabbit claims a unique color group of size one.
- **Partial final group:** Even one respondent forces the full declared group size to exist.
- **Frequency exceeding one group:** Split equal responses across as many separate colors of that size as necessary.
