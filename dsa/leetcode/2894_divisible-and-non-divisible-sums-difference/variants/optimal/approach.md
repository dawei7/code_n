## General

**Combine two sums into one signed contribution.** The desired result is

$$
\texttt{num1}-\texttt{num2}.
$$

Every integer from one through $n$ belongs to exactly one of the two sets. A number not divisible by $m$ contributes positively through `num1`. A number divisible by $m$ contributes negatively because `num2` is subtracted. Therefore the answer can be accumulated directly:

$$
\sum_{i=1}^{n}
\begin{cases}
i, & m\nmid i,\\
-i, & m\mid i.
\end{cases}
$$

The exact source expresses this with a generator:

`sum(i if i % m else -i for i in range(1, n + 1))`.

**How the conditional expression works.** `i % m` is the remainder after dividing `i` by `m`. A zero remainder means divisibility. In Python, zero is false in a condition and every nonzero integer is true.

Thus:

- when the remainder is nonzero, `i if i % m else -i` chooses `i` and adds the number;
- when the remainder is zero, it chooses `-i` and subtracts the number.

This compact truthiness use is equivalent to writing `if i % m != 0` explicitly.

**Why `range(1, n + 1)` has the correct endpoints.** Python ranges include the start and exclude the stop. Starting at one omits zero, which is outside the problem interval. Stopping at `n + 1` includes $n$. Every required integer is visited exactly once.
Let $A$ be numbers in $[1,n]$ not divisible by $m$, and $B$ be the divisible numbers. The loop contributes $+i$ for every $i\in A$ and $-i$ for every $i\in B$. Since $A$ and $B$ are disjoint and cover the whole interval, the final total is

$$
\sum_{i\in A}i-\sum_{i\in B}i
=\texttt{num1}-\texttt{num2}.
$$

No number is skipped or counted in both roles.

**Trace `n=10, m=3`.** Values one, two, four, five, seven, eight, and ten contribute positively for a total of 37. Values three, six, and nine contribute negatively for a total subtraction of 18. The generator's signed sum is `37 - 18 = 19`.

For `m=1`, every remainder is zero, so every number is negated. The result is the negative triangular sum, `-n(n+1)/2`, matching the third example.

For `m>n`, no positive number in the range is divisible by `m`. Every contribution is positive and the result is the full sum from one through $n$.

**The generator is lazy.** It does not construct a list of all $n$ signed integers. `sum` requests one contribution at a time and updates its running total. This keeps auxiliary storage constant even though the scan is linear.

**The exact source is not the manifest's constant-time formula.** The editorial includes both traversal and mathematical approaches. The protected file contains the traversal generator. It calculates a remainder for every number, so its real time complexity is $O(n)$ rather than $O(1)$. The manifest summary and bounds describe the arithmetic-series alternative, not what executes.

The direct scan is still easily fast enough for the stated `n <= 1000` constraint and is straightforward to verify. Accuracy requires naming its actual cost.

**One accumulator avoids storing either set.** The definition names `num1` and `num2`, but the function never needs the actual lists of divisible and non-divisible values. Membership of `i` is decided once, its signed effect is added immediately, and `i` can be forgotten. This explains both the constant auxiliary space and why no sorting or hash set appears.

For a smaller trace with `n=5, m=2`, the generated contributions are `+1, -2, +3, -4, +5`. Their running totals are one, negative one, two, negative two, and finally three. Separately, non-divisible values sum to nine and divisible values sum to six, so `9 - 6 = 3`. The matching totals illustrate that signing each element is algebraically identical to constructing two sums.

**Modulo is the only classification rule.** A value's size relative to `m` is insufficient: numbers larger than `m` may or may not be divisible. The remainder test handles every multiple, including `m` itself and `q*m` for larger $q$, without precomputing those multiples.

## Complexity detail

`range` and the generator are lazy. There are $n$ iterations, each performing a modulo, conditional selection, and addition, so time is $O(n)$. `sum` stores only a running integer, the generator stores current iteration state, and no $n$-element list is built; auxiliary space is $O(1)$.

The manifest's $O(1)$ time does not match this exact solution. Python integers safely hold the modest result; fixed-width languages also fit the given constraints comfortably.

## Alternatives and edge cases

- **Arithmetic formula:** Let $q=\lfloor n/m\rfloor$. The total sum is $n(n+1)/2$, and divisible numbers sum to $m q(q+1)/2$. Return $n(n+1)/2-mq(q+1)$ in genuine $O(1)$ time and space.
- **Two separate accumulators:** Compute `num1` and `num2` independently, then subtract. It is correct but stores more state and still takes $O(n)$ time.
- **`m = 1`:** Every number is divisible, so the answer is the negative total sum.
- **`m > n`:** No number is divisible, so the answer is the positive total sum.
- **`n = 1`:** The conditional handles whether one is divisible without special branching.
- **Truthiness:** Zero remainder selects `-i`; nonzero remainder selects `+i`.
- **Inclusive upper bound:** `n + 1` is necessary because Python's range stop is excluded.
- **Manifest mismatch:** Constant time belongs to the formula alternative, while the checked-in generator is linear.
