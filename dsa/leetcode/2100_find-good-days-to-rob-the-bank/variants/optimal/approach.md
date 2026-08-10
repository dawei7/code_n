## General

**Replace repeated interval checks with run lengths**

For a candidate day `i`, the condition to the left is

$$
\texttt{security[i-time]}\ge\cdots\ge\texttt{security[i]}.
$$

The condition to the right is

$$
\texttt{security[i]}\le\cdots\le\texttt{security[i+time]}.
$$

Checking both length-`time` regions separately for every day could repeat the same adjacent comparisons many times. The solution instead precomputes how long the required monotonic run extends from each day in each direction.

`left[i]` is the number of consecutive non-increasing steps ending at day `i`. `right[i]` is the number of consecutive non-decreasing steps starting at day `i`.

A value counts steps between days, not the number of days in the run. For example, `left[i] = 2` means the three-day sequence from `i - 2` through `i` satisfies the non-increasing relation.

**Build the left run lengths**

The forward loop starts at index 1. If

`security[i] <= security[i - 1]`,

then the step from `i - 1` to `i` continues a non-increasing sequence. The source assigns

`left[i] = left[i - 1] + 1`.

If the comparison fails, the zero from initialization remains. No qualifying non-increasing step can cross that increase.

Equal values are accepted because the requirement is non-increasing, not strictly decreasing. The `<=` comparison correctly allows a plateau.

**Build the right run lengths**

The backward loop starts at `n - 2`. If

`security[i] <= security[i + 1]`,

then moving right from `i` begins or continues a non-decreasing sequence. The recurrence is

`right[i] = right[i + 1] + 1`.

Processing right to left ensures the continuation length at `i + 1` is already known.

Again, equality is valid because non-decreasing permits equal adjacent values.

**Combine the two local summaries**

Day `i` has enough valid steps on both sides exactly when

`left[i] >= time` and `right[i] >= time`.

The comprehension writes this as

`time <= min(left[i], right[i])`.

If the smaller run length is at least `time`, both are. Run lengths also enforce the boundary requirement automatically: an index cannot accumulate `time` left steps unless at least `time` earlier days exist, and similarly on the right.

For `security = [5, 3, 3, 3, 5, 6, 2]` and `time = 2`, day 2 has two non-increasing steps from 5 to 3 to 3 and at least two non-decreasing steps from 3 to 3 to 5. Day 3 also has enough of both. Other indices fail at least one run-length test.

**Handle an impossible window size early**

A good day needs a total span of `2 * time + 1` days. If `n <= 2 * time`, this span is larger than the array, so the source returns an empty list before allocating run arrays.

The strict relationship is correct: a valid center requires $n\ge2\cdot\texttt{time}+1$, which is equivalent to $n>2\cdot\texttt{time}$.

When `time == 0`, the early condition is false because `n >= 1`. Every index satisfies `0 <= min(left[i], right[i])`, so the method returns all days as required.

**Why the algorithm is correct**

By induction along the forward pass, `left[i]` is exactly the maximum number of consecutive adjacent non-increasing comparisons ending at `i`. The recurrence extends the previous run if the newest comparison is valid and resets implicitly to zero otherwise.

The symmetric backward induction proves `right[i]` is exactly the maximum number of consecutive non-decreasing comparisons starting at `i`.

Therefore, `left[i] >= time` is equivalent to the entire required left segment being non-increasing, and `right[i] >= time` is equivalent to the entire required right segment being non-decreasing. The comprehension includes precisely the good days.

Indices are examined in increasing order, so the returned list is sorted even though any order is allowed. The input is not modified.

## Complexity detail

Let $n$ be the number of days.

The forward pass, backward pass, and final comprehension each take $O(n)$ time. Constantly many linear passes give total time $O(n)$.

The two run-length arrays each contain $n$ integers, so auxiliary space is $O(n)$. The returned list can also contain $O(n)$ indices.

The early impossible-size return uses constant space and time after reading `n`, but the worst case remains linear.

## Alternatives and edge cases

- **Check every candidate window directly:** This can cost $O(n\cdot\texttt{time})$ because adjacent comparisons are repeated. Run lengths reuse them.
- **Prefix counts of violations:** One can mark increases and decreases and query whether each side contains a violation. That is also linear but less direct than monotonic run lengths.
- **Sliding counters without arrays:** It is possible to combine directional information more carefully, but two arrays make the proof and boundary conditions explicit.
- **`time == 0`:** Every day is valid because both required side intervals contain zero steps.
- **Array too short:** When `n <= 2 * time`, no center can have enough days on both sides.
- **Equal guard counts:** Equality continues both permitted monotonic directions.
- **Strictly increasing array:** Positive `time` fails the left condition for every possible center.
- **Strictly decreasing array:** Positive `time` fails the right condition for every possible center.
- **All values equal:** Every index with enough boundary room is good.
- **Boundary indices:** Their run length on the missing side is too small, so they are excluded automatically for positive `time`.
- **Output order:** The source returns increasing indices, which is allowed.
- **Input preservation:** Only summary arrays are written; `security` remains unchanged.
