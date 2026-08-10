## General

Repeating the array up to $10^5$ times makes materializing the full concatenation impractical. The solution instead identifies the few shapes an optimal contiguous subarray can have.

Within one copy, the best subarray is the ordinary maximum subarray, with the empty subarray allowed to contribute zero. Across copy boundaries, a subarray consists of a suffix of its first copy, zero or more complete middle copies, and a prefix of its last copy. The total sum of one copy determines whether including many complete middle copies helps.

**Collect four facts in one scan**

The variable `s` is the running prefix sum and becomes the total array sum after the loop.

`mx_pre` is the largest prefix sum seen, starting from zero so that the empty prefix is allowed. After the scan, it is the maximum sum of a prefix of `arr`, including an empty prefix with sum zero.

`mi_pre` is the smallest prefix sum seen, also starting from the empty prefix sum zero. After the scan, `s - mi_pre` is the maximum suffix sum: choosing the suffix after the position where the prefix was smallest removes the least possible preceding total.

`mx_sub` tracks the maximum subarray sum within one copy. For the current prefix sum `s`, subtracting the smallest prefix seen gives the best sum of a subarray ending at the current point. The code updates `mi_pre` before calculating `s - mi_pre`. If the current prefix is the new minimum, this produces zero, representing an empty choice. Any subtraction using an earlier, larger minimum would be negative, so no positive candidate is lost. Starting `mx_sub` at zero enforces the contract’s permission to choose an empty subarray.

After the loop, the four important quantities are therefore the total sum `s`, best prefix `mx_pre`, best suffix `mx_suf = s - mi_pre`, and best within-copy subarray `mx_sub`.

**Handle one copy directly**

If `k == 1`, no boundary exists. The answer is simply `mx_sub`, reduced modulo $10^9+7$. This includes zero for an all-negative array.

**Cross exactly one boundary**

For at least two copies, a subarray may take the best suffix of one copy and the best prefix of the next. Its sum is

`mx_suf + mx_pre`.

These pieces belong to different copies, so they do not overlap even if their corresponding ranges overlap when viewed in the original single array. The code compares this boundary-crossing candidate with `mx_sub` because the best result might still lie wholly inside one copy.

This two-copy candidate is sufficient whenever the total array sum is nonpositive. Extending across an additional complete copy would add `s <= 0` and could not improve the sum. An optimal multi-copy interval can discard such an unhelpful complete middle copy by choosing closer boundary copies.

**Use every profitable complete middle copy**

When `s > 0` and `k > 2`, every full middle copy adds a positive amount. A boundary-spanning optimum should therefore include all `k - 2` copies between the first and last:

`(k - 2) * s + mx_pre + mx_suf`.

The first selected copy contributes its best suffix, the last contributes its best prefix, and every copy between them contributes its full total. The code compares this value with the earlier candidates. For `k = 2`, the multiplier is zero and the expression reduces to the ordinary one-boundary candidate, so the separate comparison already covers it.

For `arr = [1, 2]` and `k = 3`, the total, best prefix, and best suffix are all three. The long candidate is one complete middle sum plus a three-point suffix and three-point prefix, yielding nine, which is the sum of the entire repeated array.

For `arr = [1, -2, 1]`, the total is zero. Additional complete copies do not add value, so the best answer comes from at most two neighboring copies. Taking a suffix `[1]` and a prefix `[1]` gives two regardless of how large `k` becomes.

**Why the candidate list is complete**

Any contiguous subarray of the repeated sequence either stays within one copy or crosses at least one boundary. A within-copy interval is bounded by `mx_sub`.

A crossing interval has a suffix of its first touched copy and a prefix of its last touched copy. Replacing them by the maximum suffix and prefix cannot reduce its sum. Every fully covered copy between those ends contributes exactly `s`. If `s > 0`, the best such form spans as many complete middle copies as possible. If `s <= 0`, no complete middle copy improves the result, so a crossing choice needs only two adjacent copies. These are exactly the candidates the code evaluates, plus the empty zero candidate embedded in all maxima.

Modulo reduction occurs only after selecting the true maximum. Applying modulo to intermediate signed sums would destroy numerical order and could make a smaller actual sum appear larger.

## Complexity detail

Let $n$ be the length of `arr`. The solution scans the array exactly once and performs a constant number of arithmetic and comparison operations per element. All remaining calculations are constant time, independent of `k`. Time complexity is $O(n)$.

The method stores only scalar totals and extrema. It never builds the $kn$-element concatenated array and does not allocate prefix arrays. Auxiliary-space complexity is $O(1)$.

Intermediate values can be much larger than the final modulus because the positive total may be multiplied by `k - 2`. Python integers expand safely. In fixed-width languages, multiplication should use a sufficiently wide type before taking modulo $10^9+7$.

## Alternatives and edge cases

- **Run Kadane’s algorithm over two copies:** Scanning two conceptual copies gives the best within-copy and one-boundary result. The positive-total middle-copy contribution must still be added analytically for larger `k`.
- **Materialize all `k` copies:** This requires $O(kn)$ time and space and is infeasible at the maximum constraints.
- **Prefix and suffix arrays:** They can compute the same extrema but use $O(n)$ storage that the running sums avoid.
- **`k = 1`:** Only `mx_sub` is relevant; adding a prefix and suffix from the same copy could overlap and must not be treated as two distinct-copy pieces.
- **All values negative:** Every maximum includes the empty choice zero, so the answer is zero rather than the least negative element.
- **Total sum zero:** Complete middle copies neither help nor hurt. The best answer is captured inside one copy or across one boundary.
- **Positive total:** Every available full middle copy increases a spanning candidate, so the `k - 2` term is included.
- **Best prefix or suffix is empty:** Their stored value can be zero. This lets a crossing formula naturally choose no elements from one endpoint copy when that is optimal.
- **Modulo timing:** Compare full integer sums first and apply modulo only to the selected maximum.
- **Single-element array:** The same prefix, suffix, and total reasoning applies. A positive value repeats profitably, while a nonpositive value leaves the empty answer zero.
- **Minimum-prefix update order:** Including the current prefix in `mi_pre` permits a zero-length subarray ending here. It cannot hide a positive interval because a newly smaller current prefix would make every interval ending here negative.
