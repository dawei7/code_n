## General

**Classify one value by its remainder**

Every integer has remainder $0$, $1$, or $2$ modulo $3$.

- A value with remainder $0$ is already divisible by $3$ and costs no move.
- A value with remainder $1$ becomes divisible after subtracting $1$.
- A value with remainder $2$ becomes divisible after adding $1$.

Thus each nonzero remainder has cost exactly one. It cannot cost zero because
the starting value is not divisible by $3$, and the construction above proves
that one operation is sufficient.

**Add the independent minimum costs**

An operation changes only the chosen element, so changing one value cannot
help another. The global optimum is therefore the sum of the separate
per-element optima: count the elements for which `num % 3 != 0`. This count is
both a lower bound—each such element must change—and attainable by applying
the appropriate increment or decrement once to each counted element.

## Complexity detail

A single scan examines all $n$ values, taking $O(n)$ time. The running count
uses $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Explicit distance formula:** Add `min(num % 3, 3 - num % 3)` for every
  value. Under modulo $3$, this is equivalent to adding one for each nonzero
  remainder, but it obscures the binary nature of the cost.
- **Repeatedly mutate values:** Simulating unit changes until each value is
  divisible performs unnecessary writes; the remainder gives the minimum
  directly.
- **Recompute prefix answers:** Counting all nondivisible values in every
  growing prefix and taking successive differences is correct but takes
  $O(n^2)$ time.
- An array containing only multiples of $3$ requires zero operations.
- The minimum-length array has one element, whose answer is either zero or one.
- Values at both legal boundaries, $1$ and $50$, have nonzero remainder and
  therefore each require one operation.
