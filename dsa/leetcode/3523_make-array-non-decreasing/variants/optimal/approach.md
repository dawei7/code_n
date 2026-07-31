## General

Let the running maximum before an element be the greatest value in its prefix. If the current value is smaller than that maximum, it cannot remain as a separate element after the prefix: it would follow a larger block maximum and violate non-decreasing order. It must therefore be absorbed into a block that also contains an earlier maximum.

Conversely, a value that is at least the running maximum can begin a new block. Partition the array immediately before every such value. Each resulting block has its first value as its maximum, so replacing every block by that maximum produces precisely these retained values, in non-decreasing order. Thus every value equal to or above the running maximum contributes one element, while every smaller value contributes none. This construction achieves the upper bound established by the forced absorptions.

Scan once, counting each value that is at least the maximum seen so far and updating that maximum. The comparison must allow equality because non-decreasing arrays permit equal neighbors.

## Complexity detail

For $n = \lvert\texttt{nums}\rvert$, the scan examines every value once, so the time complexity is $O(n)$. The count and running maximum occupy constant auxiliary space, giving $O(1)$ space.

## Alternatives and edge cases

- **Explicit block stack:** A stack can merge descending blocks and reach the same result, but it uses $O(n)$ space even though only the greatest preceding value is needed.
- **Repeated prefix maximum:** Recomputing `max(nums[:i + 1])` at every position is correct but takes $O(n^2)$ time.
- **Equal values:** A value equal to the running maximum starts another valid block and must be counted.
- **Strictly decreasing input:** Only the first value can survive as a separate result element, so the answer is `1`.
- **Already non-decreasing input:** Every value is counted and the maximum possible size remains $n$.
