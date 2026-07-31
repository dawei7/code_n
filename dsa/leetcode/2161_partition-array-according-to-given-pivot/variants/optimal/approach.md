## General

**Preserve order by appending to three subsequences**

Scan `nums` in its original order. Append each value to one of three lists
according to whether it is smaller than, equal to, or greater than `pivot`.
Appending means the smaller list is exactly the original smaller-value
subsequence, and the greater list is exactly the original greater-value
subsequence, so both stability requirements hold automatically.

Concatenate the smaller, equal, and greater lists in that order. Every input
element appears once in exactly one list, all comparisons to the pivot are
represented by the required group order, and the two order-sensitive groups
retain their encounter order. The concatenation is therefore precisely the
requested partition.

## Complexity detail

Let $n$ be the length of `nums`. Classifying the values and concatenating the
three groups take $O(n)$ time. The returned array and temporary groups contain
$n$ values in total, so output-inclusive space is $O(n)$.

## Alternatives and edge cases

- **Stable insertion into one list:** Tracking group boundaries while inserting
  values can preserve order, but shifting existing list elements can take
  $O(n^2)$ time.
- **In-place Dutch national flag partition:** It uses constant auxiliary
  space, but its swaps do not preserve relative order.
- **Three full scans:** Appending smaller, equal, then greater values in separate
  passes is also stable and remains $O(n)$.
- Either outer group may be empty.
- Every value may equal the pivot.
- Repeated pivot values must all appear between the two outer groups.
- Negative values and the full allowed integer bounds use ordinary comparison.
