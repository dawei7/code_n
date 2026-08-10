## General

Every entry in `daysLate` represents a separate returned book. Its fee depends only on that book's own number of late days, and the requested answer is the sum of all individual fees. There is no interaction between books, no shared threshold across the array, and no discount based on the final total.

The fee for one delay $x$ is the piecewise function

$$
f(x)=
\begin{cases}
1, & x=1,\\
2x, & 2\le x\le 5,\\
3x, & x>5.
\end{cases}
$$

The exact Optimal source defines this rule as a local helper `f` and then sums `f(x)` for every array element.

**Handling the exceptional one-day rule first**

The helper begins with:

`if x == 1:`

`    return 1`

One day late is a special fixed fee of one. It must not fall through to the ordinary $2x$ rule, which would incorrectly charge two.

The equality check is exact. It does not say `x <= 1` because the constraints already guarantee every delay is at least one, and the stated exceptional case is specifically $x=1$.

**Handling delays above five days**

The next branch is:

`if x > 5:`

`    return 3 * x`

The strict comparison places $6$ and all larger delays in the highest-rate bracket while leaving $5$ in the middle bracket. This boundary is a common source of off-by-one errors: the statement says $2 \le x \le 5$ for the doubled fee and $x>5$ for the tripled fee.

**Using the remaining constraints for the middle bracket**

If neither earlier branch returns, `x` is not one and is not greater than five. Since the contract guarantees $x\ge1$, the only remaining possibilities are $2,3,4,5$. The helper can therefore finish with:

`return 2 * x`

No additional comparison is needed. The order of the branches partitions every legal input into exactly one fee category.

For the boundary values, the helper returns:

- $f(1)=1$;
- $f(2)=4$;
- $f(5)=10$; and
- $f(6)=18$.

These four checks capture both transitions between fee brackets.

**Adding independent book fees**

The method returns:

`sum(f(x) for x in daysLate)`

The generator visits the delays one at a time, applies the complete piecewise rule, and supplies each fee to `sum`. Python's `sum` begins from zero and accumulates all generated fees.

For `daysLate = [5, 1, 7]`:

- `f(5)` uses the middle branch and returns $10$;
- `f(1)` uses the special first branch and returns $1$;
- `f(7)` uses the greater-than-five branch and returns $21$.

Their total is $10+1+21=32$.

The expression uses a generator rather than a list comprehension. Individual fees are consumed immediately, so there is no separate array of penalties.

**Why summing local fees gives the required total**

Let the delays be $d_0,d_1,\ldots,d_{n-1}$. The statement defines each book's penalty independently as $f(d_i)$ and asks for the total penalty for all books. By definition, that total is

$$
\sum_{i=0}^{n-1} f(d_i).
$$

The helper returns the exact applicable branch of $f$ for every legal $d_i$, and the generator supplies every array position to the sum exactly once. Consequently, each required fee is included once, no unrequested fee is introduced, and the returned sum is the stated total.

There is no reason to sort the delays. Addition is independent of order, and each fee uses only its own delay. There is also no need to count how many books fall into each bracket unless one wants an alternative aggregation style; direct evaluation is simpler and already linear.

**Why the source structure is useful**

Keeping the piecewise decision in `f` separates two responsibilities:

- `f` translates one number of late days into one penalty;
- the outer generator aggregates those penalties across all books.

This mirrors the mathematical definition and makes the two threshold boundaries visible. The helper is local to `lateFee` because it is not needed elsewhere and captures no changing state.

## Complexity detail

Let $n$ be `len(daysLate)`.

The generator evaluates `f` once for each of the $n$ entries. The helper performs at most two comparisons and one multiplication, all constant-time operations for values bounded by $100$. The sum performs one addition per fee. Total running time is $O(n)$.

Every entry must be considered because changing any single unseen delay changes its individual fee and therefore may change the total. The linear scan is asymptotically optimal.

The generator does not materialize a fee list. At any point, the method stores the current delay, its fee, and the running total maintained by `sum`. The local helper has no persistent per-call collection. Auxiliary space is $O(1)$.

The maximum fee for one permitted delay is $3\cdot100=300$, and there are at most $100$ books, so the maximum total is $30{,}000$. Python handles it directly; it also fits comfortably in a standard 32-bit signed integer.

## Alternatives and edge cases

- **Explicit loop with an accumulator:** A loop that selects a branch and adds to `total` is equally $O(n)$ and may be more verbose. The generator-plus-helper source expresses the same scan compactly.
- **List comprehension before summing:** `sum([f(x) for x in daysLate])` returns the same result but allocates $O(n)$ temporary space. The generator keeps auxiliary space constant.
- **Sort by lateness:** Sorting does not help because fee calculation is independent for every book and addition ignores order. It would unnecessarily increase time to $O(n \log n)$.
- **Delay exactly one:** This must return a fixed fee of $1$, not $2x$. The first branch handles the exception.
- **Delay exactly five:** Five belongs to the inclusive middle interval, so its penalty is $10$, not $15$.
- **Delay exactly six:** Six satisfies `x > 5` and begins the tripled-rate interval, producing $18$.
- **Repeated delays:** Each array position represents a separate book, so equal delays contribute equal fees repeatedly; they must not be deduplicated.
- **One book:** The generator produces one fee, and `sum` returns it unchanged.
- **Positive-delay guarantee:** A zero or negative delay is outside the contract. The helper's final branch relies on legal remaining values being between two and five.
- **No cumulative bracket:** Ten books each one day late cost ten in total. Their delays are not combined into ten days before applying the fee rule.
