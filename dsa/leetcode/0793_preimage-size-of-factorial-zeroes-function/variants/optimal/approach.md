## General

**Count factors of five instead of computing a factorial**

A trailing zero is created by a factor of ten, and $10 = 2 \cdot 5$. Factorials contain many more factors of two than factors of five, so the number of trailing zeros in `x!` is exactly the total number of factors of five contributed by integers from one through `x`.

Multiples of five contribute at least one factor. Multiples of 25 contribute one additional factor, multiples of 125 contribute another, and so on. Therefore:

$$
f(x)
=
\left\lfloor\frac{x}{5}\right\rfloor
+
\left\lfloor\frac{x}{25}\right\rfloor
+
\left\lfloor\frac{x}{125}\right\rfloor
+\cdots.
$$

The recursive helper computes the same sum:

`f(x) = x // 5 + f(x // 5)`.

After dividing by five once, the recursive call contributes `floor(x / 25)`, then `floor(x / 125)`, and so forth. The base `f(0) = 0` stops when no higher power of five can contribute.

**Use the monotonic shape of the function**

As `x` increases, factorial `x!` gains factors but never loses them. Hence `f(x)` is nondecreasing.

Most consecutive values lie on plateaus. For example, `f(0)` through `f(4)` are all zero. At multiples of five the function increases, and at multiples of higher powers of five it may jump by more than one.

Because of those jumps, some target values `k` never occur. When a value does occur, it occupies a consecutive block of `x` values. The task asks for the length of that block.

**Define a lower-bound boundary**

Let `g(q)` be the smallest nonnegative integer `x` such that:

$$
f(x) \ge q.
$$

Then:

- every `x < g(k)` has `f(x) < k`;
- every `x` from `g(k)` through `g(k+1)-1` has `k \le f(x) < k+1`;
- since `f(x)` is integer-valued, that middle condition is exactly `f(x) = k`.

Therefore the number of solutions is:

$$
g(k+1)-g(k).
$$

This boundary-difference idea handles both possibilities automatically. If `f` jumps over `k`, the two boundaries coincide and the difference is zero. If `k` forms a plateau, their difference is the plateau length.

**Search only a finite range**

The implementation defines:

`g(k) = bisect_left(range(5 * k), k, key=f)`.

The range contains candidate integers zero through `5k - 1`. A lower bound may be returned at index `5k`, immediately after the range.

Why is this large enough? For positive `k`:

$$
f(5k) \ge \left\lfloor\frac{5k}{5}\right\rfloor = k.
$$

Thus the first point with `f(x) \ge k` is no later than `x = 5k`. Searching indices up to that insertion boundary safely contains the answer.

For `k = 0`, `range(0)` is empty and `bisect_left` returns zero. This correctly gives `g(0)=0`.

**How `bisect_left` works with a key**

`range(5 * k)` behaves like a sorted sequence of candidate `x` values. The key function transforms a candidate into `f(x)` for comparison with target `k`.

Because `f` is nondecreasing, these transformed values are sorted even though they contain duplicates and jumps. `bisect_left` returns the first index whose transformed value is at least the target—the exact lower-bound definition of `g`.

No array of zero counts is created. `range` is lazy, and `f` is evaluated only for the logarithmically many candidates inspected by binary search.

**Trace `k = 0`**

`g(0)=0`.

For `g(1)`, the search range is candidates zero through four. Their zero counts are all zero, so the insertion point for one is at index five. Thus:

$$
g(1)-g(0)=5-0=5.
$$

The five preimages are zero through four, matching the example.

**Trace a missing value**

Around `x = 25`, the zero count jumps because 25 contributes two factors of five. Specifically, `f(24)=4` and `f(25)=6`, so value five is skipped.

The first `x` with `f(x)\ge5` and the first with `f(x)\ge6` are both 25. Therefore `g(6)-g(5)=0`, correctly reporting no preimage for five.

**Why an existing preimage has size five**

Between consecutive multiples of five, adding one to `x` does not add a new factor of five, so `f` stays constant across blocks of five candidate integers. At a multiple of 25 or higher, the jump may skip values, but it does not create a shorter positive plateau for a value that is actually attained.

The boundary formula does not need this special property, but it explains why the problem's output is always either zero or five.


The helper computes the exact trailing-zero count by summing all powers-of-five contributions. Its values are monotone, so each lower-bound call returns the first `x` at or above its target count.

The half-open interval `[g(k), g(k+1))` contains exactly the integers whose count is at least `k` but below `k+1`, which for integers means exactly `k`. Subtracting endpoints returns precisely the requested preimage size.

## Complexity detail

Let $K = k+1$ to keep the zero case inside logarithmic notation. A binary search over a range of size $O(K)$ performs $O(\log K)$ key evaluations.

Each recursive `f(x)` call divides `x` by five until zero, taking $O(\log K)$ time. Two lower-bound searches therefore take $O(\log^2 K)$ time, matching $O(\log^2(k+1))$.

The manifest lists $O(1)$ auxiliary space, which would be true if the powers-of-five sum were computed iteratively. The exact source implements `f` recursively, so one key evaluation can hold $O(\log K)$ call frames. Binary search itself is implemented by the library without a user-visible candidate array, and `range` is constant-space. The exact auxiliary call-stack bound is therefore $O(\log(k+1))$.

## Alternatives and edge cases

- **Iterative factor-of-five sum:** Repeatedly divide `x` by five in a loop. It preserves the same time bound and makes auxiliary space genuinely $O(1)$.

- **Direct binary search written by hand:** Maintain numeric low and high bounds for the first `f(x) \ge q`. It is more verbose but avoids reliance on keyed `bisect_left`.

- **Search for one exact value only:** Finding an arbitrary `x` with `f(x)=k` does not itself count the whole plateau; two boundaries do.

- **Compute factorials:** Values become enormous and the factors-of-five formula already gives the needed property directly.

- **Zero target:** The empty-range lower bound and the next boundary correctly produce five.

- **Skipped target:** Equal lower boundaries produce zero.

- **Attained target:** The boundary difference produces five without hard-coding that fact.

- **Exclusive range endpoint:** `bisect_left` may return `5k` as an insertion point even though that candidate is not stored in the range, which is exactly what the upper boundary permits.

- **Large `k`:** The search uses logarithmically many candidates and never constructs `x!`.
