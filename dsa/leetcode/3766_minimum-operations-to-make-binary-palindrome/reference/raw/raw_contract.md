## Function Contract

**Inputs**

- `nums`: A nonempty array of positive integers.

Each array position is solved separately; changing one value has no effect on any other position. Because each operation changes a value by exactly 1, converting an original value $x$ to a chosen binary palindrome $p$ costs exactly $\lvert x-p\rvert$ operations.

Let $N = \lvert\texttt{nums}\rvert$ and let $V = \max(\texttt{nums})$.

**Return value**

Return `ans`, where `ans[i]` is the smallest absolute difference between `nums[i]` and any nonnegative integer whose ordinary binary representation is palindromic. Preserve the input order.
