## General

**What the encoded depth tells us**

Preorder visits a node before its left subtree and then its right subtree. The traversal string adds the exact depth before every value. Together, these facts identify the parent of each new node: a node at depth `d` belongs to the most recently visited node at depth `d - 1`.

The stack stores that active ancestry. After a parsed node at depth `d` is pushed, `stack[0]` is the root, `stack[1]` is the node on the active path at depth one, and so on through `stack[d]`, the new node itself.

When traversal goes deeper by one level, the stack already has exactly the parent path. When traversal returns to a sibling or a higher subtree, obsolete descendants are popped until the stack length equals the new node's depth. At that point, the top is its parent.

**Parse one token at a time**

The variable `index` always points to the first unconsumed character.

First, the code counts consecutive dashes. Each dash increments `depth` and advances `index`. The input format guarantees that every dash run is followed by at least one digit, so the exact loop `while traversal[index] == "-"` does not run beyond the string even though it does not repeat an explicit bounds check.

Next, the code parses all consecutive digits. Starting from zero, `value = value * 10 + int(traversal[index])` shifts the decimal number left one place and adds the next digit. This correctly handles multi-digit values such as `401` or `10^9`. When the next dash or the end of the string is reached, `value` is complete and a `TreeNode` is created.

Dashes cannot be confused with a negative sign because node values are strictly positive. Every dash belongs solely to depth encoding.

**Restore the correct parent path**

Before attaching the new node, the loop `while len(stack) > depth: stack.pop()` removes nodes at the new node's depth or below.

If the next node is one level deeper than the previous node, `len(stack) == depth` already, so nothing is popped and the previous node is the parent.

If the next node is at the same depth, the previous node is popped. The new top is their common parent.

If the traversal has finished several nested subtrees and returns multiple levels, several nodes are popped. Each node is pushed once and can be popped once, so this cleanup remains linear overall.

For a valid traversal, the stack cannot become too short. A node at depth `d > 0` always has an already parsed ancestor at depth `d - 1` because preorder outputs parents before children.

**Choose left or right**

If `stack` is empty, the new node has depth zero and is the root. No parent attachment occurs.

Otherwise, `stack[-1]` is the parent. The code assigns the new node to `parent.left` if that field is empty; otherwise, it assigns `parent.right`.

This rule is valid because preorder visits the left child and its entire subtree before the right child. Therefore, the first direct child encountered for any parent is its left child and the second is its right child.

The source guarantee that a one-child node has a left child is essential. Without it, a single encoded child could be either left or right, and depth plus preorder alone would not distinguish the two trees. With the guarantee, the first-child rule reconstructs the unique original structure.

After attachment, the node is pushed because subsequent tokens may be its descendants.

**Trace the first example**

For `"1-2--3--4-5--6--7"`, parse value one at depth zero. The stack is empty, so one becomes the root and is pushed.

Parse two at depth one. The stack length is already one, so root one is the parent. Its left field is empty, so two becomes the left child. Push two.

Parse three at depth two. Two is the parent and receives three as its left child. The stack now represents `1 -> 2 -> 3`.

The next token, four, also has depth two. The cleanup pops three until stack length is two. Node two is again the parent. Its left child is occupied, so four becomes its right child.

The token five has depth one. The cleanup pops four and two until only root one remains. One already has left child two, so five becomes its right child.

Values six and seven repeat the same depth-two process under five. At the end, `stack[0]` still refers to root one even though deeper nodes also remain in the stack, so returning `stack[0]` returns the complete reconstructed tree.

**Why descendants do not confuse sibling attachment**

Suppose a parent has a left child with a deep subtree. All those descendant nodes sit above the parent in the stack while that subtree is active. When the right child token finally appears at the left child's depth, the cleanup removes the entire descendant path and the left child itself. The parent becomes the top, and its occupied left field directs the new node to the right.

No explicit “subtree complete” marker is needed. The next token's dash count announces exactly how far preorder has moved upward.

**Why every node is attached correctly**

Inductively assume every earlier token has been attached exactly as in the original tree and the stack contains the most recent node at each active depth. For a new node at depth `d`, preorder and the depth encoding imply that its parent is the latest node at depth `d - 1`. Popping to length `d` exposes precisely that node.

If this is its first emitted child, preorder and the one-child rule make it the left child. If a left child already exists, preorder has completed that subtree and the new direct child must be the right child. Pushing the node restores the path invariant. The induction begins with the unique depth-zero root, so all nodes and edges are reconstructed correctly.

**Why the root remains available**

The root is pushed first. Every later depth is positive, so cleanup never needs a stack length below one. Thus the root is never popped. The input contains at least one node, which makes `stack[0]` safe at return time.

## Complexity detail

Let `L = len(traversal)` and `H` be the tree height. The parser advances `index` monotonically. Every dash and digit is consumed once. Each node is pushed once and popped at most once, so all stack cleanup across the whole method costs linear time. Total time is `O(L)`, matching the manifest.

The stack holds at most one node per active depth, using `O(H)` auxiliary space. A skewed tree can have `H` equal to the number of nodes; a balanced tree uses much less. The newly allocated tree itself contains one node per input value and is required output, so it is normally excluded from auxiliary-space analysis. Including output construction gives `O(K)` space for `K` nodes.

## Alternatives and edge cases

- **Recursive parser with expected depth:** A shared string index can attempt a node only when the next dash count equals the requested depth, then recursively build left and right children. It is elegant but uses the call stack and requires careful handling when a child is absent.
- **Array indexed by depth:** Keep the most recent node at every depth and overwrite `levels[depth]` for each token. The parent is `levels[depth - 1]`. This is equivalent to the stack path and can avoid explicit popping.
- **Repeated substring splitting:** Splitting around dash patterns is fragile because depth changes and multi-digit values make separators context-dependent. A single index parses the grammar directly.
- **One-node traversal:** It has depth zero, is pushed as the root, and `stack[0]` is returned without any attachment.
- **Multi-digit values:** The digit loop consumes the entire number, so `1-401--349` is not mistaken for several nodes.
- **Deep left-only tree:** Every next depth increases by one, nothing is popped, and every new node becomes the left child of the previous node.
- **Returning several levels upward:** The cleanup can pop multiple nodes, revealing the correct ancestor in one token step.
- **Two children:** The first direct child fills `left`; after its subtree finishes, the second direct child finds `left` occupied and fills `right`.
- **Only one child:** The source guarantee says it is left, which is exactly where the first-child rule places it.
- **Why the guarantee matters:** If a lone right child were allowed, the same preorder values and depths could describe either a left child or a right child, so reconstruction would be ambiguous.
- **Positive values:** Dashes can be treated exclusively as depth markers because values never carry a minus sign.
- **Valid encoding assumption:** The exact dash-count loop relies on a digit following every dash run and on depth never jumping without a parent. These are guaranteed by the source traversal.
- **Recursion avoidance:** The iterative stack avoids Python recursion-limit failures for a highly skewed tree, while retaining the same `O(H)` path storage.
