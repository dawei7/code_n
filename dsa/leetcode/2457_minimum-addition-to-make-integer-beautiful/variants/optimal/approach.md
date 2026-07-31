## General

If `n` is not already beautiful, any positive addition changes some decimal position and may zero positions to its right through rounding. For a fixed position, the smallest useful change is to raise its non-zero digit to the next multiple of ten; this makes every processed lower position zero. Trying positions from right to left therefore considers candidate results in increasing order, so the first beautiful result gives the minimum addition.

Maintain the current digit sum instead of converting and summing the entire number after every rounding step. Suppose the current digit is $d>0$. Adding `(10 - d) * place` removes $d$ from the digit sum and carries one into the higher prefix. Ordinarily that adds one, but each trailing `9` in the prefix becomes `0`, reducing the sum by another nine. Thus the update is `digit_sum - d + 1 - 9 * trailing_nines`.

A zero digit needs no addition; advance to the next position. For a non-zero digit, count the prefix's trailing nines, update the digit sum, apply the rounding addition, and advance. Once the maintained sum is at most `target`, the difference between the rounded value and the original `n` is the requested `x`.

Every skipped zero is visited once. A `9` examined by the inner carry scan is immediately changed to zero by that carry, so it cannot be charged repeatedly to later rounds. Consequently, the total work across both loops is linear in the number of decimal digits.

## Complexity detail

Let $d=\lfloor\log_{10} n\rfloor+1$ be the number of decimal digits of the original input. The initial digit sum takes $O(d)$ time. The outer scan visits $O(d)$ positions, and trailing-nine scans are amortized $O(d)$ because every scanned `9` is consumed by a carry. Total time is therefore $O(d)=O(\log n)$.

The algorithm stores only a fixed number of integers, so auxiliary space is $O(1)$.

## Alternatives and edge cases

- **Recompute the digit sum after each rounding:** This is concise and correct, but rescanning up to $d$ digits after as many as $d$ rounds takes $O(d^2)$ time.
- **Increment one value at a time:** Testing `n`, `n + 1`, and so on eventually finds the minimum, but the addition can be proportional to `n`.
- **String prefix preprocessing:** Prefix sums and trailing-nine counts also produce an $O(d)$ solution, but require $O(d)$ auxiliary storage.
- **Already beautiful:** Return `0` before any position changes.
- **Zero decimal positions:** Skip them; adding a full place value would bypass smaller candidates unnecessarily.
- **Carry through nines:** Every carried-over `9` becomes `0` and must reduce the maintained digit sum by nine.
- **Target one:** A power of ten is always beautiful, which also explains the guarantee that a solution exists for every legal input.
- **Minimum rather than any solution:** Processing positions from least significant upward is essential because it examines the smallest possible rounding boundaries first.
- **Upper input bound:** The returned addition may change the number of digits, so implementations must use an integer type wide enough for the result.
