## General

**Split the required sum of XOR values**

For a current point `(x, y)` and an earlier point `(p, q)`, let

$$
a = x \mathbin{\mathrm{XOR}} p.
$$

If their distance is `k`, the other coordinate must contribute $k-a$, so `y XOR q = k - a`. Both contributions are nonnegative, which limits $a$ to the integers from $0$ through `k`.

XOR is its own inverse. For a fixed $a$, the only possible partner coordinates are therefore

`p = x XOR a` and `q = y XOR (k - a)`.

Enumerate all `k + 1` choices of $a$ and look up each required pair `(p, q)` in a frequency map of points already processed. Add its stored frequency to the answer.

**Count each index pair exactly once**

Insert `(x, y)` only after all lookups for the current index. The map consequently contains exactly the eligible earlier indices, enforcing $i < j$ without a separate condition. Duplicate coordinates are stored as frequencies, so one lookup accounts for every earlier duplicate.

Every qualifying pair is found: its actual value $a = x \mathbin{\mathrm{XOR}} p$ appears in the enumeration and reconstructs its earlier endpoint. It is found only once because that XOR value uniquely determines $a$. Conversely, every map hit satisfies both reconstructed XOR equations, whose sum is `k`, so no invalid pair is counted.

## Complexity detail

Let $n$ be the number of points. For each point, the algorithm performs `k + 1` expected-constant-time hash lookups, taking $O(nk)$ expected time. The frequency map stores at most $n$ distinct coordinate pairs, using $O(n)$ space.

The benchmark fixes `k = 0` and uses $n$ as `size`, so the hash method performs one lookup per point. A correct pairwise comparison checks all $\binom{n}{2}$ index pairs, completes the three legal tiers, and fails the scaling verdict with $O(n^2)$ growth.

## Alternatives and edge cases

- **Check every pair:** Directly compute the distance for all $i < j$. This is simple and correct but costs $O(n^2)$ time.
- **Precompute all transformed partners:** Materializing every point's `k + 1` possible partners retains $O(nk)$ time but consumes unnecessary additional space.
- **`k = 0`:** Both XOR contributions must be zero, so only identical coordinate rows pair; a group of frequency $f$ contributes $\binom{f}{2}$.
- **Duplicate points:** Store frequencies rather than mere membership, because each earlier index forms a separate pair.
- **Zero contribution in one coordinate:** The enumeration must include both endpoints $a = 0$ and $a = k$.
- **Pair order:** Looking up before inserting prevents self-pairs and counts every unordered index pair once.
- **Hash behavior:** The time bound assumes expected constant-time tuple lookup; adversarial hash behavior is not required by the contract.
