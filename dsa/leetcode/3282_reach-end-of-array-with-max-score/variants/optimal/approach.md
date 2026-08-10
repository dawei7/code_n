## General

A jump from `i` to `j` earns

`(j - i) * nums[i]`.

Interpret that jump as crossing each unit boundary between consecutive indices `i, i+1, ..., j-1`. It contributes `nums[i]` once for every crossed boundary. Thus any complete route assigns one departure value to each of the $n-1$ boundaries.

For boundary after index `t`, the jump crossing it must have started at some index no greater than `t`. The greatest possible contribution for that boundary is therefore the maximum value seen in prefix `nums[0..t]`.

This gives an upper bound:

$$
\sum_{t=0}^{n-2}\max(\texttt{nums}[0..t]).
$$

The source computes exactly this sum. `mx` stores the prefix maximum. It scans `nums[:-1]` because there is no boundary after the final index. For each departure-capable index, it updates `mx` and adds it to `ans`.

**Why the bound is achievable.** Start at index zero. Whenever a later index introduces a new larger prefix maximum, jump to that record index; from there, it can supply the larger value for subsequent boundaries. Eventually jump to the last index. Every boundary is crossed by a jump beginning at the latest record maximum available before it, so its contribution equals the computed prefix maximum.

For `[1,3,1,5]`, boundary prefix maxima are one, three, and three, summing to seven. Jump zero to one earns one, then one to three earns six.

For `[4,3,1,3,2]`, prefix maximum across every boundary is four. A direct jump from zero to four earns four times four, totaling sixteen.

**Why a large future value cannot help earlier boundaries.** Bob cannot jump backward. A value at index `u` can contribute only to boundaries at or after `u`, so the prefix restriction is unavoidable.

**Why jumping at every record maximum suffices.** Non-record indices have value no larger than the current record. Starting a jump there would assign an equal or smaller contribution to future boundaries, so they never need to be departure points in an optimal route.

Positive values make the initial `mx=0` harmless. The first scanned element replaces it before contributing. The same reasoning would work with negative values only if initialization used negative infinity, but negatives are outside the contract.

The algorithm calculates the score without constructing the actual sequence of jumps. The record-max proof supplies existence, and only the numeric maximum is requested.

## Complexity detail

The scan visits $n-1$ elements and performs constant work at each, giving $O(n)$ time.

Only `ans`, `mx`, and the loop value are stored, so auxiliary space is $O(1)$. In Python, `nums[:-1]` creates a shallow list copy of $n-1$ elements, however. Therefore the exact expression temporarily uses $O(n)$ memory, conflicting with the manifest's strict $O(1)$ claim. Iterating by index or using `itertools.islice` would realize constant auxiliary space.

The answer may be roughly $10^{10}$ under constraints; Python integers handle it.

## Alternatives and edge cases

- **Dynamic programming over destinations:** Trying every previous jump start costs $O(n^2)$. Prefix maxima collapse the transition structure.
- **Greedy jump to the next larger value:** This can construct an optimal route, but summing boundary maxima is simpler when only the score is needed.
- **Always jump one step:** It earns the sum of original departure values, which can miss carrying an earlier large value across many boundaries.
- **Always jump directly to the end:** This is optimal only when `nums[0]` remains the prefix maximum throughout.
- **Single element:** There are no jumps or boundaries; `nums[:-1]` is empty and the answer is zero.
- **Strictly increasing values:** Prefix maximum changes at every index, and unit jumps between records achieve the sum.
- **Strictly decreasing values:** The first value remains best, so a direct final jump is optimal.
- **Equal record values:** Jumping to the equal value is unnecessary but would not change score.
- **Last element's value:** It cannot be used as a departure because the route ends there, so excluding it is correct.
- **Input preservation:** The method never assigns into `nums`, though slicing creates a temporary copy.
- **Exact-space mismatch:** The mathematical algorithm is constant-space; the concrete slice prevents the submitted source from being strictly so.
- **Boundary-count identity:** A jump of length `j-i` crosses exactly `j-i` unit boundaries, which is why multiplying by `nums[i]` equals adding that departure value once per crossed boundary.
- **Route construction from records:** Whenever a new prefix maximum appears before the final index, the current route can jump to it. Skipping all other indices then realizes every prefix-max contribution simultaneously.
- **Why local contributions combine:** Every route crosses each boundary exactly once because indices only increase. Maximizing the permitted contribution independently at each boundary does not create incompatible choices; record-max jumps realize the complete set.
- **Positive-value assumption:** With legal positive values, more distance under a larger prefix maximum never hurts. The same formula can extend to arbitrary values with a corrected negative-infinity initialization.
