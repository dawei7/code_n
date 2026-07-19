## General
**Use stacks to reach least-significant digits first**

Addition begins at the rightmost digits, but the input order exposes the most significant digits first and may not be reversed. Copy each list's digits into a stack so popping produces the required right-to-left order.

**Propagate the carry while either stack remains**

Repeatedly pop one digit from each nonempty stack, add them with the carry, and split the total into `digit = total % 10` and `carry = total // 10`. Continue while either stack or the carry remains, which naturally handles unequal operand lengths and a new leading digit.

**Prepend each computed digit**

Digits are computed least-significant first but the result must be forward ordered. In the native linked form, create each new result node with the current head as its `next`. The app-local list adaptation collects reverse digits and reverses them once at the end.

**Why the produced digits equal the arithmetic sum**

At each decimal position, the algorithm adds exactly the two operand digits at that place plus the carry from the previous place. Remainder modulo ten is the result digit and integer division is precisely the carry into the next position. Induction from the units position through the final carry proves the full forward digit sequence represents the sum.

## Complexity detail
Every digit is pushed and popped once, so time is $O(m + n)$. The operand stacks and returned digits use $O(m + n)$ space; the native result nodes are required output.

## Alternatives and edge cases
- **Reverse both input lists:** permits ordinary forward addition but violates the requirement not to modify the inputs unless they are restored.
- **Recursive alignment by length:** can propagate carries without explicit stacks but uses $O(m + n)$ call-stack space and more intricate carry handling.
- **Rescan from the head for every right-side digit:** remains correct but takes $O((m + n)^2)$ time.
- **Different lengths:** a missing digit contributes zero.
- **Final carry:** prepend it as a new most-significant digit.
- **Both inputs zero:** return exactly one zero digit.
