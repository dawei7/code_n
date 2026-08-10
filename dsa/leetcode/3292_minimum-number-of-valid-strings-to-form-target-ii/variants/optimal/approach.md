## General

**Separate the problem into matching and minimum covering.** At each target position $i$, first determine the longest substring beginning there that is a prefix of any word. Call that length $d_i$. Because every shorter prefix of a valid prefix is also valid, position $i$ can start a piece ending at any position from $i+1$ through $i+d_i$. Once all such reaches are understood, the second task is to cover the entire target with the fewest consecutive pieces.

The exact source accelerates the matching task with polynomial rolling hashes. It does not use the deterministic Z-functions mentioned in the manifest summary. `Hashing(target, base, mod)` builds two arrays. `h[r]` is the hash of the first $r$ target characters, and `p[r]` is `base` raised to $r$ modulo `mod`. The query

`(h[r] - h[l - 1] * p[r - l + 1]) % mod`

returns the hash of the one-based target interval from $l$ through $r$. Precomputation makes every substring-hash query $O(1)$.

**Index all valid prefixes by length.** Let $m$ be the maximum word length. The source creates `s[0]` through `s[m]`, where `s[length]` is a set containing the rolling hash of every word prefix of that exact length. It processes each word from left to right, updating the prefix hash one character at a time and inserting it into the corresponding set. Duplicate prefixes collapse naturally because sets preserve only membership, which is all the algorithm needs.

For a target start $i$, helper `f(i)` binary-searches a length between zero and `min(n - i, m)`. For a proposed `mid`, it hashes `target[i:i+mid]` through the one-based call `query(i + 1, i + mid)` and checks membership in `s[mid]`.

Binary search is legal because the predicate is monotone. If a target substring of length $q$ equals a prefix of some word, then each of its first $p<q$ characters equals the length-$p$ prefix of that same word. Thus every smaller length is also valid. Once a length is invalid, no larger length can be valid, apart from the hash-collision caveat discussed below. `f(i)` therefore returns the maximum valid reach $d_i$.

**Convert reaches into minimum jumps.** Imagine target boundaries numbered $0$ through $n$. A valid piece starting at boundary $i$ can move to any boundary in $(i,i+d_i]$. The problem is now the same layered greedy structure as minimum jumps through an interval of reachable boundaries.

The source maintains three values:

- `ans` is the number of pieces already committed.
- `last` is the farthest boundary reachable with exactly those committed pieces.
- `mx` is the farthest boundary discovered using one additional piece from any start processed in the current layer.

At each index $i$, the code computes `dist = f(i)` and updates `mx = max(mx, i + dist)`. When `i == last`, every possible starting boundary reachable with the current number of pieces has now been considered. If `mx == i`, none of them advances beyond the boundary, so forming the target is impossible and the source returns `-1`. Otherwise it commits the next piece layer by assigning `last = mx` and incrementing `ans`.

Updating `mx` before testing the boundary is important: a piece that starts exactly at `last` is reachable and must be allowed to extend the next layer. The loop continues over all target indices, but each layer boundary guarantees those indices are reachable; if a layer ever cannot progress, the method exits immediately.

**Why the greedy layer boundary gives the minimum.** After finishing indices through the old `last`, `mx` is the farthest boundary reachable with `ans + 1` pieces from any boundary reachable with `ans` pieces. Choosing a shorter reach cannot expose a start beyond `mx` in fewer pieces, because all starts in the current layer have already been examined and their intervals begin no later than `last`. Therefore committing the farthest possible boundary never increases the number of future pieces. By induction, each increment of `ans` completes exactly one breadth-wise reachability layer, so the first layer reaching the end uses the minimum number of valid strings.

**The exact correctness guarantee is probabilistic.** The source uses one modulus, `998244353`, and one base, `13331`. Different strings can theoretically have the same modular hash. A collision can make membership appear true for a substring that is not actually a word prefix, potentially producing a false reach and an incorrect answer. This is usually very unlikely on ordinary data, but it means the implementation is not deterministic in the strict sense claimed by the manifest. Double hashing or direct verification could reduce or remove this risk at additional cost.

## Complexity detail

Let $S$ be the sum of all word lengths, $T=\lvert\texttt{target}\rvert$, and $L$ be the maximum word length. Constructing target hash and power arrays costs $O(T)$ time. Building every word-prefix hash performs one operation and expected-$O(1)$ set insertion per word character, totaling expected $O(S)$ time.

For each of the $T$ target starts, `f(i)` performs $O(\log\min(T,L))$ binary-search iterations, each with an $O(1)$ hash query and expected-$O(1)$ set lookup. The greedy scan itself is $O(T)$. Total expected time is therefore

$$
O\left(S+T\log\min(T,L)\right).
$$

This is tighter than the manifest's stated `O(S + WT)` and follows the exact source. The sets can retain one hash per word character in the worst case, so they use $O(S)$ space. Target hash and power arrays use $O(T)$, and the outer list of sets uses $O(L)$. Since $L\le S$, total auxiliary space is $O(S+T)$, or explicitly $O(S+T+L)$. The manifest's `O(T + L)` omits the potentially linear-in-$S$ prefix-hash memberships.

## Alternatives and edge cases

- **Z-function matching:** Concatenate each word with the target and use Z-values to update longest prefix matches. This is deterministic, but doing it independently for every word costs roughly $O(S+WT)$ and corresponds more closely to the manifest summary than to the exact source.
- **Trie scan from every target position:** It is simple and deterministic but can cost $O(TL)$ or $O(T^2)$ in repetitive inputs, which is too slow for target length up to $5\cdot10^4$.
- **Double rolling hash:** Store and compare a pair of residues. This keeps the same asymptotic bounds and makes accidental collision dramatically less likely, though it is still probabilistic.
- **Direct string verification after a hash hit:** It removes false positives but can destroy the fast worst-case matching bound if many long candidates require character-by-character checks.
- **Greedy longest piece only at the current committed boundary:** This misses possible extensions beginning at intermediate reachable positions. The `mx` scan must consider every start in the current layer before committing the next boundary.
- **No prefix starts at boundary zero:** Then `f(0) == 0`, `mx` remains zero, and the first boundary check returns `-1` immediately.
- **A gap after several pieces:** At a later `last`, if every start in the current layer ends no farther than that boundary, `mx == i` detects the unreachable suffix and returns `-1`.
- **Word longer than the remaining suffix:** `f(i)` caps its search at `n - i`, preventing out-of-range queries while still allowing every fitting prefix.
- **Repeated words or repeated prefixes:** Sets deduplicate equal hash values, which saves storage and does not change membership semantics.
- **Length zero during binary search:** Zero is the known-valid lower bound and is never queried from `s[0]`. The upward-biased midpoint ensures progress and returns zero when no positive prefix matches.
- **One-character target:** The first iteration either discovers reach one and returns one after the loop, or detects no progress and returns `-1`.
- **Hash-collision risk:** A single modular residue is not proof of string equality. The low practical probability should not be described as deterministic correctness.
- **Annotation mismatch:** `Hashing.__init__` annotates `s` as `List[str]`, while the caller passes the string `target`. Both support `len` and indexing, so runtime behavior is fine, but the annotation does not accurately describe the actual argument.
- **Manifest mismatch:** The protected source's algorithm and measured storage must govern this explanation: rolling-hash binary search gives expected $O(S+T\log\min(T,L))$ time and $O(S+T)$ space, not the Z-function method or the listed reduced storage.
