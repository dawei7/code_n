# Guided Example: Count Subarrays With Fixed Bounds

## 1. The instance and the two conditions a subarray must satisfy

A fixed-bound subarray of `nums` is a contiguous slice whose minimum equals
`minK` **and** whose maximum equals `maxK`. This lesson works through the
official first example:

- **Input:** `nums = [1, 3, 5, 2, 7, 5]`, `minK = 1`, `maxK = 5`
- **Required output:** `2`

Both conditions are simultaneously necessary, and they pull in opposite
directions. Requiring the minimum to equal `minK` forbids every value strictly
below `minK`; requiring the maximum to equal `maxK` forbids every value strictly
above `maxK` and additionally demands that an occurrence of `maxK` is actually
inside the slice. A slice can therefore fail for three independent reasons:
a value below the floor drops the minimum, a value above the ceiling raises the
maximum, and a slice whose values all lie in range may still contain no `minK`
or no `maxK`, so neither equality holds. The third failure mode is what makes
this problem interesting: `[3, 5, 2]` passes both range tests, yet its minimum
is 3 and it is not fixed-bound.

---

## 2. Counting by right endpoint instead of enumerating subarrays

There are $\frac{n(n+1)}{2}$ subarrays, which is $2.1 \times 10^{9}$ at the
constraint limit $n = 10^{5}$. Every subarray, however, has exactly one right
endpoint, so instead of generating pairs we can fix the right endpoint `i` and
ask a purely local question:

> How many start indices $s$ produce a slice `nums[s..i]` that is fixed-bound?

Summing those answers over all `i` counts each subarray exactly once, because no
subarray has two right endpoints. The answer for this instance is the sum of six
per-endpoint counts.

Three positions summarize everything the slice `nums[s..i]` could contain:

| Tracked position | Meaning | Initial value | Why it is needed |
|---|---|---|---|
| `k` | latest index holding a value outside $[\texttt{minK}, \texttt{maxK}]$ | -1 | any slice containing it is disqualified |
| `j1` | latest index holding a value equal to `minK` | -1 | the slice must contain that occurrence |
| `j2` | latest index holding a value equal to `maxK` | -1 | the slice must contain that occurrence |

All three begin at -1, meaning "this event has not happened yet", and each is
refreshed to the current index whenever its condition holds at that index.

---

## 3. The invariant that turns three positions into a count

> **Frontier invariant.** After the update at endpoint `i`, a start index $s$
> yields a fixed-bound subarray `nums[s..i]` if and only if
> $k < s \le \min(j_1, j_2)$.

*Necessity.* If $s \le k$, the slice contains the out-of-range value at index
`k`, so either its minimum is strictly below `minK` or its maximum is strictly
above `maxK`. If $s > j_1$, the slice begins after the most recent `minK`, and
since `j1` is the latest such index there is no `minK` at all in
`nums[s..i]`; symmetrically for $s > j_2$. So any admissible start must satisfy
$s > k$, $s \le j_1$ and $s \le j_2$.

*Sufficiency.* If $k < s \le \min(j_1, j_2)$, then no index in $[s, i]$ is
out of range — every out-of-range index is at most `k`, which is below $s$ — so
every element satisfies $\texttt{minK} \le x \le \texttt{maxK}$. The slice
contains index `j1` with value `minK`, so its minimum is exactly `minK`, and it
contains index `j2` with value `maxK`, so its maximum is exactly `maxK`.

The admissible starts therefore form one unbroken integer interval, and its size
is $\min(j_1, j_2) - k$ when that quantity is positive and zero otherwise:

$$
\text{valid}(i) = \max\bigl(0,\ \min(j_1, j_2) - k\bigr).
$$

The maximum with zero is not cosmetic. When `k` is the *later* of the two
frontiers it means the most recent disqualifying value sits to the right of the
most recent required value, so no start is admissible at all, and the raw
difference is negative.

---

## 4. Worked trace on `nums = [1, 3, 5, 2, 7, 5]`

| Endpoint `i` | `nums[i]` | `k` | `j1` | `j2` | $\min(j_1,j_2) - k$ | `valid(i)` | Running total |
|---|---|---|---|---|---|---|---|
| 0 | `1` | -1 | 0 | -1 | $-1 - (-1) = 0$ | 0 | 0 |
| 1 | `3` | -1 | 0 | -1 | $-1 - (-1) = 0$ | 0 | 0 |
| 2 | `5` | -1 | 0 | 2 | $0 - (-1) = 1$ | 1 | 1 |
| 3 | `2` | -1 | 0 | 2 | $0 - (-1) = 1$ | 1 | 2 |
| 4 | `7` | 4 | 0 | 2 | $0 - 4 = -4$ | 0 | 2 |
| 5 | `5` | 4 | 0 | 5 | $0 - 4 = -4$ | 0 | 2 |

