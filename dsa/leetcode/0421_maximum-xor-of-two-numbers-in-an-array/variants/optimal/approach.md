## General
**Build the answer from its most significant bit**

An XOR value is larger than another when its highest differing bit is `1`. Therefore decide the result from bit 30 down to bit 0. Once a high bit is known to be attainable, no choice involving lower bits can justify giving it up.

**Compare only the prefixes relevant to the current bit**

Extend a mask by one bit and store every number's prefix `number & mask` in a set. Suppose the already confirmed answer is `best`; tentatively set the new bit with `candidate = best | (1 << bit)`. Two full numbers can realize this candidate prefix exactly when their masked prefixes `p` and `q` satisfy `p ^ q = candidate`.

For a prefix `p`, the necessary partner is uniquely `candidate ^ p`. A set lookup tests whether that partner exists, so a single pass over the prefixes decides whether the candidate bit is feasible.

**Why each accepted prefix remains realizable**

At every iteration, `best` is the largest prefix attainable by some pair of input numbers. If the partner test succeeds, those two stored prefixes witness the candidate and it becomes the new `best`. If it fails, no pair can have that bit set while preserving the already chosen higher bits, so leaving the bit zero is forced. Induction over the descending bits makes the final 31-bit value the maximum complete XOR.

## Complexity detail
The algorithm performs 31 passes over `n` values. The integer width is fixed by the input contract, so time is $O(31n) = O(n)$. A prefix set can hold `n` values, giving $O(n)$ auxiliary space.

## Alternatives and edge cases
- **Binary trie:** insert every bit string and greedily follow the opposite bit for each number; it also takes $O(n)$ time and $O(n)$ space, with a larger implementation constant.
- **Pairwise comparison:** test every pair directly in $O(n^2)$ time and $O(1)$ auxiliary space.
- **Single element:** pairing the value with itself produces XOR zero.
- **Duplicate values:** equal values contribute zero but do not interfere with better pairs.
- **Zero and the highest allowed bit:** the prefix construction naturally handles leading zeros and values up to $2^{31} - 1$.
