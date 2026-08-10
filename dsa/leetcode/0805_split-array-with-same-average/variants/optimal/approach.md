## General

**Reduce the split to finding one proper subset**

Let the array length be `n` and total sum be `s`. Suppose a nonempty subset `A` has size `k` and sum `sumA`.

Its average equals the complete array average when:

$$
\frac{sumA}{k}=\frac{s}{n}.
$$

If this holds, the nonempty complement `B` automatically has the same average:

$$
\frac{s-sumA}{n-k}=\frac{s}{n}.
$$

Therefore it is enough to find one nonempty proper subset whose average equals the full-array average. The complement supplies the second group.

**Transform average equality into zero-sum equality**

Fractions are inconvenient for subset search. Replace every value `v` by:

`v * n - s`.

For a subset of size `k`:

$$
\sum_{v\in A}(vn-s)
=
n\sum_{v\in A}v-ks.
$$

This transformed sum is zero exactly when:

$$
n\cdot sumA=k\cdot s,
$$

which is the cross-multiplied average condition.

The complete transformed array itself sums to:

$$
n\cdot s-n\cdot s=0.
$$

That is why the search must exclude selecting the entire array; the full set is always a trivial zero-sum choice but would leave an empty complement.

**Notice that the exact source mutates `nums`**

The loop writes each transformed value back into `nums[i]`. This saves a separate transformed array but changes the caller-provided list.

All subsequent subset sums refer to transformed values. The original values are no longer needed after `s` and `n` have been recorded.

An implementation that must preserve input would build a new list instead.

**Why meet in the middle is necessary**

There are $2^n$ subsets, and `n` may be 30. Split the transformed array at:

`m = n >> 1`.

The left half has `m` elements and the right half has `n-m`. Each side has at most 15 elements, so enumerating its masks requires about $2^{n/2}$ work rather than $2^n$.

A desired subset may use only the left half, only the right half, or elements from both.

**Enumerate nonempty left subsets**

Masks from one through `(1 << m) - 1` represent all nonempty left subsets.

For a mask, the generator adds transformed value `v` at position `j` exactly when:

`i >> j & 1`

is one.

If the resulting sum `t` is zero, that left subset is a valid answer. It is proper because the left half contains fewer than all `n` elements when `n >= 2`.

Otherwise, the sum is inserted into `vis`. Only distinct sums are needed; which left mask produced a sum is irrelevant for existence.

**Enumerate nonempty right subsets**

The second mask loop similarly computes each nonempty right-half sum `t`.

If `t == 0`, the right subset alone is a valid nonempty proper subset.

For a subset using both halves, transformed sums must cancel:

$$
leftSum+rightSum=0.
$$

Thus the required left sum is `-t`. Membership `-t in vis` finds whether some nonempty left subset supplies it in expected constant time.

**Why the complete right mask is excluded from cross-half matching**

The cross condition also requires:

`i != (1 << (n - m)) - 1`.

This prevents combining the complete right half with the complete left half, which would select the entire array and falsely exploit its guaranteed zero transformed sum.

At first it seems that excluding every cross-match using all right elements might also discard a proper subset that uses all right elements but only part of the left. It does not lose a real solution.

If such a proper combined subset has transformed sum zero, its nonempty complement lies entirely in the left half. Since the total transformed sum is zero, that complement also has sum zero. The earlier left-only enumeration would already have returned true.

Therefore all-right cross combinations are either the forbidden whole array or redundant with a left-only zero-sum subset.

**Why the complete left mask may remain in `vis`**

The code does not remove the full-left sum from `vis`. Combining it with a proper right subset is a proper overall subset and is valid.

Combining full left with full right is the only forbidden case, and the right-mask condition blocks it.

This asymmetric rule is sufficient and avoids storing subset sizes or mask identities in the set.

**Trace the average logic**

For `nums = [1,2,3,4,5,6,7,8]`, `n = 8` and `s = 36`. The transformed values are:

`[-28,-20,-12,-4,4,12,20,28]`.

Subset `[1,4,5,8]` corresponds to transformed values `[-28,-4,4,28]`, whose sum is zero. Its original average is $18/4=4.5$, equal to the full average $36/8=4.5$.

The complement has the same average automatically.

**Single-element input**

When `n == 1`, no partition into two nonempty arrays exists. The method returns false before transformation or subset enumeration.


The algebra proves a subset has the full average if and only if its transformed sum is zero. Any nonempty proper zero-sum subset yields the required split, and any valid split yields such a subset.

The two mask loops cover every nonempty subset by its left and right portions. Left-only and right-only zeros return directly; mixed subsets are found by complementary sums. The sole whole-array false positive is excluded, with all-right proper solutions already covered through their left complements.

Therefore the method returns true exactly when a valid split exists.

## Complexity detail

Let left size be $m=\lfloor n/2\rfloor$ and right size be $n-m$. The exact source computes every mask sum by scanning its whole half and also creates a half slice inside each mask expression.

Its literal time is:

$$
O\left(m2^m+(n-m)2^{n-m}\right)
=
O\left(n2^{n/2}\right).
$$

The manifest's $O(2^{n/2})$ suppresses this polynomial factor; an incremental subset-sum enumeration can realize that tighter conventional meet-in-the-middle expression.

`vis` can contain up to $2^m-1$ distinct sums, so auxiliary space is $O(2^{n/2})$. The transformed values reuse the input list rather than allocating another $O(n)$ array.

## Alternatives and edge cases

- **Incremental mask sums:** Derive a mask's sum from the mask with its lowest set bit removed, avoiding a full half scan per subset.

- **Subset-size dynamic programming:** Track possible sums for each chosen size and test `sum * n = size * total`. It is useful when numeric sums are small enough.

- **Enumerate all subsets directly:** It costs $O(2^n)$ and ignores the small-half opportunity at `n <= 30`.

- **One element:** A two-nonempty-part split is impossible.

- **All equal values:** Any nonempty proper subset has the same average, so a zero transformed subset is found.

- **Whole transformed array:** Its sum is always zero but it is not a legal subset answer.

- **Left-only or right-only solution:** Each half loop checks zero before cross matching.

- **All-right mixed candidate:** Its complementary left-only subset prevents the exclusion rule from losing a solution.

- **Input mutation:** Copy `nums` first if callers require the original values afterward.
