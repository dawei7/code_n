# Guided Example: Average Value of Even Numbers That Are Divisible by Three

## 1. The Instance We Will Trace

- **Input:** `nums = [1, 3, 6, 10, 12, 15]`
- **Required output:** `9`

We must average the integers that are *both* even *and* divisible by $3$, then round that average down to an integer. This instance is chosen because it contains a value that is divisible by $3$ but odd ($3$ and $15$), a value that is even but not divisible by $3$ ($10$), and exactly two values that satisfy both tests ($6$ and $12$), so the intersection of the two conditions is visible and non-trivial.

## 2. The Selection Predicate Collapses to One Test

An integer $x$ qualifies when $x \equiv 0 \pmod 2$ and $x \equiv 0 \pmod 3$ simultaneously. Since $2$ and $3$ are coprime, the Chinese remainder situation is degenerate: a number divisible by both is divisible by their least common multiple,

$$
\operatorname{lcm}(2, 3) = 6 ,
$$

and conversely every multiple of $6$ is divisible by both $2$ and $3$. Hence

$$
x \ \text{qualifies} \iff x \equiv 0 \pmod 6 .
$$

The two conditions are not independent filters to be applied one after the other with an "or" anywhere; they intersect, and the intersection is a single arithmetic progression. The table below makes the collapse explicit for the first twelve positive integers, marking divisibility by $2$ in the first column and divisibility by $3$ in the first row.

| | $x \equiv 0 \pmod 3$ | $x \not\equiv 0 \pmod 3$ |
|---|---|---|
| $x \equiv 0 \pmod 2$ | qualifies: $6, 12, 18, \dots$ | even only: $2, 4, 8, 10, \dots$ |
| $x \not\equiv 0 \pmod 2$ | divisible by $3$ only: $3, 9, 15, \dots$ | neither: $1, 5, 7, 11, \dots$ |

Only one of the four cells qualifies, and it is exactly the multiples of $6$. This is the whole content of the problem's selection step; everything else is bookkeeping.

## 3. The Aggregate State and the Single Pass

The two quantities that must be accumulated are the **sum** $S$ of the qualifying values and the **count** $k$ of qualifying values. Their ratio is the required average, and nothing else about the input is needed. Both start at zero and are updated in one left-to-right pass:

| step | index | $\text{nums}[i]$ | even? | divisible by $3$? | multiple of $6$? | $S$ after | $k$ after |
|---|---|---|---|---|---|---|---|
| 1 | 0 | $1$ | no | no | no | $0$ | $0$ |
| 2 | 1 | $3$ | no | yes | no | $0$ | $0$ |
| 3 | 2 | $6$ | yes | yes | yes | $6$ | $1$ |
| 4 | 3 | $10$ | yes | no | no | $6$ | $1$ |
| 5 | 4 | $12$ | yes | yes | yes | $18$ | $2$ |
| 6 | 5 | $15$ | no | yes | no | $18$ | $2$ |

The final state is $S = 6 + 12 = 18$ with $k = 2$, so the average is

$$
\frac{S}{k} = \frac{18}{2} = 9,
$$

an exact integer, and the expected output is $9$. Note where the two rejected boundary cases fall: $3$ and $15$ pass the divisibility test but fail the parity test, while $10$ passes parity and fails divisibility. A single test of divisibility by $6$ agrees with the conjunction on every row, which is the practical payoff of the collapse in Section 2.

## 4. Rounding Down Is Not Rounding to Nearest

The statement defines the average of $n$ elements as their sum divided by $n$, **rounded down** to the nearest integer. The returned value is therefore

$$
\left\lfloor \frac{S}{k} \right\rfloor ,
$$

the floor of the exact rational average, not the nearest integer and not a truncated decimal. Three instances separate these rules.

| input | qualifying values | $S$ | $k$ | exact average $S/k$ | floor | nearest integer | returned |
|---|---|---|---|---|---|---|---|
| `[1, 3, 6, 10, 12, 15]` | $6, 12$ | $18$ | $2$ | $9$ | $9$ | $9$ | $9$ |
| `[6, 6, 6, 12]` | $6, 6, 6, 12$ | $30$ | $4$ | $7.5$ | $7$ | $8$ | $7$ |
| `[996, 999, 1000, 6]` | $996, 6$ | $1002$ | $2$ | $501$ | $501$ | $501$ | $501$ |

The middle row is decisive: the exact average is $7.5$, and the required answer is $7$. Rounding to nearest would return $8$ and fail. The denominator is $k$, the number of *qualifying* values, not `nums.length`; in the traced instance that distinction is the difference between $18/2 = 9$ and $18/6 = 3$.

Because the constraints guarantee $\text{nums}[i] \ge 1$, every qualifying value is positive, so the floor of $S/k$ coincides with the integer quotient of $S$ by $k$ and no sign correction is needed.

## 5. The Invariant and Why the Method Is Correct

**Accumulation invariant.** After the first $t$ elements have been read, $k$ equals the number of indices $i < t$ with $\text{nums}[i] \equiv 0 \pmod 6$, and $S$ equals the sum of the values at exactly those indices.

