## General

**Why a completed-course set is enough state**

There are at most fifteen courses, which strongly suggests representing a subset with a bitmask. Bit position `i` represents course `i`, while bit zero is deliberately unused because course labels begin at one. A one bit in `cur` means that course has been completed in an earlier semester.

Future choices depend only on which courses are complete, not on the exact semesters in which they were taken. Therefore, two schedules reaching the same mask are equivalent for all future decisions. The stored breadth-first search visits each reachable completed-course mask at most once.

For each course `y`, `d[y]` is a prerequisite bitmask. The statement `d[y] |= 1 << x` adds prerequisite course `x` for every relation from `x` to `y`. A course with no prerequisites keeps mask zero.

**Why breadth-first search minimizes semesters**

The queue begins with `(0, 0)`: no courses completed after zero semesters. Every transition chooses the courses taken in one new semester and enqueues a resulting mask with time `t + 1`. All edges in this state graph therefore have equal cost of one semester.

Breadth-first search processes states in nondecreasing distance from the start. The first time the full mask is removed from the queue, its associated `t` is the fewest possible transitions and hence the minimum number of semesters.

The full mask is `(1 << (n + 1)) - 2`. Shifting creates bits zero through `n`, subtracting two leaves bits one through `n` set and bit zero clear. This exactly matches the course-bit convention.

**Finding courses available next semester**

For each course `i`, the condition `(cur & d[i]) == d[i]` asks whether every prerequisite bit is already present in `cur`. It uses the current completed set only, so a course selected for the coming semester cannot unlock another course in that same semester. This matches the rule that prerequisites must be completed in previous semesters.

The loop initially places every eligible course into `nxt`, including courses already completed. Why is that safe? Any completed course had all prerequisites satisfied when it was taken, and completed bits never disappear, so it still passes the eligibility test. The statement `nxt ^= cur` then removes exactly those completed-course bits. XOR is safe here because `cur` is a subset of the preliminary `nxt`; the result contains available and unfinished courses only.

**Taking all courses when at most k are available**

If `nxt.bit_count() <= k`, the algorithm takes every available course. Deferring one cannot help. Taking an additional eligible course uses capacity that would otherwise be unused, never removes an option, and can only satisfy more prerequisites in future semesters. The resulting mask is `nxt | cur`.

The visited set prevents enqueueing the same completed-course subset twice. Since BFS reaches a mask first with the smallest semester count, later paths to the same mask cannot improve the answer.

**Choosing exactly k when too many are available**

If more than `k` courses are available, a semester may choose a subset. Taking fewer than `k` is never better: every chosen course is already eligible, courses have no negative effect, and completing an extra course can only expand later availability. Thus it is sufficient to examine subsets containing exactly `k` courses.

The code saves the full available mask in `x` and then enumerates all nonempty submasks with

`nxt = (nxt - 1) & x`.

This standard operation moves from one submask of `x` to the next smaller submask. Only masks whose `bit_count() == k` are enqueued. During this enumeration, the variable `nxt` is intentionally overwritten; `x` preserves the original available set, and `nxt` is not needed afterward.

**Why the search is complete and correct**

Every legal semester choice from a state is either all available courses when their count is at most `k`, or some size-`k` subset when their count is larger. The dominance arguments show that choices taking fewer available courses need not be considered in an optimal schedule.

The submask loop enumerates every size-`k` subset of the available set. Hence every nondominated first-semester choice of an optimal remaining schedule appears as a BFS transition. Repeating this reasoning at subsequent masks means at least one optimal schedule is represented in the state graph. BFS returns its minimum number of transitions.

The directed prerequisite graph is guaranteed acyclic and all courses are completable, so a non-full state always eventually leads toward a legal completion. The exact function has no explicit return after the queue loop because the guarantee makes queue exhaustion without finding the full mask impossible.

## Complexity detail

There are at most $2^N$ completed-course masks. For each visited mask, computing availability scans $N$ courses, contributing $O(N2^N)$ work.

When more than $k$ courses are available, the source can enumerate all submasks of that available mask. Across subset states, the standard combined bound for choosing a completed mask and a submask of remaining courses is $O(3^N)$. Accounting for bit counting in an $N$-bit model gives the manifest's conservative $O(N3^N)$ time. With Python integers and $N \le 15$, `bit_count` is effectively tiny, but the exponential enumeration remains dominant.

`vis` and the queue can each contain $O(2^N)$ masks. The prerequisite array uses $O(N)$ entries. Thus auxiliary space is $O(2^N + N)$, matching the manifest. Each integer mask itself uses $O(N)$ bits in a bit-sensitive accounting.

## Alternatives and edge cases

- **Subset dynamic programming:** Let a table store the minimum semesters needed to reach each completed mask and relax legal course subsets. It explores essentially the same state space with a different traversal order.
- **Topological greedy without subset search:** Always choosing arbitrary available courses can be suboptimal when capacity is limited, because the chosen courses unlock different future chains.
- **Enumerating subsets smaller than k:** This is unnecessary when more than k courses are available; adding another currently eligible course cannot hurt.
- **No prerequisites:** Up to k courses can be taken each semester, so the answer is $\lceil N/k \rceil$.
- **k equals n:** Every currently available course is taken together, though prerequisite chains can still require several semesters.
- **Long prerequisite chain:** Only the next course becomes available each time, so one course is taken per semester regardless of k.
- **Courses selected together:** They cannot satisfy one another's prerequisites in that semester because availability is computed solely from `cur`.
- **Unused bit zero:** All course masks consistently use positions one through n; the full-mask expression clears bit zero.
- **Duplicate states:** `vis` is required because different semester choices can produce the same completed set.
- **Guaranteed DAG:** Without acyclicity, the queue could exhaust before the full mask and the exact source would implicitly return `None`.
