## General

**Reduce the schedule to the labels that create the tightest spacing requirement.** Every task takes exactly one interval. If cooldowns never force an idle interval, the answer is simply the number of tasks. Idles are needed only when repeated copies of a frequent label cannot be separated by enough other work.

The exact solution first builds `Counter(tasks)`. Let:

- $T$ be the total number of tasks;
- $x$ be the largest frequency of any label;
- $s$ be the number of labels whose frequency equals $x$.

For `["A","A","A","B","B","B"]`, $T=6$, $x=3$, and $s=2$ because both A and B occur three times.

**Why the most frequent tasks define a schedule skeleton.** Begin with one label that occurs $x$ times. Its first $x-1$ copies each need at least $n$ intervening intervals before the next copy:

`A _ _ A _ _ A`

when $x=3$ and $n=2$. Another way to group the same picture is:

`[A _ _] [A _ _] [A]`.

There are $x-1$ complete frames. Each frame begins with one occurrence and covers $n+1$ intervals: the task interval itself plus the $n$ intervals that must separate it from the next copy. The final occurrence does not require a cooldown after it, so it belongs to a shorter last frame.

**Account for ties at the maximum frequency.** If $s$ labels all appear $x$ times, each complete frame must reserve one position for each of those labels, and the last frame contains all $s$ final occurrences. For A and B, a skeleton is:

`[A B _] [A B _] [A B]`.

The first $x-1$ frames still have length $n+1$, while the final frame has length $s$. This creates the formula

$$
(x-1)(n+1)+s.
$$

The value is a lower bound: the $x$ copies of every maximum-frequency label must respect cooldown, so the first and last rounds cannot be squeezed closer than this skeleton permits.

**Why the number of tasks is a second lower bound.** Every task consumes one CPU interval, even when no idle is required. Therefore, no schedule can be shorter than $T$. The skeleton formula can be smaller than $T$ when many other labels are available. For example, those other tasks can fill every apparent blank and may extend the schedule without creating idle time. The result must consequently be at least

$$
\max\left(T,\,(x-1)(n+1)+s\right).
$$

That is exactly what the return statement computes.

**Why this lower bound is achievable.** Place the $s$ most frequent labels once in each of $x$ rounds. Between consecutive rounds, reserve enough total positions so that two occurrences of the same label are $n+1$ intervals apart. Now distribute every less-frequent label among the open positions. No such label has more than $x$ copies, so its occurrences can be spread across different rounds rather than duplicated too closely inside one round.

If the other tasks do not fill all reserved positions, the unfilled positions are genuine idles, and the skeleton length is achievable. If they do fill all positions and more tasks remain, insert the surplus into the already dense rounds. In that case the total task count is at least the skeleton length, and a schedule of length $T$ is achievable without idle intervals. Thus one of the two lower bounds is also a realizable upper bound, proving the maximum formula is the optimum.

**Trace the first example.** Frequencies are A:3 and B:3, so $x=3$ and $s=2$. With $n=2$:

$$
(3-1)(2+1)+2=8.
$$

The task-count bound is 6, so the answer is 8. The schedule `A, B, idle, A, B, idle, A, B` realizes it.

For `["A","C","A","B","D","B"]` with $n=1$, A and B have the maximum frequency 2, so $x=2$ and $s=2$. The skeleton gives $(2-1)(1+1)+2=4$, but $T=6$. There are enough distinct tasks to eliminate all idle time, so the maximum correctly returns 6.

**Understand each source expression.** `max(cnt.values())` obtains $x$. The input is guaranteed nonempty, so `max` never receives an empty collection. `sum(v == x for v in cnt.values())` obtains $s$: in Python, each true comparison contributes 1 and each false comparison contributes 0. The method never constructs an actual schedule because only the minimum length is requested.

## Complexity detail

Counting all tasks takes $O(T)$ time. Scanning the frequency values to find $x$ and then count $s$ takes $O(U)$ time, where $U$ is the number of distinct labels. Because labels are restricted to the 26 uppercase English letters, $U\le26$ is a fixed constant. Total time is therefore $O(T)$.

The counter stores at most 26 entries, so its auxiliary space is $O(26)=O(1)$ under the stated alphabet. If task labels came from an unbounded domain, the same code would use $O(U)$ space instead. The remaining variables are scalars, and no schedule-sized structure is built. These facts match the manifest's $O(T)$ time and $O(1)$ space.

All arithmetic fits comfortably in Python integers. With at most $10^4$ tasks and $n\le100$, the formula is also small enough for ordinary fixed-width integer types.

## Alternatives and edge cases

- **Max-heap simulation:** Repeatedly choose the most frequent available labels in cycles of length $n+1$. This can construct the timing explicitly and generalizes well, but it is more machinery than the closed formula needs.
- **Sort 26 frequencies and count idle slots:** Use one maximum label to create gaps, then fill them with other frequencies. This is also constant-alphabet linear time but has more bookkeeping around tied maxima.
- **Cooldown queue simulation:** Track time, a max heap of available labels, and a queue of cooling labels. It is useful when an actual schedule is needed, but unnecessary for returning only the length.
- **`n = 0`:** The skeleton cannot force a gap, and the maximum returns exactly $T$.
- **Every task label is unique:** Then $x=1$ and $s=T$; the skeleton equals $T$, so no idle is introduced.
- **Only one distinct label:** Here $s=1$; the answer is $(x-1)(n+1)+1$, representing one task followed by $n$ idles between repetitions.
- **Several maximum-frequency labels:** The final `+ s` term is essential. Omitting it undercounts the last round.
- **Enough filler tasks:** When $T$ exceeds the skeleton, the result is $T$ because useful work fills all cooldown gaps.
- **Nonempty input guarantee:** It makes `max(cnt.values())` safe. An empty task array would require a separate return of 0.
- **Fixed alphabet assumption:** Constant space depends on A through Z. With arbitrary labels, describe counter storage as $O(U)$.
