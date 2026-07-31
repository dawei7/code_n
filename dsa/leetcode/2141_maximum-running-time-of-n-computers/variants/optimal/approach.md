## General

**Test a proposed common duration**

For all computers to run for $t$ minutes, they need $n t$ battery-minutes in
total. A single battery can contribute at most $\min(b,t)$ toward that goal:
even a larger battery cannot power two computers simultaneously, so more than
$t$ minutes from it cannot be used within a $t$-minute schedule.

Consequently, $t$ is feasible exactly when

$$
\sum_{b \in \texttt{batteries}} \min(b,t) \geq n t.
$$

Instantaneous swaps at integer times allow all capped contributions to be
distributed across the computers, making this energy condition sufficient as
well as necessary.

**Binary-search the monotone boundary**

If duration $t$ is feasible, every shorter duration is feasible. Search the
inclusive range from zero through
$\left\lfloor S/n \right\rfloor$, where $S$ is the total battery capacity.
When the midpoint is feasible, retain it and search higher; otherwise search
lower. The final retained value is the greatest feasible duration.

## Complexity detail

Let $m$ be the number of batteries and
$S=\sum_{b\in\texttt{batteries}} b$. Each feasibility test scans $m$
capacities, and binary search performs $O(\log(S/n))$ tests. The total time is
$O(m\log(S/n))$, with $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Test durations sequentially:** The same feasibility condition remains
  correct, but checking every duration through the answer takes $O(mS/n)$
  time.
- **Sort and discard oversized batteries:** A reviewed greedy redistribution
  can achieve $O(m\log m)$ time, but its averaging argument is less direct.
- When `n` is one, all battery capacities can be consumed sequentially.
- With exactly `n` batteries, the smallest battery determines the answer.
- Capacity beyond $t$ from one battery is capped because it cannot power
  multiple computers at the same instant.
