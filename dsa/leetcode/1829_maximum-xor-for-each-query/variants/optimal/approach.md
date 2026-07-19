## General
**Identify the best result bit by bit**

Let $x$ be the XOR of every value currently in the array. Since each input value uses at most `maximumBit` bits, $x$ also has no set bit above that width. To maximize `x XOR k`, every permitted result bit should be 1, producing the mask

$$
M = 2^{\texttt{maximumBit}} - 1.
$$

At each bit where $x$ is 0, choose 1 in $k$; where $x$ is 1, choose 0. Thus the unique maximizing value is the complement of $x$ within the permitted width, computed as `x ^ M`.

**Reuse the XOR after each removal**

Compute the XOR of the complete array once. Append its masked complement for the first query. The problem then removes the last current element, so process `nums` from right to left. Because `value ^ value = 0`, update the aggregate with `current_xor ^= value`; this cancels exactly the removed element and leaves the XOR of the next shorter prefix.

The answers are appended while removals proceed from the original suffix toward the beginning, which is already the required query order. There is no need to reverse the result.

**Why every recorded value is optimal**

For any current prefix, each allowed bit of $k$ can be selected independently. Choosing the opposite of the corresponding aggregate-XOR bit makes that result bit 1, the largest possible choice, so the complete result becomes $M$ and no allowed $k$ can produce a larger value. After recording it, the cancellation update exactly reconstructs the next prefix XOR. Induction over the removals therefore establishes that every output entry is the optimal $k$ for its query.

## Complexity detail
The initial XOR scan and the reverse removal scan each visit the $n$ values once, giving $O(n)$ time. The returned answer contains $n$ integers and therefore uses $O(n)$ space; excluding that required output, the mask and current XOR use $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Recompute every remaining prefix XOR:** This is correct but revisits the same elements after each removal, taking $O(n^2)$ time.
- **Test every possible `k`:** Exhaustive search uses $O(n2^{\texttt{maximumBit}})$ candidate checks even though the maximizing bits follow directly from the mask.
- **Maintain explicit prefix XORs:** A prefix array also answers each stage in $O(1)$ after $O(n)$ preprocessing, but it uses extra storage that cancellation does not need.
- **Single element:** Produce its masked complement, then finish after removing it.
- **Zero aggregate XOR:** The answer is the full mask $M$.
- **Aggregate equal to the mask:** The maximizing answer is zero.
- **Repeated values:** Equal elements may cancel in pairs, but each occurrence is still removed in its own query.
- **Maximum bit width:** With `maximumBit = 20`, the mask is $2^{20}-1$ and remains within the allowed integer range.
- **Ascending order:** The input guarantee is preserved, but the XOR reasoning does not depend on numerical ordering; only removal from the last position matters.