Reading the table:

- Endpoints 0 and 1 contribute nothing because `maxK` has not appeared; `j2`
  is still -1, so $\min(-1, 0) = -1$ and the raw difference is zero.
- Endpoint 2 is the first moment both required values are present, and the
  single admissible start is $s = 0$, giving the slice `[1, 3, 5]`.
- Endpoint 3 admits the same single start, giving `[1, 3, 5, 2]`. The value `2`
  is inside the allowed range and changes no frontier.
- Endpoint 4 is out of range (`7 > 5`), so `k` jumps to 4. The raw difference
  turns negative and the maximum with zero refuses to count anything.
- Endpoint 5 is exactly `maxK`, so `j2` advances to 5 — and the count stays
  zero: the disqualifying `7` at index 4 dominates the refreshed `j2 = 5`.

Endpoint-by-endpoint, the admissible start intervals are:

| Endpoint `i` | Admissible starts $(k, \min(j_1,j_2)]$ | Start indices | Subarrays counted |
|---|---|---|---|
| 2 | $(-1,\ 0]$ | `{0}` | `[1, 3, 5]` |
| 3 | $(-1,\ 0]$ | `{0}` | `[1, 3, 5, 2]` |
| 4 | $(4,\ 0]$ | $\emptyset$ | none |
| 5 | $(4,\ 0]$ | $\emptyset$ | none |

The two counted slices are exactly the two the problem statement names, and the
total of the `valid(i)` column is `2`, matching the required output.

---

## 5. A second look: overlapping required values accumulate multiplicities

The trace above contributes 1 per eligible endpoint, which hides how the count
can grow faster than the number of endpoints. Running the same frontier rules on
`nums = [1, 5, 1, 5]` with `minK = 1` and `maxK = 5` shows the accumulation.

| Endpoint `i` | `nums[i]` | `k` | `j1` | `j2` | `valid(i)` | New subarrays counted at this endpoint |
|---|---|---|---|---|---|---|
| 0 | `1` | -1 | 0 | -1 | 0 | none |
| 1 | `5` | -1 | 0 | 1 | 1 | `[1, 5]` |
| 2 | `1` | -1 | 2 | 1 | 2 | `[5, 1]`, `[1, 5, 1]` |
| 3 | `5` | -1 | 2 | 3 | 3 | `[1, 5]`, `[5, 1, 5]`, `[1, 5, 1, 5]` |

Every value lies inside `[1, 5]`, so `k` never moves and each endpoint simply
opens one more admissible start. The total is 6, which is the count of
four-element subarrays that contain both a `1` and a `5`. Notice that
`valid(i)` can exceed 1: it counts *starts*, not events, and each extra
admissible start is a genuinely different subarray.

---

## 6. Boundary and degenerate instances handled by the same rule

| Instance | `k` behaviour | `j1`, `j2` behaviour | Result | Reason |
|---|---|---|---|---|
| `nums = [1]`, `minK = 1`, `maxK = 5` | never set | `j2` stays -1 | 0 | the required `maxK` is absent |
| `nums = [1, 2, 2]`, `minK = 1`, `maxK = 3` | never set | `j2` stays -1 | 0 | all values in range, but no `maxK` |
| `nums = [1, 1, 1, 1]`, `minK = maxK = 1` | never set | `j1 = j2 = i` | 10 | every value refreshes both frontiers; all $\frac{4 \cdot 5}{2}$ subarrays qualify |
| `nums = [2, 2, 3, 2]`, `minK = maxK = 2` | `k = 2` at the `3` | `j1 = j2` at each `2` | 4 | only runs of the single allowed value count |
| `nums = [1, 5, 6, 1, 5]`, `minK = 1`, `maxK = 5` | `k = 2` at the `6` | refreshed after the reset | 2 | the reset splits the array into independent segments |
| `[1000000, 1, 1000000]`, `minK = 1`, `maxK = 1000000` | never set | `j1 = 1`, `j2` at each extreme | 3 | the allowed interval spans the full legal value range |
| `nums = [1, 3, 5, 2, 7, 5]`, `minK = 1`, `maxK = 5` | `k = 4` at the `7` | `j1 = 0`, `j2 = 5` | 2 | the instance traced in Section 4 |

When `minK = maxK` the allowed interval collapses to one value, so `j1` and
`j2` move together and the rule degenerates into counting maximal runs of that
value: `[1, 1, 1, 1]` yields $1 + 2 + 3 + 4 = 10$, while `[2, 2, 3, 2]` yields
$1 + 2 + 0 + 1 = 4$ because the `3` resets the frontier.

