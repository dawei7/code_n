# Guided Example: Find the Pivot Integer

## 1. The equality being asked for and the instance we trace

The official instance traced here is $n = 8$, whose expected answer is $x = 6$. The task is
to find an integer $x$ with $1 \le x \le n$ such that the sum of the integers from $1$ to $x$
inclusive equals the sum of the integers from $x$ to $n$ inclusive:

$$
\sum_{i=1}^{x} i \;=\; \sum_{i=x}^{n} i .
$$

If no such integer exists the answer is $-1$. With $n \le 1000$ the totals are small: the
largest possible sum is $\sum_{i=1}^{1000} i = 500500$, so every value fits comfortably in
ordinary integer arithmetic.

There is one detail in the statement that decides the whole solution: the pivot $x$ appears
on **both** sides. It is the last term of the left sum and the first term of the right sum,
so it is counted twice when the two sides are added together. Everything else follows from
that double count.

| Quantity | Definition | Value for $n = 8$ |
|:---|:---|:---:|
| $T(n)$ | the total $\sum_{i=1}^{n} i = \dfrac{n(n+1)}{2}$ | $36$ |
| $P(x)$ | the prefix $\sum_{i=1}^{x} i = \dfrac{x(x+1)}{2}$ | depends on $x$ |
| $S(x)$ | the suffix $\sum_{i=x}^{n} i = T(n) - T(x-1)$ | depends on $x$ |
| pivot condition | $P(x) = S(x)$ | holds at $x = 6$ |
| double-count identity | $P(x) + S(x) = T(n) + x$, because $x$ is counted twice | $21 + 21 = 36 + 6$ |

## 2. Worked trace of the instance $n = 8$

The table below evaluates the condition literally, one candidate at a time. The prefix is the
running sum from the left, the suffix is the running sum from the right, and the two columns
meet only at $x = 6$.

| Candidate $x$ | $P(x) = 1 + \dots + x$ | $S(x) = x + \dots + 8$ | $P(x) = S(x)$? | $x^{2}$ | $x^{2} = T(8) = 36$? |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | $1$ | $36$ | no | $1$ | no |
| 2 | $3$ | $35$ | no | $4$ | no |
| 3 | $6$ | $33$ | no | $9$ | no |
| 4 | $10$ | $30$ | no | $16$ | no |
| 5 | $15$ | $26$ | no | $25$ | no |
| 6 | $21$ | $21$ | **yes** | $36$ | **yes** |
| 7 | $28$ | $15$ | no | $49$ | no |
| 8 | $36$ | $8$ | no | $64$ | no |

The equality holds at $x = 6$, where both sides equal $21$, so the answer is $6$. The last two
columns already hint at the simplification derived next: the equality column and the
perfect-square column turn true at exactly the same candidate. That is not a coincidence.

## 3. Deriving the closed-form condition

The literal condition is a statement about two sums, but it collapses to a statement about a
single square. The derivation uses only the triangular-number formula and one cancellation.

| Step | Statement | Why it is valid |
|:---:|:---|:---|
| 1 | $P(x) = S(x)$ | the defining condition of a pivot |
| 2 | $\dfrac{x(x+1)}{2} = T(n) - \dfrac{(x-1)x}{2}$ | substitute the two triangular numbers |
| 3 | $x(x+1) = n(n+1) - (x-1)x$ | multiply both sides by $2$ |
| 4 | $x^{2} + x = n^{2} + n - x^{2} + x$ | expand both sides |
| 5 | $2x^{2} = n^{2} + n$ | the $+x$ terms cancel on both sides |
| 6 | $x^{2} = \dfrac{n(n+1)}{2} = T(n)$ | divide by $2$ |

The pivot condition is therefore equivalent to a single equation: **the pivot integer exists
exactly when the triangular number $T(n)$ is a perfect square, and then $x = \sqrt{T(n)}$.**

Two consequences follow immediately and both matter for the implementation. First, uniqueness
is free: a positive number has at most one non-negative square root, so there cannot be two
valid pivots — the statement's uniqueness guarantee is a theorem here, not an extra
condition to enforce. Second, the answer is completely determined by $T(n)$, so the search
over candidates is not really a search over a sum equality but a test of whether
$T(n)$ is a perfect square.

