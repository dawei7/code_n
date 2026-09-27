# Guided Example: Maximum Difference by Remapping a Digit

## 1. What a single remap actually does

Bob picks a source digit $a$ and a target digit $b$, both from $\{0,1,\dots,9\}$, and rewrites **every** occurrence of $a$ in `num` as $b$. Positions holding other digits are untouched. Write the input as the digit string $d_0d_1\cdots d_{k-1}$ read left to right, so that $k$ digits encode the value

$$N \;=\; \sum_{i=0}^{k-1} d_i\,10^{\,k-1-i}.$$

A remap $\rho_{a\to b}$ substitutes $b$ for $d_i$ exactly at those positions $i$ with $d_i = a$. Three facts follow, and they shape the entire solution.

1. **The unit of change is a digit value, not a position.** In `11891` the digit $1$ sits at positions $0$, $1$ and $4$. Any remap whose source is $1$ moves all three of them together, and cannot move one of them alone.
2. **Absent sources and self-targets are no-ops.** If $a$ never occurs in `num`, or if $b = a$, the result is `num` itself. Such remaps are legal, they are simply never extreme — except when the input already consists only of $9$s.
3. **The two extremes are chosen independently.** The problem allows a different source digit for the minimum than for the maximum, so the answer is not the gap between two outcomes of one shared remap.

Comparing candidate results is a left-to-right comparison of digit strings of the same length, because a single unit in the leading place outweighs every lower place combined:

$$\sum_{j=1}^{k-1} 9\cdot 10^{\,k-1-j} \;=\; 10^{\,k-1}-1 \;<\; 10^{\,k-1}.$$

That place-value dominance is the invariant that justifies both greedy choices below.

## 2. The instance we work through

We trace `num = 11891`, whose repeated digit $1$ happens to drive *both* extremes. That coincidence is a property of this input, not of the problem, and Section 5 shows inputs where the two optimal sources differ. Decomposing the input:

| Position $i$ | Digit $d_i$ | Place value $10^{\,4-i}$ | Contribution $d_i\cdot10^{\,4-i}$ |
|---|---|---|---|
| 0 | 1 | 10000 | 10000 |
| 1 | 1 | 1000 | 1000 |
| 2 | 8 | 100 | 800 |
| 3 | 9 | 10 | 90 |
| 4 | 1 | 1 | 1 |
| — | — | total $N$ | 11891 |

## 3. Maximizing: replace the leftmost digit that is not 9

**Greedy claim.** If some digit of `num` differs from $9$, let $p$ be the leftmost such position and put $c = d_p$. Then the largest achievable value comes from $\rho_{c\to9}$.

**Why no other remap can beat it.** Fix any remap $\rho_{a\to b}$, let $M$ be its result, and let $M^{*}$ be the result of $\rho_{c\to9}$. Every position strictly left of $p$ already holds $9$ in the input, and a remap can only rewrite a digit as $b \le 9$, so $M_i \le M^{*}_i = 9$ for all $i < p$; at position $p$ the candidate holds $9$ while again $M_p \le 9$. Therefore, at the first position $j \le p$ where $M$ and $M^{*}$ differ, all earlier positions agree and $M_j < M^{*}_j$, so $M < M^{*}$ by place-value dominance.

The only escape is that no such $j$ exists, meaning $M$ agrees with $M^{*}$ through position $p$. That forces $M_p = 9$, so $b = 9$ and position $p$ is an occurrence of the source digit, i.e. $a = c$. From position $p+1$ onward the candidate leaves digits alone while $M$ can only lift digits up to $9$, hence $M \ge M^{*}$. So $M^{*}$ is maximal, and remapping the leftmost non-9 digit to $9$ is the unique maximizing move up to ties.

**Applying it to `11891`.** Scanning from the left, $d_0 = 1 \neq 9$, so $p = 0$, $c = 1$, and the maximizing remap is $1 \to 9$. Alternatives lose for concrete reasons:

| Remap tried | Resulting digits | Value | Comparison with the optimum |
|---|---|---|---|
| $1\to9$ (chosen) | `99899` | 99899 | optimal: the leading place is saturated |
| $1\to8$ | `88898` | 88898 | target too small, leading digit drops from 9 to 8 |
| $8\to9$ | `11991` | 11991 | source too far right; the leading digit stays 1 |
| $9\to9$ | `11891` | 11891 | identity remap, so the value is unchanged |

## 4. Minimizing: send the leading digit to zero

**Greedy claim.** The smallest achievable value comes from $\rho_{d_0\to0}$: the leading digit and every other occurrence of that same digit become $0$.

**Why the leading digit must be attacked.** Let $\rho_{a\to b}$ produce $M$ and let $M_{*}$ be the candidate result. Position $0$ keeps $d_0$ unless $a = d_0$, in which case it becomes $b$. Either way $M_0 \ge 0$. If $M_0 = 0$ then $a = d_0$ and $b = 0$, so the remap *is* the candidate. Otherwise $M_0 \ge 1$, so $M \ge M_0\cdot10^{\,k-1} \ge 10^{\,k-1}$, while the candidate has leading digit $0$ and therefore $M_{*} \le 10^{\,k-1}-1$ by the dominance bound. Hence $M > M_{*}$. No remap that leaves the leading digit non-zero can be minimal, and zeroing *all* occurrences of the leading digit is exactly what one remap does.

