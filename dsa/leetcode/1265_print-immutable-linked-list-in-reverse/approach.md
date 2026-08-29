## General

**Why ordinary linked-list reversal is unavailable**

A normal singly linked list can sometimes be reversed by changing each node's next pointer. This list is immutable, and the interface exposes only `getNext()` and `printValue()`. There is no permitted way to read a value into a separate variable, change a link, or move directly from a node to its predecessor.

Forward movement is easy: repeatedly call `getNext()`. Reverse output is harder because the tail must print first even though it is discovered last. The exact solution uses the program's call stack to remember every node encountered on the forward trip. Recursive return then visits those remembered nodes in the opposite order.

**The two phases hidden in a tiny function**

For a non-null `head`, the method first calls itself on `head.getNext()`. It does not print the current node yet. This continues until the recursive call receives `None`, the position just beyond the tail. That call fails the `if head` condition and returns immediately.

Only after the recursive call returns does the source execute `head.printValue()`. The deepest non-null call belongs to the tail, so it prints first. That call finishes, revealing the previous node's suspended call, which prints next. Unwinding continues until the original head prints last.

For a list `1 -> 2 -> 3 -> 4`, the calls are conceptually nested as `solve(1)` waiting for `solve(2)`, which waits for `solve(3)`, which waits for `solve(4)`, which waits for `solve(None)`. The empty call returns. Then nodes print in the order four, three, two, one.

This order depends on placing `printValue()` after the recursive call. Printing before recursion would produce the original head-to-tail order and fail the task.

**What each stack frame remembers**

Every active invocation has its own local reference named `head`. While the deeper invocation follows the next pointer, the earlier frame remains suspended and retains its node reference. No node field is changed. The call stack is therefore acting as an implicit stack of immutable node handles.

The function never needs direct access to a stored value. When a frame resumes, it asks that exact node to print itself by calling the provided `printValue()` API. This respects the interface restriction that values are not publicly readable.

The return type is `None` because output is a side effect. There is no result list to return, and the method does not attempt to concatenate values. Every real node calls `printValue()` exactly once.

**Why the output is complete and reversed**

Consider a suffix beginning at some node `u`. Assume the recursive call on `u.getNext()` prints every node after `u` exactly once in tail-to-front order. Once that call is finished, the method prints `u` exactly once. The resulting output is the entire suffix beginning at `u` in reverse.

The base suffix beginning at `None` contains no nodes and prints nothing, which is correct. Applying the inductive reasoning backward through the list shows that the initial call prints every list node exactly once, from tail to head.

No mutation occurs because the only node methods invoked are the two approved operations. `getNext()` observes the next node, and `printValue()` produces output. The source assigns neither a node value nor a next pointer.

**Why linear extra space is intentional in this variant**

The most direct way to reverse a forward-only sequence is to remember all elements until the end is known. Recursion makes that memory implicit and keeps the implementation exceptionally small. The follow-up asks about smaller-space tradeoffs, but the exact Optimal artifact chooses the standard linear-time, linear-stack solution. Its behavior should be understood on those terms rather than attributing a constant-space technique to this code.

The local `if head` check also gives the recursion a clean sentinel. Although the package says the input list is nonempty, every valid list ends with `getNext()` returning `None`, so one empty recursive call is always necessary to start unwinding.

## Complexity detail

Let $n$ be the number of nodes. The method makes one non-null call for each node and one final call for `None`. Each non-null call performs one `getNext()` and one `printValue()`, both treated as constant-time interface operations. Total time is $O(n)$.

Before any node prints, all $n$ non-null calls are simultaneously active. Each frame stores a node reference and return information, so recursion consumes $O(n)$ stack space. The output is printed directly rather than accumulated, so there is no result array. Total auxiliary space is $O(n)$.

The $O(n)$ time is optimal because every node must be printed once. Achieving both linear time and constant space is impossible with only a one-way link unless the environment provides another capability: without remembering nodes, returning to an earlier node requires restarting from the head and causes repeated traversal.

The constraint allows up to one thousand nodes. That is near Python's usual default recursion limit, and surrounding call frames can make a maximum-length list a practical recursion-risk in some runtimes. The accepted source uses recursion, but an explicit stack is operationally safer if the execution environment does not guarantee adequate recursion depth.

## Alternatives and edge cases

- **Explicit node stack:** Traverse forward, append every node reference, then pop and call `printValue()`. It has the same $O(n)$ time and $O(n)$ space while avoiding recursion-depth limits.
- **Square-root decomposition:** Store the start of blocks of about $\sqrt n$ nodes and recursively reverse one block at a time. It keeps $O(n)$ time while reducing space to $O(\sqrt n)$, at the cost of much more logic and extra passes.
- **Divide and conquer:** Repeatedly find subrange midpoints, print the right half before the left, and use $O(\log n)$ stack space. Because a singly linked range takes linear time to split, total time grows to $O(n\log n)$.
- **Repeated scan with constant space:** Find the last unprinted node by restarting from the head each time. This respects immutability and uses $O(1)$ space but costs $O(n^2)$ time.
- **Mutating reversal is forbidden:** Any solution that rewires next pointers violates the immutable interface even if it would otherwise be linear time and constant auxiliary space.
- **Single node:** The recursive call reaches `None` immediately, then the only node prints once.
- **Duplicate values:** Nodes, not distinct values, are processed. Equal values at different positions each print in their proper reverse position.
- **Negative and zero values:** The solution never inspects numeric contents, so their sign has no effect.
- **Nonempty public input:** The contract supplies at least one node, but the function also safely handles `None` by printing nothing.
- **API-only access:** The code does not assume fields such as `val` or `next` and therefore respects the platform-provided immutable node abstraction.
- **Recursion limit:** For environments with a shallow call-stack limit, prefer the explicit stack even though its asymptotic space is identical.
