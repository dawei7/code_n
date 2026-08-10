## General

**Two facts determine a node's local situation**

Inverting a node multiplies every value in its subtree by negative one. A node's final sign therefore depends on the parity of inversions among its ancestors and itself:

- an even number leaves its original sign;
- an odd number negates it.

The distance constraint adds a second requirement. A node may be inverted only if the nearest inverted ancestor is at least `k` edges away. Inversions in different child branches are not ancestor-related and impose no restriction on one another.

For a subtree DP, the information passed from ancestors is exactly:

1. current inversion parity;
2. distance to the nearest inverted ancestor, capped at `k`.

Distances larger than `k` are equivalent because both permit inversion. Capping keeps only `k+1` distance states.

**Root the undirected tree iteratively**

The source builds both adjacency directions, then creates `parent` and `order` starting from root zero.

Python's loop:

`for node in order`

continues over elements appended to the list, so this acts as an iterative traversal. Every neighbor other than the tree parent receives its parent and is appended.

The graph is guaranteed to be a tree, so excluding the parent is enough to avoid revisiting a node. This avoids recursive traversal depth problems for up to `50,000` nodes.

Processing `reversed(order)` ensures every child's DP arrays exist before its parent is evaluated.

**Define the even and odd arrays**

For node `u` and distance state `d` from zero through `k`:

- `even[u][d]` is the maximum sum in `u`'s subtree when the number of inverted ancestors above `u` is even and the nearest inverted ancestor is distance `d` away;
- `odd[u][d]` is the same when that ancestor-inversion parity is odd.

Distance `k` means “at least `k` or none.” It is the only state in which inverting `u` is allowed.

Under even parity, keeping `u` contributes `nums[u]`. Under odd parity, its inherited sign is already flipped, so keeping contributes `-nums[u]`.

**Compute the option that does not invert u**

The source initializes:

`keep_even[d] = nums[u]`

`keep_odd[d] = -nums[u]`

for every distance state.

If `u` is not inverted, parity stays the same for each child. The nearest inverted ancestor becomes one edge farther away. Thus child distance is:

`min(d+1,k)`.

For `d<k`, the source adds `child_even[d+1]` or `child_odd[d+1]`. At `d=k`, it adds the child's capped `k` state.

Children are conditionally independent once the state at `u` is fixed: an inversion in one child subtree is not ancestor-related to an inversion in another child subtree. Their optimal sums can be added.

**Compute the option that inverts u**

Inverting `u` is legal only when incoming distance is `k`.

Under inherited even parity, inversion flips `u` to `-nums[u]`. Under inherited odd parity, it flips the already-negated sign back to `nums[u]`. The source starts:

`invert_even = -nums[u]`

`invert_odd = nums[u]`.

For every child, `u` becomes the nearest inverted ancestor at distance one, and parity toggles:

- even above `u` becomes odd for the child, so add `child_odd[1]`;
- odd above `u` becomes even for the child, so add `child_even[1]`.

After all children, these inversion totals compete only with `keep_even[k]` and `keep_odd[k]`. States below `k` cannot choose inversion because an inverted ancestor is too close.

**Why the distance sent to children is one**

The child is exactly one edge below `u`. If `u` is inverted, the nearest inverted ancestor of that child is `u` itself, regardless of any higher inverted ancestor. Sending state one accurately resets the constraint clock.

For `k=1`, state one is already capped and permits the child to invert too. This matches the rule: two distinct ancestor-related nodes at distance one satisfy a minimum distance of one.

**Finalize one node**

After adding all child contributions:

`keep_even[k] = max(keep_even[k], invert_even)`

and similarly for odd parity.

The resulting arrays are stored as `even[u]` and `odd[u]`. Child arrays are then replaced by `None` because no other parent will need them in a tree. This reduces retained references during processing, though worst-case memory remains linear times `k`.

**Why parity is enough for value signs**

Two inversions on the path to a node cancel:

`(-1)^2 = 1`.

The exact number of inverted ancestors is irrelevant beyond even or odd. However, the exact identity of the nearest recent inverted ancestor matters for legality, which is why parity alone would be insufficient and the capped distance is stored separately.

**Why the DP enforces every distance constraint**

When an inversion is selected, it is allowed only in distance state `k`, proving every nearest inverted ancestor is at least `k` away. The chosen node then resets descendants to distance one. Each non-inverted edge increments that distance until it reaches the cap.

Therefore, no descendant can be inverted before traversing at least `k` edges from the chosen ancestor.

Inversions in separate branches never appear in one another's ancestor chain. The DP optimizes children independently, exactly as the problem permits.

**Why every legal inversion set is represented**

Take any legal inversion set. At each node, choose the DP's keep or invert branch according to membership in that set. Along every root-to-node path, the distance state evolves exactly as the nearest inverted ancestor distance, and legality guarantees every invert branch occurs at state `k`. Parity evolves by toggling at each selected node.

The DP therefore includes that set's exact final sum. Conversely, every DP choice set is legal by the distance-state transition. Maximizing over both choices at every node yields the global optimum.

**Root answer**

The root has no inverted ancestor, so its distance is treated as capped `k`. It also has even inherited parity. The requested maximum is:

`even[0][k]`.

This state compares keeping and inverting the root and includes all optimized child subtrees.

## Complexity detail

Rooting the tree and building traversal order take `O(n)` time. For each parent-child edge, the DP loops through `k` distance states once while combining that child. Total time is `O(nk)`.

Each node may hold two arrays of length `k+1`, giving `O(nk)` worst-case space. The parent, order, graph, and answer references add `O(n)`. Clearing child arrays can improve practical retention for some shapes but does not change the worst-case bound; a star can have many child arrays ready before the root combines them.

The iterative tree traversal avoids recursion-stack overflow. Final sums may reach roughly `n * 5*10^4` in magnitude, so fixed-width code should use 64-bit integers.

## Alternatives and edge cases

- **Greedily invert negative subtrees:** Overlapping subtree inversions change signs by parity and the distance rule couples ancestor choices, so local subtree sums are not enough.
- **Track the exact nearest-ancestor distance without capping:** Distances above `k` have identical future legality. Capping reduces unbounded depth to `k+1` states.
- **Track parity only:** It determines signs but cannot decide whether another inversion is far enough from an ancestor.
- **Track distance only:** It enforces legality but cannot determine whether current values are negated by inherited inversions.
- **Recursive tree DP:** Mathematically equivalent, but a chain of `50,000` nodes risks Python recursion failure; the protected source roots iteratively.
- **k equals one:** Every ancestor-descendant pair of distinct nodes is far enough, and state one immediately allows another inversion.
- **k exceeds tree depth:** Along any root-to-leaf path, at most one inversion can occur, though separate branches may each contain one.
- **Zero node value:** Inverting does not change that node's contribution but may still beneficially toggle descendants.
- **Negative nums value:** Odd parity turns it positive; the DP compares whether inversion timing improves the whole subtree.
- **Sibling inversions:** They are unrestricted because neither sibling is an ancestor of the other, and child DPs are added independently.
- **Root inversion:** Always legal because there is no inverted ancestor; it appears only in root state `k`.
- **Leaf node:** Keep arrays contain its signed value, and inversion competes at distance `k` without child terms.
- **Capped no-ancestor state:** Distance `k` represents both exactly `k` and any larger distance, including infinity at the root.
- **Child-array clearing:** Safe because a rooted tree gives every child exactly one parent consumer.
