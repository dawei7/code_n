## General

**Search for the first integer whose square is too large**

For a non-negative integer `x`, the desired result is the unique integer $a$ satisfying

$$
a^2 \le x < (a+1)^2.
$$

Equivalently, the integers begin with a feasible region whose squares do not exceed `x`, followed by an infeasible region whose squares are larger. This implementation advances binary search until `left` becomes the first infeasible integer. It then returns `left - 1`, the last feasible integer and therefore the floor square root.

Values zero and one are handled immediately. Their floor square roots equal the values themselves, and the later search interval `[1, x // 2]` would be empty or unsuitable for them. For every `x >= 2`, the answer is at least one and at most `x // 2`. The upper bound is exact enough for `x == 2`, and for larger values a positive integer square root is always no more than half of `x`.

**Interpret the loop boundaries**

The loop uses an inclusive candidate interval `[left, right]`. Values strictly below `left` have already been proved feasible. Values strictly above `right` have already been proved infeasible. Candidates inside the interval have not yet been classified.

The midpoint `left + (right - left) // 2` is the lower middle. Writing it as an offset from `left` is the standard fixed-width-safe form: unlike `(left + right) // 2`, it does not require adding two potentially large positive endpoints before division. Python would not overflow either expression, but the form preserves the robust binary-search habit.

If the midpoint is too large, `right = mid - 1` classifies `mid` and everything above it as infeasible. Otherwise, `left = mid + 1` classifies `mid` and everything below it as feasible. Both updates exclude `mid`, so the inclusive unknown interval strictly shrinks regardless of which middle is selected.

**Avoid a potentially overflowing square**

Rather than computing `mid * mid`, the code tests `mid > x / mid`. For a positive midpoint, this is mathematically equivalent to $\texttt{mid}^2>x$. Avoiding the product matters when the same algorithm is translated to a language whose integer type can overflow.

In this Python source, `/` performs floating-point division. Under the given bound $x \le 2^{31}-1$, binary64 precision is ample to distinguish the relevant integer boundary, so the comparison behaves as intended. An all-integer expression `mid > x // mid` would communicate the floor-boundary reasoning more directly and avoid depending on floating-point precision; it is the safer general form for larger arbitrary-precision inputs.

The midpoint is never zero in this loop because `left` starts at one. Consequently `x / mid` cannot divide by zero.

**Trace both kinds of midpoint**

For `x = 8`, the search begins at `[1, 4]`. Midpoint 2 is feasible because $2 \le 8/2$, so `left` becomes 3. Midpoint 3 is infeasible because $3 > 8/3$, so `right` becomes 2. The loop ends with `left == 3` and `right == 2`. Returning `left - 1` gives 2.

For a perfect square such as `x = 9`, midpoint 2 is feasible and later midpoint 3 is also feasible because the comparison is strict: $3 > 9/3$ is false. The search advances past 3. The first infeasible value is 4, so the returned predecessor is exactly 3.

**Why `left - 1` is guaranteed to be the answer**

At the start of every iteration, every integer below `left` is feasible and every integer above `right` is infeasible. Each comparison preserves this invariant by moving a classified midpoint to the appropriate outside region. The loop stops when `left > right`, meaning no unclassified candidates remain.

At that moment, `left` is the smallest value in the known infeasible region, while `right`, which equals `left - 1`, is the largest value in the known feasible region. The feasibility transition occurs exactly after $\lfloor\sqrt{x}\rfloor$, so `left - 1` is the requested answer. This boundary proof covers both perfect squares and values between squares; an explicit equality branch is unnecessary.

**Why the algorithm respects the problem restriction**

The implementation uses comparison, division, addition, subtraction, and integer halving. It never calls a square-root routine, exponent function, or exponent operator. It computes the root from the monotone ordering of integer candidates rather than approximating a real square root and rounding it afterward.

## Complexity detail

For `x >= 2`, the initial interval has at most `x // 2` candidates. Each iteration discards at least half of the current unknown interval, giving $O(\log x)$ iterations. Under the conventional constant-width arithmetic model for the stated 32-bit constraint, each iteration costs constant time, so total time is $O(\log x)$ as declared by the manifest. The constant-time returns for zero and one also satisfy this upper bound.

The implementation stores only the two boundaries and one midpoint. It is iterative, does not allocate a candidate array, and has no recursive call stack. Auxiliary space is therefore $O(1)$.

## Alternatives and edge cases

- **Integer quotient comparison:** Replace `x / mid` with `x // mid`. It avoids floating-point conversion and is the preferred exact form while retaining overflow safety.
- **Multiply and compare:** `mid * mid <= x` is very readable in Python, whose integers grow as needed, but direct translation can overflow a 32-bit or 64-bit product.
- **Closed interval returning `right`:** The same updates leave `right` as the last feasible value at termination, so returning `right` is equivalent to returning `left - 1`.
- **Upper-middle converging bounds:** Keep the answer inside `[l, r]`, use an upper midpoint, and update `l = mid` when feasible. It returns the meeting endpoint but requires careful midpoint bias to avoid an infinite loop.
- **Newton's method:** It usually needs fewer iterations, but proving integer convergence and choosing a safe stopping rule adds conceptual complexity.
- **`x < 2`:** The early return is necessary for the chosen `[1, x // 2]` initial interval.
- **`x == 2`:** The only candidate is one; it is feasible, and the returned predecessor boundary is one.
- **Perfect square:** Equality is classified as feasible because the too-large comparison uses `>`, not `>=`.
- **Value between squares:** The first too-large integer is one greater than the desired floor root.
- **Maximum constrained value:** The comparison avoids forming a potentially overflowing square, and binary search uses only logarithmically many iterations.
- **Floating precision scope:** The selected `/` comparison is reliable for this 32-bit domain, but an integer quotient is necessary for a solution intended to scale without that constraint.
- **No built-in exponentiation:** Even though a language library could compute a real square root quickly, using it would violate the explicit contract and could introduce rounding corrections.
