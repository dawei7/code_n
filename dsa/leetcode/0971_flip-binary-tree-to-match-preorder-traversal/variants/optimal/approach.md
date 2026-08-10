## General

**Preorder makes each flip decision locally forced**

Preorder visits current node, then one child subtree, then the other. Without a flip, left comes first; with a flip, right comes first.

After the current node matches the next voyage value, the following voyage value tells which nonempty child must be visited next. Unique values remove ambiguity.

DFS uses shared pointer `i`, Boolean `ok`, and answer list `ans`.

**Match the current root**

If `root is None` or `ok` is false, return.

For a real node, `root.val` must equal `voyage[i]` because preorder always visits root before descendants. A mismatch makes the task impossible, so set `ok = False`.

On a match, increment `i` to the value expected from the first child subtree.

**Keep child order when left matches**

If the left child is absent, there is nothing useful to flip before the only possible right subtree. DFS calls left, which returns, then right.

If left exists and `root.left.val == voyage[i]`, voyage expects left next. Natural order is forced: visit left and then right.

**Flip when left cannot be next**

If a left child exists but its value is not next, natural preorder cannot work.

The only alternative is right-first order. Record `root.val` in `ans`, then visit right before left.

If right also fails to match, recursion detects the mismatch and sets failure. No separate precheck is needed.

**Why voyage access is safe**

After matching a node, the code may read `voyage[i]` only when a left child exists.

Then at least one unvisited tree node remains. Voyage length equals tree node count, and every previous visit consumed one entry, so another entry exists. At a leaf, `root.left is None` short-circuits before access.

**Trace**

For root one with left two, right three, and voyage `[1, 3, 2]`:

- One matches.
- Next expected value is three, but left is two.
- Flip at one is forced; record one.
- Visit three, then two.

The answer is `[1]`.

For root one with child two and voyage `[2, 1]`, root fails immediately. Flipping children cannot change the first preorder value, so return `[-1]`.

**Why flip count is minimum**

Whenever a flip is recorded, a present left child does not match the unique required next value. Every successful solution must avoid left-first traversal there, so the flip is mandatory.

Whenever left matches, flipping would visit a different unique value and fail. Not flipping is mandatory.

The algorithm makes only forced decisions and therefore performs the smallest possible number of flips.


DFS consumes voyage in exactly the preorder created by its child-order decisions. Every node match advances one entry.

At each node, unique values make the alternatives exhaustive: matching left means natural order, otherwise only right-first can work. Recursive induction proves success exactly when some flip set exists.

If a mismatch occurs, `ok` propagates and final output is `[-1]`. Otherwise, recorded flips generate the target traversal.

**Why partial flips are discarded after failure**

The algorithm may append values before discovering an impossibility deeper in the tree. Those earlier decisions do not form a valid complete solution.

The final conditional ignores `ans` whenever `ok` is false and returns only `[-1]`, exactly as required.

**Pointer invariant**

Before entering a real-node call, `i` identifies the voyage value that this node must match. After the node succeeds, `i` identifies the first value belonging to whichever child subtree is visited next.

After both child calls finish successfully, `i` points immediately after the complete preorder sequence of the current subtree. This invariant lets one global pointer replace copied voyage slices.

**Why every voyage value is consumed on success**

The input tree and voyage contain the same number `N` of unique values. A successful traversal visits every tree node exactly once and increments `i` once per node.

Therefore, if `ok` remains true, `i = N` automatically. The code does not need a separate final length check.

**Why flipping a node with no left child is unnecessary**

If only a right child exists, natural preorder already visits that child immediately after the root because the left call is empty. Swapping it to the left would produce the same sequence of node values.

The code does not record such a redundant flip, which is necessary for minimum flip count.

**Why a failed forced flip proves impossibility**

When left does not match the next unique voyage value, left-first is impossible. The code tries the only alternative, right-first. If the right subtree then mismatches, neither orientation can work at this node.

Failure is therefore conclusive rather than a reason to backtrack to some third ordering.

## Complexity detail

Let `N` be nodes and `H` height.

Each node is visited once with constant work, so time is `O(N)`.

The answer can contain `O(N)` values and recursion uses `O(H)` frames. Total space including output is `O(N)`.

## Alternatives and edge cases

- **Physically swap children:** Unnecessary and mutates input; traversal order models flips.
- **Backtrack over both orders:** Unique next values make the choice forced.
- **Already matching:** Return an empty list.
- **Root mismatch:** Immediately impossible.
- **Missing left child:** Visit right naturally without recording a meaningless flip.
- **Wrong right after forced flip:** Recursion sets failure.
- **Leaf:** Match it and both child calls return.
- **Unique values:** Essential for identifying the next child.
- **Failure after earlier flips:** Final `[-1]` replaces the partial list.
- **Answer order:** Produced preorder decision order is acceptable.
