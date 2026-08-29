## General

**Sorting identifies the two trimmed tails**

The task removes the smallest five percent and largest five percent by element count. After sorting `arr` in ascending order:

- the smallest values occupy the beginning;
- the largest values occupy the end;
- the values to average form one contiguous middle slice.

The source sorts the input list in place with `arr.sort()`.

**Calculate the slice boundaries**

For length `n`, the source computes:

`start = int(n * 0.05)`

`end = int(n * 0.95)`.

The constraint says `n` is a multiple of 20. Therefore, five percent of `n` is an integer $n/20$, and 95 percent is $19n/20$.

The slice `arr[start:end]` excludes indices below `start` and excludes index `end` and everything after it. It removes exactly $n/20$ values from the front and:

$$
n-\frac{19n}{20}=\frac{n}{20}
$$

values from the back.

Using integer arithmetic `n // 20` and `n - n // 20` would avoid floating representation entirely, but the exact source uses decimal multiplications followed by `int`.

**Why positional trimming handles duplicates**

The instruction removes a percentage of elements, not every element equal to a threshold. If several equal values straddle a trim boundary, only the required number of occurrences is removed.

Sorting and slicing operate by position, so they remove exactly the correct count. Which identical occurrence is considered removed makes no numerical difference.

**Compute the middle mean**

`t = arr[start:end]` creates a new list containing the retained 90 percent.

The arithmetic mean is:

`sum(t) / len(t)`.

At least 18 of 20 elements remain, so `t` is non-empty. Python’s slash performs floating-point division even when the sum divides evenly.

The source applies `round(..., 5)` and returns that float. The problem accepts values within $10^{-5}$, so five decimal-place rounding is adequate for the requested tolerance.

Rounding is not required by the mathematical task; returning the unrounded division would also be accepted. It is nevertheless part of the exact implementation.

**A trace**

For an array of 20 elements, `start = 1` and `end = 19`. Sorting places the one smallest element at index zero and the one largest at index 19. Slice indices one through 18 retain 18 elements.

In the first example, those retained values are all two, so their sum divided by 18 is exactly two.

For length 40, two elements are removed from each end and 36 remain.

**Why this gives the required mean**

Sorting preserves the multiset of values while ordering it. The first $n/20$ positions are exactly a choice of the smallest five percent, and the last $n/20$ positions are exactly the largest five percent. The middle slice contains all and only the remaining values.

The returned quotient is their arithmetic mean, and rounding changes it only within the accepted numerical tolerance.

**Input mutation**

`arr.sort()` permanently changes the caller-provided list to ascending order. The method then creates `t` as a separate slice. A caller needing the original order must pass a copy.

## Complexity detail

Let $N$ be the array length.

Sorting dominates at $O(N\log N)$ time. Creating the middle slice, summing it, and determining its length each take $O(N)$ or less. Total time is $O(N\log N)$.

The slice `t` contains $0.9N$ values, so it uses $O(N)$ additional space. Python’s Timsort may also use $O(N)$ temporary storage. Total auxiliary space is $O(N)$.

The in-place mutation of `arr` does not eliminate the slice allocation in the exact source.

## Alternatives and edge cases

- **Sum the sorted middle without slicing:** Use `sum(arr[start:end])` still creates a slice in Python; an index loop or iterator such as `islice` can avoid the $O(N)$ middle copy.
- **Selection algorithms:** Find the lower and upper order-statistic boundaries in linear expected time, but handling exact counts and duplicates is more complex.
- **Counting sort:** With values bounded by $10^5$, a frequency array can compute the trimmed sum in $O(N+V)$ time and $O(V)$ space.
- **Heap trimming:** Keeping tails in heaps can avoid full sorting but is unnecessary for $N\le1000$.
- **Length 20:** Exactly one value is removed from each end.
- **Length multiple of 20:** It guarantees both five-percent counts are integers and retained length is exactly 90 percent.
- **Duplicate boundary values:** Slicing removes the required number of occurrences; equal copies are interchangeable.
- **All values equal:** Trimming does not change the mean.
- **Zeros and large values:** Sorting and ordinary arithmetic handle the full allowed range.
- **Floating boundary calculation:** The exact code uses `int(n * 0.05)` and `int(n * 0.95)`; integer formulas `n // 20` and `n - n // 20` are more robust conceptually.
- **Five-place rounding:** It is within the accepted tolerance, though Python’s rounding semantics may use ties-to-even.
- **Input mutation:** The original order is lost because `arr.sort()` is in place.
- **Non-empty retained set:** Removing ten percent from a length of at least 20 always leaves elements for division.
