## General

**Every new parent remains an original ancestor.** A node either keeps its original parent or moves to its closest original ancestor with the same character. All final edges therefore point upward along the original tree. This lets one traversal of the original tree determine the simultaneous final structure without physically rebuilding it first.

**Maintain the current ancestor path separately for each character.** `d` maps a character to a stack of nodes with that character on the active root-to-current DFS path. On entering node `i`, the source appends it to `d[s[i]]`. Because DFS call nesting exactly represents ancestry, the item immediately before `i` on this same-character stack is its closest same-character ancestor.

After all children are processed, if the stack length exceeds one, `d[s[i]][-2]` is the required new parent. Otherwise no same-character ancestor exists and `fa`, the original parent passed into DFS, remains the parent. The root has `fa = -1` and is never attached upward.

Popping `i` on exit is essential. It removes the node before DFS moves to a sibling, which is not its descendant and must not treat it as an ancestor.

**Accumulate final subtree sizes in postorder.** `ans[i]` begins at one for the node itself. Original descendants are processed before `i` chooses and reports to its final parent. Each completed node adds its accumulated final-subtree size to the node that will actually be its parent after simultaneous changes.

If a child or deeper descendant jumps over `i` to a higher ancestor, its DFS completion adds its size directly to that higher target, not to `i`. It therefore does not incorrectly remain in `i`'s final subtree. If it remains below `i`, its chain of final-parent additions eventually contributes to `ans[i]` before `i` itself is sent upward.

**Why simultaneous changes are respected.** The nearest same-character ancestor is selected from the original DFS path, not from parents already modified during traversal. The stack contains original ancestors because recursion follows original `g`. No mutation of `parent` or `g` occurs. Thus one node's computed reparenting cannot alter another node's ancestor search, exactly matching simultaneous evaluation.

Consider a node $x$ that moves to ancestor $y$ and carries final descendants beneath it. By the time $x$ finishes, all those descendants have already contributed to `ans[x]` if their final parent paths pass through $x$. Adding the whole `ans[x]` to `ans[y]` transfers the complete final subtree in one operation.
After DFS finishes a node $i$ but before adding it upward, `ans[i]` equals the number of nodes whose final-parent chain reaches $i$ without first leaving its original subtree. Child completions either add to $i$ or bypass it according to their exact final parent. The stack selects $i$'s exact final parent, so transferring `ans[i]` preserves the invariant at that ancestor. Postorder induction yields every final subtree size, with the root accumulating all $n$ nodes.

**The original parent parameter is still needed.** When no same-character ancestor exists, the operation says to do nothing, so `fa` remains the final parent. It is not generally the top item of any character stack. Passing it explicitly handles this fallback.

**Recursion risk.** A valid original tree may be a chain of $10^5$ nodes. The recursive source can exceed CPython's normal recursion limit. The algorithm is linear, but a robust implementation needs iterative entry/exit events or an increased recursion limit.

## Complexity detail

Building children lists costs $O(n)$. DFS enters and exits every node once. Stack append, lookup, second-last access, pop, and size addition are expected $O(1)$, so total time is $O(n)$.

Adjacency, answer, all character stacks together, and recursion stack use $O(n)$ space. Although `d` has multiple lists, each active node appears in exactly one and is removed once. The output itself has $n$ integers.

## Alternatives and edge cases

- **Build a new parent array first:** One DFS can record each final parent, followed by a second postorder over the rebuilt tree. It is easier to visualize but requires another adjacency structure.
- **Iterative DFS with enter/exit events:** It preserves character-stack semantics while avoiding recursion-depth failure.
- **Search ancestors naively per node:** Walking parent links can cost $O(n^2)$ on a chain; per-character stacks make closest lookup constant-time.
- **No matching ancestor:** The node keeps `fa` and its accumulated size is added there.
- **Immediate parent has same character:** It is stack position `-2` and remains or becomes the selected parent.
- **Matching ancestor several levels above:** The node bypasses intermediate parents, and its size is added directly to the matching ancestor.
- **Root:** It has no parent, is never transferred, and ends with size $n$.
- **Sibling with same character:** It has been popped before the sibling is visited, so it is never mistaken for an ancestor.
- **All characters equal:** Every node's nearest same-character ancestor is its original parent, so subtree sizes remain unchanged.
- **All path characters distinct:** Every node keeps its original parent for lack of a match.
- **Simultaneous semantics:** Because stacks reflect the original path, earlier computed moves never influence later ancestor selection.
- **Deep tree:** The exact recursion is not safe for the full maximum depth without runtime adjustment.
- **Unused final tree:** The source computes sizes directly and deliberately never materializes final edges.
