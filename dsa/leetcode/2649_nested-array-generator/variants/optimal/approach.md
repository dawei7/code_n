## General

Recursive inorder traversal needs to remember, for every currently open array, which element should be visited next. Represent that suspended work explicitly with a stack of frames. Each frame stores an array and its next unread index; begin with one frame for the outer input.

Inspect the top frame. If its index has reached the array length, that array is complete, so pop the frame. Otherwise read the indexed value and advance the frame immediately. For an integer, yield it. For a nested array, push a fresh frame for that array so its entire contents are visited before returning to the parent's following element.

At every suspension point, the stack describes the unique path from the outer array to the array containing the next possible integer. Indices below the top frame point just after the nested array currently being explored. Consequently, finishing and popping a child resumes its parent at exactly the correct position. This is the same depth-first left-to-right order as recursive inorder traversal.

Using an explicit stack avoids constructing a flattened copy and remains safe even for very deep legal inputs. The generator is lazy: it pauses as soon as one integer is yielded and retains only the traversal frames needed to resume.

## Complexity detail

Let $N$ be the total number of integer entries and nested-array entries, and let $d$ be the maximum nesting depth. Each entry is inspected once and each array frame is pushed and popped once, giving $O(N)$ total time across complete consumption. The explicit traversal stack contains at most one frame per active nesting level, so auxiliary space is $O(d)$. The yielded output is streamed rather than stored by the generator.

## Alternatives and edge cases

- **Recursive generator with `yield*`:** This mirrors the definition elegantly, but an explicit stack avoids depending on the JavaScript call-stack limit at large nesting depth.
- **`arr.flat(Infinity)`:** Flattening first gives the right order but violates the no-flattened-copy challenge and loses lazy production.
- **Queue traversal:** Breadth-first processing changes the required recursive left-to-right order.
- Empty arrays push a frame that is immediately popped and yield nothing.
- An empty outer array completes on the first `next()` call.
- Integers may repeat or equal zero; traversal preserves every occurrence without filtering or deduplication.
- Increment the parent index before descending so returning from a child cannot revisit that child.
