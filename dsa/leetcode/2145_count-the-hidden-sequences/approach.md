## General

Once the first hidden value is chosen, every later value is forced by the differences. The algorithm therefore does not generate many sequences separately. It constructs the shape of one representative sequence relative to a starting value of zero, finds that shape’s vertical span, and counts how many integer shifts fit inside the allowed interval.

**Build prefix offsets rather than absolute values**

Let the first hidden value be $h$. Define prefix offsets by $p_0=0$ and $p_{i+1}=p_i+\texttt{differences}[i]$. Then every hidden element is $\texttt{hidden}[i]=h+p_i$.

This formula automatically preserves every required consecutive difference because

$$
(h+p_{i+1})-(h+p_i)=p_{i+1}-p_i=\texttt{differences}[i].
$$

The exact loop stores the current prefix offset in `x`. It initializes `x = mi = mx = 0` so that the first sequence offset $p_0=0$ is included. For every difference `d`, it performs `x += d`, then updates `mi = min(mi, x)` and `mx = max(mx, x)`.

No other property of all prefix offsets is needed. Shifting by $h$ preserves their relative positions, so only the smallest and largest determine whether the complete sequence fits.

**Translate all element bounds into one interval for h**

Every hidden value must be at least `lower`. The tightest lower constraint comes from the smallest offset:

$$
h+mi\ge lower,
$$

so $h\ge lower-mi$.

Every hidden value must also be at most `upper`. The tightest upper constraint comes from the largest offset:

$$
h+mx\le upper,
$$

so $h\le upper-mx$.

Therefore valid first values are exactly the integers in the inclusive interval $[lower-mi,\;upper-mx]$. Its integer count is

$$
(upper-mx)-(lower-mi)+1
=(upper-lower)-(mx-mi)+1.
$$

This is the expression returned by the exact solution.

**Interpret the span**

The quantity `mx - mi` is the width required by the forced sequence shape. The allowed range has width `upper - lower`. If the required shape is wider, no shift can fit. If it fits, the leftover width tells how far the shape may slide, and adding one counts both endpoints.

The call `max(calculated_count, 0)` handles the impossible case without a separate early return. A negative raw count means the valid-start interval is empty.

For `differences = [1,-3,4]`, the offsets are $0,1,-2,2$. Thus `mi = -2` and `mx = 2`, giving span four. The allowed interval from one through six has width five, so the number of shifts is $5-4+1=2$. Choosing $h=3$ gives `[3,4,1,5]`, and choosing $h=4$ gives `[4,5,2,6]`.

**Why counting first values counts sequences**

Each possible first value $h$ produces exactly one sequence because every next value is fixed by its difference. Different first values produce different sequences because their first elements differ. Conversely, every valid hidden sequence has some first value satisfying the derived interval. The mapping between valid $h$ values and valid sequences is one-to-one, so counting the interval gives the desired answer.

**Why intermediate prefix values matter**

Checking only the final cumulative difference is insufficient. The sequence may temporarily go below `lower` or above `upper` even if its first and last values fit. Tracking both `mi` and `mx` across every prefix captures every intermediate constraint simultaneously.

**Why only the span remains in the final formula**

Moving the representative sequence upward by one increases every hidden element by one but leaves all differences unchanged. The absolute values of `mi` and `mx` merely shift the valid starting interval; its length depends only on their difference. This is why the count simplifies to the allowed width minus the required span plus one.

## Complexity detail

Let $n$ be the length of `differences`. The loop visits each entry once and performs constant-time addition and comparisons, so time is $O(n)$.

Only `x`, `mi`, and `mx` are maintained regardless of input length. The bounds and return expression also use scalar integers. Auxiliary space is $O(1)$.

Prefix sums may be as large as the sum of absolute differences, but Python integers expand as needed and do not overflow under the legal constraints.

## Alternatives and edge cases

- **Store every prefix offset:** Building the representative sequence in a list and then taking its minimum and maximum is correct but uses $O(n)$ space instead of the exact constant-space scan.
- **Try every starting value:** There can be up to 200,001 candidates, and validating each would repeat the same prefix work. The interval derivation counts all candidates at once.
- **Check only total difference:** A path can leave the allowed range in the middle and later return. Minimum and maximum prefix offsets are both necessary.
- **Early impossibility check:** The editorial may return as soon as `mx - mi > upper - lower`. The exact source finishes the scan and clamps the final count to zero; both are correct.
- **All zero differences:** Every offset is zero, so each allowed starting integer gives a constant valid sequence. The count is `upper - lower + 1`.
- **Single allowed value:** When `lower == upper`, a valid sequence exists only if every prefix offset is identical, meaning every hidden element stays at that value.
- **Negative differences:** They lower `x` and may update `mi`; no special case is needed.
- **Positive differences:** They may update `mx` symmetrically.
- **Alternating differences:** Even when the final offset returns to zero, the intermediate span controls feasibility.
- **Exact fit:** If `mx - mi == upper - lower`, exactly one shift fits, and the formula returns one.
- **Span too wide:** The raw formula is nonpositive and `max(..., 0)` returns zero.
- **Inclusive endpoints:** The final `+ 1` is required because both the smallest and largest valid starting values count.
- **Initial offset zero:** Initializing `mi` and `mx` to zero includes `hidden[0]`. Starting them only from the first accumulated difference could miss the first element’s constraint.
- **Input preservation:** The solution only reads `differences` and never constructs or modifies a hidden sequence array.
