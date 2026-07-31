## General

Sort tasks by increasing end time. When processing `[start, end, duration]`, keep every second already activated: those choices may be shared with this task at no extra cost. If fewer than `duration` active seconds lie in its interval, activate exactly the missing number of unused seconds, choosing them from right to left.

Choosing the latest available seconds is safe. Suppose another feasible continuation used an earlier unused second $y$ where the greedy schedule chooses a later second $x$ for the current task. Replacing $y$ with $x$ preserves the current task. Every future task ends no earlier than the current task; if its interval contains $y$, its start is at most $y<x$ and its end is at least $x$, so it also contains $x$. Repeating this exchange transforms an optimal continuation into one containing all greedy choices. Thus the greedy schedule never uses more seconds than an optimum.

A Fenwick tree stores whether each time coordinate is active and answers how many selected seconds lie in `[start, end]`. A disjoint-set predecessor structure stores the latest still-inactive coordinate at or before a requested time. After activating `time`, link it to the predecessor of `time - 1`; path compression then skips activated runs. Each coordinate is activated at most once.

## Complexity detail

Let $n$ be the number of tasks, $T$ the largest end time, and $N=n+T$. Sorting costs $O(n \log n)$. The algorithm performs two Fenwick queries per task and one Fenwick update for each of at most $T$ activated seconds; disjoint-set operations have inverse-Ackermann amortized cost. The total is therefore $O(N \log N)$ time and $O(T)$ auxiliary space.

## Alternatives and edge cases

- **Boolean timeline scan:** Counting active seconds across every task interval and searching backward one coordinate at a time is correct under the small bound but takes $O(nT)$ time.
- **Segment tree:** Range counts plus a rightmost-unused search also support the same greedy choice in $O(N \log N)$ time, with a larger implementation constant.
- **Identical or nested tasks:** Already active seconds are reused; a task adds only its unmet duration.
- **Inclusive endpoints:** Both `start` and `end` are legal execution seconds and must participate in range counts.
- **Noncontinuous execution:** A task's selected seconds may be separated; only their count inside its interval matters.
- **Unlimited concurrency:** One active second can advance every task whose interval contains it, regardless of how many such tasks exist.
