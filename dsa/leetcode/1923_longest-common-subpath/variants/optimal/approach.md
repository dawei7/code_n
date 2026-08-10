## General

**Search for a length instead of comparing every pair of subpaths**

Let $T$ be the total number of cities listed across all paths, and let $L$ be the length of the shortest path. A common subpath cannot be longer than $L$. More importantly, feasibility is monotone: if every friend shares some contiguous subpath of length $k$, then every friend also shares its prefix of every smaller length. Thus the possible lengths form an initial range from $0$ through the optimum.

The exact solution binary-searches this range with `l = 0` and `r = min(len(path) for path in paths)`. It chooses the upper middle `(l + r + 1) >> 1`. When `check(mid)` succeeds, `mid` is feasible and becomes the new lower bound. Otherwise it is too large, so the upper bound becomes `mid - 1`. The upper middle is necessary because the successful branch assigns `l = mid`; using the lower middle could repeat the same state. When the bounds meet, `l` is the largest feasible length.

**Represent each fixed-length window with a rolling hash**

Comparing every candidate window element by element would be expensive. The solution assigns a polynomial hash to every contiguous window. It uses base `133331` and modulus $2^{64}+1$. First it precomputes powers:

`p[k] = base^k mod mod`.

For each path, it builds a one-based prefix-hash array `h`. After processing city value `x` at prefix position `i`, it records `h[i] = h[i - 1] * base % mod + x`. Although the addition is not immediately followed by a remainder, every substring calculation takes a final remainder, and the next multiplication also reduces modulo `mod`. The stored value therefore supplies the same residue needed by the rolling-hash formula.

For a window beginning at one-based position `i` and ending at `j = i + k - 1`, its hash is

`(h[j] - h[i - 1] * p[k]) % mod`.

Multiplying the earlier prefix by `base^k` aligns it with the longer prefix. Subtracting cancels everything before the window, leaving the ordered polynomial contribution of exactly those $k$ city values. Python's remainder operator converts a negative difference to the canonical nonnegative residue.

The preprocessing arrays `p` and `hh` are built once. Every binary-search check reuses them, so computing a window hash takes constant expected-time arithmetic rather than rescanning its $k$ cities.

**Require a candidate to occur in every path**

For a proposed length $k$, `check` creates a global `Counter` named `cnt`. It scans every window in every prefix-hash array. Each path also receives a fresh local set `vis`. When a hash appears in that path, it is added to `vis` and its global count is incremented only if the same hash has not already appeared in that path.

This deduplication is essential. The question asks how many different friends' paths contain a subpath, not how many total occurrences exist. Without `vis`, one path containing the same window many times could increase a count to the number of friends by itself and create a false success.

After all paths are scanned, `max(cnt.values()) == m` asks whether some hash was seen in all $m$ paths. A count cannot exceed $m$ because each local set permits at most one increment per path. Therefore equality to $m$ means that the corresponding hashed window occurs at least once in every path.

For each positive $k$ tested by the binary search, every path has length at least $k$ because the search upper bound is the shortest path length. Each path consequently contributes at least one window, so `cnt` is nonempty and `max` is safe. Length zero is known to be feasible and is never passed to `check`.

**Why the result follows**

Assuming unequal windows do not collide under the chosen hash, `check(k)` is true exactly when a length-$k$ city sequence occurs in every path. The per-window formula gives equal hashes to equal sequences. Per-path deduplication makes the counter measure path membership, and a count of $m$ establishes membership in every path. Conversely, any genuinely common subpath produces the same hash once in each path and reaches count $m$.

Binary search then preserves the invariant that `l` is feasible and no answer can exceed `r`. A successful midpoint raises the known feasible length; a failed midpoint and monotonicity eliminate that midpoint and every longer length. At termination the two bounds are equal to the greatest feasible length.

The parameter `n`, the total number of possible city labels, is not used by the implementation. Hashing depends on the actual ordered values in `paths`; the label-range guarantee is sufficient, and no array indexed by all possible cities is needed.

