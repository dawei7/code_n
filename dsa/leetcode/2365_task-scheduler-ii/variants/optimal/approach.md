## General

**Schedule every task as early as legality permits.** Let `day` be the day of
the most recently completed task. Without a type conflict, the next task can
run on `day + 1`. If its type last ran on day $d$, it cannot run again before
$d+\texttt{space}+1$. Therefore its earliest day is the maximum of those two
bounds.

Store the last completion day for every task type, jump `day` directly to the
computed bound, and update that type's entry. Skipped day numbers represent
the necessary breaks without simulating them individually.

Completing a task earlier can never delay any later task: it preserves order
and weakly lowers both the next-day bound and this type's future cooldown
bound. Inductively, every scheduled day is the earliest possible for that
prefix, so the final day is minimal.

## Complexity detail

Each of $n$ tasks performs one expected-constant-time hash lookup and update,
for $O(n)$ expected time. Up to $n$ distinct task types use $O(n)$ space.

## Alternatives and edge cases

- **Day-by-day simulation:** Testing readiness on every calendar day is
  correct but can take $O(n\cdot\texttt{space})$ time.
- **Next-allowed-day map:** Store the first legal future day instead of the
  last completion day; the formulas are equivalent.
- **Distinct tasks:** No breaks are needed when no type repeats.
- **Already satisfied gap:** Intervening work counts as elapsed days.
- **Large result:** Repeated tasks with large `space` require 64-bit totals.
