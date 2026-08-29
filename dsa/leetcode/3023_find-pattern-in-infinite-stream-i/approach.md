## General

**Represent the pattern as bits, not as a string.** The stream and `pattern` contain only 0 and 1. The exact solution packs those bits into Python integers and maintains a rolling encoding of the most recent $M$ stream values. When that encoding equals the packed pattern, the current window is a match.

Instead of one $M$-bit integer, the source splits the representation into two halves. Let

$$
h=\left\lfloor\frac{M}{2}\right\rfloor
\quad\text{and}\quad
r=M-h.
$$

The first $h$ pattern bits are packed into `a`, and the remaining $r$ bits into `b`. Repeatedly executing `value = value << 1 | bit` appends a bit on the right: the old bits shift toward more significant positions and the new bit occupies the least significant position. Consequently equality of packed integers is equality of the corresponding fixed-length bit sequences, including their order.

**Masks keep only each half's allowed width.** `mask1 = (1 << half) - 1` has its lowest $h$ bits set. `mask2 = (1 << (m - half)) - 1` has its lowest $r$ bits set. Applying `& mask1` or `& mask2` discards older bits that lie beyond the respective half.

For example, a width-three mask is binary `111`. If a rolling value temporarily becomes `1011`, masking leaves `011`, exactly the newest three bits.

**Maintain the newest half in `y`.** For every call to `stream.next()`, the source first appends the new bit to `y`:

`y = y << 1 | v`.

At this instant `y` may contain $r+1$ bits. The bit that just overflowed its $r$-bit capacity is the oldest bit of this newest half. It belongs at the right edge of the older half, so the code extracts it with

`v = y >> (m - half) & 1`.

It then applies `y &= mask2`, leaving precisely the newest $r$ stream bits.

**Transfer the overflow into `x`.** The extracted bit is appended to `x` by `x = x << 1 | v`, and `x &= mask1` keeps only the newest $h$ transferred bits. Once at least $M$ stream values have been read, the pair $(x,y)$ therefore represents exactly the last $M$ values: `x` holds the older first $h$ positions of the window, and `y` holds the newer final $r$ positions.

This is effectively a two-register shift register:

$$
\text{old bits discarded}
\leftarrow x \leftarrow y \leftarrow \text{new stream bit}.
$$

The split keeps both integers to at most about half the pattern length. Under the problem's $M\le100$ constraint, each is at most 50 bits, comfortably handled by ordinary Python integer operations.

**Do not compare before the window is full.** The loop counter begins at 1 and counts values consumed from the stream. During the first $M-1$ iterations, `x` and `y` contain a partially filled window with implicit leading zeros. Comparing then could report a false match for a pattern beginning with zeros. The condition `i >= m` prevents that.

Once the window is full, `a == x and b == y` is true exactly when both halves match. Together they cover all $M$ positions, so the whole pattern matches. If the window ends at consumed position $i-1$ in zero-based terms, its start is

$$
i-M.
$$

That is the returned value `i - m`.

**A miniature trace.** Suppose $M=5$, so $h=2$ and $r=3$. After enough input, imagine the last five bits are `1,0,1,1,0`. Register `x` encodes `10` and `y` encodes `110`. When the next bit 1 arrives, `y` temporarily represents `1101`. Its overflow is the leading 1; masking leaves `101`. Appending the overflow to old `x=10` gives `101`, and the two-bit mask leaves `01`. The new five-bit window is therefore `0,1,1,0,1`, split as `01` and `101`, exactly as required.

**Why the first equality is the required answer.** The stream is consumed from left to right and the method compares every length-$M$ window in increasing start-index order: start 0 after $M$ reads, start 1 after $M+1$ reads, and so forth. It returns immediately on equality. Thus no earlier matching index can have been skipped.

The problem guarantees that a match occurs within its stated bound, so the unbounded `count(1)` loop is safe under the contract. Without that guarantee, a streaming API would need a limit or a “not found” convention.

## Complexity detail

Let $M$ be the pattern length and let $S$ be the number of stream values consumed through the end of the first match. Packing the pattern takes $O(M)$ time. Each stream value performs a fixed number of shifts, masks, comparisons, and assignments, so under the bounded-width machine-operation model the search takes $O(S)$ time. Total time is $O(M+S)$.

The source stores four packed integers plus counters and masks. Because $M\le100$, those integers have bounded size, so auxiliary space is $O(1)$ under the actual problem constraints. In a bit-complexity model with unbounded $M$, the registers collectively store $M$ bits and integer operations act on $O(M)$-bit values; space would be $O(M)$ and per-step cost would no longer be strictly constant.

The local manifest describes a KMP prefix-function solution with $O(M)$ space. That is not the protected source. This implementation uses exact rolling bit packing—there is no prefix table and no hash collision because the registers encode the bits themselves.

## Alternatives and edge cases

- **KMP over the stream:** A prefix-function matcher also finds the first occurrence in $O(M+S)$ time and $O(M)$ space. It is valuable for arbitrary alphabets and unbounded patterns, but it is not the algorithm implemented here.
- **Store a deque of the last $M$ bits:** Comparing the whole deque with the pattern at each step can cost $O(MS)$ time unless another matching mechanism is added.
- **Single packed integer:** One can keep all $M$ bits in one register with an $M$-bit mask. The two-half version keeps each register within roughly 50 bits under the stated limit and makes the shift across their boundary explicit.
- **Rolling hash:** Hashing would use compact state but could collide. This source's bit representation is exact for binary data.
- **Pattern length one:** Then `half` is zero and `mask1` is zero. `x` always remains zero, while `y` stores the single newest bit. The comparison still works.
- **Pattern begins with zeros:** Waiting until `i >= m` is essential; otherwise a partially filled register's implicit leading zeros might appear to match too early.
- **All-zero pattern:** Once a full window of zeros arrives, both registers equal zero and the correct start is returned. Partial windows are still excluded.
- **Overlapping matches:** The rolling window advances by one element, so overlaps are examined. Returning the first match means later overlaps do not matter.
- **No rewind:** The method consumes the stream only forward and keeps enough rolling state to avoid requesting an old value again.
- **Guaranteed eventual match:** The infinite loop relies on the reference contract. If used outside that contract, it might never terminate.
