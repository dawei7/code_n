## General

**Count permutations that come before the given one.** Lexicographic rank is determined position by position. At index $i$, every still-unused value smaller than `perm[i]` could occupy this position and would create a permutation that is lexicographically smaller, regardless of how its suffix is arranged.

If $r=n-i-1$ positions remain after the current one, each smaller available choice creates exactly $r!$ suffix permutations. Therefore, the zero-based rank is:

$$
\sum_{i=0}^{n-1}
c_i\,(n-i-1)!,
$$

where $c_i$ is the number of values smaller than `perm[i]` that have not appeared earlier. These $c_i$ values are the permutation's Lehmer-code digits.

**Why a simple value formula needs a data structure.** Since `perm` contains values 1 through $n$, there are `x - 1` values smaller than current `x` in total. Some have already appeared in the fixed prefix and are no longer available. The source uses a Binary Indexed Tree, or Fenwick tree, to count those seen values efficiently.

The tree stores one at value position `x` after `x` has been processed. Its prefix query `tree.query(x)` returns how many seen values are at most `x`. Because a permutation never repeats `x`, the current value is not yet in the tree, so this is also the number of seen values strictly smaller than `x`.

Thus:

`cnt = x - 1 - tree.query(x)`

is exactly the number of unused smaller values.

**Fenwick prefix queries.** Internal array `c` uses 1-based indices. To query a prefix, the method repeatedly adds `c[x]` and clears the lowest set bit with:

`x -= x & -x`.

Each stored Fenwick cell summarizes a block ending at its index. Removing the lowest set bit jumps to the preceding disjoint block. At most $O(\log n)$ blocks cover a prefix.

**Fenwick updates.** `update(x, 1)` marks value `x` as seen. It adds one at all Fenwick cells whose summarized ranges contain `x`, moving upward by:

`x += x & -x`.

This also takes $O(\log n)$ time. The tree is created with `n + 1` as its logical size, giving one unused extra capacity but not affecting correctness.

**Precompute factorial weights modulo the answer modulus.** Array `f` has length $n$ and starts with ones. For `i >= 1`:

`f[i] = f[i - 1] * i % mod`.

By induction, `f[i]` stores $i!$ modulo $10^9+7$. At permutation position `i`, the required suffix weight is `f[n - i - 1]`.

The source adds `cnt * factorial_weight` modulo the modulus to `ans`. It performs a final `ans % mod` after the loop. Keeping each term reduced is sufficient; `ans` may temporarily exceed the modulus by a factor of $n$, but Python integers safely hold it.

**A trace for `[3,1,2]`.** Factorials needed are $2!=2$, $1!=1$, and $0!=1$.

- At index zero, no values are seen. Two values, 1 and 2, are smaller than 3, so this position contributes $2\cdot2!=4$.
- Mark 3 seen.
- At index one, no unused value is smaller than 1, so the contribution is zero.
- Mark 1 seen.
- At index two, the only remaining value is 2 and no smaller unused value remains.

The rank is four, matching the listed lexicographic order.

**Why the sum counts each earlier permutation exactly once.** Take any permutation lexicographically smaller than `perm` and locate its first differing position $i$. Its prefix before $i$ equals the target prefix, and its value at $i$ is one of the $c_i$ smaller unused choices. Its remaining values can appear in any of $(n-i-1)!$ orders. The term for $i$ counts exactly these permutations. Different first-difference positions form disjoint groups, so summing all terms neither misses nor double-counts.

**Zero-based indexing appears naturally.** The identity permutation `[1,2,\ldots,n]` has every `cnt=0`, yielding rank zero. No extra subtraction is needed.

## Complexity detail

Factorial preprocessing takes $O(n)$ time. Each of the $n$ permutation values performs one Fenwick query and one update, each $O(\log n)$. Total time is $O(n\log n)$.

The Fenwick array and factorial array each contain $O(n)$ integers, so auxiliary space is $O(n)$. The use of `__slots__` avoids a normal attribute dictionary for the one tree object but does not change asymptotic storage.

Modulo arithmetic bounds factorial entries, while tree counts never exceed $n$.

## Alternatives and edge cases

- **Order-statistics balanced tree:** Store unused values and ask how many are smaller at each position. It gives the same $O(n\log n)$ bound.
- **Segment tree:** Supports the same prefix-count queries but uses more code and usually a larger constant.
- **Scan unused values:** A Boolean array plus a linear prefix count at every position takes $O(n^2)$ time.
- **One-element permutation:** Its only rank is zero; `f[0]` supplies $0!=1$ but `cnt` is zero.
- **Identity permutation:** Every Lehmer digit is zero.
- **Reverse permutation:** Every digit is as large as possible, producing rank $n!-1$ before the required modulo.
- **Current value not yet seen:** This permutation guarantee makes `query(x)` equivalent to counting seen values below `x`.
- **No duplicates:** Fenwick cells contain occurrence counts of zero or one at leaf values.
- **Factorial zero:** `f[0]=1` correctly represents the one empty suffix arrangement.
- **Large rank:** Terms are reduced modulo $10^9+7$ as required.
- **Final modulo:** Needed because `ans` is a sum of already reduced terms and may still exceed the modulus.
- **Tree size `n + 1`:** The extra logical slot is harmless.
- **Input order:** `perm` is read only and never sorted; original order is the object being ranked.
- **Fenwick bit operation:** `x & -x` isolates the least significant set bit controlling block size.
- **Zero-based output:** The Lehmer factorial sum directly counts earlier permutations, so it is already an index.
