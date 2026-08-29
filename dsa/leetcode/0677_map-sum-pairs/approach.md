## General

**Store each prefix's answer inside a trie**

A `sum(prefix)` query asks for all keys beginning with the same character sequence. In a trie, all such keys pass through the node representing that prefix.

The exact implementation stores an aggregate `val` at every non-root trie node:

`node.val = sum of the current values of all inserted keys that pass through this node`.

With this invariant, a prefix query only has to follow its characters and return the aggregate at the final node. It does not traverse all descendant keys during the query.

**Trie structure**

Each node has:

- a 26-element `children` array for lowercase letters;
- an integer `val` for the prefix aggregate.

Character `c` maps to `ord(c) - ord("a")`. The source guarantees lowercase English letters, so every index is between zero and twenty-five.

A path from the trie root spells a prefix. Several keys with the same beginning share those nodes and therefore contribute to the same aggregates.

**Why overwriting a key needs a delta**

`insert(key, val)` overrides the old value when the key already exists. Simply adding the new `val` along the path would double-count the old contribution.

The separate dictionary `d` stores the current exact value for every full key. The update amount is:

`x = new_value - old_value`.

The code obtains the old value as `self.d[key]`. Because `d` is a `defaultdict(int)`, a never-inserted key has old value zero.

After computing `x`, it stores the new full-key value in `d` and adds only `x` to every trie node on the key's path.

**Examples of positive, zero, and negative deltas**

On first insertion `("apple", 3)`, the old value is zero, so the delta is three. Prefix nodes for `a`, `ap`, `app`, `appl`, and `apple` each gain three.

If `"apple"` is later overwritten with five, the delta is two. Adding two raises every affected prefix total from its old contribution of three to the new contribution of five.

If it is overwritten with one, the delta is negative four. Subtracting four removes the excess old contribution. Although inserted values are positive, update deltas can be negative.

If the same value is inserted again, the delta is zero. The traversal may still occur, but all aggregates remain unchanged.

**Insert along the path**

`Trie.insert(w, x)` begins at the root. For each key character:

1. Compute its child index.
2. Create a child node if necessary.
3. Move to that child.
4. Add delta `x` to that node's aggregate.

The root aggregate is not updated. Prefix queries are guaranteed nonempty, so every legal query ends at a child node and does not need an empty-prefix total.

**Answer a prefix query**

`Trie.search(w)` follows the prefix characters.

If a required edge is absent, no inserted key has that prefix, so it returns zero immediately. Otherwise, after consuming every prefix character, the reached node's `val` is returned.

There is no need for terminal markers because queries ask for prefix sums, and the full-key dictionary already handles overwrite identity. A key may itself be a prefix of a longer key; both contributions pass through its final node and are correctly included there.

**A shared-prefix walkthrough**

After inserting `"apple" = 3`, querying `"ap"` reaches the `ap` node whose aggregate is three.

Insert `"app" = 2`. Its delta two updates nodes `a`, `ap`, and `app` but stops there. Now:

- `sum("ap")` is five because both keys share that prefix;
- `sum("apple")` is three because only the longer key reaches that node;
- `sum("app")` is five because `"app"` itself and `"apple"` both begin there.

**Why the aggregate invariant remains true**

Initially, no keys exist and every node aggregate is zero.

Suppose the invariant holds before an insertion. Changing one key from old value to new value changes the correct sum for exactly the prefixes of that key, and each such sum changes by `new - old`. The trie update visits exactly those prefix nodes and applies exactly that delta. All unrelated prefix nodes remain unchanged.

Therefore, the invariant holds after every insertion. A search that reaches a prefix node returns its correct current sum, while a missing node correctly represents an empty key set.

## Complexity detail

Let `K` be a key length and `P` a queried prefix length.

One insertion performs one dictionary access and walks `K` trie edges, taking expected `O(K)` time. One sum query walks at most `P` edges, taking `O(P)` time.

Across `I` inserts of representative key length `K` and `Q` queries of representative prefix length `P`, this is `O(IK + QP)`, matching the manifest. More precisely, use the sums of the actual inserted and queried string lengths.

The trie creates at most one node per distinct inserted prefix, bounded by the total inserted-key characters. Each node has 26 references, a fixed constant. The exact-value dictionary stores every distinct full key. Total persistent space is `O(IK)` under the same aggregate notation.

## Alternatives and edge cases

- **Brute-force dictionary scan:** Store full key-value pairs and test `key.startswith(prefix)` for every query. Insert is simple, but a query can inspect every key and character.

- **Prefix hash map:** During insertion, update a hash-map total for every prefix using the same delta. Queries become expected `O(P)` to hash the prefix or effectively constant after string hashing, but repeated prefix strings consume storage.

- **Trie with descendant traversal at query time:** Store values only at terminal nodes and sum descendants for each query. This makes queries proportional to the matching subtree instead of prefix length.

- **Overwrite without subtracting the old value:** This overcounts every prefix of a repeated key. Delta propagation is the central correctness step.

- **New key:** The default old value zero makes the delta equal to the inserted value.

- **Same key and same value:** Delta zero leaves all prefix sums unchanged.

- **Overwrite with a smaller value:** A negative delta correctly lowers aggregates.

- **One key prefixes another:** The shared node aggregate includes both values, as required by “starts with.”

- **Missing prefix:** Search encounters a null child and returns zero.

- **Prefix equals a full key:** The result includes that key and every longer key beginning with it.

- **Empty prefix:** The formal constraints require a nonempty prefix. The exact root aggregate is not maintained, so an empty query would return zero rather than the sum of all keys.

- **Lowercase alphabet:** Array indexing relies on it. A dictionary of children would be needed for arbitrary characters.

- **Duplicate dictionary identity:** `d` distinguishes full keys, while trie nodes intentionally combine shared prefixes.

- **Persistent side structures:** Both the trie and `d` are necessary in this design: the trie answers prefixes, and `d` supplies old values for replacement deltas.
