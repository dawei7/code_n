## General

An integer has alternating bits when every pair of adjacent digits in its binary representation differs. Valid patterns look like `10101` or `1010`; invalid patterns contain `00` or `11` somewhere.

The exact solution examines the binary representation directly with bit operations. It repeatedly reads the least significant bit, compares it with the bit read on the previous iteration, and shifts the integer right to expose the next bit.

**Reading one bit**

The expression

`curr = n & 1`

uses bitwise AND with `1`. Since `1` has only its least significant bit set, every higher bit is cleared. The result is:

- `0` when the current least significant bit of `n` is zero;
- `1` when it is one.

No conversion to a binary string is necessary.

After the comparison, `n >>= 1` shifts all bits one place to the right. The bit just inspected is discarded, and its left neighbor in the original representation becomes the new least significant bit.

For example, starting from decimal `10`:

- binary `1010` yields current bit `0`;
- right shift produces binary `101`, whose current bit is `1`;
- later shifts expose `0` and then `1`.

The inspection order is right to left, but adjacency is symmetric. If every pair differs when read from the least significant side, every pair also differs in the usual left-to-right representation.

**The role of `prev`**

`prev` stores the bit from the preceding loop iteration—that is, the original bit immediately to the right of `curr`.

The invariant at the beginning of each iteration is:

> Every adjacent pair among the bits already removed from `n` alternates, and `prev` is the most recently removed bit.

When `prev == curr`, two adjacent original bits are equal. The alternating requirement is violated, so the method returns `False` immediately. No later bits can repair an already invalid pair.

When they differ, the newly examined pair is valid. Assigning `prev = curr` extends the verified suffix by one bit, and the right shift prepares the next adjacent comparison.

**Why `prev` starts at `-1`**

Before the first bit is read, there is no previous bit to compare with. The code uses `-1` as a sentinel because a real binary digit can only be zero or one.

Therefore, the first comparison can never report equality. The first real bit is accepted and stored in `prev`. From the second iteration onward, both `prev` and `curr` are genuine adjacent bits.

An explicit “first iteration” branch would also work, but the sentinel keeps the loop uniform.

**Loop termination**

The input is positive. Each right shift divides it by two while discarding the remainder, so eventually `n` becomes zero. At that point every significant bit has been examined.

Leading zeroes are not part of an integer's standard binary representation and must not be checked. Stopping when `n == 0` correctly ignores the infinitely many conceptual zero bits to the left. Otherwise, every positive number would eventually appear to contain adjacent zeroes.

If the loop finishes without finding equal adjacent bits, every adjacent pair in the complete significant representation differs, and the method returns `True`.

**A valid trace**

For `n = 5`, the binary representation is `101`.

- First iteration: `curr = 1`. It differs from sentinel `-1`. Set `prev = 1` and shift to binary `10`.
- Second iteration: `curr = 0`. It differs from `prev = 1`. Set `prev = 0` and shift to binary `1`.
- Third iteration: `curr = 1`. It differs from `prev = 0`. Shift to zero.
- The loop ends and returns `True`.

**An invalid trace**

For `n = 11`, binary is `1011`.

- The least significant bit is `1` and becomes `prev`.
- After one shift, the next bit is also `1`.
- `prev == curr`, so the method returns `False` immediately.

Although the duplicate pair appears at the right end, the same early exit works for a duplicate pair anywhere: shifts eventually bring that pair into consecutive iterations.

**Why the method is correct**

If the algorithm returns `False`, it has observed two consecutive iterations with equal bits. Consecutive iterations read adjacent positions in the original integer, so an invalid adjacent pair truly exists.

If it returns `True`, each significant bit after the first was compared with its immediate right neighbor and found different. Those comparisons cover every adjacent pair exactly once. Hence the entire representation alternates.

Together, these directions prove that the returned Boolean is true exactly for numbers with alternating bits.

## Complexity detail

Let `w` be the number of significant bits in `n`:

$$
w=\lfloor\log_2 n\rfloor+1.
$$

Each loop removes one bit and performs constant work. The running time is

$$
O(w)=O(\log n).
$$

Under the source's fixed 32-bit upper bound, `w <= 31`, so the work is also bounded by a small constant. Expressing it as `O(\log n)` shows how the method scales for arbitrary-size positive integers.

The method stores only `prev` and `curr` and mutates the local integer `n`. Its auxiliary space usage is

$$
O(1).
$$

It does not allocate a binary string or recursion stack.

## Alternatives and edge cases

- **Convert to a binary string:** `bin(n)` followed by adjacent-character comparisons is straightforward, but it uses `O(\log n)` extra string space.

- **XOR pattern observation:** If `n` alternates, then `x = n ^ (n >> 1)` consists entirely of ones. Such a number satisfies `x & (x + 1) == 0`. This gives a compact constant-number-of-operations test for fixed-width integers but is less immediately intuitive.

- **Single-bit numbers:** `1` has no adjacent pair, so the property is vacuously true. The loop processes its only bit and returns `True`.

- **Most significant bit:** The loop checks it against its right neighbor but does not compare it with a leading zero, because leading zeroes are not part of the representation.

- **Adjacent zeroes:** The algorithm detects `00` just as it detects `11`; both make `prev == curr`.

- **Positive-input guarantee:** The loop and complexity discussion assume `n >= 1`. If zero were allowed, its usual representation `0` would also contain no adjacent pair and the current loop would return `True` without iteration.

- **Right shift versus division:** For positive integers, `n >>= 1` is equivalent to integer division by two and directly expresses that one binary digit is discarded.

- **Sentinel selection:** `-1` is safe only because genuine extracted bits are restricted to zero and one.

- **Mutating `n`:** Only the local parameter value changes. The caller's integer is immutable and unaffected.

- **Early exit:** Finding one equal pair proves failure, so continuing to scan would add work without changing the result.
