## General
**Store XOR prefixes**

Build `prefix` with one extra leading zero, where `prefix[k]` is the XOR of `arr[0]` through `arr[k - 1]`. The update `prefix.append(prefix[-1] ^ value)` constructs all $n+1$ prefix values in one pass.

For a query `[left, right]`, `prefix[right + 1]` contains the desired subarray together with the elements before `left`. XORing it with `prefix[left]` cancels that common earlier prefix because $x\mathbin{\mathtt{XOR}}x=0$ and $0\mathbin{\mathtt{XOR}}y=y$. Thus `prefix[right + 1] ^ prefix[left]` contains exactly the inclusive queried range.

Answering each query with this identity preserves query order and takes constant time after preprocessing. It also handles `left = 0` through the stored zero prefix and a one-element query because every other contribution cancels.

## Complexity detail
Constructing the prefix array takes $O(n)$ time, and answering all $q$ queries takes $O(q)$ time, for $O(n+q)$ total. The prefix array uses $O(n)$ space and the required answer uses $O(q)$ space, giving $O(n+q)$ including output.

## Alternatives and edge cases
- **Direct range scan:** XORing each queried subarray independently uses constant auxiliary space but can take $O(nq)$ time when many ranges are long.
- **Segment tree:** Range XOR queries can be answered in $O(\log n)$ after $O(n)$ construction and support updates, but the array is immutable here, so prefix XOR is simpler and faster.
- **Single-element range:** The answer is that element because the two surrounding prefixes cancel.
- **Full-array range:** Use `prefix[n] ^ prefix[0]`, which is the XOR of the whole array.
- **Repeated or overlapping queries:** Each constant-time prefix lookup is independent; no query mutates shared state.
- **XOR cancellation:** Equal values may cancel within a range, so zero is a valid answer even though every input value is positive.
