## General
**Group source numbers by decimal width**

There are 9 one-digit numbers contributing 9 digits, 90 two-digit numbers contributing 180 digits, and generally `9 * start` numbers of width `digits`, where `start` is `1, 10, 100, ...`. Subtract whole block sizes until `n` falls inside the current width.

**Locate the containing number with zero-based arithmetic**

Within the chosen block, use `offset = n - 1`. The source number is `start + offset // digits`, and `offset % digits` is its digit index from the left. Subtracting one before division handles exact block and number boundaries without special cases.

**Extract the digit without materializing the sequence**

If the requested index is `i` from the left of a `digits`-wide number, divide by `10 ** ((digits - 1 - i))` and take the result modulo ten. This isolates exactly the desired place value.

**Why block subtraction preserves the target**

Each removed block contains complete source numbers and exactly its calculated number of digits, so subtracting it changes only the target's coordinate system. Once the remaining position lies in one fixed-width block, quotient and remainder uniquely identify its number and digit, proving the returned value matches the global sequence.

## Complexity detail
The number of decimal-width blocks before position `n` is $O(\log n)$, and each block uses constant arithmetic. The algorithm stores a fixed number of integers, using $O(1)$ space.

## Alternatives and edge cases
- **Binary search the containing integer:** is correct, but recomputing cumulative digit counts across widths at each search step takes $O((\log n)^2)$ time.
- **Build the concatenated string:** is simple for tiny positions but needs $O(n)$ time and space.
- **Convert only the containing number to text:** keeps logarithmic time but allocates a short $O(\log n)$ string.
- Position 9 is the last one-digit value; position 10 begins the number 10.
- Position 189 ends the two-digit block; position 190 begins 100.
- The requested digit can be zero.
- Large positions require sufficiently wide arithmetic for block sizes.
