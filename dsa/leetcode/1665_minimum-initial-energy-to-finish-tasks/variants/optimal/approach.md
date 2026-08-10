## General

**Two different numbers describe a task**

A task `[a, m]` consumes `a` energy but requires at least `m` energy before it begins. Since `a <= m`, completing it leaves at least `m - a` energy when started at the minimum. The difference

$$
m-a
$$

measures how much starting threshold remains after paying the task’s actual cost. Tasks with a larger difference impose a relatively high entry requirement compared with what they consume.

The exact source sorts with key `a - m` in ascending order. Because `a - m = -(m - a)`, this is equivalent to ordering tasks by `m - a` in descending order: the largest threshold-minus-cost gap comes first.

**Why that order is optimal**

Consider two adjacent tasks `A = [a, m]` and `B = [b, q]`. If `A` is performed before `B`, the starting energy must satisfy both `E >= m` and `E - a >= q`. The minimum sufficient energy for this pair is

$$
R_{AB} = \max(m, a+q).
$$

If the order is reversed, it is

$$
R_{BA} = \max(q, b+m).
$$

Suppose `A` has at least as large a gap as `B`:

$$
m-a \ge q-b.
$$

Rearranging gives `a + q <= b + m`. Also `m <= b + m` because `b` is positive. Therefore both arguments of `R_{AB}` are at most `b + m`, and `b + m` is one argument of `R_{BA}`. Hence

$$
R_{AB} \le R_{BA}.
$$

So whenever a smaller-gap task appears before a larger-gap task, swapping the pair cannot increase the required initial energy. Repeatedly removing such inversions leads to descending `m-a` order. This exchange argument proves that the sorting key used by the source admits an optimal schedule.

**Simulate the chosen schedule by buying only missing energy**

The variables have concrete meanings:

- `ans` is the total initial energy committed so far;
- `cur` is the energy currently left after completing the already processed tasks.

Both begin at zero. For a task `[a, m]`, if `cur >= m`, the task can start without changing the chosen initial amount. If `cur < m`, the schedule lacks exactly `m - cur` energy at this point. The source adds that deficit to `ans` and sets `cur = m`.

This can be understood as increasing the original starting budget. Any energy added to the initial budget would survive through all previous fixed task costs and appear as the same extra amount now. Raising by precisely the deficit is necessary—anything less cannot start the current task—and sufficient. Adding more would never help minimize `ans`, so the greedy simulation adds only what is forced.

After the threshold is met, `cur -= a` pays the actual energy cost. Because `a <= m` and `cur >= m`, remaining energy never becomes negative.

**A trace**

For `tasks = [[1, 2], [2, 4], [4, 8]]`, the gaps are one, two, and four, so sorting puts `[4, 8]` first, then `[2, 4]`, then `[1, 2]`.

At the first task, `cur` is zero, so eight units are added to `ans` and `cur`. Spending four leaves four. The second task can begin at exactly four and leaves two. The last can begin at exactly two and leaves one. No later deficit is needed, so `ans = 8`.

For a schedule in which the current energy already exceeds a task’s minimum, no energy is added. This leftover is not wasted; it is carried to later tasks after subtracting only actual costs.

**Why the simulated amount is minimal for the sorted order**

Inductively, after each processed prefix, `ans` is the smallest initial energy that can execute that prefix in the chosen order, and `cur` equals that initial energy minus the sum of actual costs in the prefix. When `cur >= m`, the current minimum remains feasible and cannot be lowered without invalidating the already proven prefix optimum. When `cur < m`, every feasible initial energy must increase by at least the deficit, and adding exactly it establishes feasibility. The invariant therefore continues.

The exchange argument proves that no other ordering requires less initial energy than the sorted order, and the deficit simulation computes the minimum for that order. Together they prove that the returned `ans` is globally minimal.

## Complexity detail

Let `n` be the number of tasks. Computing sort keys and sorting the tasks takes $O(n\log n)$ time. The subsequent loop visits every task once and performs constant-time arithmetic, adding $O(n)$ time. Total running time is $O(n\log n)$.

The built-in `sorted(tasks, ...)` creates a new list of `n` references rather than modifying the input list. That list uses $O(n)$ space. Python’s sorting implementation also uses temporary memory whose worst-case bound is $O(n)$. The loop itself uses only constant scalar space, so total auxiliary space is $O(n)$, matching the manifest.

The input’s task sublists are not altered; only their references are reordered in the new sorted list.

## Alternatives and edge cases

- **Sort by `m-a` descending:** This is mathematically identical to sorting `a-m` ascending and may express the scheduling intuition more directly.
- **Reverse construction with ascending gap:** One can derive the necessary initial budget while conceptually placing tasks from the end. It reaches the same order but often makes the energy invariant harder to explain.
- **Binary search the initial energy:** For a fixed order feasibility is easy, but choosing the right order remains the main problem. Binary search adds a logarithmic factor and does not replace the exchange proof.
- **Sort only by minimum requirement:** A large minimum may also have a large actual cost; minimum alone does not capture how much useful energy remains afterward. The gap is the correct comparison key.
- **Task with `a == m`:** Its gap is zero, so it appears late. Starting at its threshold leaves zero energy, making it less valuable to schedule before high-gap tasks.
- **Several equal gaps:** Either relative order is safe because the pairwise proof gives equality or non-increase in both directions for the ordering criterion.
- **One task:** The loop raises `ans` directly to that task’s minimum and returns it, which is plainly optimal.
- **Leftover energy after all tasks:** The objective minimizes initial energy, not final energy. Some leftover may be unavoidable because a high starting threshold can exceed total consumption.
- **Already sufficient current energy:** The branch does not add anything to `ans` and spends only `a`.
- **Large deficit:** Raising `cur` to exactly `m` is sufficient even after previous tasks because added initial energy propagates unchanged through their fixed costs.
- **Input mutation:** Using `sorted` preserves the original order in `tasks`. An in-place `sort` could reduce the list-allocation distinction but would modify the caller’s array.
