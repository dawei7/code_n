## General
**Separate the first product from later groups:** For $n>4$, the leading group `n * (n - 1) / (n - 2)` evaluates to $n+1$. Every complete later block has the form `-a * (a - 1) / (a - 2) + (a - 3)`. Since `a * (a - 1) / (a - 2)` evaluates to $a+1$ for these decreasing positive integers, a complete block contributes $-(a+1)+(a-3)=-4$.

**Collapse the repeating blocks:** Decreasing `a` by four and adding the next block preserves this fixed correction. Only the final incomplete block depends on the remainder of `n` modulo $4$. Simplifying those four endings yields $n+1$ when `n % 4 == 0`, $n+2$ when the remainder is `1` or `2`, and $n-1$ when the remainder is `3`.

**Handle the short expressions directly:** The periodic derivation assumes a full leading group and a later operator boundary. Therefore return `1`, `2`, `6`, and `7` directly for `n` from `1` through `4`. These values also prevent a remainder formula from being applied before its algebraic pattern begins.

The block identity accounts for every complete set of four decreasing operands, and the remainder case accounts for every operand left at the end. Thus the closed form is exactly the value produced by a precedence-aware simulation.

## Complexity detail
The result uses a fixed number of comparisons and arithmetic operations, independent of $n$, for $O(1)$ time. It stores only the input and its remainder, so auxiliary space is $O(1)$.

## Alternatives and edge cases
- **Stack simulation:** Applying multiplication and division immediately while storing additive terms mirrors precedence clearly, but processes all $n$ operands and uses $O(n)$ space.
- **Four-term streaming simulation:** Accumulating one operator block at a time reduces auxiliary space to $O(1)$ but still takes $O(n)$ time.
- **Values below five:** Return the explicitly evaluated results because the stable four-value pattern has not started.
- **Incomplete final block:** The remainder modulo $4$ determines which multiplication, division, or addition operands are missing.
- **Operator precedence:** Do not evaluate the full expression strictly from left to right; multiplication and division bind before addition and subtraction.
