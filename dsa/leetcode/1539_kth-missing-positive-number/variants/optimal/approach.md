## General

**Count missing positives before an array value**

If no positive integers were missing, the value at zero-based index `i` would be `i + 1`. When the actual value is `arr[i]`, the difference

$$
\operatorname{missing}(i)=\texttt{arr[i]}-i-1
$$

is the number of positive integers missing strictly before `arr[i]`.

For example, at index three with value seven, there should have been four present values up to that position. Among positive integers one through six, only three array values occur before seven, so three values are missing. The formula gives $7-3-1=3$.

Because `arr` is strictly increasing by at least one, this missing-count function never decreases. That monotonicity makes binary search possible.

**Handle an answer before the first array element**

If `arr[0] > k`, then positive values one through `k` are all absent: the array's first present value occurs later. The $k$-th missing positive is therefore exactly `k`.

This early return also establishes a useful fact for the remaining code. When it does not run, `arr[0] <= k`, so the missing count before index zero is `arr[0] - 1 < k`. The binary-search boundary will consequently end at least at one, making `left - 1` a valid index in the final expression.

**Find the first position with at least k missing values**

The search interval is half-open: `left = 0` and `right = len(arr)`. It seeks the smallest index whose missing count is at least `k`. The value `len(arr)` acts as a valid insertion position meaning no actual element reaches that count.

At midpoint `mid`, the code computes `arr[mid] - mid - 1`.

If this count is at least `k`, the first qualifying position is `mid` or lies to its left, so `right = mid`.

If the count is smaller, `mid` cannot be the first qualifying position, and neither can any earlier index because the function is nondecreasing. The search moves to `left = mid + 1`.

When `left == right`, `left` is the lower-bound insertion point. Every real index before it has fewer than `k` missing positives before its value. If `left` is inside the array, that index has at least `k`.

**Recover the answer from the previous present value**

Let `p = left - 1`. By the early-return argument, `p` is always valid. The number of missing positives before `arr[p]` is

`arr[p] - p - 1`.

The target is still `k - (arr[p] - p - 1)` missing steps beyond `arr[p]`. Since no array value occurs before the lower-bound position that would reach the target count, advancing that many integer values gives the answer:

`arr[p] + k - (arr[p] - p - 1)`.

The source writes this with `p` expanded as `left - 1`. Algebraically, the `arr[p]` terms cancel, leaving `k + left`. The longer expression makes explicit how many missing values have already been passed.

**Why the formula works when left equals n**

If every array position has a missing count below `k`, the lower bound is `len(arr)`. Then `p` is the last valid array index. All remaining positive integers after `arr[p]` are missing because the array has ended.

The same “remaining missing steps” formula extends past the last element and returns the correct value. No access to `arr[left]` occurs, so the half-open sentinel is safe.

**Tracing the first example**

For `[2,3,4,7,11]`, missing counts are one, one, one, three, and six. With `k = 5`, the first count at least five occurs at index four, so `left = 4` and `p = 3`.

Before value seven, three positives are missing. Two more missing values are needed: eight and nine. The expression returns `7 + 5 - 3 = 9`.

For `[1,2,3,4]` and `k = 2`, all missing counts are zero, so `left = 4`. The previous value is four, and the second missing value after it is six.

**Why the algorithm is correct**

The formula `arr[i]-i-1` exactly counts missing positives before each present value and is monotone. Standard lower-bound search therefore finds the first position where the cumulative missing count reaches `k`, or the end when it never does.

The previous array element has fewer than `k` missing values before it. Advancing by precisely the remaining deficit lands on the $k$-th missing positive. The early case covers targets before the first present value, so all possible answer locations are handled.

## Complexity detail

Let $N$ be the array length. The early test is constant time. Binary search halves the index interval on every iteration and performs constant work, so time is $O(\log N)$.

The algorithm stores two boundaries, one midpoint, and arithmetic temporaries. It uses $O(1)$ auxiliary space and does not modify or copy the input, matching the manifest.

Strict increase is what guarantees the missing-count sequence is nondecreasing. The constraints also make ordinary fixed-width arithmetic safe here, while Python integers would handle larger values automatically.

## Alternatives and edge cases

- **Linear adjustment of k:** Scan values from left to right and increment `k` whenever a present value is at most the current target. It is simple but costs $O(N)$.
- **Enumerate positive integers:** Test membership until the $k$-th miss; without a set this is slow, and with a set it uses extra space.
- **Return k plus left:** This is algebraically identical to the stored final expression but hides the “remaining missing count” derivation.
- **Answer before arr zero:** The explicit early return handles it and keeps `left-1` safe later.
- **Answer between two values:** The lower bound points to the right-hand present value, while the formula starts from the previous one.
- **Answer after the array:** `left == N` is valid because the source indexes only `left-1`.
- **Array starts at one:** There are no missing positives before the first element, so search handles later gaps or the tail.
- **Large initial gap:** If it already contains the target rank, the result is simply `k`.
- **No internal gaps:** The binary search reaches the end, and the answer is `N+k` when the array is `[1,2,\ldots,N]`.
- **Strictly increasing requirement:** Duplicates would break the simple count formula and its monotonic interpretation.
- **One-element array:** Both the early-gap case and the after-array case remain valid.
- **Half-open search interval:** Using `right = len(arr)` deliberately represents an answer beyond the final array element.
