## General
**Locate the first possible occurrence.** Binary search for the leftmost index `first` whose value is at least `target`. If `target` exists, this is its first occurrence because equal values are contiguous in a non-decreasing array.

**Test the majority-sized offset.** More than half of $n$ means at least $\lfloor n/2 \rfloor+1$ occurrences. Starting at `first`, that many equal values exist exactly when index `first + n // 2` is inside the array and still contains `target`. This single lookup simultaneously proves the target exists and reaches the strict-majority count.

**Why no second boundary is needed.** If the offset value is `target`, sorted contiguity guarantees every position from `first` through that offset is also `target`, establishing enough occurrences. If it is out of bounds or contains a larger value, the target's contiguous block is too short. A smaller value cannot occur there because `first` is the first value at least as large as `target`.

## Complexity detail
The lower-bound binary search halves its remaining range each step, taking $O(\log n)$ time. The offset check is constant time, and only index variables are stored, so auxiliary space is $O(1)$.

## Alternatives and edge cases
- **Count every element:** A linear scan is straightforward but ignores the sorted order and takes $O(n)$ time.
- **Two binary searches:** Finding both lower and upper bounds also gives the exact frequency in $O(\log n)$ time, but the majority-offset test needs only the lower bound.
- **Exactly half:** The result is `false` because majority requires strictly more than half.
- **Absent target:** The lower bound may equal `n` or point to a larger value; the offset test safely returns `false`.
- **Single element:** It is a majority precisely when it equals `target`.
- **Target at an endpoint:** The same lower-bound and offset logic applies without a special case.
