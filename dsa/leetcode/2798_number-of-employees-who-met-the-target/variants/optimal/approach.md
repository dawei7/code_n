## General

The requested answer depends independently on every employee's recorded hours. Maintain a counter initially equal to zero and scan `hours` from left to right. For each value, test `worked >= target`; increment the counter exactly when that inclusive comparison is true.

After any prefix has been processed, the counter equals the number of qualifying values in that prefix. The next comparison either leaves the count unchanged for a value below `target` or adds the newly qualifying employee. By induction, after the final entry the counter is exactly the number of employees who worked at least the required hours.

No ordering is needed. The scan handles duplicates independently, and equality must count because the requirement is “at least,” not strictly greater than.

## Complexity detail

Let $n$ be the number of employees. The algorithm performs one comparison per array entry, so it takes $O(n)$ time. The counter and current loop value use $O(1)$ auxiliary space.

The contract limits $n$ to $50$, which is too small for honest runtime scaling across asymptotic classes. The bounded-domain certificate therefore verifies the one-pass work directly and exercises the complete legal length boundary through correctness evidence.

## Alternatives and edge cases

- **Filter then measure:** Constructing a list of qualifying entries is correct and remains $O(n)$ time, but it unnecessarily uses $O(n)$ additional space.
- **Sort and binary search:** Sorting enables a threshold boundary search but costs $O(n \log n)$ time and may mutate the input, offering no benefit for one query.
- **Generator sum:** `sum(worked >= target for worked in hours)` expresses the same one-pass constant-space logic compactly.
- Values exactly equal to `target` must be counted.
- A target of zero qualifies every entry because all worked-hour values are non-negative.
- The answer can be zero when every value is smaller, or $n$ when every value qualifies.
- A single employee and the maximum length of fifty use the same loop without special cases.
