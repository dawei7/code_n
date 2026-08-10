## General

**Logs contain end times, not durations**

Each log entry gives an employee ID and the absolute time when that task ended. The first task begins at time zero. Every later task begins as soon as the previous task ends, so its duration is

$$
\text{current leave time} - \text{previous leave time}.
$$

The strictly increasing leave times ensure every duration is positive. The employee count `n` determines the valid ID range but is not otherwise needed by the scan.

The solution maintains:

- `last`, the previous task's leave time;
- `mx`, the longest duration seen so far;
- `ans`, the employee ID chosen for that longest duration.

All three start at zero. For the first task, subtracting `last = 0` from its leave time gives the correct duration from time zero.

**Understand the local reassignment of `t`**

The loop receives `uid` and the raw leave time in `t`. It then executes `t -= last`, so the local variable `t` now means task duration rather than leave time.

After the best-answer test, the line `last += t` may look unusual. At that moment,

$$
\texttt{t}
=
\text{current leave time}
-
\texttt{last}_{old}.
$$

Therefore

$$
\texttt{last}_{old} + \texttt{t}
=
\text{current leave time}.
$$

The addition restores `last` to the absolute leave time of the current task. Writing `last = original_leave_time` would be more direct, but the original value has been overwritten in the local `t` variable. The algebra shows that the update is equivalent and keeps the next duration correct.

**Update on a longer task or a better tie**

The condition

`mx < t or (mx == t and ans > uid)`

implements both ranking rules. If the current duration `t` is larger, the current task must replace the previous choice. If durations tie, the current employee replaces `ans` only when `uid` is smaller.

The assignment `ans, mx = uid, t` updates the chosen employee and its duration together. If neither condition holds, the existing pair remains better: it has a longer duration, or it has the same duration with an equal or smaller employee ID.

Because durations are positive, the first log always has `t > mx` when `mx` is initially zero. Thus `ans` is initialized to the first actual worker through the normal update logic, even if that worker's ID is not zero.

**Trace the chronological scan**

For `logs = [[0,3],[2,5],[0,9],[1,15]]`:

- The first duration is `3 - 0 = 3`, so the best becomes employee 0 with duration 3, and `last` becomes 3.
- The second duration is `5 - 3 = 2`, which does not replace the best, and `last` becomes 5.
- The third duration is `9 - 5 = 4`, so employee 0 becomes the best with duration 4.
- The fourth duration is `15 - 9 = 6`, so employee 1 becomes the final answer.

For `[[0,10],[1,20]]`, both durations are 10. The first task selects employee 0. The second tie does not replace it because `ans > uid` is false for 0 and 1. The smaller ID is correctly retained.

**The scan invariant**

After processing the first $r$ logs, `last` equals the leave time in the $r$th processed log. The pair `(mx, ans)` describes the best task among those $r$ entries under the ordering “larger duration first, then smaller employee ID.”

The duration calculation and algebraic `last` update preserve the first statement. For the second statement, the conditional compares the new task with the best of all earlier tasks using exactly that ordering. It replaces the pair if and only if the new task ranks ahead. This is the standard induction step for maintaining a running optimum.

After the final log, every task has been considered exactly once and `ans` is the required worker ID.

It does not matter if the same employee appears in multiple non-adjacent logs. The problem ranks tasks by individual duration, and each occurrence is compared separately. If one employee owns several tied maximum tasks, the returned ID is still that employee; if several employees tie, the numeric condition selects the smallest.

## Complexity detail

Let $m$ be `len(logs)`. The loop performs one subtraction, a constant number of comparisons, and constant-size assignments per entry, so time is $O(m)$. The solution never loops through all `n` employee IDs because employees without logged tasks cannot own the longest task.

Only `last`, `mx`, `ans`, and loop-local scalars are stored, so auxiliary space is $O(1)$. The input log array is read without modification; rebinding local `t` does not change `logs`.

The maximum leave time is only 500 under the constraints, so arithmetic easily fits fixed-width types. The same algorithm works for much larger times if the integer type can hold the differences.

## Alternatives and edge cases

- **Precompute a duration array:** Subtract consecutive leave times, then find the best pair. This is also $O(m)$ time but uses $O(m)$ unnecessary storage.
- **Sort tasks by duration:** Sorting can apply a compound key of negative duration and employee ID, but costs $O(m\log m)$ when a single pass suffices.
- **Track totals per employee:** Summing all work by an employee answers a different question. The problem asks for the employee owning one longest task, not the greatest total time.
- **One log:** Its duration is its leave time minus zero, so its employee is returned regardless of ID.
- **Tie between tasks:** The condition replaces the answer only for a smaller ID, so log order cannot override the stated tie-break.
- **Same employee appears repeatedly:** Each task duration is evaluated independently; no accumulation is performed.
- **First worker has nonzero ID:** Positive first duration replaces the zero-initialized best and records the actual ID.
- **Strictly increasing leave times:** This guarantee makes durations positive and lets zero serve as a safe initial maximum.
- **Unused `n` parameter:** The scan does not need the number of possible employees because IDs are already present in logs and guaranteed valid.
- **Local variable mutation:** `t -= last` changes only the unpacked integer variable, not the nested entry stored in `logs`.
