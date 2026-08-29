## General

**Count set bits without visiting zero positions**

The straightforward method examines every one of the 32 bit positions. The
stored optimal method uses Brian Kernighan's observation to perform one loop
iteration per set bit instead. It repeatedly changes the least significant
remaining 1-bit to 0 and increments the answer.

This works especially well for sparse numbers. A power of two such as 128 has
only one set bit, so the loop executes once even though that bit may be far from
the least significant position.

**Understand what subtracting one does in binary**

Consider a positive integer `n` and locate its least significant 1-bit. All
positions to its right must be zeros. Subtracting one changes that chosen 1 to
0 and changes every trailing zero on its right to 1. Bits to its left remain
unchanged.

For example:

`n     = 1011000`

`n - 1 = 1010111`

The rightmost 1 in `n` is the fourth bit from the right. Subtraction clears it
and fills the three lower zero positions with ones.

**Use AND to remove exactly that bit**

The update `n &= n - 1` compares those two patterns position by position. Bits
to the left of the rightmost 1 are unchanged in `n - 1`, so any set bits there
remain set after AND. At the rightmost 1 position, `n - 1` contains zero, so
AND clears it. In every lower position, original `n` contains zero, so the new
ones introduced by subtraction are cleared by AND.

Consequently, the result is the original number with exactly its least
significant set bit removed and every other set bit preserved. One update can
never remove two set bits and can never create a set bit.

**Make the counter match the transformation**

Each loop iteration performs one such removal and increments `ans` once. If the
input initially contains $p$ set bits, after one iteration it contains $p-1$,
after two it contains $p-2$, and after $p$ iterations it becomes zero.

The loop condition `while n` stops precisely at that point. Since the counter
also increased $p$ times, `ans` equals the original Hamming weight.

**Trace the first example**

For `n = 11`, binary representation is `1011`.

- `1011 & 1010` gives `1010`; count becomes one.
- `1010 & 1001` gives `1000`; count becomes two.
- `1000 & 0111` gives `0000`; count becomes three.

The loop ends and returns 3. Notice that the zero bit between the set positions
never receives a separate iteration.

**Why the method is exact**

At the beginning of each iteration, `ans` equals the number of set bits already
removed, while current `n` contains exactly the original set bits not yet
removed. The AND update removes exactly one of them, and the increment records
that removal, so this relationship remains true.

At termination, current `n` contains no set bits. Therefore all original set
bits have been removed and counted exactly once. Nothing else can contribute to
`ans`, which proves the returned count is neither too small nor too large.

**Why positivity matters in Python**

The Reference restricts `n` to a positive signed 32-bit value. Python represents
negative integers with an effectively unbounded sign extension for bitwise
operations. Applying this loop to a negative Python integer without first
masking it to a fixed width would not model a finite 32-bit pattern and might
not terminate as intended. The positive-domain guarantee makes each update
strictly reduce `n` toward zero.

Although zero is outside the stated positive range, the method would return
zero for it because the loop would execute no iterations.

**Repeated-call follow-up**

For many calls, one can precompute the Hamming weight of every byte value from
0 through 255. A 32-bit input is split into four bytes, and four table lookups
are summed. The table has fixed size 256 and avoids a data-dependent number of
bit-clearing iterations. Modern runtimes may also expose a hardware-backed
population-count operation such as Python's `int.bit_count()`.

The current method remains attractive because it needs no table initialization
and is tiny, exact, and particularly fast on inputs with few set bits.

## Complexity detail

Let $p$ be the number of set bits. The loop executes exactly $p$ times, so a
bit-width-sensitive bound is $O(p)$. Under the fixed signed 32-bit contract,
$p \le 31$, making the manifest time bound $O(1)$. If integer width were allowed
to grow, calling the method constant time would no longer be appropriate.

Only `ans` and the evolving integer `n` are stored. Their logical widths are
bounded by 32 bits, so auxiliary space is $O(1)$.

## Alternatives and edge cases

- **Check every bit:** AND with a moving mask for 32 iterations; simpler fixed work but ignores sparsity.
- **Parallel mask-and-add:** Sum neighboring bit counts in five fixed stages, as the competitive variant does.
- **Byte lookup table:** Four fixed lookups per call make a useful repeated-call optimization with a 256-entry cache.
- **Built-in population count:** `n.bit_count()` is concise and usually highly optimized, though it hides the interview technique.
- **Binary-string count:** Correct for positive inputs but allocates a textual representation.
- **Power of two:** Exactly one iteration because `n & (n - 1)` becomes zero immediately.
- **All low 31 bits set:** Executes 31 iterations, still constant under the fixed-width contract.
- **Zero:** Returns zero naturally even though the Reference says positive.
- **Negative Python integer:** Mask to the intended width first; otherwise the finite-word reasoning does not apply.
- **Variable-width integers:** Report complexity in the word length or popcount instead of calling it unconditional $O(1)$.
