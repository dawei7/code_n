## General

**Reuse the active prefix**

The next row is shorter than the current row, so it can be written into positions starting at zero. For an active row of length $m$, replace each `nums[i]` for $0\le i<m-1$ with `(nums[i] + nums[i + 1]) % 10`, then treat only the first $m-1$ positions as active.

Updating from left to right is safe. When computing position $i$, `nums[i]` still contains the old current value and `nums[i + 1]` has not yet been overwritten. Values earlier than $i$ are no longer needed by any later pair.

After one pass, the active prefix is exactly the next array specified by the process. Repeating this invariant until the active length is one leaves the triangular sum at `nums[0]`.

## Complexity detail

Let $n=\lvert\texttt{nums}\rvert$. The algorithm performs

$$
(n-1)+(n-2)+\cdots+1=\frac{n(n-1)}{2}
$$

updates, so time is $O(n^2)$. It modifies the input and uses $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Allocate every row:** List comprehensions closely mirror the definition but use $O(n)$ peak auxiliary space.
- **Delete from the front:** Treating each row as a queue can make physical shifts add a cubic-time cost.
- **Binomial coefficients:** The final digit is a binomially weighted sum modulo 10, but handling coefficients modulo a composite base is more intricate than the bounded simulation.
- **Single digit:** No transformation occurs; the input digit is already the answer.
- **Modulo after each addition:** Reducing each pair immediately keeps every active value a decimal digit.
- **Input mutation:** The in-place method intentionally overwrites the supplied list; the returned scalar is independent of its final inactive suffix.
