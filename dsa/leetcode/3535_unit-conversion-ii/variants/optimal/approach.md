## General

**The intended relative-factor idea**

Choose unit zero as a common reference. Define `F[u]` as:

the number of units of type `u` equivalent to one unit of type zero.

If these factors are known, a query from unit `A` to unit `B` is a ratio. One unit zero equals `F[A]` units of `A`, so one unit `A` equals `1/F[A]` units of zero. Converting onward to `B` gives:

`F[B] / F[A]`.

Modulo prime `MOD = 10^9+7`, division becomes multiplication by an inverse:

`answer(A,B) = F[B] * inverse(F[A]) mod MOD`.

This is the formula used by the protected query loop:

`res[y] * pow(res[x], mod - 2, mod) % mod`.

Fermat's little theorem gives `a^(MOD-2) mod MOD` as the inverse of nonzero `a`.

**How a forward conversion propagates a factor**

Conversion `[s,t,w]` means:

one unit `s` equals `w` units `t`.

If one unit zero equals `F[s]` units `s`, substituting the conversion gives:

`F[t] = F[s] * w`.

The source stores directed adjacency `s -> t` with weight `w` and recursively passes:

`mul * w % mod`.

Starting from `F[0] = 1`, this correctly computes all reference factors when every unit is reachable from zero following only the listed forward directions.

**Why the ratio formula is correct when all factors are valid**

Suppose `F[A] = p` and `F[B] = q` as exact rational conversion quantities relative to zero. Then:

one zero unit = `p` A units = `q` B units.

Dividing both equalities by `p` shows:

one A unit = `q/p` B units.

All input factors are between one and `10^9`, strictly below `MOD`. In the finite field modulo this prime, every factor is nonzero, and a product of nonzero factors remains nonzero. Therefore a correctly computed `F[A]` has a modular inverse.

The ratio also handles reverse and cross-branch queries without explicitly walking their paths. Shared factors from zero to a common ancestor cancel algebraically.

**What the protected DFS actually builds**

The source creates:

`g[s].append((t,w))`

for each conversion and adds no reverse adjacency. `dfs(0,1)` follows only these forward edges. It writes `res[s] = mul` and recursively visits each stored child.

No visited set or parent parameter is used. If the directed conversions happen to form an outward arborescence rooted at zero, every node is visited exactly once and the reference-factor algorithm works.

However, that outward orientation is not what this problem guarantees.

**Material correctness defect: reverse edges are missing**

The contract guarantees unique conversion from unit zero to every unit using a combination of forward or backward conversions. The underlying `n-1` conversions form a connected tree, but individual input edges may point toward or away from zero.

For a listed conversion `s -> t` with factor `w`, traversal from `t` back to `s` is legal with factor `1/w`. A correct bidirectional graph must include:

- forward adjacency `s -> t` with weight `w`;
- reverse adjacency `t -> s` with weight `inverse(w) mod MOD`.

The protected source includes only the first.

For a legal counterexample, take `conversions = [[1,0,2]]`. It states one unit of type one equals two units of type zero. Unit zero can uniquely convert to unit one by using that conversion backward, so the input satisfies the contract.

But `g[0]` is empty. DFS visits only zero, leaving `res[1] = 0`. Query `[0,1]` should return `inverse(2)`, while the source returns zero. Query `[1,0]` should return two, but it attempts to “invert” zero with `pow(0,MOD-2,MOD)` and again returns zero. Zero has no multiplicative inverse; Python's exponentiation returning zero does not make that operation valid.

The manifest summary says “Build a bidirectional conversion tree,” but the protected solution does not do so. This is a genuine source/manifest mismatch and a correctness failure for legal inputs.

**A second defect: recursive depth**

Even if every conversion happens to point outward from zero, the exact Python DFS can recurse once per node on a valid chain of length up to `100,000`. The source does not raise Python's recursion limit. It can therefore fail with `RecursionError` around depth one thousand.

An iterative traversal is needed for robust execution across the full constraints.

**What a correct traversal would maintain**

In a corrected bidirectional tree, an iterative stack can hold `(node,parent,factor)`. From edge traversal:

- use factor `w` in the listed forward direction;
- use `inverse(w)` in the reverse direction.

The parent prevents immediately walking back along the undirected tree. The invariant is that the carried factor equals `F[node]`. Since the underlying path from zero is unique, each node receives one unambiguous value.

After that preprocessing, the exact protected ratio formula answers every query in constant time.

**Same-unit queries expose unvisited factors too**

Mathematically, converting a unit to itself always yields one. For a correctly computed nonzero factor:

`F[u] * inverse(F[u]) = 1`.

But if the protected forward-only DFS leaves `u` unvisited with factor zero, even query `[u,u]` returns zero. This further demonstrates that zero initialization cannot safely represent a legal unit factor.

## Complexity detail

Under the stronger, unstated assumption that all nodes are forward-reachable, building adjacency and DFS take `O(n)` time, and each of `Q` modular inverse queries uses `pow` with exponent `MOD-2`. Since `MOD` is a fixed constant for problem analysis, this is treated as `O(1)` per query, giving `O(n+Q)` total time.

More explicitly, modular exponentiation costs `O(log MOD)` multiplications per query. Because `MOD` never changes, the manifest suppresses that constant factor.

Adjacency, factors, and the recursive stack use `O(n)` total asymptotic space. The recursion stack can reach `O(n)` and can fail practically in Python.

A corrected iterative bidirectional implementation keeps the same `O(n+Q)` problem-level time and `O(n)` space. It adds one reverse adjacency per conversion and can optionally precompute inverse factors during graph construction.

## Alternatives and edge cases

- **Correct bidirectional iterative traversal:** Add reciprocal weighted edges, track the parent, and compute every reference factor without recursion. This is the direct repair.
- **Walk the tree separately for every query:** Correct but can cost `O(nQ)`. Common reference factors reduce each query to one ratio.
- **Lowest common ancestor with path products:** Useful in more general dynamic settings, but unnecessary when all factors relative to one root can be precomputed.
- **Use ordinary integer fractions:** Exact rational numerators and denominators can grow rapidly. Modular factors and inverses match the required output.
- **Add reverse edges without a parent/visited check:** That creates immediate two-node recursion cycles. Bidirectional traversal must avoid returning to the parent.
- **Conversion oriented toward zero:** This is legal and is exactly the case the protected source misses.
- **Outward-only tree:** The factor logic works, subject to the recursion-depth defect.
- **Deep chain:** The recursive source may fail even with correct outward orientation.
- **Query from a unit to itself:** The correct answer is one; an unvisited zero factor makes the protected result wrong.
- **Factor one:** Forward and reverse factors are both one.
- **Cross-branch query:** The ratio `F[B]/F[A]` correctly cancels the shared root path when factors are valid.
- **Nonzero inverse guarantee:** Listed factors are less than the prime modulus, so valid path factors never become zero modulo `MOD`.
- **Zero in res:** It signals an unvisited node in this source, not a legitimate conversion factor.
- **Manifest mismatch:** The advertised bidirectional construction is absent from `solution.py` and must not be assumed.
