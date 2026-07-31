## Description

You are given a linked list of length `n`. In addition to `next`, every node has a `random` pointer that may refer to any node in the list or to `null`.

Construct a deep copy containing exactly `n` brand-new nodes. Each clone must preserve its original node's value, while its `next` and `random` pointers must target the corresponding cloned nodes so that the copied pointer structure matches the original. No pointer in the copied list may refer to an original node.

For example, if original node `X` has `X.random -> Y`, then the corresponding copied nodes `x` and `y` must satisfy `x.random -> y`.

Return the head of the copied list.

The displayed input and output encode the `n` nodes as `[val, random_index]` pairs. Here `val` is `Node.val`, while `random_index` is the zero-based index targeted by `random`, or `null` when there is no target. Your native solution receives only the original list's `head`.
