## General

**Separate the universal decrease from the chosen-index bonus**

In every operation, all elements decrease by at least `y`.

The selected index decreases by `x` instead, which can be viewed as:

$$
y+(x-y).
$$

Therefore, after exactly $t$ operations:

- every value receives a baseline decrease of $t\cdot y$;
- each time an index is selected, it receives an additional decrease of $x-y$.

Since $x>y$, the extra decrease is positive.

**Ask whether a proposed operation count is feasible**

Binary search needs a Boolean function `check(t)`:

> Can all values be made non-positive using at most $t$ operations?

After the baseline, an original value $v$ has residual:

$$
v-t y.
$$

If this is already non-positive, that index needs no special selection. The code enters the calculation only when `v > t * y`.

**Required selections for one positive residual**

Each time this index is chosen, its residual decreases by another $x-y$.

The minimum number of choices needed is:

$$
\left\lceil\frac{v-t y}{x-y}\right\rceil.
$$

The helper adds this quantity to `cnt` for every still-positive element.

`cnt` is therefore the total number of operation slots that must choose particular indices.

**Why `cnt <= t` is necessary**

There are only $t$ operations, and each operation chooses exactly one index.

If the summed requirements exceed $t$, there are not enough selections to give every residual the necessary extra decrease. No ordering of operations can overcome that shortage.

Thus `cnt > t` proves infeasibility.

**Why `cnt <= t` is sufficient**

Assign each index exactly its calculated required number of selections. Their total fits within the $t$ available operations.

Any unused selection slots can choose arbitrary indices. Extra decreases never hurt the goal of making values less than or equal to zero.

All indices also receive the same $t y$ baseline regardless of selection order. Therefore a schedule exists whenever the total required selections fits.

**Trace the first example at `t = 3`**

For `nums = [3,4,1,7,6]`, `x = 4`, and `y = 2`, the baseline is six.

Values 3, 4, and 1 are already non-positive after baseline. Value 7 has residual one and needs one extra selection because `x-y=2`. Value 6 needs none.

Total required selections are one, no more than three, so three operations are feasible.

At `t = 2`, the baseline is four. Value 7 needs two selections and value 6 needs one, totaling three slots when only two exist. Thus two operations are infeasible.

**Feasibility is monotone**

If $t$ operations are feasible, any larger number is also feasible.

Increasing $t$ provides more selection slots and increases the baseline decrease on every value. Neither change can make an already feasible instance impossible.

The predicate therefore changes only once from false to true, which is exactly the structure binary search requires.

**Choose safe search bounds**

The lower bound is zero because no negative number of operations exists.

The upper bound is `max(nums)`. Since `y >= 1`, after that many operations the baseline alone is at least every original value:

$$
\max(\texttt{nums})\cdot y\ge\max(\texttt{nums}).
$$

So `check(r)` is guaranteed true, even without focused selections.

**Binary-search the first feasible value**

At each iteration, `mid = (l + r) >> 1`.

If `check(mid)` is true, the answer may be `mid` or smaller, so `r = mid`. Otherwise all counts through `mid` are infeasible, so `l = mid + 1`.

When the bounds meet, every smaller count is false and that count is true. It is the minimum.

**No simulation is necessary**

Operation order looks complicated because one index receives $x$ while all others receive $y$.

The baseline-plus-bonus algebra removes ordering completely. Only the number of times each index is selected matters, and the feasibility sum captures exactly those counts.


For fixed $t$, the ceiling formula is the exact minimum focused selections for each residual. Summing gives a necessary and sufficient feasibility condition because operation slots can be assigned independently and leftover decreases are harmless.

The condition is monotone and the bounds contain at least one feasible value. Standard lower-bound binary search therefore returns the smallest feasible operation count, which is the requested answer.

## Complexity detail

Let $n$ be the array length and $M=\max(\texttt{nums})$. One feasibility check scans all $n$ values in $O(n)$ time. Binary search performs $O(\log M)$ checks, for total time $O(n\log M)$.

The helper stores only counters and arithmetic temporaries, and binary search stores two bounds. Auxiliary space is $O(1)$. `nums` is not modified.

## Alternatives and edge cases

- **Priority-queue simulation:** Repeatedly chooses a largest residual but is slower and obscures the universal `y` contribution.
- **Integer ceiling formula:** `(need + bonus - 1) // bonus` avoids floating division and is an equivalent implementation.
- **Already feasible at zero:** Input values are positive, so this does not occur under current constraints.
- **One element:** Every operation selects it, and the formula still reduces to repeated decrease by `x`.
- **`x` only slightly larger than `y`:** Bonus is small, so more focused selections may be required.
- **Large `y`:** Baseline quickly makes many indices require zero selections.
- **Residual exactly zero:** Needs no focused selection because non-positive is allowed.
- **Required count equals `t`:** Feasible; every operation slot is assigned.
- **Unused operation slots:** May target any index because extra decrease cannot invalidate the goal.
- **Input preservation:** Feasibility uses arithmetic rather than editing values.
