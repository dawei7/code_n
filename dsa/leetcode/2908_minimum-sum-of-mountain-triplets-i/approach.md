## General

We need choose three indices $i < j < k$ whose values form a mountain: both outside values must be strictly smaller than the middle value. Among all such triples, we want the smallest possible sum.

A direct search could choose every triple of indices and test it. That follows the definition, but it repeats a great deal of work. Once the middle index $j$ is fixed, the left and right choices are independent:

- the left index may be any index before $j$ whose value is smaller than `nums[j]`;
- the right index may be any index after $j$ whose value is smaller than `nums[j]`.

For a fixed middle value, choosing anything except the smallest valid value on either side can only make the sum larger. This turns a three-index search into a scan over possible middle indices, provided we can quickly obtain the minimum value strictly before and strictly after each middle.

**Precompute the minimum on every suffix**

The array `right` has length $n+1$. Its meaning is:

$$
\texttt{right}[i] = \min(\texttt{nums}[i],\texttt{nums}[i+1],\ldots,\texttt{nums}[n-1]).
$$

The extra entry `right[n]` is initialized to positive infinity. It represents the empty suffix after the array. The reverse loop computes each real entry from the value at the current index and the already-known minimum of the suffix to its right:

`right[i] = min(right[i + 1], nums[i])`.

When index $j$ later acts as the middle, the solution reads `right[j + 1]`, not `right[j]`. That offset is crucial. It means the right candidate comes strictly after $j$, so the middle element can never accidentally be reused as the right member of the triplet.

**Maintain the left minimum during the forward scan**

The variable `left` starts at positive infinity. Immediately before processing index $j$, it equals the minimum value among indices $0$ through $j-1$. The update `left = min(left, nums[j])` happens only after the current index has been tested. This order ensures that `left` describes a strictly earlier position rather than a prefix that includes the middle itself.

Therefore, while examining `x = nums[j]`, the three relevant values are:

- `left`: the smallest value at any index before $j$;
- `x`: the proposed mountain peak;
- `right[j + 1]`: the smallest value at any index after $j$.

The peak is usable exactly when `left < x` and `right[j + 1] < x`. The comparisons are strict because the definition requires both sides to be smaller than the peak; equality does not form a mountain.

If both tests succeed, `left + x + right[j + 1]` is the minimum mountain-triplet sum having $j$ as its middle index. The solution compares this candidate with `ans` and keeps the smaller one.

**Why taking the side minima cannot miss a valid answer**

Suppose some valid triplet uses $j$ as its middle and has outside values `nums[i]` and `nums[k]`. Because `left` is the minimum of every value before $j$,

$$
\texttt{left} \le \texttt{nums}[i].
$$

The known triplet tells us `nums[i] < nums[j]`, so `left` must also be strictly smaller than `nums[j]`. Replacing `nums[i]` with the position that supplied `left` preserves validity and never increases the sum. The same reasoning applies to `right[j + 1]` on the other side. Thus, if any valid triplet exists for middle $j$, the two stored minima produce a valid triplet whose sum is no larger than that of any other triplet with the same middle.

The forward loop examines every index as a possible middle. Consequently, it evaluates the best triplet for every middle that can support one. Taking the smallest of those candidates gives the global minimum.

**Detecting the absence of a mountain**

Both `ans` and `left` initially equal positive infinity. `ans` changes only when a valid middle has a strictly smaller value on each side. If that never happens, `ans` remains infinity and the method returns `-1`. Otherwise, it returns the finite minimum found.

For example, consider `nums = [8, 6, 1, 5, 3]`. At the middle value $5$, the smallest earlier value is $1$ and the smallest later value is $3$. Both are smaller than $5$, so this middle contributes $1+5+3=9$. The fact that $1$ occurs after some earlier large values does not matter: only its position relative to the chosen middle matters, and it is correctly included in `left` by that time.

## Complexity detail

Let $n$ be the length of `nums`.

Building `right` performs one constant-time minimum operation for each array position, so it takes $O(n)$ time. The forward pass also processes every index once and performs only constant-time comparisons, additions, and minimum updates. The total time is therefore $O(n)$.

The suffix-minimum array contains $n+1$ entries, requiring $O(n)$ auxiliary space. The variables `left`, `ans`, `i`, and `x` use only $O(1)$ additional space. Thus the overall auxiliary-space bound is $O(n)$. The result itself is a single integer and does not affect this bound.

Although this first version has constraints small enough for slower methods, the exact Optimal solution deliberately uses the same linear technique that scales to the larger version of the problem. Its bound does not rely on small input limits.

## Alternatives and edge cases

- **Enumerate all triples:** Three nested loops match the definition directly and take $O(n^3)$ time. This can work for very small inputs, but it repeatedly rechecks the same left and right values.
- **Fix the middle and scan both sides:** For every $j$, scan the prefix for a valid minimum and the suffix for another. This improves the structure of the reasoning but still takes $O(n^2)$ time because the side scans are repeated.
- **Prefix and suffix arrays on both sides:** Storing a complete prefix-minimum array as well as `right` also gives $O(n)$ time, but it uses another $O(n)$ array. The running `left` variable supplies the needed prefix information with constant extra storage.
- **Equal values around the peak:** Conditions such as `left <= x` would be wrong. A side equal to the middle violates the strict mountain inequalities, so the implementation correctly uses `<` twice.
- **Middle at an endpoint:** Index $0$ has no earlier element and index $n-1$ has no later element. The infinity sentinels make their validity tests fail naturally without special branches.
- **Duplicate minima:** The algorithm stores values rather than indices, but this is safe. Any occurrence contributing to `left` is strictly before the middle, and any occurrence contributing to `right[j + 1]` is strictly after it.
- **No valid triplet:** Monotone arrays and arrays without a value having smaller elements on both sides leave `ans` unchanged, producing the required `-1`.
- **Negative infinity is unnecessary:** Array values are finite and the task minimizes sums, so positive infinity is the correct marker for “no value seen” and “no answer found.”
