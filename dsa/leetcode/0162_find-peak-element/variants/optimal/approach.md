## General

**Use the local slope to retain a peak-containing half**

Maintain a closed interval `[left, right]` that contains at least one peak. While it has more than one position,
choose `middle = (left + right) // 2` and compare `nums[middle]` with `nums[middle + 1]`. The second access is safe
because `left < right` guarantees `middle < right`.

If the midpoint value is greater, the slope falls. A peak exists at `middle` or somewhere to its left, so preserve
the midpoint with `right = middle`. Otherwise adjacent values are unequal and the slope rises; a peak exists strictly
to the right, so set `left = middle + 1`.

For a rising edge, moving right must eventually encounter a downward edge or reach the final array position. The
turning point is a peak in the first case, and the endpoint is a peak against its virtual $-\infty$ neighbor in the
second. The falling case is symmetric toward the left. Thus each update preserves a peak and strictly shrinks the
interval. When the boundaries meet, their sole remaining position must be a valid peak.

## Complexity detail

Every comparison discards approximately half of the remaining interval, giving $O(\log n)$ time. The two boundaries
and midpoint use $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Linear slope scan:** can return the position before the first descent but violates the logarithmic requirement.
- **Find the global maximum:** always returns a peak under unequal adjacent values, but still takes $O(n)$ time.
- **Set `right = middle - 1` on a falling slope:** is incorrect because `middle` may itself be the peak.
- A one-element array returns index zero immediately.
- Strictly increasing and strictly decreasing arrays converge to the final and first positions, respectively.
- Multiple peaks are allowed; the returned index must satisfy the peak property rather than match one predetermined
  answer.
