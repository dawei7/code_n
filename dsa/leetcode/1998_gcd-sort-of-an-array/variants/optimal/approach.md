## General

**Turn legal swaps into connectivity**

Two values can be swapped directly when they share a prime factor. Even when two values have gcd one, they may exchange positions indirectly through a chain of other values.

This means the important object is not an individual swap but a connected component in the graph where values connect through shared prime factors. Values in one connected component can be permuted through a sequence of swaps along component edges.

The source represents these components with Disjoint Set Union.

**Precompute distinct prime factors**

`f[value]` is a list of distinct prime divisors. The outer sieve scans candidates from two through `mx = max(nums)`. If `f[i]` is already nonempty, some smaller prime divided `i`, so `i` is composite and is skipped as a prime candidate.

For a prime `i`, the inner loop visits every multiple `j` and appends `i` to `f[j]`. After the sieve, each value has exactly its distinct prime factors.

This is a factor-list version of the sieve of Eratosthenes and avoids trial-dividing every array occurrence independently.

**Union each value with its prime-factor nodes**

The DSU parent array `p` has nodes for numerical values and primes in the bounded domain. For every input value `i` and every factor `j` in `f[i]`, the assignment

`p[find(i)] = find(j)`

merges the value with that prime's component.

If two values share a factor, both become connected to the same prime node. If they are linked through several intermediate values and factors, transitive DSU connectivity captures that chain.

`find` uses path compression: after recursively locating the representative, it points the visited node directly to that root, accelerating later queries.

**Compare the current array with its sorted target**

`s = sorted(nums)` creates the desired non-decreasing arrangement without modifying `nums`.

At every index, if current value already equals target value, nothing must move. Otherwise, the source requires

`find(num) == find(s[i])`.

This says the current value occupying that position and the value that needs to arrive belong to the same swap-connected component.

If they differ, no legal sequence can transport the target value into this position, so the method returns false. If all positions pass, it returns true.

**Why component equality is necessary**

Every allowed direct swap occurs between values sharing a prime and therefore within one DSU component. A sequence of such swaps never moves a value across components.

Thus, if a position currently contains a component different from the component of its sorted target, sorting is impossible.

**Why component equality is sufficient**

Within a connected graph, swaps along edges can realize any permutation of the items on its vertices: one can move an item along paths through successive adjacent swaps. The gcd graph's DSU component represents exactly such connectivity.

If every current position and target value agree by component, each component has the same multiset of values/positions required before and after sorting. Values can be rearranged internally to their sorted locations. Duplicate numeric values cause no difficulty because identical occurrences are interchangeable.

Therefore the per-index component test is both necessary and sufficient.

**A chain can enable a swap**

Values seven and three have gcd one, but with 21 present they belong to one component: seven shares factor seven with 21, and 21 shares factor three with three. Legal swaps through 21 can rearrange all three values. DSU captures this transitive permission even though the endpoints cannot swap directly.

**Fixed allocation detail**

The exact source allocates `p` for `10**5 + 10` nodes regardless of the actual maximum. This is safe under constraints and has fixed-domain space proportional to the maximum allowed value, not merely the largest current input when analyzing implementation bytes.

## Complexity detail

Let $M=\max(\texttt{nums})$ and $N$ be array length. The factor sieve takes $O(M\log\log M)$ aggregate factor-appending work. Unioning all distinct factors costs $O(N\log M)$ as a simple upper bound, with near-constant inverse-Ackermann DSU operations. Sorting costs $O(N\log N)$.

Total matches the manifest's $O(M\log\log M+N\log M+N\log N)$ bound. Factor lists and DSU storage use $O(M)$ space, plus $O(N)$ for sorted output.

## Alternatives and edge cases

- **Factor each number by trial division:** Avoids a full sieve when values are sparse, but repeated factorization can cost more.
- **Graph over array indices:** Connect indices sharing factors, but efficiently discovering those edges still needs factor buckets.
- **Attempt adjacent array swaps only:** The operation permits any two positions, and connectivity is over values, not neighboring indices.
- **Prime value:** Connects only through occurrences or other multiples of that prime.
- **Isolated value:** It can remain only where the sorted array requires the same component/value.
- **Transitive sharing:** Values need not have gcd greater than one directly if a chain connects them.
- **Duplicate values:** They share the same value node and are interchangeable.
- **Already sorted array:** Every position matches immediately and returns true.
- **Path compression:** Improves repeated representative queries.
- **No union by rank:** Correctness remains, though rank/size could improve robustness.
- **Values at maximum bound:** Fixed DSU allocation includes them safely.
- **Input preservation:** `sorted(nums)` creates a new target list and the original order is retained.
