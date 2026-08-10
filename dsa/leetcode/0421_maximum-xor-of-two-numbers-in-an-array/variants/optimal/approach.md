## General

**Maximize binary digits from most significant to least significant**

XOR produces a `1` at a bit position when its two input bits differ and a `0` when they agree. To maximize the numeric XOR, the highest bit matters more than every lower bit combined. Therefore, for a fixed number `x`, the best partner should differ from `x` at the most significant possible bit; after that choice, it should differ at the next bit whenever possible, and so on.

A binary trie stores all input numbers by their bit prefixes and makes that greedy choice efficient. Each trie node has two child slots: child `0` represents a number with zero at the next bit, and child `1` represents a number with one. A root-to-leaf path records one complete 31-bit number.

The constraints limit values to $2^{31}-1$, so bit positions `30` down through `0` cover every possible value, including leading zeros. Using the same fixed width for all numbers is essential: trie depth then corresponds to the same bit significance for every path.

**Build the trie**

`Trie.children` is a two-element list initialized to `[None, None]`. `__slots__ = ("children",)` prevents each node from needing an unrestricted instance dictionary; this reduces object overhead but does not change the algorithm.

To insert `x`, the loop visits bit positions from 30 down to 0. The expression `x >> i & 1` shifts bit `i` into the least-significant position and masks everything else, yielding either zero or one. If the corresponding child does not yet exist, a new `Trie` node is created. Moving to that child continues the prefix.

Shared prefixes reuse nodes. Duplicate numbers follow an existing complete path and require no new branches. After all insertions, every input value has a 31-level path from the root.

**Search for the best partner of one number**

`search(x)` starts at the root with `ans = 0`. At bit position `i`, let `v` be `x`'s bit. The preferred partner bit is `v ^ 1`, the opposite bit. If that child exists, choosing it makes XOR bit `i` equal to one, so the code executes `ans |= 1 << i` and follows the opposite branch.

If the opposite branch does not exist, every number with the already chosen prefix has the same bit `v` at this position. The XOR bit must be zero, and the search follows `children[v]` without modifying `ans`.

The fallback child is guaranteed to exist. At every level, the current node represents at least one inserted number, so if it lacks the opposite child it must have the same-bit child.

**Why choosing the opposite bit greedily is safe**

Suppose an opposite-bit branch exists at position `i`. Any partner in that branch gives XOR bit `i = 1`; every partner in the same-bit branch gives zero there. Earlier, more significant XOR bits are already identical because search follows one fixed chosen prefix. A one at bit `i` contributes $2^i$, which is greater than the maximum possible advantage from all lower bits combined, $2^i-1$. Therefore no selection in the same-bit branch can compensate for losing this one.

Once the best possible bit at `i` is fixed, the same reasoning applies recursively to the next lower bit inside the selected branch. This proves that the root-to-leaf greedy walk returns the maximum XOR obtainable between `x` and any inserted number.

For example, comparing binary prefixes of `5` and `25`, the trie can choose opposite high bits and eventually obtains `5 XOR 25 = 28`, whose binary form is `11100`.

**Find the global maximum**

The solution first inserts every number, then evaluates `trie.search(x)` for every `x`. Each search returns the best partner value for that particular input. Taking `max(...)` across all inputs therefore considers the best pair involving every possible first member and yields the global maximum.

The contract permits `i <= j`, so pairing a number with itself is legal. This matters when the array has one element: the trie contains its own path, search follows it wherever no alternative exists, and the XOR is zero. Even under the common distinct-index formulation, inserting all values is safe for arrays of at least two because choosing self produces zero and cannot hide a positive available XOR; duplicate zero answers are also valid.

The trie returns the XOR value directly rather than the partner number. Every chosen branch belongs to at least one complete inserted path, so the constructed bits always correspond to a real pair.

## Complexity detail

Let $n$ be the number of input values and let $B=31$ be the fixed number of processed bits. Insertion costs $O(B)$ per number, and search costs $O(B)$ per number. Total time is $O(nB)$, which is $O(n)$ because $B$ is fixed by the 31-bit constraint.

In the worst case, each inserted number creates up to $B$ new trie nodes, so space is $O(nB)$, simplified to $O(n)$ for fixed-width integers. The generator used by `max` is lazy and does not allocate a separate list of all search results.

If integer width were an input-dependent quantity rather than a fixed constraint, the more general bounds would be $O(n\log M)$ time and space, where $M$ is the maximum value.

## Alternatives and edge cases

- **Check every pair:** Direct XOR comparison takes $O(n^2)$ time, which is too slow for up to $2\cdot10^5$ numbers.
- **Greedy prefix hash sets:** Build the maximum answer bit by bit and test whether two observed prefixes can realize each proposed prefix XOR. It also takes $O(nB)$ time and $O(n)$ space, but the trie gives a concrete best-partner path.
- **Insert and query incrementally:** Query each value against previously inserted values, then insert it. This avoids self-pairing and has the same bounds, but the chosen code cleanly separates construction and queries.
- **Variable-width paths without leading zeros:** Misaligned depths would compare bits of different significance. Fixed 31-bit paths avoid that error.
- **Single element:** The only legal pair is the value with itself, producing zero.
- **All values equal:** Every trie search follows identical bits and returns zero.
- **Zeros:** Zero is represented by 31 zero bits and participates normally.
- **Maximum allowed value:** Bit 30 is its highest possible set bit, so the `range(30, -1, -1)` loop covers it exactly.
- **Duplicate paths:** Insertion reuses existing nodes; duplicates do not increase the asymptotic node count or change the maximum.
- **Prefer lower-bit gains over a high bit:** This is never beneficial because bit $i$ outweighs all lower positions together, which is the foundation of the greedy search.