The double count is exactly what makes the equation look surprising. A naive reading would
guess that the pivot splits the total in half, that is $P(x) = T(n)/2$. That guess is wrong,
and the traced instance shows it: $T(8)/2 = 18$, which is not triangular at all, whereas the
true pivot has $P(6) = 21$. The pivot belongs to both halves, which is why the correct
condition is $x^{2} = T(n)$ rather than $P(x) = T(n)/2$.

## 4. Which inputs have a pivot

Because the condition is a perfect-square test on $T(n)$, the inputs with a pivot are exactly
those whose triangular number is a square. They are rare and spaced far apart, and the pattern
below is worth knowing because it explains why so many inputs answer $-1$.

| $n$ | $T(n) = n(n+1)/2$ | $\sqrt{T(n)}$ | Pivot $x$ | Inside the constraint $n \le 1000$? |
|:---:|:---:|:---:|:---:|:---:|
| 1 | $1$ | $1$ | 1 | yes |
| 8 | $36$ | $6$ | 6 | yes |
| 49 | $1225$ | $35$ | 35 | yes |
| 288 | $41616$ | $204$ | 204 | yes |
| 1681 | $1413721$ | $1189$ | 1189 | no, beyond the stated bound |

The pivot inputs satisfy $n_{k+1} = 6n_{k} - n_{k-1} + 2$ and their pivots satisfy
$x_{k+1} = 6x_{k} - x_{k-1}$: for example $6 \cdot 49 - 8 + 2 = 288$ and
$6 \cdot 35 - 6 = 204$. So within $1 \le n \le 1000$ there are exactly four inputs with a
pivot — $1$, $8$, $49$ and $288$ — and every other input, including $287$ and $1000$, must
return $-1$. The neighbouring pair $287 \to 288$ is instructive: consecutive inputs can
differ in outcome, so nothing can be inferred from a neighbouring answer.

## 5. Why the derivation is correct

The correctness argument has two independent directions, and both come from the algebra of
section 3.

> **Soundness.** If $x^{2} = T(n)$ for some integer $x$ with $1 \le x \le n$, then $x$ is a
> pivot.
>
> **Completeness.** If $x$ is a pivot, then $x^{2} = T(n)$.

For soundness, run the derivation of section 3 backwards: $x^{2} = T(n)$ implies
$2x^{2} = n(n+1)$, which rearranges to $x(x+1) = n(n+1) - (x-1)x$, and dividing by $2$ gives
$P(x) = T(n) - T(x-1) = S(x)$, which is the pivot condition. Every rearrangement is an
equivalence — multiplying by $2$, expanding, and cancelling the common term $+x$ — so no
solution is introduced or lost. For completeness, the same chain read forwards turns any
pivot into a solution of $x^{2} = T(n)$.

The bound $1 \le x \le n$ follows from the square root in the allowed range rather than being
an extra case to handle. At $n = 1$ the total is $T(1) = 1 = 1^{2}$, so $x = 1$ is a pivot: the
left sum and the right sum are both simply the single term $1$, which is consistent with $x$
being counted once on each side. For $x < 1$ or $x > n$ one of the two sums would be empty or
ill-defined, so those candidates are not part of the problem's domain. Finally, since
$x^{2} = T(n)$ has at most one non-negative solution, at most one pivot exists for each $n$,
which is exactly the guarantee stated in the problem.

## 6. Boundary and trap analysis

