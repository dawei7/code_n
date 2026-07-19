## General
**Count the subarrays owned by each value**

Instead of finding a minimum independently for every subarray, make each index contribute its value once for every subarray in which that occurrence is the selected minimum. For index `mid`, suppose `left` is the nearest index to its left with a strictly smaller value, and `right` is the nearest index to its right with a value less than or equal to `arr[mid]`. A subarray owned by `mid` may choose any start from `left + 1` through `mid` and any end from `mid` through `right - 1`. It therefore contributes

$$
\texttt{arr[mid]}\,(\texttt{mid}-\texttt{left})\,(\texttt{right}-\texttt{mid}).
$$

Using a strict comparison on one boundary and a non-strict comparison on the other assigns a subarray containing equal minima to exactly one occurrence. Here it is assigned to the rightmost equal minimum, preventing both omissions and double counting.

**Discover both boundaries with one monotonic stack**

Maintain indices whose values are strictly increasing from the bottom of the stack to the top. Scan `arr` from left to right and append one conceptual sentinel smaller than every legal value. Before pushing the current index `right`, pop while `arr[stack[-1]] >= arr[right]`. For each popped `mid`, the current index is its first less-than-or-equal boundary on the right. After the pop, the new stack top is its nearest strictly smaller boundary on the left, or $-1$ if none exists.

At that moment both boundaries for `mid` are known, so add its complete contribution. Every index is eventually popped, including those flushed by the sentinel. Each non-empty subarray has a minimum; choosing its rightmost minimum gives exactly the strict-left and non-strict-right ownership just described. Thus every subarray contributes its minimum exactly once. Apply the modulus while accumulating the contributions.

## Complexity detail
Every index is pushed onto the monotonic stack once and popped once, so the total work is $O(n)$. The stack can hold $n$ indices for a strictly increasing array, requiring $O(n)$ auxiliary space.

## Alternatives and edge cases
- **Enumerate all subarrays:** Extending every start while maintaining a running minimum is correct but takes $O(n^2)$ time.
- **Range-minimum data structure:** A sparse table or segment tree answers individual minimum queries faster, yet there are still $O(n^2)$ subarrays to query.
- **Two boundary passes:** Previous-smaller and next-smaller arrays can be computed separately and then combined; this is also $O(n)$ time but stores more intermediate state.
- **Equal values:** Using the same strictness on both boundaries either double counts or misses tied-minimum subarrays; one side must break ties differently.
- **Strictly increasing input:** No index is popped until a smaller value or the sentinel arrives, so the stack may reach length $n$.
- **Strictly decreasing input:** Each new value immediately resolves earlier contributions, and the same linear bound holds.
- **Single element:** Its only subarray contributes that element once.
- **Modulo:** Reduce the accumulated contribution by $10^9+7$ so large counts remain bounded without changing the final residue.
