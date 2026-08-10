## General

We are counting ordered triples $(a,b,c)$ of nonnegative integers for three labeled children:

$$
a+b+c=n,\qquad a,b,c\le\texttt{limit}.
$$

The upper bounds make some ordinary stars-and-bars solutions invalid. Inclusion–exclusion starts with all solutions and removes precisely those violations.

**Impossible capacity**

No assignment can hold more than $3\cdot\texttt{limit}$ candies. The first branch returns zero when `n > 3 * limit`.

Besides being an early answer, this condition proves that an execution continuing into the formula can never have all three shares greater than `limit`. That observation explains the source's compact three-term expression.

**Unrestricted baseline**

If shares have no upper limit, the number of nonnegative solutions to $a+b+c=n$ is

$$
\binom{n+2}{2}.
$$

The source initializes `ans` to this value. At this stage, distributions with shares above `limit` are still included.

**Bad set for one named child**

For a fixed child, consider assignments with $a\ge\texttt{limit}+1$. Substitute

$$
a'=a-(\texttt{limit}+1)\ge0.
$$

Then $a'+b+c=n-\texttt{limit}-1$, whose number of solutions is

$$
\binom{n-\texttt{limit}+1}{2}.
$$

There are three choices for which child violates the cap. When `n > limit`, the source subtracts three times this count.

**Intersections of two bad sets**

If two children exceed the cap, their assignment was subtracted once for each child, even though it should be removed only once overall. Inclusion–exclusion adds such assignments back.

Choose the excessive pair in three ways. After reserving `limit + 1` candies for each member, the remaining unrestricted distribution count is

$$
\binom{n-2(\texttt{limit}+1)+2}{2}
=
\binom{n-2\texttt{limit}}{2}.
$$

The exact guard `n - 2 >= 2 * limit` is equivalent to $n\ge2(\texttt{limit}+1)$, the smallest total permitting this intersection. The source then adds `3 * comb(n - 2 * limit, 2)`.

**Where is the three-child intersection?**

All three children exceeding the limit would require at least

$$
3(\texttt{limit}+1)=3\texttt{limit}+3
$$

candies. Yet the initial guard allows the formula to execute only for $n\le3\texttt{limit}$. The triple intersection is therefore empty in every continuing case. When $n>3\texttt{limit}$, the valid answer was already returned as zero. No fourth term is missing.

**Accounting proof**

Take any unrestricted distribution:

- If no child violates the cap, it remains in the baseline count.
- If exactly one violates, it is subtracted once and disappears.
- If exactly two violate, it is subtracted twice and added once, so it disappears.
- Three violations cannot occur after the guard.

Thus every legal distribution contributes exactly one and every illegal distribution contributes zero.

For `n=3, limit=3`, no violation is possible, so the answer is $\binom52=10$. For `n=5, limit=2`, the calculation is $\binom72-3\binom42=21-18=3$.

## Complexity detail

The implementation executes a constant number of branches and combination calculations. With ordinary arithmetic treated as constant time, both time and auxiliary space are $O(1)$.

Unlike the editorial's enumeration alternative, the runtime does not grow with $n$ or `limit`. Python computes exact integers, and no modulo is required.

## Alternatives and edge cases

- **Enumerate the first child:** For each legal $a$, count the interval of possible $b$. This costs $O(\min(n,\texttt{limit}))$ time.
- **Two nested loops:** Choosing $a$ and $b$ then deriving $c$ is simple but can take quadratic time in the limit.
- **Generating functions:** The answer is the coefficient of $x^n$ in $(1+x+\cdots+x^{limit})^3$, but inclusion–exclusion evaluates it more directly.
- **Total above capacity:** Return zero; attempting the formula without careful generalized binomial handling could produce meaningless terms.
- **Total equal to capacity:** Only all three shares equal to `limit`, so the result is one.
- **Large limit:** When `limit >= n`, every unrestricted distribution is valid.
- **Children receive zero:** Zero is legal, so the baseline must use nonnegative rather than positive stars and bars.
- **Ordered assignments:** Permutations among children count separately because the recipients are distinct.
- **Pair-intersection boundary:** At $n=2(\texttt{limit}+1)$, exactly enough candies exist to make a selected pair excessive and give zero to the third.
- **No triple term:** Its absence depends on the initial capacity return; moving or removing that guard would require a complete generalized fourth term.
- **Why binomial arguments are shifted:** After reserving mandatory candies, distributing residual amount $r$ among three children contributes $\binom{r+2}{2}$. Substituting $r=n-limit-1$ or $r=n-2(limit+1)$ yields the exact source arguments.
- **No negative combinations:** The two conditions are mathematical existence checks as well as API guards; they prevent asking `comb` to represent a bad set with insufficient candies.
- **Second-version scale:** With inputs up to $10^6$, enumeration may already be expensive, while the exact formula's operation count is unchanged.
- **Exact integer answer:** No probability, approximation, or modular reduction is involved; inclusion–exclusion produces the full count.
