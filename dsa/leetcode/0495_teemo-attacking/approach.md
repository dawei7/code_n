## General

An attack at time `t` poisons the inclusive seconds from `t` through `t + duration - 1`. Although the statement uses inclusive integer seconds, each attack still contributes exactly `duration` seconds when its interval does not overlap another attack.

The array is already sorted in non-decreasing order, so poison intervals appear in chronological order. The task is equivalent to measuring the length of their union. Instead of constructing every interval or simulating every poisoned second, the solution measures how much new poisoned time each attack contributes before the next attack resets the timer.

**Contribution between consecutive attacks.** Consider attacks at times `a` and `b`, where `b >= a`. The poison started at `a` would last for `duration` seconds. There are two cases.

If `b - a >= duration`, the first poison interval finishes before or exactly when the next interval begins. It contributes its full `duration` seconds, and any gap afterward is unpoisoned.

If `b - a < duration`, the second attack occurs while poison from the first attack is still active. Only the seconds from `a` up to just before `b` should be charged to the first interval; the new attack takes responsibility for time from `b` onward. That contribution has length `b - a`.

Both cases are expressed by

`min(duration, b - a)`.

The loop obtains every adjacent pair with `pairwise(timeSeries)` and adds this value. Pairwise ordering is enough because the intervals all have the same duration and attack times are sorted. The next attack is the first event that can truncate the current attack's independent contribution; later attacks cannot affect the portion before that next event.

**Why initialize with one full duration.** Every attack except the last is accounted for by the gap to its successor. The final attack has no successor to truncate it, so it contributes its entire `duration`. The source initializes `ans = duration` to reserve this final contribution, then adds the contribution associated with every earlier attack through adjacent pairs.

This is equivalent to starting at zero, summing all adjacent contributions, and adding `duration` after the loop. Initializing with the final interval makes the return expression especially simple.

For `timeSeries = [1, 4]` and `duration = 2`, the gap is three. `min(2, 3) = 2` accounts for the first attack's seconds `1` and `2`, while the initial two accounts for the last attack's seconds `4` and `5`. The total is four.

For `timeSeries = [1, 2]` and `duration = 2`, the gap is one. The first attack contributes only the second from time one before the reset at time two. The final attack contributes two seconds, times two and three, giving three total. The overlapping second at time two is not counted twice.

**Inclusive endpoints do not require an extra one.** The interval `[t, t + duration - 1]` contains `duration` integer seconds. For consecutive attacks `a < b`, the distinct seconds credited before `b` are `a` through `b - 1`, a count of `b - a`. Therefore the difference formula already has the correct inclusive-second interpretation; adding one would overcount.

Duplicate attack times are permitted by non-decreasing order. If `a == b`, the gap is zero and the earlier attack contributes nothing separately. The second attack simply resets the same timer at the same second, so this is correct.

If `duration == 0`, the initial answer is zero and every minimum is zero. No seconds are poisoned. The nonempty-array constraint means initializing from the last attack's duration is always structurally valid; there is always a last attack.

Correctness follows by partitioning the union chronologically. For every non-final attack, assign it exactly the poisoned time beginning at its timestamp and ending at the earlier of its natural expiration or the next attack. These pieces do not overlap and cover all poisoned time before the last attack. The final full interval covers the remaining poisoned time. The algorithm sums exactly the lengths of these disjoint pieces, so `ans` equals the total union duration.

## Complexity detail

Let $n$ be the number of attack times. `pairwise` yields $n - 1$ adjacent pairs lazily, and the loop does constant work for each one. Total time is $O(n)$.

Only `ans` and the current pair are retained, so auxiliary space is $O(1)$. The input is already sorted and is not copied or modified.

## Alternatives and edge cases

- **Explicit interval merging:** Construct `[t, t + duration)` intervals and merge overlaps. It works but stores unnecessary interval data when chronological gaps alone determine the union length.
- **Simulate every second:** Marking poisoned timestamps can require work proportional to the numeric timeline rather than the number of attacks, which is wasteful for large times and durations.
- **Unsorted input:** The one-pass gap reasoning depends on non-decreasing times. Without that guarantee, sort first at $O(n\log n)$ cost.
- **Overlapping attacks:** Add only the gap to the next attack, preventing overlap from being counted twice.
- **Non-overlapping attacks:** A gap at least as large as `duration` contributes the full duration.
- **Duplicate timestamps:** Their gap is zero, so an immediate reset adds no separate earlier interval.
- **Zero duration:** Every contribution is zero and the result is zero.
- **Single attack:** `pairwise` yields nothing, and the initialized `duration` is exactly the answer.
- **Inclusive seconds:** `b - a` already counts the integer seconds from `a` through `b - 1`; no extra one belongs in the formula.
