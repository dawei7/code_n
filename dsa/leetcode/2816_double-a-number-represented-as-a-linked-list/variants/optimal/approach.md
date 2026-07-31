## General

**Read the carry before changing its source digit**

Ordinary multiplication proceeds from the least significant digit because each position sends a carry to its left neighbor. For doubling, however, that carry is always either zero or one, and it depends only on whether the original digit to the right is at least `5`. This makes a forward scan possible.

At a node with digit `d`, write `(2 * d) % 10`. If the next node exists and its still-original digit is at least `5`, add one to the current result digit. The scan has not yet reached that next node, so the comparison always observes the source value rather than a doubled value.

If the original first digit is at least `5`, doubling needs one extra leading digit. Prepend a zero node before the scan. Its next node triggers a carry of one, so the same rule changes the sentinel from zero to one without any separate final arithmetic case.

For every position, the algorithm writes the last digit of twice that position's source digit and adds exactly the carry produced by the suffix immediately to its right. Those are precisely the two contributions in decimal multiplication. The optional sentinel handles the only carry that has no original position, so the mutated list represents exactly twice the input.

## Complexity detail

Let $n$ be the number of input nodes. The scan visits each original node once and performs constant work per node, for $O(n)$ time. Apart from the returned list itself and at most one new leading result node, it uses $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Reverse twice:** Reversing the list, processing the usual right-to-left carries, and restoring the order is linear and constant-space, but performs extra pointer mutations.
- **Stack of nodes or digits:** A stack makes right-to-left processing straightforward but requires $O(n)$ auxiliary space.
- **Repeated predecessor searches:** Finding each digit's predecessor from the head avoids a stack but takes $O(n^2)$ time on long lists.
- The single node `[0]` remains `[0]`; it must not gain a leading zero.
- A first digit of `5` is the exact boundary at which a new leading node becomes necessary.
- A next digit of `5` through `9` contributes a carry of one to the current digit, even when digits farther right also produce carries.
- The next digit must be inspected before it is mutated; inspecting an already-doubled value would lose the source carry condition.
