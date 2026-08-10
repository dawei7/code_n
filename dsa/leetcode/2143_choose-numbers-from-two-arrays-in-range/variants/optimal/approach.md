## General

For every selected index, choosing `nums1[i]` adds to the first-array total, while choosing `nums2[i]` adds to the second-array total. A range is balanced when the difference

$$
\text{sum chosen from nums1}-\text{sum chosen from nums2}
$$

is zero.

The algorithm counts choices for every contiguous range by grouping them according to their ending index and current signed difference.

**Define the DP state**

Let `s1 = sum(nums1)` and `s2 = sum(nums2)`. Across any range, the signed difference can be as large as `s1` if every selected number comes from `nums1`, or as small as `-s2` if every selected number comes from `nums2`.

Negative indexes cannot be used directly in the DP array, so the code adds offset `s2`. Array index `j` represents actual difference

$$
j-s2.
$$

The width `s1 + s2 + 1` contains every integer difference from `-s2` through `s1`, inclusive.

The state `f[i][j]` counts selection patterns for contiguous ranges that end exactly at index `i` and whose signed difference is `j - s2`. It does not mix ranges ending earlier; that distinction is what lets the algorithm extend only contiguous ranges.

**Start new one-index ranges**

At index `i`, write `a = nums1[i]` and `b = nums2[i]`. A new range `[i,i]` has two different choices:

- choose `a` from `nums1`, producing difference $+a$ and index `a + s2`;
- choose `b` from `nums2`, producing difference $-b$ and index `-b + s2`.

The source increments both corresponding cells. If $a=b=0$, the indexes are identical and the cell is incremented twice. That is correct: choosing `nums1[i]` and choosing `nums2[i]` are considered different patterns even when their numeric values are equal.

**Extend every range that ended at the previous index**

When `i > 0`, any longer range ending at `i` is obtained uniquely by extending a range that ended at `i-1`. For every destination index `j`, the code considers both new choices.

If the current value `a` is chosen from the first array, it increases the previous difference by $a$. To finish at destination `j`, the source state must have index `j - a`. The condition `j >= a` ensures this source index is nonnegative, and the transition adds `f[i - 1][j - a]`.

If `b` is chosen from the second array, it decreases the previous difference by $b$. To finish at `j`, the previous index must be `j + b`. The condition `j + b < s1 + s2 + 1` keeps that source inside the table, and the transition adds `f[i - 1][j + b]`.

All additions are reduced modulo `10**9 + 7`.

**Count zero-difference states**

An actual difference of zero corresponds to offset index `s2` because `s2 - s2 = 0`. After row `i` is complete, `f[i][s2]` counts all balanced selection patterns for ranges ending at `i`.

The statement `ans = (ans + f[i][s2]) % mod` adds that disjoint category to the running answer. Every non-empty contiguous range has exactly one ending index, so summing these values counts each balanced range-and-choice pattern exactly once.

**Why every valid object has one construction path**

A counted DP path begins either with one of the two length-one initializations or with a prior state extended by one choice at each next index. It therefore describes a contiguous range and exactly one array choice per position.

Conversely, take any specified range `[l,r]` and its choice pattern. Its choice at `l` creates the matching base state in row `l`. Each following choice applies the corresponding transition, reaching row `r` with the pattern’s signed difference. If the range is balanced, that final state is `f[r][s2]` and is added to `ans`. This establishes both completeness and absence of duplicate paths.

## Complexity detail

Let

$$
S=s1+s2.
$$

The outer loop runs $n$ times. For every row after the first, the inner loop examines all $S+1$ difference indexes and performs constant work for two transitions. Time is $O(nS)$. Computing the two sums and initializing length-one states does not exceed this bound.

The exact code allocates `f` as `n` rows of `S+1` integers, so its auxiliary space is $O(nS)$. This differs from the manifest’s $O(S)$ claim. Only row `i-1` is needed to calculate row `i`, so a rolling two-row or one-row replacement can reduce space to $O(S)$, but the stored Optimal source retains every row.

With $n \le 100$ and values at most 100, each input-array sum is at most 10,000 and $S$ is at most 20,000. Those bounds make the pseudo-polynomial state range explicit.

## Alternatives and edge cases

- **Rolling DP rows:** Keep only the previous and current difference arrays. This preserves $O(nS)$ time and reduces auxiliary space to $O(S)$, matching the manifest but differing from the exact source.
- **Hash map of reachable differences:** Store only nonzero states for each ending index. This may save work when the reachable set is sparse but has hashing overhead and can still grow to $O(S)$ states.
- **Enumerate every range and every choice:** There are $O(n^2)$ ranges and $2^{\text{length}}$ choice patterns, which is exponential. DP merges patterns sharing an ending index and difference.
- **Track unsigned sums separately:** A two-dimensional pair of totals is much larger than tracking only their difference; equality depends solely on the difference.
- **Single index:** The range is balanced only for a choice whose selected value is zero. If both entries are zero, the two array choices are distinct and both are counted.
- **Both current values zero:** Both transitions lead to the same difference but represent different choices, so both contributions must be added.
- **All positive nonzero values:** Balanced ranges can still exist by mixing choices from the two arrays; no zero element is required.
- **Offset purpose:** Index `s2` represents difference zero, index zero represents `-s2`, and index `s1+s2` represents `s1`.
- **Lower transition boundary:** `j >= a` prevents reading a negative source index for a first-array choice.
- **Upper transition boundary:** `j + b < S + 1` prevents reading beyond the table for a second-array choice.
- **Modulo timing:** Each updated cell and the accumulated answer are reduced modulo `10**9 + 7`, keeping values bounded without changing the required modular result.
- **Different choice patterns on the same endpoints:** Their DP paths differ at the first index where they select different arrays, so both are counted even if their numeric sums coincide.
- **Contiguity:** Extending only row `i-1` ensures no index is skipped inside a range.
- **Input preservation:** The method computes sums and fills a separate table without modifying either input array.