---

## 7. Why the reasoning is correct

The frontier invariant of Section 3 is proved in both directions and holds after
every update, so it is a genuine invariant rather than a heuristic. Two
consequences make the algorithm exact.

**Soundness.** Every unit added to the total is justified by a non-empty
admissible start interval whose members were shown to produce slices with
minimum `minK` and maximum `maxK`. The method never counts a slice that fails
either equality.

**Completeness.** Every fixed-bound subarray `nums[s..i]` has one right endpoint
`i`. At that endpoint the slice contains `minK`, so $s \le j_1$; it contains
`maxK`, so $s \le j_2$; and it has no value outside the interval, so the latest
out-of-range index `k` must lie strictly before `s`. Hence $s$ belongs to the
admissible interval, and the algorithm counts it at endpoint `i` and nowhere
else. No valid subarray is lost, and none is double-counted.

A useful sanity check follows from the same argument: the running total can
never decrease, because `valid(i)` is clamped at zero, and the total can never
exceed $\frac{n(n+1)}{2}$.

---

## 8. Alternatives and why they were not chosen

| Method | Idea | Time | Auxiliary space | Trade-off |
|---|---|---|---|---|
| Enumerate every subarray | extend each start and track min/max | $O(n^2)$ | $O(1)$ | correct but hopeless at $n = 10^{5}$ |
| Monotonic queue / sliding window | maintain a window whose min is `minK` and max is `maxK`, shrink from the left | $O(n)$ amortized | $O(n)$ for the deques | same asymptotic time with more state and more edge cases |
| Two inclusion–exclusion counts | count slices whose values stay in $[1, \texttt{maxK}]$ and subtract those staying in $[1, \texttt{minK}-1]$ | $O(n)$ | $O(1)$ | elegant for range-only constraints, but it does not force an *exact* minimum and maximum |
| Sparse table plus binary search | precompute range min/max and locate the admissible start interval per endpoint | $O(n \log n)$ | $O(n \log n)$ | strictly slower and heavier than three running indices |
| Latest-position frontiers | track `k`, `j1`, `j2` and add $\max(0, \min(j_1,j_2)-k)$ | $O(n)$ | $O(1)$ | the method derived here |

Inclusion–exclusion is the most tempting wrong turn: `[3, 5, 2]` satisfies the
range condition "all values lie in $[\texttt{minK}, \texttt{maxK}]$" yet has
neither the required minimum nor the required maximum.

---

## 9. Complexity derivation

Let $n = \lvert\texttt{nums}\rvert$.

**Time.** The scan visits each index once. At index `i` it performs up to three
comparisons against `minK` and `maxK`, a constant number of index assignments, a
two-way minimum, a subtraction, and a clamp at zero. Every one of those
operations is $O(1)$, so the loop costs $\Theta(n)$ and the total is

$$
O(n).
$$

There is no nested loop and no re-scanning of earlier positions, because the
three frontiers compress all past information that any future endpoint needs.

**Auxiliary space.** The method stores exactly four integers — `k`, `j1`, `j2`
and the running answer — plus the loop index and the current value. It allocates
no prefix array, no window, no result collection and no recursion stack, so peak
auxiliary space is

$$
O(1),
$$

independent of $n$ and of the magnitude of the values, which can be as large as
$10^{6}$.

---

## 10. Traps this instance exposes

- **Confusing the range condition with the exact-bound condition:** `[3, 5, 2]`
  stays inside `[1, 5]` yet has minimum 3, so it is not fixed-bound.
- **Dropping the clamp at zero:** at endpoint 4 the raw difference is $-4$; the
  clamp is what converts "no admissible start" into a contribution of 0.
- **Keeping the earliest rather than the latest occurrence:** only the newest
  `minK` and `maxK` maximize the admissible start interval; an older position
  would undercount.
- **Keeping every out-of-range position:** only the newest one matters, because
  requiring $s > k_{\text{newest}}$ already excludes all older ones.
- **Reading the refreshed `j2` as helpful:** at endpoint 5, `j2 = 5` still
  cannot beat `k = 4`, so the contribution is 0.
- **Treating a refreshed bound as a new subarray:** `valid(i)` counts starts,
  and a start re-used at a later endpoint is a different, longer subarray.
- **Assuming each endpoint contributes at most one:** `[1, 5, 1, 5]` contributes
  1, 2 and 3 at successive endpoints.
- **Overflow of the total:** the count can reach $\frac{n(n+1)}{2}$, which
  exceeds 32-bit range at the constraint limit, so the accumulator must be a
  wide integer type.