## General

**The succession order is a family-tree preorder**

The stated successor rule visits a person, then that person’s children from oldest to youngest, including each child’s descendants before moving to the next younger sibling. That is exactly a preorder traversal of the rooted family tree:

1. process the current person;
2. recursively process each child in birth order.

The king is the root. Birth events add new children, death events only mark names, and an inheritance-order query performs the preorder while omitting marked people from the returned list.

**State stored by the class**

The constructor stores three pieces of persistent state:

- `self.king` is the root name from which every order traversal begins;
- `self.dead` is a set of people who have died;
- `self.g` maps a parent name to a list of children in birth order.

`defaultdict(list)` creates an empty child list when a name without recorded children is accessed. Across the family, the lists contain one entry per non-king person because every birth adds one parent-child edge.

Names are unique under the contract, so a string name identifies one family member unambiguously.

**Recording births**

`birth(parentName, childName)` performs:

`self.g[parentName].append(childName)`.

Appending is essential rather than inserting or sorting. Calls arrive chronologically, so the list order is oldest child to youngest child. The succession rule uses precisely that order.

The method does not need to store an explicit parent pointer because queries traverse downward from the king. It also does not update a materialized succession list, avoiding expensive insertion into the middle whenever someone in an older branch has a new child.

The contract guarantees the parent is alive when the birth is reported, though the data structure would still be able to attach a child to a marked parent.

**Recording deaths**

`death(name)` adds the name to `self.dead`. It does not remove the person from the family graph.

This distinction is central. A dead person no longer appears in the inheritance result, but that person’s descendants retain their relative place. Removing the node and its subtree would lose valid heirs. Reparenting children manually would add needless structural mutation and could disturb order.

Set membership provides expected constant-time checks during queries. Repeatedly adding the same name would be harmless at the data-structure level, although calls follow the problem’s valid event model.

**Producing the current order**

`getInheritanceOrder` creates a fresh output list `ans` and defines recursive `dfs(x)`.

The expression:

`x not in self.dead and ans.append(x)`

uses Python short-circuit evaluation. If `x` is alive, the left side is true and `append` executes. If `x` is dead, the left side is false and the append is skipped.

This expression does not control traversal of children. The subsequent loop always runs:

`for y in self.g[x]: dfs(y)`.

Therefore, a dead person is omitted but every descendant is still visited in the correct position.

Calling `dfs(self.king)` traverses the whole family tree. The returned `ans` is a new snapshot, so later births and deaths do not mutate an earlier result list.

**Why preorder matches the recursive successor definition**

For a person `x`, the next heir after `x` is the oldest unvisited child if one exists. Preorder does exactly that by entering the first child immediately.

When that child’s branch is exhausted, recursion returns to `x` and continues with the next child. If all children are exhausted, recursion returns to `x`’s parent and continues with the parent’s next child. This call-stack behavior is the same upward search described by `Successor`.

By induction, the preorder of each person’s subtree lists that person first, then each child subtree from oldest to youngest. The king’s subtree is the entire family, so its preorder is the unique succession order before death filtering.

Filtering dead names without changing traversal positions removes exactly those people and preserves the relative order of every living person. That is the requested inheritance list.

**Tracing the important death behavior**

If the order is `king, andy, matthew, bob, alex, asha, catherine` and Bob dies, DFS still reaches Bob between Matthew and Alex. It skips appending Bob, then traverses Bob’s children Alex and Asha. Catherine follows after Bob’s entire branch. The resulting order is `king, andy, matthew, alex, asha, catherine`.

This is why death must be a mark rather than a graph deletion.

## Complexity detail

Let $P$ be the number of people currently recorded, $B$ the number of birth calls, $D$ the number of death calls, and $G$ the number of inheritance-order queries.

Construction is $O(1)$. A birth performs an amortized $O(1)$ list append, and a death performs an expected $O(1)$ set insertion. Each order query visits all $P$ people, including dead ones, and performs expected constant-time set membership per person, so it takes $O(P)$ time plus output construction.

Across operations, the package summary $O(B+D+GP)$ describes the total expected work when $P$ denotes the relevant family size at query time in a simplified bound.

The graph lists, dead set, and generated output use $O(P)$ storage. Recursive DFS also uses $O(H)$ call-stack space for family-tree height $H\le P$, so total space is $O(P)$.

In exact Python execution, a chain-like family approaching $10^5$ generations may exceed the default recursion limit. An iterative preorder stack would preserve the algorithm while avoiding that practical failure mode.

## Alternatives and edge cases

- **Maintain one live succession list eagerly:** Birth into an older branch may require finding a subtree boundary and inserting in the middle, making updates expensive. Storing the family tree makes births constant time and queries linear.
- **Delete a dead node from the graph:** This can lose or misorder descendants. Death must affect output membership only.
- **Store parent pointers and call `Successor` repeatedly:** It can reproduce the definition but requires visited tracking and repeated upward navigation. One preorder traversal is simpler.
- **Iterative preorder:** Push children in reverse birth order so the oldest is popped first. It avoids recursion-depth limits while retaining $O(P)$ query time.
- **Only the king:** The order is the king if alive and empty if the king has been marked dead.
- **Dead king:** The king is skipped, but all child branches are traversed in birth order.
- **Dead parent with living descendants:** The parent is omitted and descendants remain exactly where the branch belongs.
- **Several children:** Append order preserves oldest-to-youngest succession without sorting.
- **Birth after earlier queries:** Queries rebuild from live state, so the new child appears in the correct branch on the next call.
- **Repeated queries without events:** They return equal content in separate newly allocated lists.
- **Leaf access in `defaultdict`:** Reading `self.g[x]` may create an empty list entry for a leaf, but total keys and storage remain $O(P)$.
- **Unique names:** String-keyed maps rely on the guarantee that no two people share a name.
- **Deep family chain:** Recursive traversal has $O(P)$ mathematical space but may hit Python’s recursion limit; iterative DFS is safer operationally.
