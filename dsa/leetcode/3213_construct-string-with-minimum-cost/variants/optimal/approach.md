## General

**Turn construction into prefix dynamic programming.** Appending words means the partially built string must always equal a prefix of `target`. Let `f[i]` be the minimum cost to construct exactly `target[:i]`. The empty prefix costs zero, so `f[0]=0`. Every other state begins at infinity to mean unreachable.

Suppose the last appended word has length $j$. It must equal substring `target[i-j:i]`, and the preceding operations must construct `target[:i-j]`. The transition is

$$
f[i]=\min\left(f[i],\,f[i-j]+\operatorname{cost}(\texttt{target}[i-j:i])\right).
$$

Evaluating all word lengths and every prefix endpoint finds every possible final word of every construction.

**Keep only relevant distinct lengths.** `ss = sorted(set(map(len, words)))` collects the distinct word lengths. At endpoint `i`, lengths appear in increasing order; once `j > i`, longer words also cannot fit, so the inner loop breaks.

Duplicate words or several words of the same length do not add length-loop iterations.

**Use rolling hashes for constant-time substring lookup.** Directly slicing and comparing each candidate substring could cost $O(j)$ per transition. The source computes polynomial prefix hashes of `target` with base $13331$ modulo $998244353$:

$$
h[i]=(h[i-1]\cdot base+\operatorname{ord}(target[i-1]))\bmod mod.
$$

The power table stores `p[j] = base^j mod mod`. The hash of `target[i-j:i]` is then

`(h[i] - h[i - j] * p[j]) % mod`.

The multiplication aligns the earlier prefix's polynomial positions; subtraction removes it, leaving the desired suffix hash. Python's modulo normalizes a negative intermediate into the standard nonnegative residue.

**Map word hashes to their cheapest cost.** For each word, the source computes the same polynomial hash and stores it in `d`. If multiple input entries hash to the same key, `d[x] = min(d[x], c)` keeps the lowest cost. For truly identical words, choosing a more expensive copy can never improve a construction, so this compression is correct.

`d` is a `defaultdict` returning infinity for a missing hash. A target substring with no stored key therefore creates an infinite candidate and leaves `f[i]` unreachable.

The source rebinds name `min` to a two-argument lambda. This shadows Python's built-in function but implements the two comparisons it needs. It affects only this method's local scope.

**Why the DP recurrence is correct if hash equality means string equality.** Any successful construction of prefix `target[:i]` has one final appended word. Removing it leaves a successful construction of a shorter prefix, represented by `f[i-j]`, and the transition considers its length and lookup. Thus the DP value is no greater than the optimum.

Conversely, every finite transition starts from a constructible prefix and appends a dictionary word matching the next target substring. It creates a valid construction with the summed cost, so the DP value cannot be below the true optimum. Induction over increasing `i` gives equality. If `f[n]` remains infinite, no sequence of matches reaches the entire target and the method returns $-1$.

For target `"abcdef"`, the DP can reach length three with word `"abc"` at cost one, length four with `"d"` at total two, and length six with `"ef"` at total seven. Other candidate endings are compared but do not improve it.

**The exact source is vulnerable to hash collisions.** A modular hash is not a proof of string equality. Two different strings can have the same residue. More seriously, `d` is keyed only by hash, not by `(length, hash)`. A word of one length that collides with a target substring of another considered length can be accepted because `d[x]` does not record which length produced it.

With one large modulus and typical lowercase inputs, accidental collisions may be rare, and the verified judge submission passed. Nevertheless, the implementation is probabilistic: an adversarial valid input can theoretically cause a false match or borrow the wrong cost. The correctness proof above is conditional on collision-free hashing for all relevant strings.

## Complexity detail

Let $N$ be target length, $S$ the total number of characters across `words`, $W$ the number of words, and $D$ the number of distinct word lengths.

Target hash and power construction takes $O(N)$. Hashing all words takes $O(S)$. Building the length set takes expected $O(W)$, and sorting its $D$ values costs $O(D\log D)$. The DP checks up to $D$ lengths for each of $N$ endpoints, costing $O(ND)$ expected time for dictionary lookups.

The precise total is

$$
O(N+S+D\log D+ND).
$$

The manifest's $O(ND+S)$ omits the explicit length-sort term. In many parameter regimes $ND$ dominates it, and $W\le S$, but retaining $D\log D$ describes the exact operations.

Arrays `h`, `p`, and `f` use $O(N)$ space. The hash map and length collection use $O(W+D)$ keys, bounded by $O(S)$. Total auxiliary space is $O(N+S)$, matching the manifest's broad bound.

## Alternatives and edge cases

- **Trie plus prefix DP:** From each reachable target position, walk a trie of words and relax matching endpoints. It performs exact character comparisons and avoids collisions, with cost depending on actual matched prefixes.
- **Aho–Corasick plus shortest-path DP:** Find all word occurrences in one automaton scan, then relax prefix costs. This is deterministic and efficient for many overlapping words but substantially more complex.
- **Double hash keyed by length:** Two independent moduli and a `(length, hash1, hash2)` key make collisions far less likely and prevent cross-length borrowing, though they still do not provide mathematical certainty.
- **Verify text after a hash hit:** Store candidate words per hash and compare actual substring characters. This restores determinism but can add comparison cost on collisions.
- **Direct substring dictionary:** Python slices create $O(j)$ text per tested length, potentially increasing time well beyond $O(ND)$.
- **Duplicate identical word:** Only its minimum cost matters; more expensive copies can be discarded safely.
- **Same hash, different word:** The exact map merges them and can become incorrect. This is a genuine source limitation, not just a complexity nuance.
- **Same hash across different lengths:** Because length is absent from the key, the exact source can treat a different-length word as a match for the currently tested substring.
- **Unreachable prefix:** Infinity prevents it from seeding a later finite construction.
- **Word longer than current prefix:** Sorted lengths allow an immediate break.
- **Word longer than target:** The constraints exclude it, but such a length would never fit any DP endpoint.
- **Entire target is one word:** The transition from `f[0]` reaches `f[N]` directly.
- **No construction:** `f[N]` remains infinity and returns $-1$.
- **Positive costs:** Cycles are impossible anyway because each append increases length, and positive costs make cheapest duplicate compression straightforward.
- **Built-in shadowing:** Local lambda `min` works for two arguments but would not support iterable-style calls; later maintenance must notice the rebinding.
