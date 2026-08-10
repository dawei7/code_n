## General

**Encode both requirements as prefix-state equality**

Let `a` be the bitwise XOR of the prefix through the current index. XOR of subarray `l..r` is zero exactly when the prefix XOR before `l` equals the prefix XOR through `r`, because

$$
P_{r}\mathbin{\mathrm{XOR}}P_{l-1}=0
\iff P_r=P_{l-1}.
$$

For parity balance, assign `+1` to every even value and `-1` to every odd value. Let `b` be this prefix sum. A subarray has equal even and odd counts exactly when its balance difference is zero, which again means equal prefix balances at its boundaries.

Therefore a subarray satisfies both conditions exactly when the joint prefix state

`(prefix_xor, parity_balance)`

is the same at its two boundaries.

**Seed the empty prefix**

Before reading any element, XOR and balance are both zero at boundary index `-1`. The dictionary starts with `(0,0):-1`.

This seed allows a valid subarray beginning at index zero to be measured. If the current state returns to zero at index `i`, its length is `i-(-1)=i+1`.

**Update the state for each element**

`a ^= x` incorporates the current value into prefix XOR.

`b += 1 if x%2==0 else -1` updates the even-minus-odd count. Zero is classified as even because `0%2==0`.

If the resulting pair has appeared at earlier index `p`, the subarray `p+1..i` has both zero XOR and zero parity-balance change. Its length is `i-p`.

If the pair is new, the code records the current index.

As a small trace, begin from `(0,0)` at boundary `-1`. Reading odd value three changes the state to `(3,-1)`. Reading odd one changes it to `(2,-2)`. Later XOR and balance updates may return to either state; the interval between equal occurrences then cancels in both algebraic systems simultaneously.

**Keep only the earliest occurrence**

For a fixed current endpoint and state, pairing with the earliest equal state produces the longest possible subarray. Replacing that index with a later occurrence could only shorten every future candidate using the same state.

Thus the dictionary inserts a state once and never updates it. `ans` takes the maximum length over all repeated states.

For `[3,1,3,2,0]`, the joint state before index one and after index four matches for subarray `[1,3,2,0]`. Its XOR is zero, and it contains two odd and two even values.

**Why the pair cannot be reduced to one component**

Equal XOR prefixes alone allow parity-imbalanced subarrays. Equal balance prefixes alone allow nonzero XOR. Using the tuple requires both equalities simultaneously and counts only intersections of the two conditions.

Every valid subarray has unique prefix boundaries with equal joint states, so it is discovered at its right endpoint. Every discovered repetition produces a valid subarray by subtracting the two prefix invariants. The maximum is therefore exact.

Formally, XOR is self-inverse, so equal boundary XORs yield zero without requiring ordinary subtraction. Signed parity balance does use subtraction, and equal values yield zero. Tuple equality demands both facts at once.

The dictionary value is an index rather than a count because the task asks only for maximum length. If the task asked how many valid subarrays exist, every occurrence frequency would matter instead of only the earliest index.

**Why contiguity follows from prefix boundaries**

The interval after an earlier prefix and through a later prefix is always one contiguous subarray. The method does not accidentally select a subsequence even though it stores only aggregate states; boundary subtraction/XOR includes every position between them.

## Complexity detail

Let `n` be the array length. The scan performs expected constant-time dictionary operations per element, giving expected $O(n)$ time.

At most `n+1` distinct joint states are stored, so auxiliary space is $O(n)$. XOR values and balances fit in ordinary integer state; Python tuple hashing supplies the expected-time qualification.

## Alternatives and edge cases

- **Enumerate all subarrays:** Incremental XOR and counts still require $O(n^2)$ endpoint pairs. Prefix-state hashing reduces this to linear expected time.
- **Store latest state indices:** This finds valid ranges but can miss the longest one. Earliest indices maximize length.
- **Track even count and odd count separately:** Only their difference matters for equality, so one signed balance is sufficient.
- **Use element sum parity:** Equal numbers of even and odd elements is not determined by numeric sum parity.
- **Target XOR only:** The tuple must include parity balance as a second independent invariant.
- **Single zero:** XOR is zero but parity counts are one even and zero odd, so the answer remains zero.
- **Whole-array solution:** The empty-prefix seed detects it when the final state is `(0,0)`.
- **No valid subarray:** No useful state repetition occurs and `ans` remains zero.
- **Zero values:** They alter no XOR but do add one to the even count.
- **Negative balance:** More odd than even prefixes are expected; dictionary keys handle negative integers.
- **Duplicate values:** XOR and parity updates operate per position, so every occurrence is accounted for.
- **State repeats many times:** The first occurrence stays stored, while every later repeat tests a potentially longer endpoint.
- **Even and odd counts both zero:** Only the empty interval has this property before scanning; nonempty valid intervals contain at least one of each parity.
