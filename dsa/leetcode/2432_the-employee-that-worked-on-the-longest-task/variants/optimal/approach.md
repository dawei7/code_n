## General

Let $m=\lvert\texttt{logs}\rvert$. The end of the preceding task is exactly the start of the current task. Maintain `previous_end`, initially zero, and compute each duration as `end_time - previous_end`.

Also retain the greatest duration seen and its selected employee. Replace that selection when the current duration is larger, or when the duration ties and the current employee identifier is smaller. This pairwise rule preserves exactly the best task among every prefix of the log. After the final record, the retained employee therefore satisfies both the maximum-duration requirement and its tie break.

## Complexity detail

Every one of the $m$ log entries is examined once, giving $O(m)$ time. The previous end time, best duration, and selected identifier use $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Build and sort all durations:** Sorting by descending duration and ascending employee produces the same result but costs $O(m\log m)$ time and $O(m)$ space.
- **Compare every task with every other task:** Directly proving each candidate is best takes $O(m^2)$ time.
- **Single log:** Its duration is its leave time because it starts at zero.
- **Duration tie:** Compare employee identifiers, not task positions.
- **Repeated employee:** The same employee may appear in nonconsecutive records; the task duration, rather than accumulated employee time, is being maximized.
- **Employee count:** `n` defines valid identifiers but does not affect duration calculation.
