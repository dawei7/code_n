## General
**Best future value after each position**

Sort events by start time and record the sorted starts. Build a suffix array where each position stores the greatest single-event value from that position onward. This makes the best value among every sufficiently late event available in constant time.

**Locating a compatible partner**

For each sorted event, binary-search for the first start strictly greater than its inclusive end. Combine the current value with the suffix maximum at that position; the sentinel suffix value zero also represents choosing no second event. Track the greatest combination.

The binary search excludes exactly the overlapping events, including those sharing an endpoint. Every compatible later event lies in the selected suffix, whose stored maximum is the best possible partner. Evaluating every event as the first choice therefore considers an optimal pair or optimal singleton.

## Complexity detail
Sorting costs $O(n\log n)$. Building suffix maxima is $O(n)$, and $n$ binary searches cost another $O(n\log n)$. The starts and suffix arrays use $O(n)$ space.

## Alternatives and edge cases
- **End-time sweep with a heap:** Process starts in order while removing finished events from a min-heap and retaining the best completed value; this also runs in $O(n\log n)$ time.
- **Enumerate every pair:** Testing all event pairs is correct but costs $O(n^2)$ time.
- Events with `next_start == current_end` overlap because both include that time.
- The best answer may use just one event; the suffix sentinel must permit a zero-valued second choice.
- Events may share starts, ends, and values without affecting the method.
