## General

The required array must contain node values in the linked list's forward order. The head already identifies the first node, and every node's `next` pointer identifies the following node. A single forward traversal therefore produces the output directly.

`ans` starts as an empty list. While `root` is not null, the method appends `root.val` and then advances `root = root.next`. The loop stops when the last node's next pointer is null.

The name `root` in the method signature plays the role called `head` in the description. Reassigning this local variable does not modify any node or the caller's reference; it merely moves the traversal cursor.

The traversal invariant is: before each loop iteration, `ans` contains exactly the values of all nodes strictly before `root`, in their original order. Appending the current value extends that correct prefix by one, and following `next` moves to the only node that should come next. When `root` becomes null, no nodes remain and `ans` is the complete ordered conversion.

Although nodes also have `prev` pointers, they are unnecessary when traversal begins at the head and the desired order is forward. Reading both directions would add complexity and could revisit nodes. The backward link is part of the data structure, not a requirement that every operation use it.

For `1 <-> 2 <-> 3`, the cursor visits one, two, and three. Each value is appended once, yielding `[1,2,3]`. Duplicate values do not affect traversal: five different nodes containing two produce five array entries, because the conversion preserves nodes rather than distinct values.

**Why no cycle detection is used.** A valid doubly linked list ends in null and has consistent forward links. The problem supplies such a list. On malformed cyclic data, the loop would not terminate, but adding a visited set would impose extra space for a condition outside the contract.

**Why values are copied but nodes are not.** The output type is a list of integers. Appending `root.val` captures each value, not a reference to the linked-list node. Later structural changes to nodes cannot change integers already stored in the result.

The node definition is included in a comment because the platform provides it. The user solution needs only to consume `val` and `next`; it does not construct or redefine nodes.

This is the optimal possible traversal. Any correct algorithm must inspect every node's value at least once to place it into an $n$-element output. Following `next` visits each with constant work.

## Complexity detail

Let $n$ be the number of nodes. The loop performs one append and one pointer advance per node, taking $O(n)$ time.

The returned array contains $n$ integers and therefore uses $O(n)$ required output space. Apart from the output, the traversal cursor uses $O(1)$ auxiliary space. The manifest reports $O(n)$ space because the produced array necessarily grows with the list.

Appending to a Python list is amortized $O(1)$, so all appends total $O(n)$.

## Alternatives and edge cases

- **Recursive traversal:** Append the current value and recurse on `next`. It preserves order but uses $O(n)$ call-stack space and can hit recursion limits on larger lists.
- **Traverse backward from the tail:** This would require first finding the tail and then either reversing the collected values or inserting at the front. It adds work without benefit when the head is available.
- **Use `prev` for validation:** Checking that each next node points back to the current node can diagnose malformed lists, but validation is not requested.
- **Convert through an iterator:** A custom iterator can encapsulate the same pointer loop. For a one-method task, the direct traversal is clearer.
- **One node:** Its value is appended and its null next pointer ends the loop, producing a one-element array.
- **Repeated values:** Every node contributes separately; no set or deduplication should be used.
- **Null input:** The stated list has at least one node, but the type permits optional input. If null is supplied, the loop is skipped and an empty list is returned gracefully.
- **Negative or larger values:** The pointer logic is independent of values, though the documented values are from one through fifty.
- **Input preservation:** Only the local `root` variable changes. Neither `next` nor `prev` fields are assigned, so the list structure remains intact.
- **Malformed cycle:** The exact method assumes the valid-list contract and would loop forever on a forward cycle; cycle detection is intentionally absent.
- **Platform-provided node:** The commented class documents the interface. Recreating it inside the solution would be unnecessary and could conflict with the harness.
- **Forward order versus reverse order:** The requested sequence begins at the head, so appending while following `next` is exact. Following `prev` would either stop immediately at the head or require locating the tail first and reverse the intended order.
- **Asymmetric pointer corruption:** Even if a malformed node's `prev` were wrong, this method would still follow the `next` chain it is given. The valid-list contract guarantees consistency, so the solution does not spend time cross-checking links that do not affect the requested traversal.
