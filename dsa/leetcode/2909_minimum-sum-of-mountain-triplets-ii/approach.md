## General

The goal is to minimize `nums[i] + nums[j] + nums[k]` subject to $i < j < k$ and

$$
\texttt{nums}[i] < \texttt{nums}[j]
\quad\text{and}\quad
\texttt{nums}[k] < \texttt{nums}[j].
$$

The ordering says that $j$ is the peak of the triplet. Once that peak index is chosen, the two remaining choices do not interact: the left value only needs to come from the prefix before $j$, and the right value only needs to come from the suffix after $j$. Since the objective is a sum, the best valid choice on either side is simply the smallest value on that side.

This observation is the central reduction. We do not have to search all combinations of three indices. We only have to visit every possible peak and know two range minima.

**Prepare all future right-side choices**

The reverse pass fills an array `right` where `right[i]` is the minimum value from index $i$ through the end of `nums`. It begins with an additional sentinel entry:

`right[n] = inf`.

Then, for $i$ moving from $n-1$ down to $0$,

`right[i] = min(right[i + 1], nums[i])`.

This recurrence is valid because the suffix beginning at $i$ consists of the single current element followed by the suffix beginning at $i+1$. Taking the smaller of those two known quantities produces the minimum of the whole suffix.

For a peak at index $j$, the relevant lookup is `right[j + 1]`. It is the minimum strictly to the right. Using `right[j]` would be a subtle error: that range contains the peak itself, and could falsely treat one array position as two members of the triplet.

**Carry the best past left-side choice**

During a left-to-right pass, `left` records the minimum value from the indices already passed. At the beginning it is infinity because no left index exists. For current index $j$, the solution first tests whether `left < nums[j]` and only afterward incorporates `nums[j]` into `left`.

That order gives a useful loop invariant: immediately before evaluating $j$,

$$
\texttt{left} = \min_{0 \le i < j}\texttt{nums}[i].
$$

The suffix construction similarly gives

$$
\texttt{right}[j+1] = \min_{j < k < n}\texttt{nums}[k].
$$

The current element can form the peak of at least one mountain triplet precisely when both minima are strictly smaller than it. When that is true, the best sum for this peak is

`left + nums[j] + right[j + 1]`.

The answer variable retains the minimum of these peak-specific candidates.

**Why the two minimum values are guaranteed to be valid choices**

It may initially seem that storing only values loses necessary index information. The ranges encoded by the algorithm prevent that problem. `left` was obtained exclusively from indices below $j$, and `right[j + 1]` exclusively from indices above $j$. Therefore their supplying positions automatically satisfy the required index order.

Now suppose there is a valid triplet $(i,j,k)$. Because `left` is the minimum over all earlier positions, `left <= nums[i]`. Since `nums[i] < nums[j]`, the stored left minimum is also strictly below the peak. Likewise, `right[j + 1] <= nums[k] < nums[j]`. The stored pair is therefore valid for this same peak, and its total is no greater than the total of $(i,j,k)$.

This proves two important points at once:

1. If a peak has any valid choices, testing the two side minima will recognize it.
2. The candidate computed for that peak is its smallest possible sum.

Every index is examined as the peak, so the smallest recorded candidate is the smallest valid triplet sum across the entire array.

**Sentinels make empty ranges harmless**

The suffix array has the extra infinity at `right[n]`, while `left` is also initialized to infinity. At the first index there is no left candidate, so `left < nums[0]` is false. At the final index `right[n]` supplies no finite right candidate, so the right comparison is false. The endpoints therefore reject themselves naturally.

The answer also starts at infinity. It becomes finite only after both strict comparisons succeed. Returning `-1` when it remains infinite exactly represents the case in which no mountain triplet exists.

As a small trace, take `[5, 2, 6, 1, 4]`. When the scan reaches $6$, `left` is $2$ and `right[3]` is $1$, so $2+6+1=9$ is considered. When it reaches $4$, the left minimum has become $1$, but there is no smaller value to its right. This illustrates why side minima must be tied to the current peak's strict prefix and suffix rather than taken from the array globally.

## Complexity detail

Let $n$ denote the number of elements.

The reverse suffix pass performs $n$ iterations. The forward peak pass also performs $n$ iterations, and every iteration uses a constant amount of work. These passes are sequential rather than nested, so their combined running time is $O(n)+O(n)=O(n)$.

The `right` array has $n+1$ entries and is the only data structure whose size grows with the input, giving $O(n)$ auxiliary space. The running prefix minimum and answer require $O(1)$ space.

It is possible to compute both prefix and suffix arrays, but the exact implementation stores only the suffix minima. The prefix minimum is needed in forward order and can therefore be maintained online in one scalar. The stated $O(n)$ space bound remains accurate because of `right`.

## Alternatives and edge cases

- **Cubic enumeration:** Trying every $i<j<k$ is easy to reason about but costs $O(n^3)$ time, which is unsuitable for the larger constraints of this second version.
- **Quadratic peak expansion:** Fixing each $j$ and rescanning both sides takes $O(n^2)$ time. It discovers the same two minima repeatedly instead of reusing them.
- **Two full range-minimum arrays:** A prefix-minimum array plus a suffix-minimum array also yields $O(n)$ time and $O(n)$ space. Keeping `left` as a scalar is simpler because the forward scan needs only the current prefix minimum.
- **Strict inequality:** A side value equal to the peak is invalid. The two `<` checks must not be weakened to `<=`.
- **Repeated values:** Duplicate numbers are harmless. The suffix and running prefix minima can come from any occurrence in their proper ranges, and the index ordering remains valid.
- **An endpoint cannot be the peak:** A valid peak needs at least one index on each side. Infinity sentinels make the tests fail at the endpoints without accessing outside the array.
- **Smallest values on the same side:** The globally smallest two values are not automatically a usable pair; both could lie to the left or both to the right of a peak. The range-specific minima preserve the ordering constraint.
- **No mountain exists:** Strictly increasing, strictly decreasing, or otherwise unsuitable arrays never update `ans` and correctly return `-1`.
- **Large sums:** The Python implementation uses arbitrary-precision integers, so adding three legal values does not overflow. In a fixed-width language, the maximum possible sum should be checked when choosing the numeric type.