| Situation | Instance | Trap | What actually happens | Outcome |
|:---|:---|:---|:---|:---|
| Smallest input | $n = 1$ | expect the single term to be ambiguous | $T(1) = 1 = 1^{2}$, so the pivot is the only index available | `1` |
| Simple interior pivot | $n = 8$ | split the total in half instead of solving $x^{2} = T(n)$ | $T(8)/2 = 18$ is not triangular; the real pivot is $x = 6$ with both sides equal to $21$ | `6` |
| No pivot, small | $n = 2$ | assume every small input has a pivot | $T(2) = 3$ lies strictly between $1^{2}$ and $2^{2}$ | `-1` |
| No pivot | $n = 4$ | try to force a split of the total $10$ | no integer $x$ satisfies $x^{2} = 10$; the candidate $x = 3$ gives $6$ versus $7$ | `-1` |
| Input just before a pivot | $n = 287$ | infer an answer from the neighbouring pivot input $288$ | $T(287) = 41328$ is not a square; the square root is about $203.3$ | `-1` |
| Large exact pivot | $n = 288$ | distrust the large square root | $T(288) = 41616 = 204^{2}$ exactly | `204` |
| Upper bound | $n = 1000$ | assume a pivot must exist for some large input | $T(1000) = 500500$ lies between $707^{2} = 499849$ and $708^{2} = 501264$ | `-1` |
| Floating-point square root | any pivot input | test the root with a floating-point comparison | for $n = 288$ the root is exactly $204$, but rounding can be off by one for other magnitudes; compare integers, for instance whether $204^{2}$ equals $T(n)$ | exact answer |

The last row is the practical trap. The cleanest formulation avoids the floating-point
question entirely: compute $x$ as an integer square root, then confirm by integer
multiplication that $x^{2}$ equals $T(n)$; if it does not, the answer is $-1$. A scan over
candidate $x$ values with the original sum condition is equally exact and needs no square
root at all, which is why the direct form in section 2 is a perfectly respectable solution.

## 7. Alternatives and why the square test is preferred

| Approach | Idea | Cost | Failure mode or tradeoff |
|:---|:---|:---|:---|
| Scan candidates with running prefix and suffix sums | keep a running left sum and a running right sum and compare them at every $x$ | $O(n)$ time, $O(1)$ space | exact and simple, but recomputes information the closed form settles immediately; the scan also has to update both sums at each step |
| Compare the two triangular formulas at each candidate | test $x(x+1) = n(n+1) - x(x-1)$ for every $x$ in order | $O(n)$ time, $O(1)$ space | avoids incremental sums and stays in integers; still examines up to $n$ candidates when only one can ever qualify |
| Halve the total and search for a triangular half | test whether $T(n)/2$ is triangular | $O(\log n)$ time | wrong in general: it ignores the double count of the pivot, and it already fails on the official instance $n = 8$, where $18$ is not triangular but $x = 6$ is a pivot |
| Compute $T(n)$ and take an integer square root | form $T(n) = n(n+1)/2$, extract its integer square root, and verify the square by multiplication | $O(\log n)$ time for the root, $O(1)$ space | the method derived here: one triangular number, one root, one verification, and no search |
| Binary search on the monotone predicate $x^{2} \le T(n)$ | search the largest $x$ whose square does not exceed $T(n)$, then test equality | $O(\log n)$ time, $O(1)$ space | correct because $x^{2}$ is strictly increasing in $x$; a good alternative when an integer square-root routine is unavailable |

## 8. Complexity: time and auxiliary space

Let $n$ be the input and note that $T(n) = O(n^{2})$, with $T(n) \le 500500$ under the stated
constraint.

**Time.** Forming $T(n)$ costs one multiplication and one division. Extracting the integer
square root of a number of size $O(n^{2})$ costs $O(\log n)$ iterations of the usual
converging integer method, since each iteration roughly halves the number of correct bits;
the subsequent verification is a single multiplication. The total is $O(\log n)$ time, which
for $n \le 1000$ is a handful of operations. The direct scan over candidates is the fallback
with $O(n)$ time: it performs one constant-time arithmetic test per candidate and stops at the
first success, so it is linear in the worst case, and both forms are far inside the limit. The
distinction matters conceptually rather than practically here — the closed form shows that the
answer is determined by a single arithmetic property of $n$ rather than by a search over a
sum equality.

**Auxiliary space.** Both the scan and the square-root form need only a fixed number of integer
variables: the total, the candidate or root, and a comparison result. Auxiliary space is
therefore $O(1)$. No prefix-sum array, table, or set proportional to $n$ is required, because
the equality of two triangular sums can be decided by integer multiplication alone — the whole
problem reduces to one square test.
