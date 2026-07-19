## General
**Convert an offset from the end into a fixed pointer gap**

The list length is not known when traversal begins, but two pointers can encode the required distance. Advance a fast pointer `n` steps from the head. If it becomes null at that point, exactly `n` nodes exist and the target is the original head, so return `head.next`.

Otherwise start a slow pointer at the head. Advance both pointers together until `fast.next` is null. Their fixed gap means `slow.next` is now the node `n` positions from the end. Bypass it with `slow.next = slow.next.next`.

**Stop with the slow pointer at the predecessor**

After the initial advance, fast is exactly `n` links ahead of slow. Moving both one link preserves that distance. Stop when `fast.next` is null rather than when `fast` is null: fast is then the final node, there are exactly $n - 1$ nodes after slow, and `slow.next` is the requested node. Keeping the predecessor is what makes removal a constant-time link update.

**Trace a representative input**

For `[1, 2, 3, 4, 5]` and $n = 2$, fast advances from 1 to 3. Moving both pointers until fast reaches 5 leaves slow at 3. Bypassing slow's next node removes 4 and returns `[1, 2, 3, 5]`.

**Why the fixed gap identifies the predecessor**

After the fast pointer advances `n` nodes, exactly `n` links separate it from the slow pointer. Moving both pointers together preserves that gap. When fast reaches the final node, slow is therefore one node before the element that has exactly $n - 1$ successors—the nth node from the end.

Bypassing `slow.next` removes precisely that target and leaves every other link in order. If the initial advance places fast beyond the list, the target is the head itself; handling that case separately supplies the predecessor relationship that the real list lacks. A dummy predecessor is an equivalent way to unify both cases.

## Complexity detail
The fast pointer traverses at most the full list, while the slow pointer traverses only part of it. Even though there are two pointer movements, each is linear and total time is $O(L)$ for list length `L`. Only two pointers are stored, so auxiliary space is $O(1)$.

## Alternatives and edge cases
- **Two passes:** first count nodes, then walk to the predecessor. It is still $O(n)$ time and $O(1)$ space but does not meet the one-pass follow-up.
- **Store every node:** permits direct indexing from the end but uses $O(n)$ auxiliary space.
- **Recursive removal:** naturally counts while unwinding but uses $O(n)$ call-stack space.
- Removing the only node and removing the head of a longer list both take the `fast is null` branch after the initial gap is created.
- The contract guarantees `n` is valid. Defensive handling for `n` larger than the list length would be an additional API decision, not part of this algorithm.
- A dummy node is a common variant that removes the separate head case by starting both pointers before `head`; it has the same complexity.
