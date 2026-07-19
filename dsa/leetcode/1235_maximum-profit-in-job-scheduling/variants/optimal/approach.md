## General
**Order jobs by their starting times.** Combine the three arrays into `(start, end, gain)` records and sort them by `start`. Let `dp[i]` be the maximum profit available using only jobs from sorted position `i` onward. The answer is `dp[0]`, and `dp[n] = 0` represents having no jobs left.

**Separate the skip and take choices.** At job `i`, skipping it leaves `dp[i + 1]`. Taking it earns its `gain` and forbids every later job starting before its end. Because the starts are sorted, `bisect_left(starts, end, i + 1)` finds the first compatible position `next_index`; using a lower-bound search deliberately permits a job whose start equals the current end. The take value is `gain + dp[next_index]`.

**Fill suffix states backward.** When computing `dp[i]`, both `dp[i + 1]` and `dp[next_index]` are already known. Store the larger of the skip and take values. Every compatible schedule either omits job `i`, or includes it and then uses only jobs at or after `next_index`; these disjoint choices cover all possibilities, so the recurrence preserves the optimal profit at every suffix.

## Complexity detail
Sorting $n$ jobs takes $O(n\log n)$ time. Each of the $n$ dynamic-programming states performs one $O(\log n)$ binary search, so the total remains $O(n\log n)$. The sorted jobs, start-time list, and dynamic-programming array use $O(n)$ auxiliary space.

## Alternatives and edge cases
- **Quadratic weighted-interval dynamic programming:** Scanning every earlier job to find compatible predecessors is correct but takes $O(n^2)$ time.
- **Top-down recursion with memoization:** It uses the same binary-search recurrence, but recursion adds call overhead and may exceed Python's recursion depth.
- **Sweep line with a profit frontier:** Processing start and end events can also maintain the best completed profit, though equal-time event ordering must allow an ending job before a starting job.
- **Touching endpoints:** A job with `start == previous_end` is compatible, which is why the binary search uses a lower bound for the current end time.
- **Identical time ranges:** Such jobs mutually overlap; the recurrence can select only the most profitable useful choice.
- **Unsorted input:** Sorting combined records preserves the association among each job's start, end, and profit.
- **Single job:** Its positive profit is the answer.
