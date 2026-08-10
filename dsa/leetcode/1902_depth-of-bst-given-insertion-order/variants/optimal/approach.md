## General

**Avoid constructing child pointers.** To determine final tree depth, the algorithm only needs the depth assigned to each key when it is inserted. In a binary search tree built from distinct keys, a new value descends until it attaches beneath one of its closest already-inserted values in sorted order: its predecessor or its successor. The source keeps inserted keys ordered and derives the new depth from those two neighbors.

**Use sentinels so both neighbors always exist.** `SortedDict` starts with key `0` at depth zero, key `inf` at depth zero, and the first real key at depth one. Real values are a permutation of `1` through `n`, so zero is strictly below all of them and infinity is strictly above. Even a new global minimum or maximum therefore has a predecessor and successor. Sentinel depth zero makes a missing real neighbor contribute nothing.

**Locate predecessor and successor by rank.** For new value `v`, `sd.bisect_left(v)` returns the position where `v` belongs among sorted keys. Since permutation values are distinct and `v` has not been inserted yet, position minus one is its greatest smaller inserted key. The insertion position itself is its smallest greater inserted key. Variables `lower` and `higher` store these adjacent ranks.

The expression `sd.values()[lower]` retrieves the predecessor's recorded depth, while `sd.values()[higher]` retrieves the successor's depth in matching sorted-key order. This indexed values view is a feature of the ordered-map implementation, not an ordinary Python dictionary.

**Why the deeper neighbor becomes the parent.** Consider the interval between predecessor `P` and successor `S` immediately before inserting `v`. No existing key lies strictly between them. In the current BST, one of `P` or `S` is an ancestor of the other, and the deeper one has an empty child slot facing the interval. Search for `v` follows the same comparisons as the deeper boundary key until reaching that open slot, so `v` attaches to the deeper neighbor.

Equivalently, predecessor and successor are the only possible parents. The one inserted later lies deeper in the current tree and blocks the path to the other. Recorded depth identifies that later/deeper structural boundary without storing insertion timestamps separately. Therefore the new node depth is

`1 + max(predecessor_depth, successor_depth)`.

**Update the running answer.** `ans` begins at one for the root. Each new `depth` is compared with `ans`, then `sd[v] = depth` inserts the key and its depth for later values. The maximum node depth over all inserted keys is exactly the number of nodes along the longest root-to-leaf path, which is the requested tree depth.

**Trace `[2, 1, 4, 3]`.** Root two receives depth one. Value one lies between sentinel zero at depth zero and key two at depth one, so its depth is two. Value four lies between key two at depth one and infinity at zero, also giving depth two. Value three then lies between two at depth one and four at depth two; the deeper successor four is its parent, so three receives depth three. The maximum is three.

**Why future insertions cannot change an existing depth.** BST insertion only adds a leaf and never moves existing nodes. Once a key's depth is recorded, it remains correct forever. This makes one forward pass sufficient and lets the ordered map retain only immutable key-depth facts.

**Why the formula is globally correct.** Initially the root depth is exact. Assume all inserted depths are correct. Sorted predecessor and successor delimit the only key interval containing `v`, and the BST search must attach `v` below their deeper boundary as argued above. The formula therefore assigns its exact depth. Induction covers the entire order, and taking the maximum returns final tree depth.

**The tree itself remains implicit.** No node objects, left pointers, or right pointers are allocated. The method also leaves `order` unchanged, although `order[1:]` creates a sliced list of the remaining values.

## Complexity detail

Let $n$ be the number of keys. A balanced `SortedDict` performs each rank search and insertion in $O(\log n)$ time. The loop handles $n-1$ values, so the exact runtime is $O(n\log n)$, not the manifest's stated $O(n)$. Indexed access through the sorted values view is supported efficiently by the library's maintained ordering.

The ordered map stores $n$ real entries plus two sentinels, requiring $O(n)$ space. The slice `order[1:]` also copies $O(n)$ references in this exact source. Total auxiliary space remains $O(n)$.

A genuinely linear solution is possible because keys are exactly `1..n`, using offline nearest-earlier relationships or specialized arrays, but that is not what the checked-in ordered-map implementation executes.

## Alternatives and edge cases

- **Build the BST literally:** Straight insertion is easy but can take $O(n^2)$ time for sorted order and allocates node links. The ordered predecessor/successor method guarantees logarithmic map operations.
- **Offline Cartesian-tree reasoning:** Insertion priorities and key order can reconstruct the BST in linear time with a stack or divide-and-conquer machinery, matching the manifest aspiration but adding conceptual complexity.
- **Increasing order:** Every new key has the previous maximum as deeper predecessor, producing depths `1,2,...,n` and answer `n`.
- **Single key:** The loop is empty and root depth one is returned.
- **New minimum or maximum:** One real neighbor is absent, but the zero-depth sentinel supplies the other boundary safely.
- **Distinct-key guarantee:** `bisect_left` logic assumes `v` is not already present. Duplicate-key insertion semantics are outside the contract.
- **Depth counts nodes:** Root depth is initialized to one, not zero, matching the problem's node-count definition.
- **Library dependency:** `SortedDict` and its indexable values view are not built-in `dict` behavior. A portable implementation needs another ordered map with rank/predecessor/successor operations.
- **Manifest mismatch:** The actual balanced ordered-map operations are logarithmic. Calling this exact source linear would be inaccurate.
