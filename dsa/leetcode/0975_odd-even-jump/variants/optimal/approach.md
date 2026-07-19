## General
**Separate jump selection from reachability:** Once $H_i$ and $L_i$ are known, no choices remain. Define `odd[i]` to mean that index `i` reaches the end when its next jump is odd, and define `even[i]` analogously. Then `odd[i] = even[H_i]` when $H_i$ exists, while `even[i] = odd[L_i]` when $L_i$ exists. Both states are true at the final index.

**Build next-higher destinations:** Sort indices by `(arr[i], i)`. Values then appear in ascending order and equal values in ascending index order. Scan this order with a stack of unresolved indices. Whenever the current index is larger than the stack top, it is the smallest legal forward index for that top among the smallest eligible values, so pop and record it. Repeating the pop resolves every index for which the current item is the required $H_i$.

**Reverse the value order for next-lower destinations:** Apply the identical stack procedure after sorting by `(-arr[i], i)`. Descending values make the first resolvable value the largest value not exceeding the source, and the ascending index tie key again selects the smallest legal destination. This constructs every $L_i$.

**Evaluate from right to left:** All jumps move to larger indices, so when processing `i` in reverse, the destination states have already been computed. The two recurrences therefore determine both states without recursion. Counting true entries in `odd` gives precisely the good starting indices because the first jump is odd.

## Complexity detail
Sorting two index lists costs $O(N\log N)$ time. Each index is pushed and popped at most once in each monotonic-stack pass, and the dynamic program is linear. The destination arrays, stacks, sorted indices, and two state arrays use $O(N)$ space.

## Alternatives and edge cases
- **Ordered map while scanning right to left:** Ceiling and floor queries can find $H_i$ and $L_i$ in $O(\log N)$ per index, also giving $O(N\log N)$ time, but Python has no built-in balanced search tree.
- **Scan every suffix:** Directly searching all later indices implements the tie rules transparently but requires $O(N^2)$ time.
- **Final index:** It is good without making any jump, which supplies both dynamic-programming base states.
- **Duplicate values:** Sorting equal values by ascending index is essential; a different tie order can select a later duplicate illegally.
- **Missing destination:** If the required odd or even destination does not exist, that state is false even if a jump of the opposite parity would have been possible.
