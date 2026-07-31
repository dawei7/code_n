## General

Sort the tower limits from greatest to least. This ordering lets a tower with a large limit absorb the largest remaining height without taking a height that a more restricted tower may need. For the first sorted tower, choose its full limit. For each later tower, choose the smaller of its own limit and one less than the previous chosen height.

The chosen heights are therefore strictly decreasing and never exceed their corresponding sorted limits. At each position the greedy choice is the greatest value compatible with every earlier choice. Lowering it cannot help the current total, and it cannot allow a later height to exceed this choice minus one, so no alternative continuation can recover the loss. Inductively, the greedy prefix is componentwise at least as large as any feasible strictly decreasing prefix under the same sorted limits.

If a chosen value reaches zero, the remaining tower would need a distinct positive height smaller than every earlier assignment, which is impossible. Otherwise, summing the greedy choices gives the maximum feasible total. Sorting only reorders tower-limit records; the chosen value for each record still respects that tower's bound.

## Complexity detail

Let $n$ be the number of towers. Sorting costs $O(n\log n)$ time, and the greedy pass costs $O(n)$, for $O(n\log n)$ total time. Python's in-place Timsort may use $O(n)$ auxiliary storage in the worst case; the scan itself uses $O(1)$ additional space.

## Alternatives and edge cases

- **Used-height set with repeated decrements:** Searching downward one unit at a time can take $O(n^2)$ work when many towers share a large limit.
- **Ascending construction:** Assigning restricted towers first can consume a small height unnecessarily and does not directly maximize the remaining choices.
- **Equal limits:** Sorted duplicates receive consecutive decreasing heights, which is optimal until positivity becomes impossible.
- **Limit one:** It can support only height 1; any later sorted tower forces failure.
- **Large total:** With $10^5$ towers and limits up to $10^9$, the sum exceeds 32-bit range, so fixed-width implementations need 64-bit arithmetic.
