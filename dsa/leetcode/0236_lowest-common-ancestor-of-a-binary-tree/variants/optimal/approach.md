## General
**Let each subtree report the surviving target path**

Depth-first search returns a target node when it encounters one. Otherwise it recursively searches both children.

**Two non-null child reports meet at the answer**

If both child searches return a match, the current node is the first place their paths meet and is the LCA. If only one child returns a match, propagate it upward.

For every completed recursive call, its return value is null when its subtree contains neither target; otherwise it is the target or LCA that must be propagated to the caller.

A target node correctly represents a subtree already containing that target and possibly the other below it. When non-null results arrive from both children, no descendant can contain both targets, so the current node is the lowest common ancestor. A single result remains the only possible answer in that subtree and is safely propagated.

When the current node is itself a target, returning it also handles the case where the other target lies below it: ancestors propagate this target unless a separate branch report proves that an even higher node is required. With both targets guaranteed to exist, the report that reaches the root is exactly their lowest common ancestor.

## Complexity detail
In the worst case every node is visited once, giving $O(n)$ time. Recursion occupies one root-to-leaf path, or $O(h)$ space.

## Alternatives and edge cases
- **Parent map plus ancestor set:** is iterative but uses $O(n)$ space.
- **Two root-to-target paths:** traverses more than once and stores both paths.
- One target may itself be the ancestor; targets can occur in opposite or identical-side subtrees.
