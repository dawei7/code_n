## General

The active competitive `getRow` method also uses one output list, but it updates from left to right. To avoid destroying previous-row information, it carries one old value in the scalar `old`.

The file includes `getRow2`, `getRow3`, and a separate `Solution2`, but the platform entry point is `Solution.getRow`. Those alternatives do not run as part of the selected method.

**Initial storage and row progression**

For `rowIndex = k`, `result` is allocated with $k+1$ zeros. The outer loop runs `i = 0` through `k`, constructing rows in order.

Before row `i`, positions zero through `i - 1` contain row `i - 1`, while position `i` and later positions remain zero. The line `old = result[0] = 1` establishes the current row's left boundary and initializes `old` to the previous row's position-zero value, which is also one.

The inner loop then calculates positions one through `i`. Including `j = i` is important: old row `i - 1` has no position `i`, represented by the preallocated zero, so adding its last one produces the new right boundary one.

**What `old` means during the inner loop**

Immediately before processing position `j`:

- `old` holds the previous row's value at position `j - 1`;
- `result[j]` still holds the previous row's value at position `j`, or zero when `j` is the new boundary;
- positions left of `j` already contain current-row values; and
- positions at and to the right still contain previous-row values.

The update

`old, result[j] = result[j], old + result[j]`

uses Python's simultaneous assignment. Both right-hand expressions are evaluated before either left-hand target is rebound.

Therefore new `old` saves the previous `result[j]`, while new `result[j]` becomes previous-left plus previous-current. That is exactly Pascal's recurrence. The saved value is ready to be the previous-left input for `j + 1`.

**Why tuple assignment order matters**

If the source assigned `result[j] = old + result[j]` and then `old = result[j]`, `old` would receive the new current-row value rather than the old value. The next position would be calculated from contaminated state.

One could save `result[j]` in a temporary variable explicitly. Python's tuple assignment performs that preservation compactly.

**Why the algorithm handles both boundaries**

The left boundary is forced to one before the inner loop. For the right boundary at `j = i`, `old` holds the prior row's last value one and `result[i]` is still zero. Their sum is one.

Interior positions receive the sum of the two values above. Thus the same inner statement handles every non-left position, including the new right edge.

**Establishing correctness row by row**

For `i = 0`, `result[0]` becomes one and the inner loop is empty, giving row zero.

Assume the meaningful prefix contains row `i - 1` before iteration `i`. The left boundary is set correctly. The carry invariant ensures every inner update uses the two appropriate previous-row values despite moving forward. Position `i` becomes the right boundary from one plus zero.

The prefix therefore becomes row `i`. Induction through `i = k` proves that the returned full list is row $k$.

**Tracing row index three**

The allocated state is `[0, 0, 0, 0]`.

Row zero makes it `[1, 0, 0, 0]`. Row one begins with `old = 1`; at `j = 1`, simultaneous assignment saves zero and writes `1 + 0`, giving `[1, 1, 0, 0]`.

Row two writes position one as two, while `old` saves the previous one; position two then becomes `1 + 0 = 1`, giving `[1, 2, 1, 0]`.

Row three produces three at position one, saves old two, produces three at position two, saves old one, and produces one at position three. The result is `[1, 3, 3, 1]`.

**Selection among methods in the file**

`getRow2` builds a new row from two zero-padded versions of the previous row. `getRow3` derives successive rows with an `add` helper. The separate `Solution2.getRow` allocates a new list on every row.

The active method is specifically the fixed-list, forward-carry technique. Its complexity must be measured from its nested loops, not from a different method that might use a combinatorial formula.

## Complexity detail

Let $k$ be `rowIndex`. The inner loop lengths are one, two, through $k$ across the nonzero outer rows. Their sum is

$$
\frac{k(k+1)}{2},
$$

so running time is $\Theta(k^2)$. The source header correctly says $O(n^2)$ under $n=k$; the manifest's $O(k)$ time claim is inaccurate for this method.

`result` contains $k+1$ integers and is the required output, using $\Theta(k)$ output space. Only `i`, `j`, and `old` are additional scalar state, so auxiliary space excluding output is $O(1)$.

The manifest's $O(k)$ space bound matches total returned storage. A claim of $O(1)$ in the source header uses the convention that required output is excluded.

## Alternatives and edge cases

- **Descending in-place update:** Scan right to left so both prior-row inputs remain untouched without an `old` carry.
- **Linear-time combinations:** Generate successive binomial coefficients with exact multiplication and integer division. This meets the manifest's intended $O(k)$ time.
- **Fresh-row construction:** Allocate boundaries and adjacent sums for each row. It is simple but uses additional row storage and remains quadratic time.
- **Zero-padding list comprehension:** `getRow2` expresses a row as elementwise sums of shifted copies, at the cost of new lists each iteration.
- **Full triangle:** Correct but retains all rows, using $O(k^2)$ storage when only one row is needed.
- **Row zero:** One outer iteration sets `result[0]` to one and returns `[1]`.
- **Row one:** The zero at position one combines with carry one to make the right boundary.
- **Simultaneous assignment:** Both right-hand values must be captured before either destination changes.
- **Right boundary:** Preallocated zero acts as the missing above-right value.
- **Left boundary:** Reset to one on each outer iteration.
- **Forward update without carry:** Incorrect because overwritten values contaminate later positions.
- **Output length:** Row $k$ contains exactly $k+1$ coefficients.
- **Alternative methods:** Their existence does not change which source method the judge calls.
- **`getRow3` loop criterion:** It relies on row one's second coefficient equaling the row index; this is an indirect alternative, not active logic.
- **Exact values:** Python integer addition cannot overflow for the legal range.
- **Manifest mismatch:** This nested-loop source is quadratic-time even though a different binomial algorithm can be linear.
