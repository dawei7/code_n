## General

**The order removes scheduling freedom**

Tasks must be completed in the given order. At any point, the only productive action is to execute the next task; tasks cannot be swapped to fill a waiting period. Therefore, if that next task is temporarily illegal because the same type was completed too recently, every intervening day is forced to be a break.

This makes an earliest-possible greedy schedule optimal: execute each task on the first day that is both after the previous processed day and legal for its type. Delaying it voluntarily cannot help, because every later task is blocked behind it in the fixed sequence.

**Track the next legal day for each type**

The dictionary `day` maps a task type to the earliest day on which that type may next be completed. Suppose a type is completed on day $d$. The problem requires `space` full days to pass after completion, so the next completion may occur on:

$$
d+\texttt{space}+1.
$$

For example, if a task runs on day `2` and `space = 3`, days `3`, `4`, and `5` must pass. The next same-type task can run on day `6`. Storing the next legal day directly avoids repeatedly reconstructing it from the last completion day.

`day` is a `defaultdict(int)`, so an unseen task type has stored availability zero. Real completion days begin at one, making zero safely mean “no restriction from an earlier occurrence.”

**Advance the global clock**

`ans` represents the day on which the most recently processed task was completed. It begins at zero, before any work has occurred. For each next task, the code first performs:

```python
ans += 1
```

This gives the earliest calendar day immediately after the preceding task. Even when the next task has a different type and needs no cooling period, two tasks cannot be performed on the same day, so at least this one-day advance is necessary.

The line

```python
ans = max(ans, day[task])
```

then compares that chronological next day with this type's availability. If `day[task]` is smaller, the task can run immediately. If it is larger, all days between are forced breaks, and assigning that larger value jumps directly over them.

After executing the task on the chosen `ans` day, the algorithm records:

```python
day[task] = ans + space + 1
```

This prepares the exact legal boundary for the next occurrence.

**Trace a waiting period**

Take `tasks = [5, 8, 8, 5]` and `space = 2`.

- Type `5` executes on day `1`, so its next legal day becomes `4`.
- Type `8` executes on day `2`, so its next legal day becomes `5`.
- The next task is another `8`. The ordinary next day would be `3`, but availability is `5`. The maximum jumps to day `5`, representing breaks on days `3` and `4`.
- The final `5` has ordinary next day `6`. Its stored availability is only `4`, so it executes on day `6`.

The returned value is `6`, the day on which all tasks have been completed.

**Why taking the earliest legal day is always optimal**

Assume the greedy schedule has completed the first $p$ tasks as early as possible, and let the next task have type $t$. Any valid schedule must complete it after the day used for task $p$, because only one action occurs each day and order is fixed. It must also complete it no earlier than the stored availability of type $t$, because that boundary encodes its last same-type execution plus the required gap.

The maximum of those two lower bounds is therefore the earliest day any valid schedule can use for this task. The algorithm uses exactly that day. This establishes the same “earliest possible prefix” property for $p+1$ tasks.

The property is true before the first task, so induction proves it for every prefix. In particular, the last value of `ans` is the minimum possible completion day for the whole task list.

There is no benefit from adding an optional break before a currently legal task. Doing so only shifts that task and every still-ordered successor later. It does not reduce any future same-type availability relative to actual time, because cooling boundaries are based on when tasks are executed; delaying an occurrence also delays the boundary created by that occurrence.

**Why direct jumping is safe**

When `day[task]` lies ahead of the current clock, no other task can be performed during the gap because the blocked task is next in the required order. Iterating one day at a time would only count mandatory breaks. Assigning the clock directly to the stored day preserves the resulting schedule while avoiding work proportional to potentially large idle gaps.

## Complexity detail

Let $n$ be the number of tasks. The loop processes each task exactly once. Dictionary lookup and update are expected $O(1)$, and all arithmetic is constant time under the usual model. Total expected time is $O(n)$, independent of how many break days the schedule contains.

The `day` dictionary contains one entry per distinct task type encountered. If there are $U$ types, it uses $O(U)$ space; since $U \le n$, the reported worst-case space complexity is $O(n)$.

The returned day can exceed $n$ substantially because of gaps, but Python integers handle the accumulated value without fixed-width overflow concerns.

## Alternatives and edge cases

- **Day-by-day simulation:** It can produce the same schedule, but long cooling gaps cause runtime proportional to the answer rather than the number of tasks.
- **Store last completion days:** One can save `last[task]` and compute `max(ans + 1, last[task] + space + 1)`. This is equivalent; storing the next legal day makes the lookup directly usable.
- **Reordering with a priority queue:** That solves a different task-scheduling problem. Here the input order is mandatory, so no choice of another ready task is allowed.
- **First occurrence of a type:** Its default availability is zero, so it runs on the next chronological day.
- **Consecutive equal tasks:** The second jumps to the first completion day plus `space + 1`.
- **Alternating types:** A type's cooling interval can elapse while intervening different tasks are completed, so the maximum may require no jump.
- **`space = 1`:** One full day must occur between equal types; they can be executed two calendar days apart.
- **All task types distinct:** No stored availability blocks anything, and the answer is exactly `len(tasks)`.
- **Every task has the same type:** Each consecutive execution is `space + 1` days apart, and direct jumping handles the large total efficiently.
- **Large task identifiers:** They are dictionary keys, so their numeric magnitude does not require a value-sized array.
