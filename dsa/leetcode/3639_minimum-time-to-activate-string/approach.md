## General

As time increases, more positions become `*`, so the number of valid substrings can only increase. The source binary-searches the earliest time and evaluates one time by counting the complementary set: substrings containing no activated position.

**Total number of substrings**

A string of length n has:

$$
\frac{n(n+1)}2
$$

nonempty substrings. If this total is below k, even replacing every character cannot create k valid substrings, so the source returns `-1` immediately.

If total is at least k, activation is guaranteed by time `n-1` because every position is then `*` and every substring is valid.

**Invert the order permutation**

`activation_time[index]` stores the time when that position becomes `*`.

The loop over `enumerate(order)` fills this inverse mapping. It lets `is_active(time)` scan positions in string order and determine whether each is active by comparing its stored time to the candidate.

The actual letters of `s` do not matter; only its length and activated positions affect substring validity.

**Count invalid substrings by inactive runs**

At candidate time t, a substring is invalid exactly when all its positions have activation time greater than t.

Inactive positions form maximal contiguous runs separated by active `*` positions. A run of length L contains:

$$
\frac{L(L+1)}2
$$

all-inactive substrings.

The formula follows by choosing a starting position inside the run. The first position can start `L` different substrings, the second can start `L-1`, and so on until the last position starts one. Their sum is `L+(L-1)+...+1=L(L+1)/2`. This counts substrings rather than subsequences because every chosen interval remains contiguous.

No invalid substring crosses an active separator. Therefore, summing this formula over all inactive runs gives every invalid substring exactly once.

**The scan inside `is_active`**

`inactive_run` counts the current consecutive inactive positions.

- If `activated_at>time`, extend the run.
- Otherwise, the position is active. Add the completed run's triangular count to `invalid` and reset the run to zero.

After the loop, the trailing run is added because no active separator follows it.

Valid count is:

`total_substrings-invalid`.

The predicate returns whether this is at least k.

**Monotonicity**

If the string is active at time t, it remains active later. Turning another position into `*` can only split an inactive run and convert additional substrings from invalid to valid; it cannot remove a star.

Thus candidate times form a false prefix followed by a true suffix, exactly the pattern binary search needs.

**Binary-search boundaries**

`left=0` and `right=n-1` cover every actual replacement time.

At midpoint:

- if active, an earlier answer may exist, so set right to middle;
- otherwise, set left to middle+1.

When they meet, left is the first true time. Prior impossibility checking guarantees the final time is true.

**Following `"abc"`**

Order `[1,0,2]` gives activation times `[1,0,2]`. At t=0, inactive runs have lengths 1 on each side of active index 1.

Invalid count is `1+1=2` out of six total substrings, leaving four valid. Since k=2, time zero is active.

**Why counting stars independently would be insufficient**

One star at index i belongs to `(i+1)(n-i)` substrings, but with multiple stars these sets overlap. Adding per-star contributions would double-count substrings containing several stars.

Complementary inactive runs are disjoint and avoid inclusion-exclusion.

**Why the predicate and the first true time give the answer**

For a fixed time, every invalid substring lies wholly inside one maximal inactive run, and every substring inside such a run is invalid. The triangular sum is therefore exact.

Binary search uses an exact predicate over a monotone timeline and returns the smallest time satisfying it. Together these prove the returned time is the required minimum.

It is also useful to see why one new activation preserves monotonicity algebraically. If it splits an inactive run of length `L` into lengths `a` and `b`, where `a+b=L-1`, the invalid contribution changes from `L(L+1)/2` to `a(a+1)/2+b(b+1)/2`. The latter is never larger because every interval that remains invalid was already inside the original run, while intervals containing the newly active position cease to be invalid. Thus the predicate cannot switch from true back to false.

## Complexity detail

Building activation times costs `O(n)` time and `O(n)` space.

One `is_active` call scans all n positions in `O(n)` time and constant additional space. Binary search performs `O(\log n)` calls, giving total `O(n\log n)` time.

The activation array dominates auxiliary space at `O(n)`.

## Alternatives and edge cases

- **Incremental ordered-set counting:** Add stars in order and update invalid-run contributions by splitting intervals, achieving `O(n\log n)` without binary search.
- **Union-Find in reverse:** Start fully active and restore inactive characters while tracking run sizes; useful for deriving all times.
- **Enumerate substrings:** It costs `O(n^2)` even with prefix star counts.
- **k exceeds total substrings:** Return `-1` immediately.
- **k equals total substrings:** Activation occurs only when every substring is valid, which requires all positions active.
- **k equals one:** The first replacement always creates at least one valid substring, so answer is zero.
- **Single-character string:** Time zero activates its only substring if k=1.
- **Star at an endpoint:** It leaves one inactive run rather than two.
- **Adjacent active positions:** The inactive run between them has length zero and contributes nothing.
- **Trailing inactive run:** The explicit post-loop addition is necessary.
- **Permutation guarantee:** Every position receives exactly one activation time.
- **Original character values:** They are irrelevant; source uses only `len(s)`.
- **Input preservation:** Neither `s` nor `order` is modified.
