## General

The transformation is divided into independent contiguous segments. For every possible segment, the source computes:

- cost without reversing it;
- one reversal plus the remaining cost after reversed alignment.

A prefix partition DP then chooses segment boundaries minimizing total operations.

**Cost for a fixed alignment**

`calc(l,r,rev)` aligns each target position `i` with a source character:

- direct alignment uses `word1[i]`;
- reversed alignment uses `word1[r-(i-l)]`.

Matching characters require no action. A mismatch is represented by directed pair `(a,b)`, meaning source character `a` must become target character `b`.

A replacement fixes one mismatch for one operation.

A swap can fix two mismatches together precisely when they are reciprocal:

- one position needs `a -> b`;
- another needs `b -> a`.

Swapping those two source characters satisfies both targets in one operation instead of two replacements.

**How the Counter measures operations**

`cnt` stores unmatched directed mismatch pairs. `res` starts at zero.

For mismatch `(a,b)`:

- if reciprocal `(b,a)` is pending, one copy is removed and `res` does not increase; the pair of mismatches is handled by the one operation already counted when the first mismatch appeared;
- otherwise `(a,b)` is stored and `res` increments, provisionally treating it as one required operation.

Thus every unpaired mismatch contributes one replacement, while every reciprocal pair contributes one swap.

The per-index restrictions make nonreciprocal swaps unhelpful for reducing operation count. A swap that does not fix both involved mismatches still leaves at least one of those indices needing another same-type participation or a replacement; it cannot beat handling unmatched directions individually under the stated one-use limits.

**Optional reversal**

For segment `[j,i-1]`, direct cost is `calc(...,False)`.

The reverse alternative costs:

`1 + calc(...,True)`.

The added one is the substring-reversal operation itself. After reversal, mismatch pairing is evaluated against the reversed source order.

The source takes the minimum of direct and reversed costs. It may decline to reverse even when reversal is possible, as required by “can perform” rather than “must perform.”

For a one-character segment, reversal changes nothing and adds one, so direct alignment always wins.

**Partition DP**

`f[i]` is the minimum operations to transform prefix `word1[0:i]` into `word2[0:i]`. Base `f[0]=0` represents empty prefixes.

For every end `i` and previous cut `j<i`, the final segment is `[j,i-1]`. Its optimal local cost is `t`, and the candidate complete cost is `f[j]+t`.

Taking the minimum over all `j` considers every possible final segment and therefore every partition.

Operations are restricted within each chosen substring, so different segments do not interact. Their costs add, making this optimal-substructure recurrence valid.

**Why every transformation is represented**

Any legal solution chooses a final partition. Focus on its last segment. The preceding segments form a legal solution for prefix length `j`, and the last segment either uses no reversal or one reversal, followed by swaps and replacements.

`calc` gives the minimum swaps/replacements for that alignment, while the transition includes both reversal choices. By induction, `f[j]` is optimal for the prefix. Therefore the DP candidate is no worse than that legal solution.

Conversely, every DP transition combines legal independent segment operations, so the computed minimum is attainable.

**The exact complexity differs from the manifest**

The manifest claims `O(n^2)` time and `O(n^2)` space, suggesting segment costs were precomputed or updated incrementally.

The actual source calls `calc` twice for every pair `(j,i)`. Each call loops through the entire segment, so segment work is recomputed repeatedly. No two-dimensional cost table is stored.

## Complexity detail

There are `O(n^2)` candidate segments. For a segment of length `L`, the two `calc` calls cost `O(L)` time. Summing lengths over all substrings is `O(n^3)`:

$$
\sum_{L=1}^{n} (n-L+1)L = O(n^3).
$$

Therefore exact time complexity is `O(n^3)`, not `O(n^2)`. With `n\le100`, this remains practical.

The DP array uses `O(n)` space. Each Counter contains at most the constant `26^2` directed letter-pair keys and exists only during one call. No segment-cost matrix is retained. Auxiliary space is `O(n)`, not the manifest’s `O(n^2)`.

Temporary generator/counter objects do not change this bound under the fixed lowercase alphabet.

## Alternatives and edge cases

- **Precompute all segment costs:** Filling direct and reversed costs incrementally can support an `O(n^2)` partition DP at the expense of `O(n^2)` storage, matching the manifest’s likely intended method.
- **Memoize calc results:** Caching both alignment costs avoids recomputation but still requires computing each segment once and storing quadratic results; each initial calculation remains length-dependent unless further optimized.
- **Only replacements:** Counting mismatches is correct but misses reciprocal pairs that one swap can fix.
- **Arbitrary character-frequency matching:** Equal multisets do not mean one swap suffices; the directed reciprocal pairing respects the one-swap-per-index restriction.
- **Already matching segment:** Direct `calc` returns zero, so reversal is never chosen unnecessarily.
- **Reversal alone solves a segment:** Reversed `calc` returns zero and total local cost is one.
- **Reciprocal mismatch pair:** It costs one swap rather than two replacements.
- **Unpaired mismatch:** It contributes one replacement.
- **Repeated mismatch directions:** Counter multiplicity ensures only available reciprocal copies are paired.
- **One-character segment:** Direct replacement costs zero or one; reversal cannot improve it.
- **Whole-string partition:** The transition with `j=0` considers using one segment.
- **Single-character partitions:** Every position can always be handled independently, guaranteeing a finite solution.
- **Equal input lengths:** Alignment indices are valid for every shared segment boundary, as guaranteed.
- **Modulo not needed:** Operation counts are small and exact; no modular arithmetic applies.
