## General
**Start where decimal addition starts**

Place one pointer at the final digit of each string and initialize carry to zero. Continue while either pointer remains or carry is nonzero, treating an exhausted input as contributing digit zero.

**Resolve one column completely**

Convert the available digit characters individually, add them with carry, append `total % 10` to a result list, and update carry to `floor(total / 10)`. Then move both pointers left.

**Reverse the least-significant-first result**

Column addition discovers output digits from right to left, so reverse the accumulated characters once after the scan. Keeping them in a list avoids repeatedly copying an expanding string prefix.

**Why the carry simulation is exact**

At each column, the two source digits plus incoming carry equal the mathematical contribution at that power of ten. Quotient and remainder split it into the current output digit and exactly the carry owed to the next column. Induction across columns, including a possible final carry, reconstructs the complete sum.

## Complexity detail
Let `m` and `n` be the input lengths. The scan processes $O(\max(m,n))$ columns and reverses the same number of output digits, for $O(\max(m,n))$ time. The required result list uses $O(\max(m,n))$ space; scalar auxiliary state is constant.

## Alternatives and edge cases
- **Use reversed iterators with zero filling:** expresses the same column addition with equivalent bounds.
- **Prepend each output digit:** is correct but repeatedly shifts or copies the growing result and can take quadratic time.
- **Convert whole strings to integers:** violates the problem's intended arbitrary-length digit simulation.
- Adding two zero strings returns exactly `"0"`.
- Unequal lengths continue with the remaining longer prefix.
- A final carry can make the result one digit longer than both inputs.
- Long runs of nines propagate carry across every column.
