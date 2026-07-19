## General
**Give each stack one direction**

Push new values onto an input stack. Read queue-front values from an output stack. When the output stack is empty and a front value is needed, move every input value to the output stack, reversing their order.

**The two stacks form one logical queue**

From queue front to back, the logical contents are the output stack from top to bottom followed by the input stack from bottom to top. A transfer preserves that order while making the oldest available item the output top.

**Move values only when the output side is empty**

Do not move values while the output stack still contains older items. Consequently, each enqueued value moves from input to output at most once and is popped once.

New items remain behind all items already in the output stack. When a transfer is required, reversing the input stack places its earliest pushed value on top. Thus `peek` and `pop` always select the globally earliest unremoved item, exactly matching FIFO behavior.

## Complexity detail
Each value participates in a constant number of stack operations over its lifetime, so operations are $O(1)$ amortized; an individual transfer can take $O(n)$. Stored queue values occupy $O(n)$ space.

## Alternatives and edge cases
- **Transfer on every push:** preserves FIFO order but costs $O(n)$ per insertion.
- **One dynamic-array stack with front deletion:** violates the intended stack-operation model and front deletion is linear.
- `empty` is true only when both stacks are empty; valid `pop` and `peek` calls occur only on non-empty queues.
