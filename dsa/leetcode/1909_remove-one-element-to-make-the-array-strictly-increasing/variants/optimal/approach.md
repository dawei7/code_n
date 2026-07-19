## General
**Scan while representing at most one removal**

Maintain `previous`, the last value retained by the conceptual result, and a Boolean recording whether a removal has already been used. When `current > previous`, retaining `current` preserves strict order, so advance normally.

The interesting case is `current <= previous`. One of these two neighboring values must be removed. If an earlier conflict already consumed the single removal, the array cannot be repaired.

**Choose which side of the conflict to discard**

Removing `previous` is safe when the conflict occurs at index `1`, or when `current > nums[index - 2]`; in that case, let `current` become the retained value. Otherwise `current` cannot follow the value two positions back, so discard `current` conceptually by leaving `previous` unchanged.

This local decision preserves the smallest valid retained suffix boundary whenever possible. After the first conflict it exactly represents a strictly increasing prefix obtainable with one removal. A second conflict proves that no single deletion works. If the scan finishes, the represented sequence is valid; an already increasing input is also valid because an endpoint can be removed.

## Complexity detail
The scan visits each of the $N$ elements once and performs constant work per element, giving $O(N)$ time. It stores only the retained predecessor, a Boolean, and loop indices, so auxiliary space is $O(1)$.

## Alternatives and edge cases
- **Try every removal:** Constructing or scanning all $N$ candidate arrays is straightforward but takes $O(N^2)$ time.
- **Prefix and suffix validity arrays:** Precomputing increasing prefixes and suffixes gives an $O(N)$ test for every bridge, but uses $O(N)$ extra space.
- **Already strictly increasing:** Removing either endpoint preserves strict increase, so the answer is `True`.
- **Equal adjacent values:** Equality violates strict increase and must be treated exactly like a decrease.
- **Remove the left endpoint:** Inputs such as `[5,1,2,3]` require discarding the first value.
- **Remove the right endpoint:** Inputs such as `[1,2,3,1]` require discarding the final value.
