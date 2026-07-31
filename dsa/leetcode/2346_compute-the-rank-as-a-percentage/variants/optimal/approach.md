## General

The requested formula is exactly the definition implemented by the SQL `PERCENT_RANK()` window function: `(RANK() - 1) / (partition row count - 1)`. Partition by `department_id` so ranks and denominators restart independently for every department.

Order each partition by `mark DESC`. `PERCENT_RANK()` uses standard `RANK()` semantics, so equal marks receive equal percentages and the next distinct mark keeps the appropriate rank gap. It also returns zero for a one-row partition, avoiding division by zero while matching the natural top-rank percentage.

Multiply the fractional rank by 100 and round to two decimal places. Project the original identifiers alongside that value. No final sort is required because the contract permits any result order.

## Complexity detail

Let $n$ be the number of students. A general database execution plan sorts department partitions by mark in $O(n\log n)$ time and computes the window values in $O(n)$ additional time. Partition ordering and window-result workspace can use $O(n)$ auxiliary space. Relevant indexes may reduce physical sorting work without changing the conservative bounds.

## Alternatives and edge cases

- **`DENSE_RANK()` formula:** Dense ranks remove gaps after ties and therefore produce incorrect percentages for later students.
- **Global ranking:** Omitting the department partition mixes unrelated student populations and uses the wrong denominator.
- **Manual rank and count windows:** This is equivalent when carefully handling one-row departments, but `PERCENT_RANK()` expresses the exact formula directly.
- **All marks tied:** Every student has rank 1 and percentage 0, regardless of department size.
- **Rounding:** Scaling occurs before rounding, and the final value is rounded to two decimal places.
