## General

Only ten different decimal digits exist. A good subset uses each digit at most once across all selected node values, so its entire digit usage fits in a ten-bit mask.

The source computes a mask-based knapsack DP for every subtree. Child tables are merged only when their digit masks are disjoint. After a node’s table is complete, its maximum entry is that node’s `maxScore` and is added to the requested total.

**Converting one node value into a digit mask**

`digit_mask(value)` examines decimal digits from right to left. Bit `d` records whether digit `d` has appeared.

If a digit’s bit is already set, the value itself repeats a digit. Selecting that node alone would violate the rule, so the helper returns `-1` and that node is never offered as a selectable item.

Otherwise all digit bits are combined into the value’s mask. For example, `34` produces bits three and four. A value containing zero, such as `10`, sets bits zero and one normally.

Values are positive, so the loop always processes at least one digit. There is no ambiguity between value zero and the empty mask under the constraints.

**Building a bottom-up tree order**

The parent array is converted to child lists. `order=[0]` begins at the root, and extending this same list while iterating visits every descendant after its parent.

Reversing `order` places every child before its parent. Consequently each child’s DP table is available when the parent is processed. This avoids recursive traversal and any recursion-depth concern.

**DP state**

For node `u`, `dp[mask]` is the maximum sum obtainable by a good subset of the portion of `u`’s subtree merged so far, using exactly the digits in `mask`.

Value `-1` marks an unreachable mask. All node values are positive, so every reachable score is nonnegative and `-1` is a safe sentinel.

Initialization always includes:

`dp[0]=0`,

which means choose no node from this subtree.

If `vals[u]` has no repeated digit, `dp[node_mask]=vals[u]` also allows choosing the current node. If its own representation repeats a digit, only the empty choice is initialized; descendants can still be selected later.

The statement says a subset belongs to the subtree, not that it must include the subtree root, so the empty/current-node choices are both necessary.

**Merging one child**

Suppose `dp` represents the current node plus previously processed children, and `child` is the completed table for another child subtree.

A left choice with `left_mask` and a child choice with `right_mask` can coexist exactly when

`left_mask & right_mask == 0`.

Disjoint masks mean no decimal digit appears in both selected subsets. Their combined mask is the bitwise OR, and their scores add.

For every compatible pair, the transition is:

`merged[left_mask | right_mask] = max(existing, dp[left_mask] + child[right_mask])`.

Because every child table contains reachable empty mask zero, merging never forces selection from a child. Existing choices carry forward through `right_mask=0`.

After all children are merged, `dp` represents every good subset of the full subtree and the best score for each digit mask.

**Why subtree merging is complete**

Any subset of `u`’s subtree decomposes uniquely into selections from:

- node `u` itself;
- each direct child subtree.

The child subtrees are disjoint. A union is good precisely when every component is internally good and component digit masks are pairwise disjoint.

By induction, each child table lists the best internally good selection for every mask. Sequential compatible-mask merging considers every valid combination, so the completed parent table contains the optimum for every possible overall mask.

Therefore `max(dp)` is exactly the maximum score of any good subset in `u`’s subtree.

**Two equivalent merge enumeration strategies**

The source adaptively chooses how to find compatible masks.

In the direct strategy, it forms lists of reachable left and right masks, tries their Cartesian product, and rejects pairs with an intersection.

In the submask strategy, for each left mask it computes

`available = full ^ left_mask`,

the ten-bit complement containing digits not already used. Every compatible right mask is a submask of `available`. The standard update

`right_mask = (right_mask - 1) & available`

enumerates all such submasks down to zero.

Both strategies implement the same recurrence. The source estimates their work:

- direct pairs cost `len(left_masks)*len(right_masks)`;
- complement enumeration costs the sum of `2^{10-popcount(left_mask)}`.

It chooses the smaller estimated route. This affects speed only, not reachable states or scores.

**Collecting every maxScore**

After finishing node `u`:

- `states[u]=dp` preserves its table for the parent;
- `total += max(dp)` adds `maxScore[u]`.

The modulo is applied only once at the end. Python integers prevent overflow, and delaying the modulo is essential for comparisons: DP must maximize true sums, not residues modulo `10^9+7`.

## Complexity detail

Let `D=10` be the number of possible digits. There are `2^D=1024` masks.

For a child merge, the number of disjoint ordered mask pairs over the full mask universe is `3^D`: each digit is assigned to the left mask, the right mask, or neither. The submask enumeration has this same aggregate bound. The adaptive direct branch is chosen only when its Cartesian-product estimate is no larger than the submask estimate.

Across `n-1` child merges, time is `O(n3^D)`. With fixed `D=10` this is linear in `n` with a substantial constant.

`states` retains one 1024-entry table for every node, using `O(n2^D)` space. Temporary `dp`, `merged`, and reachable-mask lists use `O(2^D)` additional space per active iteration. Total space is `O(n2^D)`.

## Alternatives and edge cases

- **Recursive tree DP:** It can use the same mask recurrence, but the iterative reversed order avoids recursion depth and makes all child dependencies explicit.
- **Always try all mask pairs:** This is correct but may do up to `4^D` raw pair checks before rejecting intersections. Adaptive submask enumeration respects compatibility more directly.
- **Always enumerate complement submasks:** It guarantees `O(3^D)` aggregate work and is simpler to analyze; the direct branch can be faster when few masks are reachable.
- **Node value with repeated digits:** That node cannot be selected at all, but its descendants remain eligible because `dp[0]` is still merged with child tables.
- **Digit repeated across different nodes:** Their masks intersect, so they cannot appear in the same good subset.
- **Value containing zero:** Bit zero is handled like every other digit.
- **Select no node:** Empty mask score zero is valid and ensures every table is nonempty.
- **Positive values:** Since all scores are nonnegative, sentinel `-1` cannot conflict with a reachable score.
- **Leaf node:** Its table contains the empty choice and, if valid, the node itself; `max(dp)` is immediate.
- **Chain tree:** Reversed iterative order processes the deepest node first without recursion.
- **Wide tree:** Child tables are merged one at a time, distributing digit capacity among siblings.
- **Modulo timing:** Applying modulo inside DP could reverse score comparisons and would be incorrect. Only the final sum is reduced.
- **All ten digits already used:** `available=0`, so only child mask zero is compatible.
- **Parent array validity:** The construction relies on the guaranteed rooted tree at node zero; no cycle detection is included.
