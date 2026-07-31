## General

**Keep one counter per denomination**

Store five inventory counts aligned with `[20, 50, 100, 200, 500]`. A deposit
adds each supplied count to the corresponding inventory entry.

**Simulate the required priority without mutating state**

For a withdrawal, scan denominations from $500$ down to $20$. At each value,
tentatively take the smaller of the available count and the quotient of the
remaining amount by that denomination. Record the selection in a separate
five-entry array.

If a positive remainder survives all five denominations, return `[-1]`
without changing inventory. Otherwise, subtract the tentative selection and
return it. This delayed commit makes rejection atomic.

At every denomination, the algorithm takes exactly the greatest count allowed
by both inventory and remaining amount, so its selection matches the mandated
largest-first procedure. A zero remainder proves the returned notes form the
request exactly. A nonzero remainder proves that this required greedy procedure
failed; retaining the tentative selection separately preserves all notes.

## Complexity detail

Let $Q$ be the number of operations in the trace. Each deposit and withdrawal
touches exactly five denominations, so every operation takes $O(1)$ time and
the complete trace takes $O(Q)$ time. Inventory and tentative selection each
use five counters, giving $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Search for any note combination:** Backtracking could find a combination that the specified greedy priority forbids, so it would implement different semantics.
- **Replay operation history:** Reconstructing inventory before every withdrawal is correct but can take $O(Q^2)$ total time.
- **Mutate then roll back:** Immediate subtraction can work with careful restoration, but a separate tentative array makes failed-withdrawal atomicity explicit.
- **Greedy failure despite another combination:** Once a larger note is selected, smaller notes may not replace it.
- **Exact depletion:** A successful withdrawal may reduce any or all denomination counts to zero.
- **Rejected withdrawal:** No denomination count may change.
- **Repeated deposits:** Counts accumulate across the lifetime of the same object.
- **Unavailable large notes:** Greedy selection naturally continues with smaller denominations.
