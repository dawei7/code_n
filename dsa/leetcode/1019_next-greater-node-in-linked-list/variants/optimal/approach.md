## General
**Expose indexed values:** Traverse the linked list once and copy node values into an array. Initialize an equally sized answer array with zeroes and keep a stack of unresolved indices.

**Resolve smaller nodes at the first greater value:** Process values from left to right. While the stack is nonempty and `values[stack[-1]] < value`, pop that earlier index and set its answer to the current value. Then push the current index as unresolved.

**Preserve the nearest qualifying node:** Stack values are non-increasing. A node is popped at the first later value that exceeds it, so no closer qualifying node was skipped. Equal values remain on the stack because the comparison must be strictly larger.

Every index is eventually resolved by its first greater value or remains on the stack with its initialized zero. Since an index is pushed once and popped at most once, the method covers all positions without repeated suffix scans.

## Complexity detail
Reading the $N$ nodes and processing the value array are linear. Each index enters and leaves the stack at most once, giving $O(N)$ time. The values, answer, and stack arrays use $O(N)$ space; the answer itself is required output.

## Alternatives and edge cases
- **Scan every suffix:** Searching rightward independently from each node is direct but takes $O(N^2)$ time on a non-increasing list.
- **Reverse monotonic stack:** Processing copied values from right to left with a stack of candidate values also achieves $O(N)$ time.
- **Strictly decreasing list:** Every answer remains zero.
- **Equal values:** They do not resolve one another; only a strictly larger value qualifies.
- **Single node:** It has no later node, so return `[0]`.
