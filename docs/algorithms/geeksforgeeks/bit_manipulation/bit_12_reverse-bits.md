# Reverse Bits

| | |
|---|---|
| **ID** | `bit_12` |
| **Category** | bit_manipulation |
| **Complexity (required)** | $O(1)$ Time, $O(1)$ Space |
| **Difficulty** | 3/10 |
| **Interview relevance** | 7/10 |
| **LeetCode Equivalent** | [Reverse Bits](https://leetcode.com/problems/reverse-bits/) |

## Problem statement

Reverse the bits of a given 32 bits unsigned integer.

**Input:** An unsigned 32-bit integer `n`.
**Output:** An integer representing the bit-reversed value.

## When to use it

- A fundamental bit-shuffling exercise that proves you know how to build binary numbers from scratch.

## Approach

**1. The Building Block Approach:**
Imagine taking a deck of cards and building a brand new, reversed stack.
You take the top card off the original deck, and place it at the bottom of the new deck.
You repeat this until the original deck is empty.
We can do exactly this with bits!

1. Create a `result` variable initialized to `0`.
2. Loop exactly 32 times (since the problem guarantees a 32-bit integer).
3. **Extract** the rightmost bit of `n` using `n & 1`.
4. **Place** that bit into our `result`! But where does it go? Since it's the rightmost bit of the original number, it needs to become the LEFTMOST bit of the reversed number!
   Actually, it's easier to just push it onto the right side of `result`, and then immediately *shift `result` to the left*! This naturally shoves the early bits further and further to the left as the loop progresses.
5. **Shift** `n` to the right (`n >> 1`) to expose its next bit.

*Critical Detail:* You MUST left-shift `result` BEFORE you add the extracted bit, otherwise your very first bit will be over-shifted by 1 position at the end of the 32 loops!

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for bit_12: Reverse Bits.

Reverse the bits of a 32-bit unsigned integer n.
"""


def solve(n):
    """Reverse the bits of the 32-bit unsigned integer n."""
    result = 0
    for i in range(32):
        # Take bit i of n, place it at bit (31 - i) of result.
        if n & (1 << i):
            result |= 1 << (31 - i)
    return result
```

</details>

## Walk-through

Let's do a 4-bit simulation to save space: `n = 13` (`1101`). We want `1011` (`11`). `result = 0`.

1. **Loop 1 (i=0):**
   - `result = 0 << 1 = 0` (`0000`)
   - `bit = 1101 & 1 = 1`
   - `result = 0000 | 1 = 0001` (`1`)
   - `n = 1101 >> 1 = 110` (`6`)
2. **Loop 2 (i=1):**
   - `result = 0001 << 1 = 0010` (`2`)
   - `bit = 110 & 1 = 0`
   - `result = 0010 | 0 = 0010` (`2`)
   - `n = 110 >> 1 = 11` (`3`)
3. **Loop 3 (i=2):**
   - `result = 0010 << 1 = 0100` (`4`)
   - `bit = 11 & 1 = 1`
   - `result = 0100 | 1 = 0101` (`5`)
   - `n = 11 >> 1 = 1` (`1`)
4. **Loop 4 (i=3):**
   - `result = 0101 << 1 = 1010` (`10`)
   - `bit = 1 & 1 = 1`
   - `result = 1010 | 1 = 1011` (`11`)
   - `n = 1 >> 1 = 0`

Result is `11` (`1011`). ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(1)$ | $O(1)$ |
| **Average** | $O(1)$ | $O(1)$ |
| **Worst** | $O(1)$ | $O(1)$ |

The loop runs exactly 32 times with constant $O(1)$ operations inside. Time complexity is strictly $O(1)$.
Space complexity is $O(1)$.

## Variants & optimizations

- **Divide and Conquer Block Swapping:** If you have to reverse bits millions of times per second, a loop of 32 shifts is actually too slow! You can reverse the entire 32-bit string in just 5 $O(1)$ operations!
  1. Swap adjacent 1-bit pairs: `n = ((n & 0xAAAAAAAA) >> 1) | ((n & 0x55555555) << 1)`
  2. Swap adjacent 2-bit blocks: `n = ((n & 0xCCCCCCCC) >> 2) | ((n & 0x33333333) << 2)`
  3. Swap adjacent 4-bit blocks: `n = ((n & 0xF0F0F0F0) >> 4) | ((n & 0x0F0F0F0F) << 4)`
  4. Swap adjacent 8-bit blocks: `n = ((n & 0xFF00FF00) >> 8) | ((n & 0x00FF00FF) << 8)`
  5. Swap adjacent 16-bit blocks: `n = (n >> 16) | (n << 16)`
  The bits are perfectly reversed without loops!

## Real-world applications

- **Digital Signal Processing (FFT):** The Cooley-Tukey Fast Fourier Transform algorithm requires array elements to be accessed in "Bit-Reversed Order". This physical hardware bit-reversal ensures that recursive signal splitting happens linearly in memory.

## Related algorithms in cOde(n)

- **[bit_07 - Swap Odd and Even Bits](bit_07_swap-odd-and-even-bits.md)** — The foundational prerequisite logic for the $O(1)$ block swapping variant.
- **[math_01 - Reverse Integer](../math/math_01_reverse-integer.md)** — Reversing Base-10 digits using `% 10` and `/ 10`, which perfectly mirrors extracting Base-2 bits using `& 1` and `>> 1`!

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
