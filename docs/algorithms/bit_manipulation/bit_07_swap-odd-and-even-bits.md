# Swap Odd and Even Bits

| | |
|---|---|
| **ID** | `bit_07` |
| **Category** | bit_manipulation |
| **Complexity (required)** | $O(1)$ Time, $O(1)$ Space |
| **Difficulty** | 4/10 |
| **Interview relevance** | 6/10 |
| **GeeksForGeeks Equivalent** | [Swap all odd and even bits](https://www.geeksforgeeks.org/swap-all-odd-and-even-bits/) |

## Problem statement

Given an unsigned integer `N`, swap all odd bits with even bits.
For example, if the given number is `23` (`00010111`), it should be converted to `43` (`00101011`). Every even position bit is swapped with the adjacent bit on the right (odd position), and every odd position bit is swapped with the adjacent bit on the left.

**Input:** An unsigned 32-bit integer `N`.
**Output:** An integer representing the swapped bits.

## When to use it

- To demonstrate proficiency with absolute **Bit Masking**.
- When you need to cleanly isolate specific repeating patterns of bits across an entire integer simultaneously.

## Approach

**1. The Logic of Swapping:**
Instead of trying to somehow select a pair of bits, swap them, and move to the next pair (which would require a loop), we can do this instantly!
If we want to swap all Even bits (0, 2, 4...) with all Odd bits (1, 3, 5...), we can break it down into two independent steps:
1. Isolate all the Even bits. Since we want them to become Odd bits, we simply right-shift them all by 1 position! (`>> 1`)
2. Isolate all the Odd bits. Since we want them to become Even bits, we simply left-shift them all by 1 position! (`<< 1`)
Finally, we just recombine the two halves using Bitwise OR (`|`).

**2. Creating the Masks:**
How do we isolate ONLY the Even bits? We need a binary number that has `1`s on every even position and `0`s everywhere else:
`1010 1010 1010 1010 1010 1010 1010 1010`
In hexadecimal, `1010` is `A`. So the 32-bit mask is `0xAAAAAAAA`.

How do we isolate ONLY the Odd bits? We need a binary number that has `1`s on every odd position:
`0101 0101 0101 0101 0101 0101 0101 0101`
In hexadecimal, `0101` is `5`. So the 32-bit mask is `0x55555555`.

**3. The Execution:**
- Extract even bits: `even_bits = n & 0xAAAAAAAA`.
- Extract odd bits: `odd_bits = n & 0x55555555`.
- Shift even bits down to odd spots: `even_bits >>= 1`.
- Shift odd bits up to even spots: `odd_bits <<= 1`.
- Recombine: `return even_bits | odd_bits`.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for bit_07: Swap Odd and Even Bits.

Swap the odd and even bits of n. Bit 0 (LSB) goes
"""


def solve(n):
    """Swap the odd and even bits of n. Bit 0 (LSB) goes to bit 1, etc."""
    even_mask = 0x55555555
    odd_mask = 0xAAAAAAAA
    even_bits = (n & even_mask) >> 1
    odd_bits = (n & odd_mask) << 1
    return even_bits | odd_bits
```

</details>

## Walk-through

`n = 23` (`00010111`).
(We will only show the lowest 8 bits for clarity. `A` mask is `10101010`, `5` mask is `01010101`).

1. **Extract Even Bits:**
   - `00010111 & 10101010` = `00000010`
2. **Extract Odd Bits:**
   - `00010111 & 01010101` = `00010101`
3. **Shift Even Bits:**
   - `00000010 >> 1` = `00000001`
4. **Shift Odd Bits:**
   - `00010101 << 1` = `00101010`
5. **Recombine (OR):**
   - `00000001 | 00101010` = `00101011` (`43`).

Result is `43`. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(1)$ | $O(1)$ |
| **Average** | $O(1)$ | $O(1)$ |
| **Worst** | $O(1)$ | $O(1)$ |

The algorithm performs exactly two ANDs, two Shifts, and one OR operation. It executes in constant $O(1)$ CPU cycles regardless of the size or value of N.
Space complexity is strictly $O(1)$.

## Variants & optimizations

- **64-bit Integers:** If the input is a 64-bit integer instead of a 32-bit integer, the masks simply double in length. `0xAAAAAAAAAAAAAAAA` and `0x5555555555555555`.
- **Endianness/Architecture:** In Python, integers have arbitrary precision. If you do `(n & 0xAAAAAAAA) >> 1`, Python handles the shifting safely. However, in C++/Java, if the integer is signed and negative, a logical right shift `>>>` MUST be used instead of an arithmetic right shift `>>`, otherwise the sign bit will duplicate itself and ruin the top of the integer!

## Real-world applications

- **Network Endianness Swapping:** Swapping 16-bit or 32-bit halves of integers when transmitting data across a network (Network Byte Order vs Host Byte Order) uses this exact identical masking and shifting strategy, just with chunkier masks like `0xFF00FF00`!

## Related algorithms in cOde(n)

- **[bit_12 - Reverse Bits](bit_12_reverse-bits.md)** — If you want to reverse the ENTIRE 32-bit string, you apply this exact swapping logic recursively! First you swap adjacent 1-bit pairs (like this algorithm), then you swap adjacent 2-bit chunks, then 4-bit chunks...

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
