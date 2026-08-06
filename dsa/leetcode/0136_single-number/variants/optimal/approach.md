## General
**XOR records parity independently at every bit position**

Fold the array into `answer` with XOR. The operation is associative and commutative, so values may be regrouped conceptually without changing the result. Each pair cancels because $x \oplus x = 0$, and zero is the identity.

After any processed prefix, `answer` is the XOR of exactly those bit patterns whose occurrence parity in that prefix is odd. Reading another value toggles its bits; reading its equal partner toggles the same bits back off. Once the full array has been processed, every duplicated value has disappeared and the promised singleton is the only remaining bit pattern. This reasoning also covers negative integers because two equal signed values have identical representations and therefore cancel.

## Complexity detail
The fold performs one XOR for each of the $n$ input values, giving $O(n)$ time. `answer` is the only algorithmic state, so auxiliary space is $O(1)$.

## Alternatives and edge cases
- **Frequency map:** also takes $O(n)$ time but violates the constant-extra-space requirement.
- **Sort and compare adjacent pairs:** uses $O(n \log n)$ time and may mutate the input.
- **Arithmetic set formula:** needs extra storage and can overflow in fixed-width languages.
- A one-element array returns that element directly through the same fold.
- Negative values require no special handling because equal bit patterns still cancel.
- The cancellation proof relies on every nonsingleton appearing exactly twice; other repetition counts require a different bit-counting method.
