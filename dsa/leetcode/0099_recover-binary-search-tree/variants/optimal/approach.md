## General

A valid BST's inorder traversal is strictly increasing. Swapping exactly two node values leaves the tree structure unchanged but makes that inorder value sequence “almost sorted.” The selected solution traverses inorder, identifies the two misplaced node objects from descending adjacent pairs, and swaps their values once traversal finishes.

**What an inversion means**

Let `prev` be the node visited immediately before the current node in inorder. Normally,

$$
\texttt{prev.val}<\texttt{root.val}.
$$

If instead `prev.val > root.val`, the adjacent pair is an inversion. At least one of those two nodes is one of the mistakenly swapped nodes.

The strict `>` comparison is appropriate because BST values are unique under the problem's model. Equality is not part of the two-swapped-values pattern.

**Adjacent swapped positions create one inversion**

Start with sorted values such as `[1, 2, 3, 4]`. Swapping adjacent values `2` and `3` produces `[1, 3, 2, 4]`. There is one inversion, `3 > 2`. The larger predecessor is the first misplaced node, and the smaller current node is the second.

On that first inversion, the source sets `first = prev` and always sets `second = root`.

**Separated swapped positions create two inversions**

Swapping `2` and `5` in `[1, 2, 3, 4, 5, 6]` gives `[1, 5, 3, 4, 2, 6]`. The descending pairs are `5 > 3` and `4 > 2`.

At the first inversion, `prev` is the too-large value moved left, so it must be remembered as `first`. The current node may merely be a correctly positioned value that follows it, so it is only a provisional `second`.

At the second inversion, the current node is the too-small value moved right. The code leaves `first` unchanged and updates `second = root`. After the full traversal, the endpoints are exactly the two swapped nodes.

This explains the asymmetry: assign `first` only once, but assign `second` on every inversion.

Another way to see the rule is to compare the corrupted sequence with its sorted order. The value moved too far left is larger than values that should precede it, so it appears on the left side of the first descending boundary. The value moved too far right is smaller than values that should follow it, so it appears on the right side of the last descending boundary. When the two positions are adjacent, the first and last boundary are the same boundary. The code's assignments implement this single rule for both cases without first determining whether the swapped positions were adjacent.

**How the recursive traversal maintains order**

For each node, `dfs` processes the left subtree, examines the current node against `prev`, updates `prev`, and processes the right subtree. That is exact inorder order.

The variables `prev`, `first`, and `second` live in the enclosing method. Declaring them `nonlocal` lets every recursive call share the same traversal history and detected endpoints.

An empty child returns immediately. The first real inorder node sees `prev is None`, so no comparison is attempted. Thereafter, `prev` always refers to the immediately preceding inorder node because it is updated after the current comparison and before entering the right subtree.

**Why swapping values repairs the tree**

The premise states that the original BST became invalid only because the values of exactly two existing nodes were exchanged. Detection finds those same node objects. Swapping `first.val` and `second.val` reverses the accidental operation.

No child pointer changes, so tree structure is preserved exactly. The method returns implicitly with `None`, matching the in-place contract.

**Why scanning the whole tree is useful**

The helper does not stop after finding the first inversion because separated swapped nodes require the second inversion to identify the smaller endpoint. It also does not terminate recursion after the second inversion; continuing is harmless and keeps the implementation simple. Under the exact-two-swaps guarantee, no later distinct inversion changes `second` incorrectly.

If the input were already valid, `first` and `second` would remain `None`, and the final swap would fail. That is outside the contract, which guarantees exactly two swapped nodes.

## Complexity detail

Every node is visited once and each visit performs constant work, so time is $O(n)$.

The exact source uses recursive inorder traversal. Its call stack reaches the tree height $h$, so auxiliary space is $O(h)$: $O(\log n)$ for a balanced tree and $O(n)$ for a skewed tree. This conflicts with the manifest's $O(1)$ space claim, which would require Morris traversal. The three shared node references are constant space but do not eliminate the recursion stack.

With at most 1000 nodes, a maximally skewed Python tree is near the default recursion limit and may still risk `RecursionError` depending on environment overhead.

## Alternatives and edge cases

- **Morris inorder traversal:** Temporary predecessor threads provide the requested $O(1)$ auxiliary space while retaining $O(n)$ time.
- **Explicit stack:** Avoid recursion-limit risk and use $O(h)$ auxiliary storage.
- **Store the entire inorder list:** Detect misplaced values in an array and traverse again to repair nodes. It is simpler conceptually but uses $O(n)$ space.
- **Adjacent swap:** Only one inversion occurs; first and second are taken from that pair.
- **Nonadjacent swap:** Two inversions occur; retain the predecessor from the first and current node from the last.
- **Extreme integer values:** Node-to-node comparisons need no infinity sentinel and handle the full range.
- **Structure preservation:** Swap only `val` fields, never node links.
- **Exact-two-node guarantee:** The final unconditional swap relies on it; a defensive general-purpose validator would check both references first.
- **Why child comparisons are insufficient:** A swapped value may still compare correctly with its immediate parent while violating an older ancestor's range. Inorder exposes the resulting global disorder.
- **No need to sort:** Sorting all inorder values would reveal the expected sequence but adds storage and loses the direct node identities needed for the final swap. Tracking two inversions is sufficient.
