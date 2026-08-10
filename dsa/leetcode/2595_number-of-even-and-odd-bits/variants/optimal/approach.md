## General

**Binary indices begin at the least-significant bit**

Bit index zero is the rightmost bit of the binary representation. Moving left increases the index by one. Therefore indices alternate:

$$
0\text{ even},\ 1\text{ odd},\ 2\text{ even},\ 3\text{ odd},\ldots
$$

The solution scans bits from right to left, exactly in this indexing order.

`ans[0]` stores the number of set bits at even indices, and `ans[1]` stores the number at odd indices.

**Read the current lowest bit**

The expression `n & 1` isolates the least-significant bit:

- if that bit is one, the result is one;
- if that bit is zero, the result is zero.

Adding this result to the appropriate counter increments it only for a set bit. No conditional branch is needed.

**Track index parity instead of the full index**

Variable `i` is not the absolute bit index. It is only its parity: zero for even and one for odd.

After processing each bit, `i ^= 1` toggles it. XOR with one changes zero to one and one to zero:

$$
0\mathbin{\char94}1=1,\qquad
1\mathbin{\char94}1=0.
$$

Since consecutive bit indices alternate parity, this is all the state required to choose the right counter.

**Move to the next bit**

`n >>= 1` shifts the integer right by one position. The processed lowest bit is discarded, and the original next bit becomes the new least-significant bit.

The local integer shrinks until it becomes zero. At that point all remaining higher positions are zero, so processing them would never change either count. The loop stops.

**A loop invariant**

At the beginning of an iteration:

- all original bits below the current position have been counted correctly;
- `n & 1` is the original bit at the current position;
- `i` is zero or one according to that position's parity.

The addition counts the current bit in the correct bucket. Toggling prepares the next position's parity, and shifting exposes the next bit. This preserves the invariant.

Initially no bit has been processed, the current position is zero, and `i=0`, so the invariant holds. When `n` reaches zero, every set bit has been counted exactly once.

**Trace `n = 50`**

$50$ has binary representation `110010`. Scanning from the right:

- index zero has bit zero, so even count stays zero;
- index one has bit one, so odd count becomes one;
- indices two and three have zero;
- index four has one, so even count becomes one;
- index five has one, so odd count becomes two.

The result is `[1,2]`.

For $n=2$, binary `10` has a zero at even index zero and a one at odd index one, producing `[0,1]`.

**Why leading zeros are irrelevant**

Binary representations conventionally omit infinitely many leading zero bits. Even if they were considered, none would increase a count. Ending when the shifted value reaches zero is therefore exact.

The input is positive, so at least one iteration occurs. The same code would return `[0,0]` for zero, though zero is outside the stated domain.

Zero bits inside the significant representation are different from omitted leading zeros. They add nothing to a counter, but the loop must still shift past them and toggle `i`. Skipping an internal zero without toggling would assign every higher set bit to the wrong parity. Processing one physical bit position per iteration preserves the original indices even when several consecutive positions contain zero.

**Local mutation does not alter caller data**

Each right shift rebinds local variable `n` to a new integer. Python integers are immutable, so no external object is mutated. Only the local working copy conceptually loses processed bits.

**Alternative fixed-mask intuition**

Another approach is to AND the original number with alternating masks such as binary `010101...` and `101010...`, then count ones in each result. The iterative scan avoids choosing a fixed integer width and directly mirrors the bit-index definition.

## Complexity detail

A positive integer $n$ has $\lfloor\log_2 n\rfloor+1$ significant bits. The loop processes one per iteration with constant work, giving $O(\log n)$ time.

The two-element answer list is required output and has constant size. Variables `i` and the shifting local `n` use $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Convert to a binary string:** Reverse `bin(n)` and inspect characters by index. This is clear but allocates $O(\log n)$ string space.
- **Alternating bit masks:** Mask even and odd positions separately and use a population-count operation, offering another constant-space bit solution.
- **Full integer index:** Incrementing an absolute index and taking modulo two works, but a one-bit parity toggle stores exactly what is needed.
- **Power of two at even index:** The result is `[1,0]`.
- **Power of two at odd index:** The result is `[0,1]`.
- **All significant bits set:** Counts differ by at most one because positions alternate parity.
- **Least-significant bit:** It always belongs to the even counter because its index is zero.
- **Leading zeros:** They are not processed and would contribute nothing anyway.
- **Positive-input guarantee:** At least one significant bit exists.
- **Local right shifts:** They do not mutate any caller-visible structure.
