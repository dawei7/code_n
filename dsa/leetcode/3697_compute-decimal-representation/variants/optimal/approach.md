## General

The ordinary decimal expansion already writes `n` as a sum of one-place values. If the digit at position $p$ is $d\ne0$, that position contributes $d\cdot10^p$, which is exactly one base-10 component. Zero digits contribute nothing and must not create result entries.

**Why this uses the fewest components.** A base-10 component begins with exactly one nonzero decimal position. Adding one such value to a partial sum can increase the number of nonzero positions by at most one; any carry only replaces trailing digits while advancing into a higher position. Therefore producing a number with $r$ nonzero decimal digits requires at least $r$ components. Taking the one canonical place value for each nonzero digit uses exactly $r$, meeting that lower bound.

Extract digits from right to left with `divmod`-style remainder and integer division. Multiply each nonzero digit by its current power of ten and append it. This discovery order is ascending by place value, so reverse the collected list once to satisfy the required descending order.

## Complexity detail

Let $D=\lfloor\log_{10}n\rfloor+1$ be the number of decimal digits. The loop processes each digit once, taking $O(D)=O(\log n)$ time. The returned list contains at most $D$ components, so including output storage the space bound is $O(D)=O(\log n)$; the algorithm uses only $O(1)$ auxiliary state beyond that result.

## Alternatives and edge cases

- **Convert to a decimal string:** Multiplying each nonzero character by its positional power is also $O(\log n)$ and clear, but numeric extraction avoids creating a second digit representation.
- **Subtract the largest component repeatedly:** This is correct but performs unnecessary searches and mutations when every component is already encoded by one decimal digit.
- **Internal zeros:** A zero digit contributes no component; for example, `102` yields two entries rather than three.
- **A power of ten:** Values such as `1000` are already single base-10 components and return a one-element list.
- **Maximum input:** $10^9$ contains ten digits but only one nonzero digit, so it returns `[1000000000]`.
- **Descending order:** Right-to-left extraction must be reversed before return; returning discovery order would violate the contract.
