## General

A decimal integer is divisible by three exactly when the sum of its digits is divisible by three. The problem can therefore be separated into two decisions:

1. Choose as many digits as possible whose sum has remainder zero modulo three.
2. Among choices of that maximum length, arrange and select digits so the resulting decimal string is lexicographically and numerically largest.

The checked-in solution sorts the digits, uses dynamic programming to maximize selected length for each remainder, and reconstructs a largest maximum-length selection from high digits to low digits.

**Why maximum length comes before digit values**

For nonzero-leading decimal strings, any number with more digits is larger than every number with fewer digits. Therefore, the primary optimization is the number of selected digits. Once length is fixed, placing larger digits earlier gives the largest value.

The all-zero case needs canonicalization to `"0"` rather than a longer string of leading zeros, which the final cleanup handles.

**Sort digits in ascending order for reconstruction**

`digits.sort()` mutates the input into ascending order. The DP itself depends only on remainders and counts, not on this order. Sorting is used so reconstruction can scan from the end and consider the largest remaining digit first.

**Define the remainder DP**

`f[i][j]` is the maximum number of digits that can be selected from the first `i` sorted digits so that their digit sum has remainder `j` modulo three.

Every state begins at negative infinity, meaning impossible. `f[0][0] = 0` represents choosing no digits with sum zero. The other two remainders cannot be formed from an empty prefix.

For digit `x` at position `i - 1`, a state may exclude or include it:

- Excluding `x` keeps `f[i - 1][j]`.
- Including `x` requires a predecessor remainder `k` such that `(k + x) % 3 == j`.

Solving for `k` gives
`(j - x % 3 + 3) % 3`. The inclusion candidate is that predecessor length plus one. Taking the maximum stores the greatest possible length for remainder `j`.

The added three keeps the intermediate value nonnegative before the final modulo.

After all digits, `f[n][0]` is the maximum count whose sum is divisible by three. If it is zero, only the empty selection works, so the method returns an empty string. A real zero digit creates a positive-length remainder-zero state, so zero-only inputs are not confused with the empty selection.

**Reconstruct the largest optimal selection**

Reconstruction starts with required remainder `j = 0` and scans `i` from `n` down to one. Because digits were sorted ascending, this visits them from largest to smallest.

For the current digit, `k` is the predecessor remainder needed if the digit is included. The equality
`f[i - 1][k] + 1 == f[i][j]` asks whether an optimal-length solution for the current state can include this digit.

If so, the method appends the digit and changes the required predecessor remainder to `k`. If both including and excluding could preserve optimal length, this equality chooses inclusion while examining the largest available digit. That greedy tie choice makes the resulting descending digit sequence lexicographically largest among all maximum-length solutions.

If the equality fails, including the digit cannot achieve the optimal stored length, so it is skipped.

Every appended digit is visited from high to low, so `arr` is already in the descending order that maximizes the decimal number. No second sort is needed.

**Canonicalize an all-zero result**

For any result containing a nonzero digit, descending order puts that digit first, so there are no leading zeros. If every selected digit is zero, `arr` contains several zeros. The loop advances `i` while another digit remains, leaving exactly one zero. Joining from that position returns `"0"`.

The DP gives a sum divisible by three, the reconstruction preserves its maximum length, and the descending greedy tie decisions maximize the value at that length. These facts establish the returned string as the largest valid multiple.

## Complexity detail

Let $n$ be the number of input digits.

Sorting `digits` takes $O(n\log n)$ time. Filling three states for each of $n$ rows takes $O(n)$ time, and reconstruction is another $O(n)$. The exact total is $O(n\log n)$.

The DP table has `n + 1` rows and three columns, using $O(n)$ space. The reconstructed digit list can also contain $O(n)$ entries. Thus the exact auxiliary space is $O(n)$.

The manifest’s $O(n)$ time and $O(1)$ space do not describe this checked-in implementation because it explicitly sorts and retains the full DP table. A frequency-count solution over ten digit values can achieve linear time with constant alphabet-sized storage, but that is a different implementation.

## Alternatives and edge cases

- **Digit-frequency greedy removal:** Count digits by remainder, remove the smallest one or two digits needed to fix the total remainder, then emit digits descending. This can achieve $O(n)$ time with fixed-size storage.
- **One-dimensional DP:** Length states can be compressed, but reconstructing the exact largest selection then needs additional decisions or predecessor information.
- **Enumerate subsets:** Exponential and infeasible for ten thousand digits.
- **No valid nonempty subset:** `f[n][0]` remains zero and the method returns an empty string.
- **One zero:** It forms the valid number `"0"`.
- **Many zeros only:** Reconstruction selects all for maximum count, and cleanup collapses the representation to one zero.
- **Nonzero plus zeros:** Descending order places nonzero digits before zeros, so no trimming occurs.
- **Input mutation:** `digits.sort()` changes the caller-provided list order.
- **Remainder subtraction:** Adding three before modulo prevents a negative predecessor index.
- **Tie during reconstruction:** Including the currently largest digit whenever optimal length permits is what maximizes lexicographic value.
- **Divisibility rule:** Only digit-sum remainder matters for divisibility by three; the final order does not change that remainder.