**Hashing is probabilistic in the exact implementation**

The solution stores only one fixed hash per window and does not compare the underlying sequences after a hash match. Different sequences can theoretically produce the same residue, so correctness has a collision risk. The large modulus makes accidental collision unlikely for ordinary data, but it is not a mathematical impossibility. This caveat belongs to the exact code: binary search and counting are logically correct over hash identities, while the identification of a hash with a unique subpath is probabilistic.

## Complexity detail

Let $T=\sum_i\lvert\texttt{paths}[i]\rvert$, let $M$ be the maximum path length, and let $L$ be the minimum path length.

Building powers costs $O(M)$ time. Building every prefix-hash array costs $O(T)$ time. A single `check(k)` examines at most one window per path position, so across all paths it performs $O(T)$ hash, set, and counter operations. The binary search performs $O(\log L)$ checks. Under expected $O(1)$ hash-table operations and the standard constant-time model for fixed-modulus arithmetic, total time is $O(T\log L)$; the one-time $O(T+M)$ preprocessing is dominated when $L>1$.

The prefix hashes contain $T$ entries plus one sentinel per path, and the power array contains $M+1$ entries. Since $M\le T$, this is $O(T)$ space. During one check, the global counter and the collection of per-path hashes can contain $O(T)$ distinct residues in the worst case. Only one local `vis` exists at a time, but its maximum size is also $O(T)$. Peak auxiliary space remains $O(T)$.

Python integers are arbitrary precision. Values are repeatedly reduced by the fixed modulus, while products temporarily have a bounded number of bits determined by that modulus and base. This does not introduce a factor depending on $T$ in the conventional complexity model.

## Alternatives and edge cases

- **Direct window comparison:** One could store tuples for every length-$k$ window and intersect sets across paths. Tuple construction and hashing can inspect $k$ elements, raising a check toward $O(Tk)$ time and greatly increasing memory.
- **Intersect hash sets path by path:** Begin with the shortest path's hash set and intersect it with each later path's set. This has similar expected bounds and can shrink candidates early; the exact solution instead uses one counter and per-path deduplication.
- **Double hashing:** Tracking two independent modular hashes makes a false collision dramatically less likely while preserving the same asymptotic bounds, at the cost of extra arithmetic and storage.
- **Verification after hashing:** Hash matches could be checked against actual slices for deterministic confirmation. Care is required to avoid turning many adversarial matches into expensive repeated comparisons.
- **Suffix-array or suffix-automaton methods:** More sophisticated string algorithms can remove or control collision risk, but generalized handling across many integer paths is substantially harder to implement and explain.
- **No shared city:** Every positive-length check fails, so binary search leaves `l = 0` and the method returns zero.
- **A single shared city only:** Length one succeeds and length two fails, producing one even when the shared city appears at different positions.
- **Repeated visits within one path:** The local `vis` prevents repeated occurrences of the same hashed subpath in one friend's route from being mistaken for occurrences across several friends.
- **Opposite order:** Subpaths are contiguous ordered sequences. `[1, 2]` and `[2, 1]` normally have different polynomial hashes and are not treated as the same path.
- **Shortest path bound:** Searching only through the minimum path length is necessary because no longer sequence can occur in that shortest path.
- **One path much longer than the others:** Each check still scans windows from all paths, so its work is governed by total length $T$, not merely by the shortest path.
- **Consecutive duplicate restriction:** The statement disallows consecutive repetitions, but the hashing logic would still handle them. The algorithm does not rely on that restriction for its reasoning.
- **Hash collision:** Because the exact code uses one fixed base and modulus with no final sequence comparison, a collision can cause a false common-subpath result. This is the principal semantic risk of the implementation.
- **Empty paths:** The stated problem domain supplies paths suitable for the common-subpath search. If an empty path were allowed, the initial upper bound would be zero and the function would return zero without calling `check`.
