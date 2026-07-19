## General
**Measure the deepest prefix deficit**

Scan from left to right, adding one for `"["` and subtracting one for `"]"`.
A bracket string with equal totals is balanced exactly when this prefix balance
never becomes negative. Let $-D$ be the minimum balance encountered, so $D$ is
the largest shortage of opening brackets in any prefix.

**Convert the deficit into swaps**

When a problematic early `"]"` is swapped with a later `"["`, every prefix
between those positions gains two balance units: the early contribution
changes from $-1$ to $+1$. Consequently, one swap can repair at most two units
of the deepest deficit, establishing a lower bound of $\lceil D/2\rceil$.

Because the total numbers of brackets are equal, an opening bracket always
exists later whenever a negative prefix needs repair. Swapping such brackets
raises the deficient range by two, and repeating this operation
$\lceil D/2\rceil$ times makes every prefix nonnegative. The lower bound is
therefore achievable, so the answer is `(D + 1) // 2`.

## Complexity detail
One scan processes each of the $N$ brackets once, taking $O(N)$ time. The
current balance and minimum balance are the only retained state, so the
auxiliary space is $O(1)$.

## Alternatives and edge cases
- **Materialize greedy swaps:** Locate a later opening bracket whenever the
  running balance is negative and swap it into place. This is correct, but
  storing and modifying the character array uses $O(N)$ space.
- **Adjacent-swap interpretation:** Counting how far brackets must move solves
  a different problem; one operation here may exchange any two indices.
- An already balanced string has no negative prefix and requires zero swaps.
- A deficit of one or two requires one swap, while deficits of three or four
  require two.
- Equal total bracket counts guarantee that balancing is always possible.
