## General
**The closest pair straddles the square root**

For `length >= width`, the width cannot exceed `sqrt(area)`. As a valid width grows toward the square root, its quotient moves toward it and the dimension difference shrinks.

**Search widths downward**

Start at `floor(sqrt(area))` and decrease until finding a divisor. Its quotient is automatically at least as large as the width.

**Why the first divisor is optimal**

The search's first divisor is the largest valid width not exceeding the square root. Every other factor pair uses a smaller width and larger length, so none can have a smaller difference.

## Complexity detail
At most `floor(sqrt(area))` widths are tested, giving $O(\sqrt{area})$ time for prime areas. Only the current width and quotient are stored, so space is $O(1)$.

## Alternatives and edge cases
- **Scan lengths upward from the square root:** is correct but may take $O(area)$ tests for a prime.
- **Enumerate all factor pairs:** continues after the optimum is already known.
- **Floating square root:** needs care near rounding boundaries; integer square root avoids them.
- **Perfect square:** returns equal dimensions immediately.
- **Prime area:** returns `[area, 1]`.
- **Area one:** returns `[1, 1]`.
- **Dimension order:** place the quotient first.
