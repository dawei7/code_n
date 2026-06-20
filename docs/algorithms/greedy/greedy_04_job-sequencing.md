# Job Sequencing Problem

| | |
|---|---|
| **ID** | `greedy_04` |
| **Category** | greedy |
| **Complexity (required)** | $O(N \log N)$ Time, $O(N)$ Space |
| **Difficulty** | 5/10 |
| **Interview relevance** | 6/10 |
| **GeeksForGeeks Equivalent** | [Job Sequencing Problem](https://www.geeksforgeeks.org/job-sequencing-problem/) |

## Problem statement

Given `N` jobs where every job is represented by a `Job ID`, a `Deadline`, and a `Profit`.
Every job takes exactly 1 unit of time to complete. Only one job can be executed at a time.
A job yields its profit ONLY if it is completed strictly on or before its deadline.
Find the maximum total profit you can earn, and the number of jobs completed.

**Input:** An array of `Job` objects `[id, deadline, profit]`.
**Output:** A tuple `(number_of_jobs_done, max_profit)`.

## When to use it

- To optimally schedule single-unit tasks before their expiration to maximize yield.
- *Constraint:* If jobs take VARIABLE amounts of time to complete (e.g., job 1 takes 3 hours, job 2 takes 5 hours), the Greedy approach fails and you must use DP (Weighted Job Scheduling).

## Approach

**1. The Greedy Choice (Maximizing Profit):**
If we want the maximum profit, we should obviously prioritize the jobs that pay the most!
We start by sorting the jobs in descending order based on their `Profit`.

**2. The Scheduling Logic (Maximizing Free Time):**
Let's say the highest-paying job has a deadline of Day 5. When should we schedule it?
- If we schedule it on Day 1, we waste a precious early slot! What if another high-paying job has a deadline of Day 1? We wouldn't be able to do both.
- We should schedule it as **LATE AS POSSIBLE**, right before it expires! If its deadline is Day 5, we schedule it on Day 5! This leaves Days 1-4 completely open for other jobs with tighter deadlines.

**3. The Time Slots Array:**
We find the absolute maximum deadline among all jobs (let's say D_{max}).
We create a `slots` array of size D_{max} + 1, initialized to `False`.
We iterate through our sorted jobs. For each job, we look at its deadline d.
We check `slots[d]`. If it's free, we schedule the job there and mark it `True`.
If Day d is already taken by a previously scheduled higher-paying job, we look backward in time: `d-1`, `d-2`, etc. We take the first available free slot!
If we reach Day 1 and all slots are full, this job cannot be completed. We skip it.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for greedy_04: Job Sequencing.

Auto-generated from challenges/algorithms/greedy.py:SPECS.
O(n²) time.
"""


def solve(deadline, profit, n):
    # Build job tuples and sort by profit descending.
    jobs = sorted(
        ((profit[i], deadline[i]) for i in range(n)),
        key=lambda j: j[0],
        reverse=True,
    )
    # latest_free[t] is the latest time slot that is still available
    # up to t. We collapse the search with a simple boolean array.
    slots = [False] * (n + 1)
    total = 0
    for p, d in jobs:
        # Find the latest free slot <= min(d, n).
        for t in range(min(d, n), 0, -1):
            if not slots[t]:
                slots[t] = True
                total += p
                break
    return total
```

</details>

## Walk-through

Jobs: `J1(d=2, p=100)`, `J2(d=1, p=19)`, `J3(d=2, p=27)`, `J4(d=1, p=25)`, `J5(d=3, p=15)`.

1. Sort descending by profit:
   `J1(2, 100)`, `J3(2, 27)`, `J4(1, 25)`, `J2(1, 19)`, `J5(3, 15)`.
2. `max_deadline = 3`. `slots = [F, F, F, F]`.
3. Evaluate `J1` (Deadline 2, Profit 100):
   - Slot 2 is free. `slots[2] = True`. `profit = 100`.
4. Evaluate `J3` (Deadline 2, Profit 27):
   - Slot 2 is taken.
   - Slot 1 is free. `slots[1] = True`. `profit = 127`.
5. Evaluate `J4` (Deadline 1, Profit 25):
   - Slot 1 is taken.
   - Loop hits 0. Cannot be scheduled! Skip.
6. Evaluate `J2` (Deadline 1, Profit 19):
   - Slot 1 taken. Skip.
7. Evaluate `J5` (Deadline 3, Profit 15):
   - Slot 3 is free. `slots[3] = True`. `profit = 142`.

Result `jobs_done = 3`, `total_profit = 142`. ✓ (Sequence: J3, J1, J5).

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(N \log N)$ | $O(Max\_Deadline)$ |
| **Average** | $O(N \log N)$ | $O(Max\_Deadline)$ |
| **Worst** | $O(N * Max\_Deadline)$ | $O(Max\_Deadline)$ |

Sorting takes $O(N \log N)$.
The nested loop iterates N times, and the inner loop goes backward from `deadline` down to 1. In the worst case (e.g. all jobs have a massive deadline of 10,000 but the slots fill up from right to left), the inner loop does $O(Max\_Deadline)$ work for every job. Total time is $O(N log N + N x Max\_Deadline)$.
If Max\_Deadline is bounded by N, it simplifies to $O(N^2)$.
Space complexity is $O(Max\_Deadline)$ for the boolean array.

## Variants & optimizations

- **Disjoint Set (Union-Find) Optimization:** We can eliminate the $O(N^2)$ backward linear search entirely! Using a Disjoint Set (`graph_09`), we can point every time slot directly to the *nearest available empty slot to its left*. If slot 5 is taken, `find(5)` instantly returns 4. If 4 is taken, it instantly returns 3! This reduces the packing phase to $O(N \cdot \alpha(N)$), making the whole algorithm strictly $O(N \log N)$ bounded by the sort!
- **Weighted Job Scheduling (DP):** If jobs take >1 unit of time, we sort by *Finish Time* and use Binary Search with DP to find the optimal sequence without overlaps (`dp_08`).

## Real-world applications

- **Freelance Contracting:** A consultant with multiple gig offers (each taking 1 day, paying different amounts, and expiring on different days) maximizing their weekly paycheck.
- **Server Maintenance Windows:** Executing high-priority background maintenance tasks on a database before daily usage spikes lock the tables.

## Related algorithms in cOde(n)

- **[greedy_01 - Activity Selection](greedy_01_activity-selection.md)** — The unweighted equivalent that maximizes the raw count of activities instead of profit.
- **[graph_09 - Union-Find](../graphs/graph_09_union-find.md)** — The data structure required to optimize the linear slot search to $O(1)$.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
