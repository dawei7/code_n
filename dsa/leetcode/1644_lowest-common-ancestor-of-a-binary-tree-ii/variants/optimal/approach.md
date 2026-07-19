## General
**Return both structural and existence information.** A postorder DFS returns two values for every subtree: an LCA candidate and the number of targets found there. A null subtree contributes no candidate and count zero. The count combines the left count, right count, and whether the current node is either target.

**Build the candidate during the same traversal.** When both child subtrees return candidates, the current node is their first meeting point and becomes the candidate. When the current node is a target, it becomes the candidate so it can later serve as the ancestor of the other target. Otherwise propagate whichever child candidate exists.

This candidate follows the standard LCA structure, but it is not returned immediately. At the root, return it only when the accumulated count is exactly two. If a target is absent, the count is below two and the result is `null`. Thus existence verification and ancestor discovery share one traversal rather than incorrectly treating the one present target as an answer.

## Complexity detail
Each of the $n$ nodes is visited once and performs constant work, so time is $O(n)$. The recursive call stack follows at most the tree height $h$, using $O(h)$ auxiliary space; $h$ is $O(\log n)$ for a balanced tree and $O(n)$ for a skewed tree.

## Alternatives and edge cases
- **Verify existence, then run ordinary LCA:** Two membership scans followed by a standard LCA traversal remain $O(n)$ but revisit the tree unnecessarily.
- **Parent pointers and ancestor sets:** Build a parent map while locating both targets, then walk their ancestor chains. This takes $O(n)$ time and $O(n)$ additional space.
- **Repeated subtree membership tests:** Choosing a branch by searching for both targets inside each subtree is correct but can take $O(n^2)$ time on a skewed tree.
- If one target is an ancestor of the other, that target is the LCA.
- If either or both targets are absent, the required answer is `null`.
- Targets are distinct, so the found count cannot reach two by matching one node twice.
- Unique node values make the app-local value representation unambiguous; the native artifact compares node identity.
- A one-node tree cannot contain both distinct targets.
