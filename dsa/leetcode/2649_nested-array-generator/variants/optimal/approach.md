## General

**Flatten lazily rather than building a flat array**

The required order is recursive left-to-right traversal:

- visit each item of the current array in order;
- yield an integer immediately;
- recurse into a nested array at the position where it occurs.

The exact generator reproduces this order with an explicit stack. It yields one integer at a time and never constructs a complete flattened copy.

This is especially important when the consumer stops early: unvisited portions of the nested structure require no work.

**A stack frame represents suspended array traversal**

Each frame has:

- `array`: the current nested array;
- `index`: the next position in that array to inspect.

The stack begins with one frame for the outer input at index zero.

The top frame is always the array whose traversal is currently active. Frames below it represent parent arrays paused while a nested child is explored.

This explicitly models the call stack that a recursive DFS would otherwise use.

**Finish and pop exhausted arrays**

At the beginning of each loop iteration, the code reads the top frame.

If:

`frame.index === frame.array.length`,

that array has no remaining values. The frame is popped, and the loop continues with its parent.

For the root frame, popping it empties the stack and terminates the generator.

An empty nested array is handled immediately: its new frame has index zero and length zero, so the next iteration pops it without yielding anything.

**Advance the parent before descending**

For a non-exhausted frame:

`value = frame.array[frame.index]`

reads the next item, then:

`frame.index += 1`

advances the frame before any descent or yield.

This timing is essential. If the value is a nested array, its child frame may remain on top for many iterations. When that child finishes, the parent must resume at the following item rather than revisit the same child forever.

Likewise, after yielding an integer and later resuming, the index already points to the next position.

**Descend into arrays, yield integers**

`Array.isArray(value)` distinguishes containers from leaves.

- For a nested array, push a fresh frame `{ array: value, index: 0 }`. The next loop iteration begins exploring that child.
- For an integer, execute `yield value`.

Yield suspends the generator with the entire stack preserved. The consumer receives exactly that integer. On the next `next()` call, execution resumes after the yield and returns to the loop.

**Trace nested traversal**

For `[[[6]],[1,3],[]]`:

1. root reads `[[6]]`, advances root index, and pushes its frame;
2. that frame reads `[6]` and pushes another frame;
3. deepest frame reads six, advances, and yields six;
4. on resumption, deepest frame is exhausted and pops;
5. its parent is exhausted and pops;
6. root reads `[1,3]` and pushes it;
7. that frame yields one and then three;
8. root finally pushes the empty array, which immediately pops;
9. root exhausts and the stack becomes empty.

The output is `[6,1,3]`.

**Why the order matches recursive inorder traversal**

Before descending, the parent frame's current position is consumed but its later positions remain pending below the child frame.

Because the stack is last-in, first-out, the entire child array is processed before the parent resumes. Within each frame, indices increase from left to right.

These are exactly recursive traversal semantics. Structural induction gives the same result:

- an integer yields itself;
- an array yields the concatenation of each child's traversal in order.

The stack implements that definition without recursion.

**Why explicit stack is important for the constraint**

Maximum nesting depth can reach $10^5$. A recursive JavaScript generator would use one language call frame per nested array and likely overflow the runtime stack.

The explicit array-backed stack stores frames on the heap and can represent very deep nesting within available memory.

Its size depends on current nesting depth, not on the total number of integers.

**Laziness and partial consumption**

Calling `inorderTraversal(arr)` creates a generator object. Traversal work occurs only as `next` requests values.

If a consumer requests the first integer and stops:

- later siblings are never inspected;
- no flat output array is allocated;
- the stack retains only the suspended path while the generator remains reachable.

This distinguishes a true generator traversal from computing `arr.flat(Infinity)` and then iterating its result.


At every loop start, frames from bottom to top describe a path of nested arrays. For each non-top parent, its index points immediately after the child represented by the next frame. The top frame's index points to its next unprocessed value.

Pushing preserves this invariant by advancing the parent first. Popping returns to the correct next parent position. Yielding an integer preserves it because the top index was already advanced.

Therefore, every integer is yielded once in recursive left-to-right order, and termination occurs exactly after all reachable items are processed.

## Complexity detail

Let $N$ be the total number of integer leaves plus array entries/containers visited. Each array item is read once, each frame is pushed and popped once, so full traversal takes $O(N)$ time.

If maximum nesting depth is $d$, at most $d+1$ frames are active, so generator working space is $O(d)$. No $O(N)$ flattened output is stored.

Per yielded integer, amortized work includes any empty-container pops encountered before the next leaf.

## Alternatives and edge cases

- **Recursive generator with `yield*`:** Elegant but risks call-stack overflow at depth $10^5$.
- **`flat(Infinity)`:** Simple but creates a full flattened array and defeats the no-copy follow-up.
- **Stack of raw values in reverse order:** Also iterative, but may push many siblings at once and use width-dependent rather than depth-only space.
- **Empty root array:** Its only frame pops and the generator finishes without yielding.
- **Empty nested array:** It contributes no integers and traversal resumes at the parent.
- **Deep singleton nesting:** Stack grows with depth but avoids language recursion.
- **Several sibling arrays:** Each is fully traversed before the next sibling.
- **Early consumer stop:** Unrequested values are never visited.
- **Index increment timing:** It must occur before descent or yield to prevent duplication.
- **Input preservation:** Frames hold references and indices but never modify arrays.
