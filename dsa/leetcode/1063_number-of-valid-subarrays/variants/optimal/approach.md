## General
**Find where each start becomes invalid:** For a starting index `i`, every subarray ending before the first later value strictly smaller than `nums[i]` is valid. If that first smaller value is at index `j`, then `i` contributes `j - i` valid endings. If none exists, it contributes `n - i`.

**Maintain unresolved starts:** Scan from left to right with a stack of indices whose first strictly smaller value has not appeared. When `nums[current]` is strictly smaller than the value at the stack top, pop that start and add `current - start` to the answer. Continue popping because the same current value may terminate several larger starts, then push the current index.

**Preserve equality:** Do not pop when values are equal. A leftmost value is permitted to equal later values, so equal indices must remain unresolved until a genuinely smaller value appears. After the scan, every remaining start extends validly to the final array position and contributes `n - start`.

Each index is resolved at exactly its first strictly smaller value: earlier scanned values were not smaller, and the current pop proves the boundary. Thus every counted ending is valid and no ending at or beyond that boundary is counted. Unpopped indices have no smaller value to their right, so their suffix contributions are all valid.

## Complexity detail
Every index is pushed once and popped once. All stack operations therefore total $O(N)$ time. The stack can contain all $N$ indices for a non-decreasing array, so auxiliary space is $O(N)$.

## Alternatives and edge cases
- **Enumerate every start and end:** Extend each subarray until a smaller value appears. It is straightforward but takes $O(N^2)$ time for non-decreasing input.
- **Segment tree plus boundary searches:** Range minima can locate invalid boundaries, but the structure and logarithmic queries are unnecessary compared with a monotonic stack.
- **Strict versus non-strict pop:** Popping equal values is incorrect because the definition allows the first element to equal later elements.
- **Strictly increasing array:** No start is blocked, so all $N(N+1)/2$ subarrays are valid.
- **Strictly decreasing array:** Every start except the last is blocked immediately, leaving exactly $N$ valid subarrays.
- **Single element:** It contributes one valid subarray.
- **Duplicate plateau before a drop:** All equal starts remain on the stack and are resolved together by the later strictly smaller value.
