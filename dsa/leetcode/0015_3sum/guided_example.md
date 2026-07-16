# Guided Example: 3Sum

We will find every distinct zero-sum value triplet in

- **Input:** `[-1, 0, 1, 2, -1, -4]`
- **Expected collection:** `[[-1, -1, 2], [-1, 0, 1]]`

The challenge is not merely to find three indices. The output must contain each **value triplet** once, even when repeated values create several index-level choices.

## 1. Sort to create monotone structure

Sorting transforms the input into

| Sorted index | 0 | 1 | 2 | 3 | 4 | 5 |
|---:|---:|---:|---:|---:|---:|---:|
| Value | -4 | -1 | -1 | 0 | 1 | 2 |

For each fixed first value $a$, the remaining task is a two-sum problem on the suffix to its right:

$$
b+c=-a.
$$

Place a left pointer $L$ at the beginning of that suffix and a right pointer $R$ at its end. Because the suffix is sorted:

- increasing $L$ replaces $b$ by a value no smaller than before, so the sum cannot decrease;
- decreasing $R$ replaces $c$ by a value no larger than before, so the sum cannot increase.

This monotonicity tells us which candidates become impossible after every comparison.

## 2. Fix -4 and eliminate an impossible suffix

First fix $a=-4$. We need a pair with sum $4$. Start with $L$ on the first `-1` and $R$ on `2`.

| $a$ | $L$ | $b$ | $R$ | $c$ | Total $a+b+c$ | Decision |
|---:|---:|---:|---:|---:|---:|---|
| -4 | 1 | -1 | 5 | 2 | -3 | too small; increase $L$ |
| -4 | 2 | -1 | 5 | 2 | -3 | too small; increase $L$ |
| -4 | 3 | 0 | 5 | 2 | -2 | too small; increase $L$ |
| -4 | 4 | 1 | 5 | 2 | -1 | too small; pointers meet |

Why is moving $L$ the only useful direction after a negative total? Moving $R$ left would replace `2` with an equal or smaller value, making the total even smaller. All pairs using the current left value are therefore impossible and can be discarded together.

No pair in the suffix completes `-4` to zero.

## 3. Fix the first -1 and find two triplets

Now fix the value at sorted index $1$, so $a=-1$. The target pair sum is $1$.

### First pointer configuration

| Role | Fixed value $a$ | Left value $b$ | Right value $c$ |
|---|---:|---:|---:|
| Position | index 1 | index 2 | index 5 |
| Value | -1 | -1 | 2 |

The total is

$$
-1+(-1)+2=0.
$$

Record the value triplet $[-1,-1,2]$. Then move both pointers inward. Moving only one pointer would keep part of the same matched boundary and risks reproducing the same value combination.

### Second pointer configuration

| Role | Fixed value $a$ | Left value $b$ | Right value $c$ |
|---|---:|---:|---:|
| Position | index 1 | index 3 | index 4 |
| Value | -1 | 0 | 1 |

Again,

$$
-1+0+1=0.
$$

Record $[-1,0,1]$. Moving both pointers inward now makes them cross, so the suffix search for this fixed value is complete.

## 4. Skip the repeated fixed value

The value at sorted index $2$ is another `-1`. Starting a second suffix search from it cannot produce a new value triplet:

- the fixed value is identical to the previous anchor;
- its suffix is strictly smaller and contains no value that was unavailable to the earlier `-1`;
- every triplet it could form has therefore already been considered.

Skip this repeated anchor. This is **deduplication by construction**: duplicates are removed at the choice point that would generate them, rather than inserted into a result set and cleaned up afterward.

## 5. Finish the remaining anchors

Fixing `0` leaves the suffix `[1, 2]`.

| $a$ | $b$ | $c$ | Total | Decision |
|---:|---:|---:|---:|---|
| 0 | 1 | 2 | 3 | too large; decrease $R$ |

The pointers meet, so no zero-sum triplet begins with `0`.

The next possible fixed value is positive. From that point onward, the fixed value and every value to its right are positive, so their sum must be positive. The outer scan can terminate.

The final collection is

$$
\bigl\{[-1,-1,2],\;[-1,0,1]\bigr\}.
$$

## Pointer movement as elimination

For a fixed anchor, imagine all candidate pairs $(L,R)$ with $L<R$. The pointers trace only a monotone path through that triangular search region.

| Observed total | Mathematical consequence | Safe elimination |
|---|---|---|
| $a+b+c<0$ | the total must increase | discard the current $L$; move $L$ right |
| $a+b+c>0$ | the total must decrease | discard the current $R$; move $R$ left |
| $a+b+c=0$ | one valid value triplet is found | record it, move both pointers, skip equal boundary values |

A pointer move is therefore not a guess. It is a proof that an entire family of pairs cannot satisfy the equation.

## Duplicate control at all three positions

There are two distinct places where repetition matters:

1. **Fixed-value duplicates:** skip an anchor equal to the preceding anchor. Otherwise the same suffix relation is solved again and the same triplets are emitted.
2. **Pointer-value duplicates:** after recording a triplet, advance $L$ past every copy of the left value just used and move $R$ past every copy of the right value just used. These copies alter indices but not the output value triplet.

For example, an input containing several zeroes may offer many index triples, but the value result `[0, 0, 0]` must appear only once.

## Why the reasoning is correct

**No valid triplet is discarded by pointer movement.** With a negative total, decreasing the right value cannot produce zero, so only increasing the left value can help. With a positive total, increasing the left value cannot produce zero, so only decreasing the right value can help. Sorted order makes both conclusions monotone.

**Every value triplet is eventually considered.** In sorted order, every valid triplet has a smallest value. The outer scan reaches that value as an anchor, and the two-pointer search explores all pair sums that can complete it without skipping a feasible zero.

**Every value triplet is emitted once.** Repeated anchors are skipped, and equal pointer values are bypassed after a match. These operations remove only alternative index realizations of an already recorded value combination.

## Traps this example exposes

- **Deduplicating only at the end:** a result set works, but it hides the stronger structural fact that repeated searches can be avoided entirely.
- **Skipping duplicates before evaluating a candidate:** two equal values may both be required, as in `[-1, -1, 2]` or `[0, 0, 0]`. Duplicate skipping must respect the role each value plays.
- **Moving the wrong pointer:** after a small sum, moving $R$ left cannot help; after a large sum, moving $L$ right cannot help.
- **Returning index triples:** this problem asks for distinct triplets of values, unlike Two Sum.
- **Stopping at the first match:** one fixed anchor can participate in several distinct triplets, as the anchor `-1` does here.

## Cost of the method

Sorting costs $O(n\log n)$. For each of at most $n$ fixed positions, the two pointers traverse the remaining suffix once, for an overall time bound of $O(n^2)$.

If the array is sorted in place, the pointer search itself uses $O(1)$ auxiliary space; the sorting routine may require $O(\log n)$ stack space or up to $O(n)$ working storage, depending on the implementation. The returned triplets are output space and are not counted as avoidable auxiliary storage.
