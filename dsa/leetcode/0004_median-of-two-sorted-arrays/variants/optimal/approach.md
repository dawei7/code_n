## General

**Find middle-ranked values without constructing the merged array**

If the two sorted arrays were merged, the median would be determined by one or two central positions in that merged order. Building the merged array would make those positions easy to read, but it would require linear time. The logarithmic goal instead suggests an **order-statistic** question: find the $k$-th smallest value across two sorted suffixes while discarding many values at once.

The helper `f(i, j, k)` uses the following contract:

- `i` is the first still-considered index in `nums1`;
- `j` is the first still-considered index in `nums2`;
- `k` is one-indexed: `k = 1` asks for the smallest value across `nums1[i:]` and `nums2[j:]`.

Nothing before `i` or `j` remains part of the current order-statistic problem. Those values have already been proved too small and discarded. This avoids slicing: the original arrays stay intact, and two indices describe the active suffixes.

**Express both odd and even medians with two ranks**

Let

$$
T = m+n,
$$

where `m = len(nums1)` and `n = len(nums2)`. The code asks for

$$
k_1 = \left\lfloor\frac{T+1}{2}\right\rfloor
\qquad\text{and}\qquad
k_2 = \left\lfloor\frac{T+2}{2}\right\rfloor.
$$

For odd $T$, these expressions are equal. For example, when $T=3$, both ranks are `2`, so averaging the same middle value with itself returns that value as a float.

For even $T$, they are the two central ranks. When $T=4$, they are `2` and `3`, and their average is the median. This lets the final code use one formula for both parities:

```python
a = f(0, 0, (m + n + 1) // 2)
b = f(0, 0, (m + n + 2) // 2)
return (a + b) / 2
```

**Resolve the easy helper states first**

Three base cases stop the recursive elimination.

If `nums1` is exhausted, all remaining candidates come from `nums2`, so the one-indexed `k`-th remaining value is

```python
nums2[j + k - 1]
```

The `-1` converts the one-indexed rank into a zero-indexed offset. The symmetric expression handles an exhausted `nums2`.

If neither array is exhausted but `k == 1`, the requested value is the smaller current head:

```python
min(nums1[i], nums2[j])
```

There is no need to know how the later values interleave; sorted order guarantees that neither suffix contains a value smaller than its own head.

**Compare the halfway candidates**

For `k > 1`, the helper sets

```python
p = k // 2
```

and tries to inspect the `p`-th remaining value of each suffix:

```python
x = nums1[i + p - 1] if i + p - 1 < m else inf
y = nums2[j + p - 1] if j + p - 1 < n else inf
```

The indices use `p - 1` because `p` is a one-indexed count from each current suffix start. `x` is therefore the last value in the first `p` active elements of `nums1`; `y` has the same meaning for `nums2`.

If an array has fewer than `p` values left, its candidate becomes positive infinity. The sentinel is not an input value and is never returned. It merely prevents the algorithm from discarding `p` elements from a suffix that does not have that many. A finite candidate from the other array will compare as smaller, so the sufficiently long suffix is reduced instead.

**Why the smaller candidate identifies a disposable prefix**

Suppose `x < y`. Every one of the first `p` active values in `nums1` is at most `x`. Among the first `p` active values in `nums2`, only the first `p - 1` can be smaller than `y`. Because `x < y`, no value in `nums2` at or after `y` can appear before any discarded value from `nums1`.

Thus each of those first `p` values from `nums1` lies among at most

$$
p + (p-1) = 2p-1
$$

values at the low end of the combined suffixes. Since `p = k // 2`, $2p-1 < k$ for both even and odd `k`. None of that prefix can be the still-requested $k$-th value. The helper discards it and adjusts the rank:

```python
f(i + p, j, k - p)
```

Removing `p` values that come before the target changes the target from the `k`-th remaining value to the `(k - p)`-th remaining value.

When `x >= y`, the symmetric reasoning discards the first `p` active values of `nums2`:

```python
f(i, j + p, k - p)
```

Equality is placed in this second branch. If several equal values straddle the desired rank, discarding `p` copies that are no greater than the target is still safe: the rank decreases by the same number of removed elements, and the target value remains equal.

**Trace the two middle ranks for an even total**

Take `nums1 = [1, 2]` and `nums2 = [3, 4]`.

For rank `2`:

