## General
**Turn the target collection into constant-time membership tests**

Place the $K$ supplied node objects in a set. Membership is based on node identity, matching the contract that `nodes` contains references from the given tree. This also avoids repeatedly scanning the target list at each visited node.

**Let each subtree report its surviving target branch**

Run a postorder depth-first search. A null pointer reports no target. When the current node is itself in the target set, report it immediately: it is allowed to be its own descendant, and any additional targets below it cannot make a deeper node outside its subtree the common ancestor.

Otherwise, collect the reports from the left and right children. Two non-null reports mean targets occur through both child branches, so the current node is the lowest place where those branches meet. With only one report, propagate that report upward; with neither, report null.

The report from any completed subtree is null exactly when it contains no target, and otherwise identifies the unique node that must be carried toward a possible meeting point. If both children report, neither child subtree contains every reported target, while the current subtree does, making the current node the lowest common ancestor. If the current node is a target, returning it is correct even when other targets lie below it because no proper descendant can be an ancestor of the current node itself. Since every requested node exists, the report reaching the top is the required answer.

## Complexity detail
Building the target set costs $O(K)$ time and space. The search visits at most all $N$ tree nodes once, so total time is $O(N + K)$. Its recursion stack uses $O(H)$ space, and together with the set the auxiliary space is $O(H + K)$.

## Alternatives and edge cases
- **One root-to-target path per node:** intersecting $K$ separately discovered paths is correct, but can require $O(NK)$ time on a skewed tree.
- **Parent map and upward counting:** parent pointers permit ancestor walks from every target, but constructing the map still visits the whole tree and stores $O(N)$ additional entries.
- **Single target:** that node is its own lowest common ancestor and is returned immediately.
- **A target contains all others:** the highest supplied target on their shared branch is the answer, not one of its descendants.
- **Targets span both root branches:** the root is the answer even when several targets occur within either branch.
