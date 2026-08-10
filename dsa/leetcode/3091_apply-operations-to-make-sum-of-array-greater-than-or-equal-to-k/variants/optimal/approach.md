## General

**Reduce a growing array to two decisions.** Initially the array is `[1]`. The two allowed operations seem to create many possible sequences: increment now or later, duplicate one value or another, and interleave both operation types. The key is to ask a simpler question: if a strategy uses exactly $a$ increment operations and $b$ duplication operations, what is the largest sum those operations could possibly create?

Every duplication increases the number of elements by one, so after $b$ duplications the final array has $b+1$ elements. An increment is most valuable when it happens before the duplications, because every later duplicate can copy that increased value. If all $a$ increments are applied to the original `1` first, its value becomes:

$$
x=a+1.
$$

Duplicating that value $b$ times produces $b+1$ equal copies and total sum:

$$
(a+1)(b+1)=x(b+1).
$$

No other ordering with the same numbers of operations can create a larger total. Delaying an increment until after some duplication makes that increment affect only one existing element, whereas doing it before duplication allows the larger value to be copied. Likewise, spreading increments among already duplicated elements cannot beat concentrating them in the value that all copies inherit.

Therefore, it is sufficient to consider plans of one canonical form: increment the initial value $a$ times, then duplicate it $b$ times.

**Find the fewest duplications for a fixed number of increments.** Once `x = a + 1` is fixed, the final sum after $b$ duplications is `x * (b + 1)`. The smallest legal number of copies is:

$$
\left\lceil\frac{k}{x}\right\rceil.
$$

Because one copy already exists, the number of duplication operations is:

$$
b=\left\lceil\frac{k}{x}\right\rceil-1.
$$

The source computes the ceiling using integer arithmetic:

`(k + x - 1) // x`.

This avoids floating-point rounding. Subtracting one yields the exact `b` stored by the code. The total operations for this candidate are `a + b`.

**Enumerate every possible increment count.** The loop uses `for a in range(k)`, so it checks $a=0,1,\ldots,k-1$. These values correspond to base values $x=1,2,\ldots,k$. There is no reason to try $a\ge k$: incrementing the original value $k-1$ times already makes it equal to $k$, requiring no duplication and costing $k-1$. Additional increments only increase the operation count.

For every `a`, the source computes the minimum matching `b` and updates `ans = min(ans, a + b)`. Because every useful value of $a$ is considered and the best $b$ for that value is chosen, the smallest recorded sum is globally optimal.

**Why balanced choices tend to win.** The constraint is approximately:

$$
(a+1)(b+1)\ge k.
$$

For a fixed product, the sum of two positive factors is smallest when the factors are close. That is why good candidates usually place both $a+1$ and $b+1$ near $\sqrt{k}$. For $k=11$, choosing $a=3$ gives $x=4$. Three copies are enough because $\lceil 11/4\rceil=3$, so $b=2$ and the total is five operations. The final array can be `[4,4,4]` with sum 12.

The exact source does not calculate the square root or inspect only two balanced candidates. It simply enumerates all $k$ possible values of $x$. This is easy to verify and remains fast for the constraint $k\le 10^5$.

**A proof that no interleaving is better.** Take any legal strategy with $a$ increments and $b$ duplications. Imagine moving an increment earlier across a later duplication. If the duplication copies the incremented element, moving the increment earlier leaves the original effect and may also increase the new copy; the sum does not decrease. If it copies another element, the operations can be rearranged without reducing the attainable maximum, and concentrating future copies on the largest value is at least as good. Repeating this exchange moves all increments before all duplications and places them on the value that will be copied.

The canonical plan therefore reaches at least the sum of the original strategy using the same $a+b$ operations. If any arbitrary strategy reaches $k$, an enumerated canonical strategy with that same operation budget can also reach $k$. Conversely, every enumerated candidate is directly executable. The minimum over the candidates is exactly the requested minimum.

**Why overshooting is allowed.** The target says the final sum must be greater than or equal to $k$, not exactly $k$. The ceiling selects the first copy count that reaches the threshold. A product such as 12 for $k=11$ is valid, and forcing an exact product could incorrectly reject the optimal plan.

## Complexity detail

The loop performs exactly $k$ iterations. Each iteration uses a fixed amount of integer arithmetic and one comparison, so the exact implementation takes $O(k)$ time and $O(1)$ auxiliary space.

This is a direct mismatch with the local Optimal manifest, which claims $O(1)$ time and describes choosing balanced factors around $\sqrt{k}$. That would describe a different mathematical implementation. The checked-in `solution.py` contains `range(k)` and must be documented as $O(k)$. Under the given upper bound of $10^5$, the linear scan is still comfortably practical.

Python's integers handle the additions and products safely. In this problem all values are small anyway: `k + x - 1` is at most about $2k$, and no array is actually constructed.

## Alternatives and edge cases

- **Square-root formula:** Check factor sizes around $\sqrt{k}$ to obtain an $O(1)$ or small $O(\sqrt{k})$ implementation, depending on how candidates are generated. This is the idea in the manifest, not the loop in the source.
- **Breadth-first search over arrays:** It models the operations literally but creates an enormous state space and ignores the factor reduction.
- **Dynamic programming by reachable sum:** It is unnecessary because operation order can be normalized analytically.
- **`k = 1`:** The initial array already has sum one. With `a = 0`, the formula gives `b = 0` and returns zero.
- **No increments:** The `a = 0` candidate keeps value one and needs `k - 1` duplications.
- **No duplications:** The `a = k - 1` candidate raises the sole element to `k`.
- **Overshoot:** Ceiling division deliberately allows the product to exceed `k`.
- **Perfect factorization:** If `k` is divisible by `x`, the ceiling becomes exact and no surplus copy is added.
- **Why subtract one:** `ceil(k / x)` is the required number of array elements, while one element exists from the start.
- **Candidate initialization:** `ans = k` is a safe loose upper bound; the loop will find at most `k - 1` operations for positive `k`.
- **Operation commutation:** Moving increments earlier never reduces the maximum final sum because later duplicates can copy the increase.
- **Concentrating increments:** Increasing the value that is repeatedly duplicated dominates distributing the same increments after copies already exist.
- **No final array allocation:** The factor pair proves a legal construction, so the code needs only operation counts.
- **Manifest discrepancy:** Complexity and method should be read from the exact source: it is an exhaustive linear scan, not a direct balanced-factor calculation.
