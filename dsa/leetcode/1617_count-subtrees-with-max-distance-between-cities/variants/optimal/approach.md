## General
**Represent each city subset as a bitmask.** With $n \le 15$, all $2^n$ subsets can be examined directly. Skip masks containing fewer than two cities because their diameter is zero. For every other mask, select its least-significant city bit as a traversal start.

**Use one restricted traversal to prove connectivity.** Traverse only neighbors whose bits belong to the current mask. Because the original graph is a tree, the traversal never needs a general visited set: carrying the parent prevents returning along the only edge just used. Count the reached cities. If that count differs from `mask.bit_count()`, the selected cities do not form a connected subtree and the mask contributes nothing.

**Find the diameter with a second tree traversal.** During the connectivity traversal, retain a farthest reached city. In any tree, a farthest vertex from an arbitrary start is an endpoint of a diameter. Traverse the same induced subtree again from that endpoint; the greatest distance reached is the subtree diameter. Increment the result bucket for that distance.

Every accepted mask is connected by the reached-count test, and every connected city subset appears as exactly one mask. The two-traversal tree property supplies its exact maximum pairwise distance. Therefore each qualifying subtree increments exactly one correct distance bucket, and no disconnected or single-city subset is counted.

## Complexity detail
There are $2^n$ masks. Each restricted traversal examines at most $n$ cities and their incident tree edges, and a connected mask needs two such traversals. The total time is $O(2^n n)$. The adjacency lists, traversal stack, and result array each use $O(n)$ space; the masks are processed one at a time.

## Alternatives and edge cases
- **All-pairs distances per connected mask:** Precompute tree distances, then inspect every selected city pair to obtain each diameter. This is correct but takes $O(2^n n^2)$ time when many subsets are connected.
- **Edge-count connectivity test:** In a subset of a tree, having exactly one fewer internal edge than vertices proves connectivity, but finding the diameter still needs either pair scanning or a traversal.
- **Enumerate endpoint pairs:** Dynamic programming can count subtrees for each proposed diameter endpoint pair, but avoiding duplicate counts requires more intricate tie-breaking.
- Single-city masks are connected but have diameter zero, which has no output bucket.
- The smallest tree has one two-city subtree and returns `[1]`.
- A path of $n$ cities has exactly $n-d$ connected intervals of diameter $d$.
- A star has many diameter-two subtrees, because every selection containing the center and at least two leaves is connected.
- City labels are 1-based in `edges` but are normalized before bit operations.
