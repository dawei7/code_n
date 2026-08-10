## General

**Binary addition follows the same rule as decimal addition**

Addition starts with the least significant characters at the right ends of `a` and `b`. At each position, add the available input bits and the incoming carry. The output bit is the total modulo 2, and the next carry is the total divided by 2.

Because each input bit is 0 or 1 and the incoming carry is at most 1, the position total is 0, 1, 2, or 3. Its quotient by 2 is always a valid carry bit, and its remainder is always a valid output bit.

**Use independent pointers for unequal lengths**

`i` starts at the last character of `a`, and `j` starts at the last character of `b`. The strings may have different lengths, so each contribution is conditional. If a pointer is negative, that input contributes zero at the current higher position.

This is equivalent to conceptually padding the shorter string with leading zeros, but it avoids constructing a padded copy.

**One variable temporarily holds the column total**

At loop entry, `carry` is the incoming carry from the previously processed lower bit. The assignment adds the current bits into that variable. Then `carry, v = divmod(carry, 2)` replaces it with the outgoing quotient and stores the remainder in `v`.

For example, adding bit 1, bit 1, and carry 1 gives total 3. `divmod(3,2)` returns `(1,1)`: write output bit 1 and carry 1 leftward. Adding two ones with no carry gives total 2, which produces output 0 and carry 1.

Reusing the variable is safe because the old carry has already been included in the total before it is overwritten.

**Why the loop includes `or carry`**

The loop continues while either input has an unread bit or a carry remains. After both pointers move below zero, a carry of 1 represents a new most significant bit and must still be appended.

For `"11" + "1"`, the two ordinary positions produce low-to-high bits 0 and 0, with carry 1 left over. The extra iteration appends 1, giving reversed accumulation `["0","0","1"]` and final result `"100"`.

If no carry remains after the inputs are exhausted, the loop stops without introducing an unnecessary leading zero.

**Build low-to-high and reverse once**

Arithmetic naturally produces the least significant output bit first. `ans.append(str(v))` records bits in that production order. Appending to a Python list is amortized constant time and does not repeatedly copy the entire existing prefix.

At the end, `ans[::-1]` reverses the piece order and `"".join(...)` constructs the final most-significant-first string. The reverse slice creates another list of references, but both its time and space are linear and match the output scale.

**A complete trace**

For `a = "1010"` and `b = "1011"`:

- units: $0+1+0=1$, append 1, carry 0;
- twos: $1+1+0=2$, append 0, carry 1;
- fours: $0+0+1=1$, append 1, carry 0;
- eights: $1+1+0=2$, append 0, carry 1;
- final carry: append 1.

The produced order is `10101` from low to high in this symmetric example, and reversing yields the same displayed string `"10101"`.

**The positional invariant**

Before each iteration, `ans` contains the correct low-order result bits for every processed position, in reverse order, and `carry` is exactly the amount transferred into the next unprocessed position. Pointers identify the next available bits.

Adding the current contributions and applying quotient/remainder preserves this invariant. When no bits or carry remain, every binary position has been resolved. Reversing the collected bits therefore yields the exact sum.

**No full integer conversion**

Input lengths can reach 10,000 characters. Direct bit-string processing works regardless of machine integer width and stays faithful to the representation. Only one-character conversions are performed.

## Complexity detail

Let $L=\max(m,n)$. The loop performs at most $L+1$ iterations. Reversing the list and joining the result are also $O(L)$, so total time is $O(L)$.

The bit list, reversed list of references, and returned string are all $O(L)$. Peak construction space is therefore $O(\max(m,n))$, matching the manifest. Pointer and carry state are constant.

## Alternatives and edge cases

- **Preallocate an output array:** Reserve $L+1$ positions and fill from right to left, then omit an unused leading slot. It avoids a reverse slice but needs careful start indexing.
- **Repeated string concatenation:** It is syntactically shorter but can copy the growing prefix repeatedly and become quadratic under a conservative analysis.
- **Pad the shorter input:** It simplifies paired indexing but allocates an unnecessary leading-zero string.
- **Convert complete strings to integers:** Python permits it, but this bypasses the intended arbitrary-length bit addition and may be unavailable in fixed-width environments.
- **Different lengths:** A negative pointer contributes zero, so the longer prefix is processed correctly.
- **Final carry:** The loop condition emits it as a new leading 1.
- **Both inputs zero:** One iteration appends zero and returns `"0"`.
- **No leading zeros:** The source adds no leading zero; any final extra bit is a real carry.
- **Maximum length:** Work scales with characters, not numeric magnitude.
- **Input preservation:** Strings are immutable and never sliced or altered.