*Proof by induction on $t$.* For $t = 0$ both quantities are $0$ and the claim is vacuous. Assume it holds for $t-1$. When element $\text{nums}[t-1]$ is read, it is added to $S$ and counted in $k$ precisely when it is a multiple of $6$, and otherwise both are left untouched. Either way the two updates keep the stated correspondence, so the claim holds at $t$.

**Correctness of the selection.** By Section 2, "multiple of $6$" is equivalent to "even and divisible by $3$", so the elements counted by $k$ are exactly the elements the statement asks us to average. The invariant therefore identifies $k$ with the true number of admissible elements and $S$ with their true sum, so $S/k$ is the true average and $\lfloor S/k \rfloor$ is the required rounded-down value. Nothing about element order, duplicates, or magnitude enters the argument; only membership in the progression of multiples of $6$ matters, and each element is tested once and counted once.

**The empty case.** If $k = 0$ there is no admissible element and the average is undefined; the statement prescribes the answer $0$ for exactly this situation. Returning $0$ before forming a ratio also avoids the division by zero that the formula would otherwise attempt.

## 6. Boundaries and Traps This Problem Exposes

| situation | concrete instance | outcome and the trap it exposes |
|---|---|---|
| No qualifying element | `[1, 2, 4, 7, 10]` | Answer $0$. Every value is odd or fails divisibility by $3$; the prescribed $0$ is a special case, not the average of an empty list. |
| Even but not divisible by $3$ | `[2, 4, 8, 10, 14]` | Answer $0$. An "even numbers only" filter accepts all five and produces a wrong non-zero average. |
| Divisible by $3$ but odd | `[3, 9, 15, 18]` | Qualifying value is $18$ alone, so the answer is $18$. A "divisible by three" filter sums $45$ and answers $11$. |
| Fractional average | `[6, 6, 6, 12]` | $S = 30$, $k = 4$, exact average $7.5$, answer $7$. Rounding to nearest gives $8$. |
| Exactly one qualifier | `[1, 6, 7]` | Answer $6$: the average of a single element is that element. |
| Singleton without a match | `[1]` | Answer $0$, and no division is performed. |
| Repeated qualifiers | `[6, 6, 6, 12]` | Each occurrence is counted separately; deduplicating the input would change both $S$ and $k$. |
| Values at the upper bound | `[996, 999, 1000, 6]` | $996 = 6 \cdot 166$ and $6$ qualify; $999$ is odd and $1000$ is not a multiple of $6$. Answer $501$. |
| Sum magnitude | any input | With at most $1000$ elements of value at most $1000$, $S \le 10^6$; no overflow concern arises, and no accumulator can grow unexpectedly. |
| Positivity of the input | any input | All values are positive, so flooring equals taking the integer quotient. With negative values the two would differ, and the floor would have to be computed deliberately. |

## 7. Alternative Methods and Their Trade-offs

| method | time | auxiliary space | trade-off |
|---|---|---|---|
| Single pass accumulating $S$ and $k$ (derived above) | $O(n)$ | $O(1)$ | One divisibility test per element and two scalars of state; no element is stored and the answer is formed once at the end. |
| Build a filtered list, then sum it | $O(n)$ | $O(k)$ | Easier to inspect while debugging, but it materializes data that the aggregate already summarizes. |
| Sort, then scan the multiples of $6$ | $O(n \log n)$ | $O(n)$ | Ordering is irrelevant to a sum and a count, so the logarithm buys nothing. |
| Histogram of value frequencies, then weighted sum over the multiples of $6$ | $O(n + V)$ | $O(V)$ where $V$ is the value range | Useful if the same array were queried many times with different predicates, since each query becomes a pass over the frequency table; for one query it is strictly more work and more memory. |
| Test parity and divisibility as two separate conditions | $O(n)$ | $O(1)$ | Equivalent, but it performs two tests instead of one and obscures the fact that the conjunction is a single arithmetic progression. |
| Test divisibility by $6$ through repeated subtraction | $O(n \cdot V/6)$ | $O(1)$ | Correct but needlessly slow; the modulo operation answers the same question in constant time. |

## 8. Complexity Derivation

Let $n = \texttt{nums.length}$.

- **Scanning.** Each element is read once and subjected to one constant-time divisibility test, so the pass costs $O(n)$ time with no dependence on the magnitudes of the values.
- **Accumulation.** Each element adds at most one term to $S$ and one unit to $k$: two constant-time updates, already counted inside the pass.
- **Finalization.** One division and one floor, $O(1)$.

The total running time is $\Theta(n)$, and the lower bound is genuine: an element that is never examined could be a multiple of $6$, so every element must be read at least once.

For auxiliary space, the method holds one sum and one counter regardless of $n$ — the running state is a constant number of machine integers — so it needs $O(1)$ auxiliary memory. The only quantity that grows with the input is the input itself, which is given. This is why the single-pass formulation is the right shape for this problem: the answer depends only on two aggregates, and both of them can be maintained in constant space.