1. `f(0, 0, 2)` has `p = 1`, `x = 1`, and `y = 3`.
2. Because `1 < 3`, discard the first value of `nums1` and call `f(1, 0, 1)`.
3. `k == 1`, so return `min(2, 3) = 2`.

For rank `3`:

1. `f(0, 0, 3)` has `p = 1`, `x = 1`, and `y = 3`; discard `1` and call `f(1, 0, 2)`.
2. Again `p = 1`, now with `x = 2` and `y = 3`; discard `2` and call `f(2, 0, 1)`.
3. `nums1` is exhausted, so return `nums2[0] = 3`.

The final result is `(2 + 3) / 2 = 2.5`.

**Why the helper keeps asking the same mathematical question**

At every call, `f(i, j, k)` denotes the $k$-th smallest value in exactly the two represented suffixes. A base case answers that question directly. A recursive case removes `p` values proved to lie before the requested rank, then subtracts `p` from the rank. The value being sought is unchanged even though its rank inside the smaller remaining collection changes.

Because `p >= 1` whenever `k > 1`, every recursive call makes progress. More strongly, `k - p = \lceil k/2 \rceil`, so the requested rank is roughly halved. Eventually `k` becomes `1` or an array is exhausted. The returned value is therefore the original requested order statistic, and averaging the two selected ranks gives the median.

## Complexity detail

Let $T=m+n$.

- **Time complexity of this exact implementation: $O(\log T)$ per order-statistic query.** Each recursive call replaces `k` with `k - \lfloor k/2 \rfloor = \lceil k/2 \rceil`. The recursion depth is therefore logarithmic in the requested rank, which is at most $T$. The median invokes the helper twice, a constant factor, so the total remains $O(\log(m+n))$.
- **Auxiliary space of this exact Python implementation: $O(\log T)$.** Each recursive call occupies a Python stack frame, and Python does not perform tail-call optimization. The arrays are not copied, so the call stack is the only input-dependent auxiliary storage.

The branch manifest declares the stronger partition-search targets $O(\log(\min(m,n)))$ time and $O(1)$ space. Those bounds belong to an iterative binary search over a partition of the smaller array, such as the Competitive variant. They do not exactly describe this recursive `k`-th-elimination source when one array is much larger than the other. The explanation states the implementation's actual costs so that the code and analysis remain technically consistent.

## Alternatives and edge cases

- **Binary search on a partition of the smaller array:** Choose how many values the left half takes from the smaller array and derive the cut in the other array. This achieves $O(\log(\min(m,n)))$ time and $O(1)$ auxiliary space, matching the manifest's stronger bounds, but its cross-boundary inequalities require a more delicate derivation.
- **Iterative `k`-th elimination:** The same prefix-discarding method can be written as a loop that updates `i`, `j`, and `k`. It preserves $O(\log(m+n))$ time while reducing stack space to $O(1)$.
- **Partial two-pointer merge:** Repeatedly take the smaller current head until reaching the middle ranks. This uses $O(1)$ auxiliary space but $O(m+n)$ time in the worst case, so it misses the required logarithmic target.
- **Full merge:** Constructing the sorted union is conceptually simple, but it requires $O(m+n)$ time and $O(m+n)$ additional storage.
- **One array is empty:** The first helper condition indexes directly into the other array at the requested offset. The global constraint guarantees that both are not empty simultaneously.
- **One suffix is shorter than `p`:** Positive infinity prevents an out-of-range access and forces elimination from the other suffix. The sentinel is only a comparison device.
- **Odd combined length:** Both rank formulas are identical, so the same middle value is found twice and averaging leaves it unchanged.
- **Even combined length:** The formulas select the lower and upper central values separately, then divide their sum by `2` to return a floating-point median.
- **Duplicate values:** Equality goes to the branch that removes a prefix of `nums2`. Removing equal copies and reducing `k` together preserves the requested value even when several identical elements occupy central ranks.
- **Negative values:** Sorted comparisons and order ranks do not depend on sign. The infinity sentinel remains greater than every legal input value.
- **Very different array lengths:** The helper remains safe, but its recursion can depend on $\log(m+n)$ rather than $\log(\min(m,n))$; this is the exact reason the smaller-array partition method has a stronger bound.
- **No mutation:** Only suffix indices change. Neither input array is sliced, sorted again, merged, or modified.
