## General

**Why the digits are processed from right to left.** The head node stores the most significant decimal digit, but ordinary multiplication with a carry starts at the least significant digit. When a digit is doubled, its carry must be added to the digit immediately to its left. A singly linked list only provides links toward the right, so starting at the head would discover a carry after passing the node that needs it.

The exact solution handles this direction mismatch by reversing the input list. After reversal, the original last digit becomes the first node, so carries flow in the same direction as the links.

**How the reversal helper works.** The nested `reverse` function creates a dummy node whose `next` field represents the head of the reversed prefix. For each original node `cur`, it first saves `cur.next` in a local variable named `next`. Saving that pointer is essential because the next assignment changes `cur.next`.

It then inserts `cur` at the front of the reversed prefix:

`cur.next = dummy.next`

`dummy.next = cur`

Finally, `cur = next` advances to the untouched suffix. After every iteration, `dummy.next` leads through exactly the nodes already visited, in reverse order, while `cur` leads through the unvisited original suffix. When `cur` becomes `None`, every link has been reversed and `dummy.next` is the new head.

The local name `next` shadows Python's built-in `next` function, but no built-in iterator advancement is needed in this helper, so the shadowing does not affect behavior.

**Build the doubled digits with a running carry.** After the first reversal, `head` points to digits from least significant to most significant. The code creates a new dummy result node and lets `cur` point to the last constructed result node. It initializes multiplier `mul` to two and `carry` to zero.

For each reversed input digit, it computes

`x = head.val * mul + carry`.

The new digit is `x % 10`, and the carry for the next more significant position is `x // 10`. Because an input digit is at most nine and the incoming carry is at most one, $x$ is at most nineteen, so the outgoing carry is always zero or one.

A newly allocated `ListNode(x % 10)` is appended to the result. The input node's value is not overwritten. The input cursor then advances through the reversed original list.

For `189`, reversal exposes digits nine, eight, and one. The computations are eighteen, seventeen, and three. They append digits eight, seven, and three while the carries are one, one, and zero. This result list is still reversed, representing `873` in link order rather than the required `378`.

**Handle a final carry.** After every original digit has been processed, a nonzero carry represents one new most significant digit. In the reversed working order, that digit belongs at the tail, so the code appends one more node. For `999`, the three calculated output digits are eight, nine, and nine, followed by carry one.

**Reverse the new result into normal order.** The last statement calls `reverse(dummy.next)`. This reversal acts on the newly allocated result nodes, not on the original nodes. It returns the most-significant-first representation expected by the contract.

The two reversals serve different objects: the first destructively reverses the input list so its digits can be read in carry order; the second reverses the freshly built output list so it can be returned in display order.
Suppose the loop is about to process original digit position $p$, counting from the least significant end. The already constructed result contains the correct lower $p$ digits of twice the input, and `carry` is exactly the value that decimal multiplication sends into position $p$. Computing twice the current digit plus this carry, storing its remainder modulo ten, and carrying its quotient by ten is precisely the grade-school multiplication rule. This preserves the invariant for the next position. The optional final carry completes the most significant position, so reversing the constructed digits yields exactly twice the represented integer.

**The exact source is not the in-place forward scan described by the manifest.** The manifest says the method reads the next digit to determine carry while scanning from the most significant side and mutates the list in place. This code instead reverses the supplied nodes, reads from the least significant side, and allocates an entirely new output list.

That distinction has an observable side effect. The first reversal is never undone on the original nodes. The variable `head` is consumed until it becomes `None`, but external references to original nodes see their links reversed. In particular, the caller's old head becomes the tail of the reversed original chain. The returned list is correct and independent, but this is not a preservation-oriented or in-place implementation.

## Complexity detail

Let $n$ be the number of input nodes. The first reversal visits all $n$ nodes. The multiplication loop visits the same $n$ input nodes and creates $n$ output nodes, plus at most one carry node. The final reversal visits the $n$ or $n+1$ output nodes. Total time is $O(n)$.

The reversal helper itself uses only a dummy node and a constant number of pointers, so its auxiliary workspace is $O(1)$. The multiplication loop also uses constant scalar state. However, the exact method allocates a new output list of $n$ or $n+1$ nodes. Including those allocations, additional space is $O(n)$.

If the required returned list is excluded from auxiliary-space accounting, the scratch space is $O(1)$. That convention can explain an $O(1)$ auxiliary label, but it should not imply that the code reuses the original nodes: it does not. No recursion stack is used.

## Alternatives and edge cases

- **Forward one-pointer mutation:** Before doubling a digit, inspect whether the next original digit is at least five; that fact determines whether the current doubled digit receives a carry from the right. A leading node may be added when the first digit is at least five. This achieves $O(n)$ time, $O(1)$ auxiliary space, and mostly reuses the input list, matching the manifest.
- **Reverse and mutate the same nodes:** Reverse the input, double node values in place with carry, append a carry node if needed, and reverse it back. This retains the easy grade-school direction while avoiding a complete second list and restoring the original node order as the returned result.
- **Stack of nodes or digits:** A stack permits right-to-left processing without changing links, but it uses $O(n)$ auxiliary storage.
- **Recursive carry propagation:** Recursing to the tail and handling digits while unwinding follows the correct direction, but a list of up to $10^4$ nodes can exceed Python's recursion limit.
- **Input value zero:** The one node containing zero produces `x = 0`, no final carry, and a returned one-node zero list.
- **Leading carry:** Any most significant digit at least five may produce a result with one extra digit; the explicit carry append handles it.
- **Long run of nines:** Carry one propagates through every node, as in `999` becoming `1998`.
- **No leading zero in the result:** A final node is created only for carry one, and otherwise the doubled most significant digit remains nonzero for every positive input.
- **Input mutation:** External aliases to the original list observe reversed links even though the returned list uses new nodes. A production implementation should either document this or restore/reuse the input deliberately.
