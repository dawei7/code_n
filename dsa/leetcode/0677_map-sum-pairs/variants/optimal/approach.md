## General
**Store a total at every trie prefix**

Each trie node represents the prefix spelled along its root-to-node path and stores the sum of all key values sharing that prefix. A sum query follows its prefix characters and returns the reached node's total, or zero if an edge is missing.

**Convert replacement into a delta update**

Keep a separate map from complete keys to their current values. When inserting `key` with `value`, compute `delta = value - old_value`. Add this delta to the root and every trie node along the key. A new key contributes its full value, while replacing a key removes the old contribution and adds the new one without revisiting unrelated keys.

**Why every prefix total stays exact**

Initially all totals are zero. An insertion changes the contribution of exactly one key by `delta`; precisely the prefixes on that key's trie path should change by the same amount, and no other prefix includes the key. Inductively, every node total remains the sum of current values for its prefix. Following a query prefix therefore returns exactly the requested aggregate, including after any number of replacements.

## Complexity detail
Let `I` be the number of insertions, `K` the maximum key length, `Q` the number of sum calls, and `P` the maximum queried prefix length. Inserts take $O(K)$ time and queries take $O(P)$, for $O(IK + QP)$ across the operation sequence. At most one trie node is created per inserted character, so trie and key-value storage use $O(IK)$ space.

## Alternatives and edge cases
- **Hash every possible prefix:** update a hash-map total for each key prefix using the same delta; it has equivalent $O(K)$ insertion and $O(1)$ query time but materializes prefix strings.
- **Scan all stored keys per query:** keep only a key-value map and test `startswith`; insertion is simple, but each sum costs $O(DK)$ for `D` stored keys.
- **Trie without cached totals:** descend to the prefix and traverse its entire subtree for every query, making repeated broad-prefix sums unnecessarily expensive.
- Replacing an existing key must remove its old value rather than double-counting it.
- A prefix equal to a complete key includes that key and all longer keys sharing it.
- A prefix not present in the trie has sum zero.
