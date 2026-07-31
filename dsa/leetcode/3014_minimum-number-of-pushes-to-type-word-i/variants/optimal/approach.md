## General

**Count available positions by push cost.** Each of the eight usable keys contributes one position costing one push, one position costing two pushes, and so on. Because every letter in `word` is distinct and occurs once, the identities of the letters do not affect the total; only $N=\lvert\texttt{word}\rvert$ matters.

**Fill the cheapest positions first.** If a used letter occupied a more expensive position while a cheaper position was empty, moving that letter to the cheaper position would reduce the total and preserve every mapping rule. Therefore an optimal remapping fills all eight one-push positions before any two-push position, all eight two-push positions before any three-push position, and so forth.

Write $N=8q+r$, where $0\le r<8$. There are $q$ complete cost levels. Their total is

$$
8(1+2+\cdots+q)=4q(q+1).
$$

The remaining $r$ letters each cost $q+1$ pushes. Hence the answer is $4q(q+1)+r(q+1)$.

## Complexity detail

The implementation uses the string length and a constant number of arithmetic operations, so its time complexity is $O(1)$ and its auxiliary space complexity is $O(1)$. The legal source domain is capped at 26 letters; the package therefore uses a verified bounded-domain certificate instead of pretending that out-of-contract runtime scaling is meaningful.

## Alternatives and edge cases

- **Explicit slot construction:** Build the costs `[1] * 8 + [2] * 8 + ...` and sum the first $N$ entries. This is easy to visualize but does unnecessary work compared with the closed form.
- **Round-robin key assignment:** Assign letters cyclically across the eight keys and count their positions. It reaches the same minimum in $O(N)$ time because the letters have equal frequency.
- **Fewer than eight letters:** Every letter can occupy a one-push position, so the answer equals $N$.
- **A multiple of eight:** The remainder is zero, so no partially filled cost level is added.
- **Maximum length:** At $N=26$, the layout uses eight one-push, eight two-push, eight three-push, and two four-push positions.
