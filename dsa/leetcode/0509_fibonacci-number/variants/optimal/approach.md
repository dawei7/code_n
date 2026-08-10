## General

The recurrence says each Fibonacci value depends only on the previous two:

$$
F(k+1)=F(k)+F(k-1).
$$

There is no need to retain the entire sequence. The source carries just two consecutive values and advances them together.

Before the loop starts,

- `a = 0 = F(0)`;
- `b = 1 = F(1)`.

The loop runs exactly `n` times. Its invariant is:

> before iteration `k`, `a = F(k)` and `b = F(k + 1)`.

This is true initially for `k = 0`. The simultaneous assignment

`a, b = b, a + b`

changes the pair to

$$
(F(k+1), F(k)+F(k+1))=(F(k+1),F(k+2)).
$$

That is exactly the invariant for the next iteration.

**Why simultaneous assignment matters.** Python evaluates every expression on the right using the old values before assigning either variable. The new `a` receives old `b`, while new `b` receives old `a + old b`.

If this were written naively as

`a = b`

followed by

`b = a + b`,

the second statement would use the already-updated `a` and compute the wrong sum. In a language without tuple assignment, save one old value in a temporary variable.

After exactly `n` iterations, the invariant gives `a = F(n)` and `b = F(n + 1)`. The method returns `a`, which is the requested value.

For `n = 4`, the pairs progress as follows:

- before any iteration: `(a, b) = (0, 1) = (F(0), F(1))`;
- after one: `(1, 1) = (F(1), F(2))`;
- after two: `(1, 2) = (F(2), F(3))`;
- after three: `(2, 3) = (F(3), F(4))`;
- after four: `(3, 5) = (F(4), F(5))`.

Returning three matches `F(4)`.

**Base cases need no branches.** If `n = 0`, `range(0)` performs no iterations and `a` remains zero. If `n = 1`, one update makes `a` equal one. The initial pair and loop count therefore encode both given base cases naturally.

This iterative dynamic programming avoids the duplicated work of direct recursion. A naive call to `F(n)` branches into `F(n - 1)` and `F(n - 2)`, and those branches repeatedly solve the same smaller values. Here each next Fibonacci number is computed once from the current pair.

The pair contains exactly the information needed for the next step. Suppose an algorithm has already reached `F(k)` and wants `F(k + 1)`. The recurrence needs `F(k - 1)` as well, so one value is not enough. Once `F(k + 1)` has been computed, however, no future transition needs `F(k - 1)` again: the new adjacent pair `F(k), F(k + 1)` completely replaces the old pair. This explains both why two variables are sufficient and why retaining an array of all earlier values is unnecessary.

The loop variable itself is unused and is written as `_` by Python convention. The number of iterations matters, but the numeric loop index does not. Each iteration means “advance the consecutive Fibonacci pair by one position.”

The constraint ends at thirty, so every result is small. Python integer growth is not a concern. For mathematically large `n`, integer addition itself costs time proportional to the number of result bits, but the manifest uses the standard unit-cost arithmetic model.

Correctness follows directly from the invariant proof. The pair begins with the correct consecutive Fibonacci values, one update preserves the consecutive-value relationship by the recurrence, and induction extends that fact through all `n` iterations. The first component is therefore exactly the requested sequence position when the loop ends.

## Complexity detail

The loop performs `n` iterations, each with constant many arithmetic assignments under the ordinary model, so time is $O(n)$. There is no recursion and no table.

Only `a`, `b`, the loop counter, and `n` are stored. Their count does not grow with `n`, so auxiliary space is $O(1)$. The integer values themselves grow in bit length for unbounded `n`; within the stated `n <= 30` domain, that representation size is bounded.

## Alternatives and edge cases

- **Naive recursion:** It mirrors the definition but recomputes subproblems, taking exponential time and linear call-stack depth.
- **Memoized recursion:** Caching each `F(k)` reduces time to $O(n)$ but uses $O(n)$ cache and stack space.
- **Full bottom-up table:** Store values from `F(0)` through `F(n)`. It is correct and linear but retains entries that the next transition no longer needs.
- **Fast doubling or matrix exponentiation:** These methods compute Fibonacci numbers in $O(\log n)$ arithmetic steps. They are useful for huge `n` but more complex than required by this exact optimal branch and constraint.
- **Closed-form formula:** Floating-point rounding can produce incorrect integers for large indices, whereas the recurrence uses exact integer arithmetic.
- **`n = 0`:** No loop iteration occurs, and initialized `a = 0` is returned.
- **`n = 1`:** One simultaneous update returns one.
- **Update order:** Sequentially overwriting `a` before calculating `b` is incorrect unless the old value is saved. Python tuple assignment handles this safely.
- **No off-by-one adjustment:** Running exactly `n` iterations and returning the first pair component follows directly from the stated invariant.