**Applying it to `11891`.** The leading digit is $1$, so the minimizing remap is $1 \to 0$; positions $0$, $1$ and $4$ all become $0$, producing the digit string `00890` with value 890. Leading zeros are explicitly allowed and only mean the result is numerically below $10^{\,k-1}$; they do not make the value invalid.

| Position $i$ | $d_i$ | Under $1\to9$ (maximize) | Contribution | Under $1\to0$ (minimize) | Contribution |
|---|---|---|---|---|---|
| 0 | 1 | 9 | 90000 | 0 | 0 |
| 1 | 1 | 9 | 9000 | 0 | 0 |
| 2 | 8 | 8 | 800 | 8 | 800 |
| 3 | 9 | 9 | 90 | 9 | 90 |
| 4 | 1 | 9 | 9 | 0 | 0 |
| — | — | **Maximum** | **99899** | **Minimum** | **890** |

The answer is the difference of the two independent optima, $99899 - 890 = 99009$, which matches the authored expectation for this input. Notice the asymmetry between the two columns: every occurrence of the chosen source moves, so the maximizing step adds $8\cdot(10000+1000+1) = 88008$ to the input while the minimizing step removes $11001$ from it.

## 5. The general rule, checked against boundary inputs

Two scans settle any input: find the leftmost digit below $9$ for the maximum, and read position $0$ for the minimum. If every digit is $9$, the maximum is the input unchanged and only the minimum moves.

| `num` | Maximizing remap | Maximum | Minimizing remap | Minimum | Difference |
|---|---|---|---|---|---|
| `1` | $1\to9$ | 9 | $1\to0$ | 0 | 9 |
| `90` | $0\to9$ | 99 | $9\to0$ | 0 | 99 |
| `909` | $0\to9$ | 999 | $9\to0$ | 0 | 999 |
| `999` | none needed, already maximal | 999 | $9\to0$ | 0 | 999 |
| `123456` | $1\to9$ | 923456 | $1\to0$ | 23456 | 900000 |
| `100000000` | $1\to9$ | 900000000 | $1\to0$ | 0 | 900000000 |
| `10000` | $1\to9$ | 90000 | $1\to0$ | 0 | 90000 |

Every row agrees with the package's authored cases. In the `90` and `909` rows the maximizing source is $0$, which first appears *after* the leading digit, while the minimizing source is $9$: the two optima genuinely use different sources, so they must be derived separately rather than read off one shared remap.

## 6. Why the reasoning is correct

The two claims together cover all $10 \times 10 = 100$ legal remaps without enumerating them, and the case analysis is exhaustive in exactly one way:

- If the maximizing remap's target is below $9$, the leftmost differing position is at or before $p$ and its result is strictly smaller than the candidate.
- If the target is $9$, the result either matches the candidate through $p$ — in which case its source must be the leftmost non-9 digit and the result is at least the candidate — or it differs earlier and is smaller.
- For the minimum, the only remap that can place $0$ in the leading position is the one whose source is the leading digit and whose target is $0$; every other remap keeps a leading digit of at least $1$ and therefore a value of at least $10^{\,k-1}$, which exceeds every value the candidate can reach.
- When all digits are $9$, no remap increases the value, so the maximum is $N$ itself; the minimizing argument is unaffected because it never required a non-9 digit to exist.

The final subtraction is sound because the statement grants the two directions independent remaps: the maximum and the minimum are separately realizable outcomes, and the requested quantity is their gap.

## 7. Traps this instance exposes

| Tempting move | What it produces on `11891` | Why it is wrong |
|---|---|---|
| Remap the "unusual" digit $8$ to $9$ | `11991` | A gain in a lower place cannot compensate for a smaller leading digit. |
| Zero a lower digit for the minimum | `11091` from $8\to0$ | The leading digit still contributes $10^4$; only zeroing that place drops the value below $10^{\,k-1}$. |
| Assume one source digit serves both extremes | accidentally correct here, since $1$ is both the leading digit and the leftmost non-9 digit | On `90` the maximum needs $0\to9$ and the minimum needs $9\to0$; the choices are independent. |
| Reject a result because it has leading zeros | would discard `00890` | Leading zeros are permitted; `00890` is simply the number 890 and it is the true minimum. |
| Expect a remap to help when every digit is $9$ | — | On `999` every remap to $9$ is the identity, so the maximum is `999` and only the minimum changes. |
| Remap a digit that appears only once | e.g. $8\to9$ again | A single occurrence in a low place moves the value far less than a repeated digit in a high place, so "appears once" is not a criterion for choosing the source. |

## 8. Time and auxiliary space

Let $k$ be the number of decimal digits of `num`, so $k \le 9$ because $1 \le \texttt{num} \le 10^{8}$.

- **Time** $O(k)$: one left-to-right scan locates the leftmost digit below $9$; building the maximizing digit string, building the minimizing digit string, and evaluating both results are each a constant number of linear passes over the $k$ positions. No pair of digits is ever enumerated, so the work does not depend on the $100$ possible remaps.
- **Auxiliary space** $O(k)$: the two constructed digit strings (equivalently, the digit array of the input) are the only storage beyond a few integer accumulators.

Both bounds are constant over the stated constraint range, and writing them with $k$ keeps the dependence on the input length explicit.
