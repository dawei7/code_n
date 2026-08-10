## General

**Read the bits in their existing most-significant-first order**

The linked list places the most significant bit at its head. While traversing from head to tail, the algorithm receives the binary digits in exactly the order used when writing the number.

Suppose the bits processed so far represent value $A$. Appending a new bit $b$ to the right of a binary numeral shifts every existing place value one position left, multiplying $A$ by two, and adds $b$ in the new units place:

$$
A_{\text{new}}=2A+b.
$$

The exact expression `ans = ans << 1 | head.val` implements this recurrence. Left shift by one multiplies a nonnegative integer by two. Since `head.val` is zero or one and the shifted value's lowest bit is zero, bitwise OR inserts the new bit exactly like addition.

**Trace the list `1 -> 0 -> 1`**

`ans` begins at zero. Reading one gives `0 << 1 | 1 = 1`. Reading zero gives `1 << 1 | 0 = 2`, whose binary form is `10`. Reading the final one gives `2 << 1 | 1 = 5`, binary `101`. The returned decimal integer is five.

For a one-node list containing zero, the one iteration leaves `ans` at zero.

**A prefix invariant proves correctness**

Before each iteration, `ans` equals the decimal value of all nodes before `head`. The shift makes room for the current bit, and OR places that bit in the new least-significant position, so the invariant holds for the longer processed prefix.

The list is finite and nonempty. Reassigning `head = head.next` advances exactly once per iteration until `None`. At termination, the processed prefix is the entire list, so `ans` is its binary value.

The method does not alter node values or links. It moves only its local reference `head`, leaving the caller's list intact.

**Connect the recurrence to positional notation**

For processed bits $b_0,b_1,\ldots,b_r$, their value is

$$
b_0 2^r+b_1 2^{r-1}+\cdots+b_r.
$$

Appending bit $b_{r+1}$ moves every existing bit one power higher:

$$
2\left(b_0 2^r+b_1 2^{r-1}+\cdots+b_r\right)+b_{r+1}.
$$

That is exactly the shift-and-OR update. The recurrence is therefore not merely accumulating bits in an arbitrary way; after every node it equals the ordinary base-two positional interpretation of the prefix.

Consider a longer list `1 -> 1 -> 0 -> 1`. Accumulator values become one, three, six, and thirteen. Written in binary, those prefixes are `1`, `11`, `110`, and `1101`. This makes the invariant visible at every step.

Leading zeroes also fit the recurrence. Starting with several zero nodes keeps the accumulator zero until the first one, after which later shifts place that one at its correct power. The numerical value ignores leading zeroes exactly as ordinary binary notation does.

**Why no power table or reversal is needed**

One could first determine the list length and assign explicit powers of two to nodes, but the streaming recurrence incorporates place value as digits arrive. It needs one pass and constant working storage.

The maximum list length is thirty, so the result fits in a common 32-bit signed positive range, though Python would support larger values automatically.

**Bitwise precedence in the exact line**

Python parses shifting before bitwise OR, so `ans << 1 | head.val` means `(ans << 1) | head.val`. Parentheses could improve readability but do not change execution.

Because node values are restricted to one bit, OR and addition are equivalent after the shift. If arbitrary larger values were allowed, OR would no longer represent appending a single binary digit; the contract is essential.

## Complexity detail

Let $n$ be the number of nodes. The loop visits each node once and performs constant-time work in the conventional bounded-integer model, so time is $O(n)$.

Only the accumulator and current node reference are stored, giving $O(1)$ auxiliary space. No recursion stack, bit list, or converted string is created.

At the bit-operation level, accumulator size grows with the prefix length, but the package bound of thirty bits supports the standard constant-word analysis.

## Alternatives and edge cases

- **Arithmetic recurrence:** `ans = ans * 2 + head.val` is mathematically identical and may be clearer to readers unfamiliar with bit operations.
- **Convert to a string:** Collect bits, join them, and parse base two. It works but uses $O(n)$ extra space.
- **Explicit powers of two:** Count length first, then sum each bit times its power. This requires two passes or stored length and is less direct.
- **Single zero node:** Returns zero.
- **Leading zeroes:** They leave the accumulator unchanged initially and do not affect the represented value.
- **All ones:** Each iteration doubles and adds one, producing $2^n-1$.
- **Nonempty guarantee:** The method would also return zero for `None`, but empty input is outside the contract.
- **Binary-value guarantee:** OR is valid because every node is exactly zero or one.
- **Input immutability:** Advancing the local pointer does not detach or modify nodes.
- **Operator precedence:** The shift occurs before OR in Python; explicit parentheses can document that intent.
