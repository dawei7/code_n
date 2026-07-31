## General

**Define a suffix decision**

Let `best[i]` be the maximum points obtainable starting when question `i` is
the next available question. The state needs only an index: every earlier
choice has already determined which suffix remains, and it has no other effect
on later rewards.

**Compare solving with skipping**

Skipping question `i` leads to `best[i + 1]`. Solving it earns `points` and
makes the next `brainpower` positions unavailable, so the next decision is at
`i + brainpower + 1`. If that index lies beyond the exam, its suffix value is
zero. Therefore:

$$
\texttt{best[i]} =
\max\left(\texttt{best[i + 1]},
\texttt{points} + \texttt{best[i + brainpower + 1]}\right).
$$

Compute states from right to left so both referenced suffixes are already
known. The two terms enumerate the only decisions at question `i`, and each
uses an optimal value for the suffix it leaves. Their maximum is consequently
optimal for `i`; applying this reasoning backward makes `best[0]` the answer.

## Complexity detail

Let $n$ be the number of questions. Each of the $n$ suffix states performs
constant work, giving $O(n)$ time. The dynamic-programming array contains
$n+1$ values and uses $O(n)$ space.

## Alternatives and edge cases

- **Top-down memoization:** The same recurrence with a cache is also $O(n)$,
  but recursion depth can reach $n$ and exceed Python's call-stack limit.
- **Uncached recursion:** Exploring both solve and skip branches recomputes
  suffixes and takes exponential time in the worst case.
- A brainpower value may skip beyond the array; that solve branch then receives
  no additional suffix points.
- The final question's solve value is simply its points, regardless of its
  brainpower value.
- A locally larger reward need not be optimal if solving it suppresses a more
  valuable combination later.
