## General

**Why this is a graph-copy problem**

The `left` and `right` references form a binary tree, but every node also has a `random` reference that may point to any node, to itself, or to `None`. Once those random edges are included, the structure behaves like a directed graph. It can contain cycles even though the child edges alone cannot. For example, one node can point randomly to a descendant while that descendant points randomly back to the first node.

A deep copy must satisfy two conditions at once. First, every original node needs one newly allocated `NodeCopy` with the same value. Second, every copied `left`, `right`, and `random` field must point to the copy of the original target, never to an object in the old structure. Merely copying values or recursively following only the two child links would not be enough.

The stored solution uses recursive depth-first search plus a dictionary named `mp`. Its central meaning is:

> If `mp[old]` exists, it is the one and only copy corresponding to original node `old`.

This mapping both prevents infinite recursion through cycles and ensures that several references to the same original target become several references to the same copied target.

**Following the exact control flow**

The inner function `dfs(root)` returns the copied counterpart of `root`.

1. If `root is None`, it returns `None`. This preserves absent child and random references without allocating a fake node.
2. If `root in mp`, that original node has already been discovered. The function immediately returns its existing copy.
3. Otherwise, it creates `NodeCopy(root.val)`. At this moment the new object has the correct value, while its three outgoing references still need to be connected.
4. Crucially, it stores `mp[root] = copy` before following any outgoing edge.
5. It recursively obtains the copied targets of `root.left`, `root.right`, and `root.random`, assigning the three returned values to the matching fields of `copy`.
6. Once all three fields are connected, it returns `copy`.

The outer method initializes `mp = {}` and returns `dfs(root)`. Defining the helper before the dictionary assignment is valid in Python because the helper body is not executed when the function object is defined. By the time `dfs(root)` is called, `mp` has been created in the enclosing method scope, and the closure can read and update it.

**Why registration must happen before recursion**

The line that inserts the new object into `mp` comes before the three recursive calls. This order is the key to supporting random-pointer cycles. Suppose a node's `random` field points to itself. The first call allocates its copy and registers the pair. When the recursive call follows `random` back to the same original object, the membership test succeeds and returns the already allocated copy. The copied random field therefore points to itself, exactly as required, and recursion terminates.

The same reasoning handles longer cycles and cross-links. If node `A` eventually reaches already discovered node `B`, `dfs(B)` reuses `mp[B]` instead of creating another object. Registering only after cloning all neighbors would fail: a cycle could return to `A` before `A` had been recorded, causing endless recursion and duplicate allocations.

**Why all nodes are reached**

Every tree node is reachable from the root by some sequence of `left` and `right` edges. The DFS follows both child fields for every newly discovered node, so it necessarily discovers every node in the underlying binary tree. Following `random` as a third edge is safe and can find a node earlier than the child traversal would, but it does not create a duplicate because `mp` records identity.

The dictionary uses node objects as keys, not node values. That distinction matters because different nodes are allowed to have the same `val`. Mapping by value would merge such nodes and corrupt the shape. Object identity lets two equal-valued originals receive two separate copies while still preserving shared references to the same actual original.

**Why the result is a deep copy**

Consider the first call that discovers any original node `u`. It creates exactly one new object with value `u.val` and records it. Every later call for `u` returns that same object, so there is neither a missing copy nor a duplicate copy for `u`.

For any labeled edge from `u` to `v`, the assignment for that label calls `dfs(v)`. If `v` is null, the returned field is null. Otherwise, the returned object is precisely `mp[v]`. Therefore, the copied edge leaves `mp[u]` and targets `mp[v]`. This applies independently to `left`, `right`, and `random`. All values and all labeled relationships are preserved.

Finally, every non-null field assigned by the algorithm comes from `dfs` and is therefore a `NodeCopy` object from `mp`, rather than an original `Node`. The returned root is consequently structurally equivalent but object-independent: changing a copied node does not change the corresponding original node.

## Complexity detail

Let $N$ be the number of non-null nodes. Each node is newly processed once. On that first visit, the code performs one allocation, one dictionary insertion, and three recursive edge calls. A later visit through another edge performs a dictionary lookup and returns immediately. There are at most three outgoing references per node, so the total number of edge examinations is at most $3N$. Under expected constant-time dictionary operations, total time is $O(N)$.

The dictionary contains one entry for every original node, using $O(N)$ auxiliary space. Recursive calls also occupy stack frames. In the worst case, a highly skewed child structure or a long random-edge path can make the active recursion depth $O(N)$. Thus auxiliary space is $O(N)$.

The copied graph itself contains $N$ newly allocated nodes and is the required output. Some conventions exclude required output from auxiliary-space accounting; the dictionary and call stack still establish the same $O(N)$ bound. Python dictionary behavior is expected-time analysis, while pathological hash collisions are outside the usual model. With up to one thousand nodes in the stated constraints, recursion depth can also approach Python's default recursion limit, which is a practical consideration even though it does not change the asymptotic bound.

## Alternatives and edge cases

- **Two-pass tree traversal:** First copy only the `left` and `right` structure while recording old-to-new pairs, then traverse the original tree again to assign random references. It is also $O(N)$ time and space, but the one-pass graph DFS is shorter and naturally treats all three fields uniformly.
- **Breadth-first graph cloning:** Use a queue and the same old-to-new dictionary. This preserves the asymptotic bounds and avoids recursive call depth, at the cost of more explicit queue and neighbor-handling code.
- **Cloning by values:** A map from `val` to copy is incorrect because several distinct nodes may share one value. Keys must identify original objects.
- **Copying a random target immediately without memoization:** This can allocate the same logical node multiple times and can recurse forever when random edges form a cycle.
- **Empty tree:** The first base case returns `None`, so the method correctly produces no allocated root.
- **Random pointer is null:** `dfs(None)` returns `None` and assigns a null random field.
- **Random pointer targets the same node:** Early insertion into `mp` makes the copied node's random field point back to that same copied object.
- **Several pointers share one target:** Every call for that target returns the same dictionary value, preserving aliasing in the copy.
- **Repeated values:** Equal `val` fields do not imply equal nodes; identity-based dictionary keys keep their copies separate.
- **Highly skewed structure:** Correctness is unchanged, but recursive depth may reach $N$. An iterative breadth-first implementation avoids a language recursion-limit failure.
- **Mutation independence:** The result is deep only because all non-null assigned references are copied objects. No field should be assigned directly from `root.left`, `root.right`, or `root.random`.
