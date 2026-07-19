## General
**Build the lexicographically smallest feasible prefix**

Scan `s` from left to right while maintaining the chosen characters as a
monotonic stack. When the current character is smaller than the stack top,
removing the top improves the first position where the candidate changes.
Such a removal is allowed only if the current and remaining source characters
can still fill the stack to length `k`.

**Protect the required letter count while popping**

Track how many copies of `letter` are already selected and how many remain at
or after the current position. A non-`letter` stack top may be removed whenever
the length guard permits. A `letter` top may be removed only when the selected
copies left behind plus all remaining copies can still reach `repetition`.
This prevents a lexicographic improvement from destroying feasibility.

**Reserve enough output slots while pushing**

If the stack has room, always admit the current character when it equals
`letter`. A different character is admitted only when the number of open
output slots is strictly greater than the number of required `letter` copies
still missing. Otherwise, that slot must be reserved for a future required
copy.

Every pop replaces an earlier, larger character with a smaller feasible one,
so it improves the candidate without eliminating any valid completion. Every
skipped non-`letter` is either unnecessary for length or would occupy a slot
reserved by the repetition constraint. Because each decision preserves at
least one completion and greedily minimizes the earliest undecided position,
the final length-`k` stack is the lexicographically smallest valid
subsequence.

## Complexity detail
Each of the $N$ characters is pushed at most once and popped at most once.
Counting remaining copies and joining the result are also linear, so the total
time is $O(N)$. The stack can contain up to `k` characters and therefore uses
$O(N)$ space in the worst case.

## Alternatives and edge cases
- **Greedy suffix scan per position:** For each output slot, scan all possible
  next indices and select the smallest character that leaves a feasible
  suffix. This is correct but can take $O(Nk)$ time.
- **Dynamic programming:** States for source position, selected length, and
  required copies can recover the optimum but require prohibitive
  $O(Nk \cdot \text{repetition})$ work.
- When `repetition == k`, every selected character must equal `letter`.
- Extra copies of `letter` beyond the minimum are allowed and may be
  lexicographically beneficial.
- A selected required copy cannot be popped after too few copies remain in the
  suffix.
- Non-`letter` characters must be rejected once every open slot is needed for
  the repetition requirement.
- When `k == N`, the only subsequence is the entire source string.
