## General

The prescribed removal order always pairs the first unprocessed element with the last unprocessed element. Two indices can represent that state without physically deleting anything: start `left` at the beginning and `right` at the end, then move both inward after processing a pair.

To append the decimal digits of `nums[right]` to `nums[left]`, find the smallest power of ten strictly greater than the right value. If that multiplier is $p$, the concatenated number is computed as `nums[left] * p + nums[right]`. Starting at `10` correctly gives one decimal place even when the right value has one digit, and the loop handles the boundary values `10`, `100`, `1000`, and `10000` without logarithms or strings.

Continue while `left < right`. When the pointers meet, the array had odd length and that single middle value must be added unchanged. If they cross, every element belonged to an outer pair. Each original position is therefore processed exactly once in the same order as the destructive simulation.

## Complexity detail

Let $n$ be the length of `nums`. The pointers process two elements per outer iteration. Determining the decimal multiplier uses at most five steps because every value is at most $10^4$, so it is constant work under the source constraints. Total time is $O(n)$. Only indices, the multiplier, and the running total are stored, giving $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Remove from both ends:** Repeatedly calling `pop(0)` on an array shifts all remaining elements and can turn the simulation into $O(n^2)$ time.
- **String concatenation:** Converting both values to text is concise and correct, but creates temporary strings and is unnecessary for bounded positive integers.
- **Single element:** No concatenation occurs; the sole value is added directly.
- **Odd length:** The two pointers eventually meet at the unique middle element, which must not be concatenated with itself.
- **Different digit widths:** The multiplier depends on the right value only because its digits are appended after the left value.
- **Powers of ten:** A right value such as `100` requires multiplier `1000`; the strict-greater loop condition preserves its trailing digit positions.
- **Large total:** Many concatenated pairs can make the sum exceed 32-bit range, so fixed-width implementations need a 64-bit result.
