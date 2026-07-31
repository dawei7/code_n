## General

An index selected by both subsequences contributes its value twice to `X XOR Y`, so it cancels. An index selected by exactly one contributes once, and an index selected by neither contributes nothing. Therefore `X XOR Y` is precisely the XOR of the symmetric difference of the two index sets.

Every subset can occur as such a symmetric difference: choose that subset as the first subsequence and choose the second subsequence empty. Preserving order imposes no further restriction because any index subset is a subsequence. The problem is consequently identical to finding the maximum XOR obtainable from any subset of `nums`.

**Build a binary linear basis.** Store at most one basis vector for each highest set bit. To insert a value, inspect bits from high to low. If a basis vector already owns the current highest bit, XOR it away; otherwise store the reduced value at that bit. A value reduced to zero was already representable. These elimination steps preserve the span of all subset XORs.

After processing every value, greedily improve an initially zero answer from the highest pivot downward. Replace the answer by its XOR with a basis vector exactly when that produces a larger integer. A higher bit dominates every lower bit, so each greedy decision is optimal and the final value is the maximum element of the represented XOR span.

## Complexity detail

Each of the $n$ values examines at most $B=31$ bit positions, and maximizing examines the basis once. Time is $O(nB)$ and the basis occupies $O(B)$ space. Under the fixed input bound, both simplify to linear time and constant auxiliary space.

The benchmark defines its size as $n$ and supplies independent powers of two. The accepted basis remains linear in $nB$. A calibrated correct alternative enumerates all $2^n$ subsets and evaluates their XORs, preserving every output while showing exponential growth.

## Alternatives and edge cases

- **Enumerate all subsets:** It directly expresses the reduced problem but requires exponential time.
- **Track reachable XORs in a set:** Repeatedly adding `value XOR reachable` is correct, yet the state space can grow exponentially before the 31-bit cap helps.
- **Disjoint-subsequence assumption:** The subsequences may overlap; overlap cancels in the final XOR rather than creating an extra restriction.
- **Empty subsequences:** They establish that every ordinary subset XOR is achievable and ensure zero is always a candidate.
- **Duplicate values:** Equal vectors are linearly dependent; inserting the later copy reduces to zero.
- **Zero values:** Zero changes neither the span nor the maximum.
- **Combination beats every element:** The optimum can require XORing several independent basis vectors.
