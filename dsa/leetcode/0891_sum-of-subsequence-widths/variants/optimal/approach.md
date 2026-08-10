## General

Enumerating all nonempty subsequences would require exponential time. The useful transformation is to stop thinking about one subsequence at a time and instead ask how many times each array value contributes as a maximum and how many times it contributes as a minimum.

Sorting `nums` places values in nondecreasing order. Subsequences are defined by original indices, but width depends only on selected values, not their original order. Sorting is safe for counting because each chosen index still represents one occurrence. Duplicate values remain separate sorted positions and therefore retain the correct multiplicity of index-based subsequences.

Consider sorted position $i$ with value `nums[i]`.

**Count its appearances as a maximum.** To make this occurrence the chosen maximum, it must be included. Any subset of the $i$ positions before it may also be included, while positions after it are excluded for this particular contribution assignment. There are

$$
2^i
$$

choices for the earlier positions. Thus `nums[i]` contributes $+\text{nums}[i]\cdot2^i$ across maximum terms.

With duplicate values, a subsequence may have more than one occurrence tied for its maximum. The positional counting assigns that subsequence's maximum contribution to its rightmost selected occurrence. This creates a unique assignment and avoids double-counting, while the numeric maximum remains the same value.

**Count its appearances as a minimum.** To make position $i$ the chosen minimum, include it and choose any subset of the $n-1-i$ later positions. There are

$$
2^{n-1-i}
$$

such choices. With ties, the leftmost selected occurrence can serve as the unique representative. The negative contribution is therefore $-\text{nums}[i]\cdot2^{n-1-i}$.

Summing both roles gives the standard formula

$$
\sum_{i=0}^{n-1}
\text{nums}[i]
\left(2^i-2^{n-1-i}\right).
$$

**How the exact loop combines the two halves.** Instead of computing two powers for each index, the code pairs a value from the left orientation with one from the mirrored orientation:

```text
ans += (nums[i] - nums[n - 1 - i]) * 2^i
```

The first part sums `nums[i] * 2^i`. In the second part, let $j=n-1-i$; then $2^i=2^{n-1-j}$, so it sums exactly the negative minimum contribution `-nums[j] * 2^(n-1-j)`. The mirrored expression is therefore algebraically identical to the standard formula.

The variable `p` starts at 1, representing $2^0$. After each iteration, `p = (p << 1) % mod` doubles it to the next power of two while keeping it reduced modulo $10^9+7$.

**Why widths emerge from separate contributions.** Every nonempty subsequence contributes

$$
\max(\text{subsequence})-\min(\text{subsequence}).
$$

If all maximum terms from all subsequences are grouped by the index representing their maximum, they form the positive count above. Grouping all minimum terms by their representative index forms the negative count. Linearity of summation allows those global groups to be subtracted without ever constructing an individual subsequence.

For sorted `[1,2,3]`, maximum multiplicities are 1, 2, and 4; minimum multiplicities are 4, 2, and 1. The net sum is

$$
1(1-4)+2(2-2)+3(4-1)=6.
$$

Singleton subsequences are included in both roles and contribute zero because their maximum equals their minimum.

Modulo is applied after every addition. Intermediate differences may be negative, but Python's modulo produces a nonnegative residue, and modular arithmetic preserves the final required remainder.

## Complexity detail

Let $n$ be the array length. Sorting costs $O(n\log n)$. The contribution loop is $O(n)$.

- **Time complexity:** $O(n\log n)$.
- **Space complexity:** The manifest states $O(n)$, accounting for sorting's temporary storage. The contribution calculation itself uses $O(1)$ scalar state.

The exact code sorts `nums` in place, modifying its order. No power-of-two array is stored because `p` is updated incrementally.

## Alternatives and edge cases

- **Enumerate all subsequences:** This takes $O(2^n)$ subsets and is impossible for $n=10^5$.
- **Precompute all powers of two:** It simplifies indexing but uses $O(n)$ extra storage. The running `p` avoids that array.
- **Use the direct coefficient formula:** Add `nums[i] * (pow2[i] - pow2[n-1-i])`. It is equivalent to the mirrored-pair loop.
- **Do not sort:** The number of smaller and larger eligible values cannot be inferred from position without sorted order.
- **One value:** Positive and negative contributions cancel, yielding width zero.
- **All values equal:** Every subsequence has width zero, and the global maximum/minimum contributions cancel.
- **Duplicate values:** Sorted occurrences are still distinct indices. The representative tie convention counts every subsequence once.
- **Singletons:** They are included among nonempty subsequences but add zero width automatically.
- **Negative intermediate residue:** Python modulo normalizes it; no manual correction is needed.
- **Large power counts:** Reducing `p` after every doubling prevents enormous intermediate powers while preserving the result.
- **Input mutation:** `nums.sort()` changes the caller's array. Sorting a copy would preserve it at linear additional storage.
- **Subsequence order:** Sorting is used only for combinatorial counting. Width ignores the selected order, so original-order constraints do not change a selected set's width.
