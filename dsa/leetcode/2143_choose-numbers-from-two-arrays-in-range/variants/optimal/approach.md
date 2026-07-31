## General

**Express balance as a signed difference**

Treat choosing `nums1[i]` as adding `nums1[i]` to a difference and choosing
`nums2[i]` as subtracting `nums2[i]`. A selection is balanced exactly when its
final difference is zero.

**Keep only ranges ending at the current index**

For each index, maintain a map from difference to the number of choice patterns
for ranges ending at the preceding index. Start two new singleton patterns,
one with difference `nums1[i]` and one with difference `-nums2[i]`. These must
be added separately even if their keys coincide, because choosing different
arrays defines different selections.

Extend every preceding pattern in both possible ways. Replacing the map with
these starts and extensions ensures that its entries describe exactly all
ranges ending at `i`, without mixing in ranges that ended earlier. Add the
count at difference zero to the answer and reduce every count modulo
$10^9+7$.

Every balanced range has a unique right endpoint and a unique sequence of
extensions from its singleton start, so it is counted once. Conversely, every
zero-difference state corresponds to equal selected sums.

## Complexity detail

Define

$$
S = \sum_{i=0}^{n-1} \max(\texttt{nums1[i]},\texttt{nums2[i]}) + 1.
$$

There are $O(S)$ possible signed differences. Processing $n$ indices therefore
takes $O(nS)$ time and the current and next maps use $O(S)$ space.

## Alternatives and edge cases

- **Enumerate ranges and choice masks:** Trying all $2^k$ choices for each
  length-$k$ range is correct but exponential.
- **Restart difference DP at every left endpoint:** This avoids explicit choice
  masks but repeats suffix transitions and takes $O(n^2S)$ time.
- Choosing equal values from different arrays still creates distinct patterns.
- A zero chosen from one array contributes no magnitude but retains its array
  identity and must not be discarded.
- Only nonempty ranges are counted because every state starts at an actual
  index.
- Counts must be reduced modulo $10^9+7$ during transitions.
