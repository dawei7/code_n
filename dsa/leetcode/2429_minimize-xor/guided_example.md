# Guided Example: Minimize XOR

## 1. The Instance and What Makes It Hard

Two positive integers are given: `num1 = 1` and `num2 = 12`. We must return a positive
integer $x$ that satisfies two requirements at once.

- **Cardinality constraint:** $x$ carries exactly as many set bits as `num2`. Writing
  `num2 = 12` in binary gives `01100`, so the required count is $\kappa = 2$.
- **Objective:** the value $x \oplus \text{num1}$ must be as small as possible.

The test data guarantees that this $x$ is unique, so the two requirements do not merely
bound a range of acceptable answers — they pin down a single integer.

`num1 = 1` is the smallest legal input and has exactly one set bit, at position $0$. Since
$\kappa = 2$ exceeds the number of set bits available in `num1`, no choice of $x$ can
match `num1` everywhere: at least one bit of the XOR is forced to $1$. The interesting
question is *which* forced mismatch is cheapest, and that is precisely what this instance
exposes. Had we picked `num1 = 3`, `num2 = 5` instead, the answer would be the trivial
copy $x = 3$ with $x \oplus \text{num1} = 0$, and the second decision phase would never
appear.

## 2. XOR Cost Is a Weighted Sum of Independent Bit Positions

Because XOR never carries between positions, the objective decomposes exactly:

$$
x \oplus \text{num1} = \sum_{p \ge 0} \bigl[x_p \ne (\text{num1})_p\bigr] \cdot 2^{p},
$$

where $x_p$ denotes bit $p$ of $x$. Every position contributes independently, and a
mismatch at position $p$ costs the fixed weight $2^{p}$. The decisive numerical fact is
that binary weights grow faster than the sum of everything below them:

$$
2^{p} \;>\; \sum_{i=0}^{p-1} 2^{i} \;=\; 2^{p} - 1 .
$$

| Position $p$ | Weight $2^{p}$ | Sum of all lower weights $\sum_{i<p} 2^{i}$ | Dominates lower positions? |
|---|---|---|---|
| 0 | 1 | 0 | no lower positions exist |
| 1 | 2 | 1 | yes, by 1 |
| 2 | 4 | 3 | yes, by 1 |
| 3 | 8 | 7 | yes, by 1 |
| 4 | 16 | 15 | yes, by 1 |

The table says something stronger than "higher bits matter more": one mismatch at
position $p$ costs strictly more than mismatches at *every* lower position combined.
Consequently any candidate that mismatches at a high position can be improved by moving
that mismatch downward, no matter what happens below. The optimisation is therefore
lexicographic from the most significant bit to the least, and a greedy scan from high to
low cannot be trapped by a later trade-off.

## 3. The Two-Phase Greedy Rule

The budget is the $\kappa = 2$ set bits that $x$ is allowed to spend. Matching `num1` at
a position whose bit is $1$ costs nothing in the XOR but consumes one unit of budget.
Because of the domination lemma, budget should be spent on the highest such positions
first. That gives the first phase:

1. **Descending match phase.** Walk positions from $29$ down to $0$. Whenever bit $p$ of
   `num1` is $1$ and budget remains, set $x_p = 1$ and decrement the budget. This buys a
   zero at the most expensive XOR positions.

If the budget survives this phase, then `num2` has more set bits than `num1` and some
ones of $x$ have nowhere to match. Every remaining one must land on a position where
`num1` has $0$, and each such placement creates an unavoidable mismatch. To minimise the
total, those ones belong at the *cheapest* positions:

2. **Ascending fill phase.** Walk positions from $0$ upward. Whenever bit $p$ of `num1`
   is $0$ and budget remains, set $x_p = 1$ and decrement the budget. Stop as soon as the
   budget is exhausted.

The two phases differ in direction for the same reason: phase 1 buys the most expensive
savings available, phase 2 pays the least expensive unavoidable costs. Once the budget
reaches zero, every remaining bit of $x$ is dictated as $0$.

## 4. Step-by-Step Construction

For `num1 = 1` the binary layout is `00001` over five significant positions, with the
sole set bit at position $0$. The initial budget is $\kappa = 2$.

| Step | Scan | Position $p$ tested | Bit $p$ of `num1` | Budget before | Action | $x$ after (binary) | Budget after |
|---|---|---|---|---|---|---|---|
| 0 | — | — | — | 2 | start from $x = 0$ | `00000` | 2 |
| 1 | descending | 4, 3, 2, 1 | `0` at each | 2 | no match available, budget untouched | `00000` | 2 |
| 2 | descending | 0 | `1` | 2 | match: set $x_0 = 1$ | `00001` | 1 |
| 3 | ascending | 0 | `1` | 1 | not a zero position, skip | `00001` | 1 |
| 4 | ascending | 1 | `0` | 1 | fill: set $x_1 = 1$ | `00011` | 0 |
| 5 | ascending | 2 | `0` | 0 | budget exhausted, halt | `00011` | 0 |

Assembling the chosen positions $\{0, 1\}$ gives

$$
x = 2^{1} + 2^{0} = 3,
$$

and the realised objective is

$$
x \oplus \text{num1} = 3 \oplus 1 = \texttt{0b00011} \oplus \texttt{0b00001} = \texttt{0b00010} = 2 .
$$

This agrees with the authored expectation for the pair `(1, 12)`, whose answer is `3`.

## 5. State Before and After Each Phase

The same reasoning is easier to audit when the state is read as a whole. The budget column
counts set bits of $x$ still unspent, and the last column is the objective the partial
assignment already guarantees.

| Stage | Budget remaining | Chosen set positions of $x$ | $x$ (binary) | $x$ (decimal) | $x \oplus \text{num1}$ |
|---|---|---|---|---|---|
| Initial | 2 | $\{\}$ | `00000` | 0 | 1 |
| After descending match phase | 1 | $\{0\}$ | `00001` | 1 | 0 |
| After ascending fill phase | 0 | $\{0, 1\}$ | `00011` | 3 | 2 |
| Output | — | — | `00011` | 3 | 2 |

The descending phase drove the objective from $1$ to $0$ by cancelling the only set bit
`num1` offers. The ascending phase had to reintroduce a cost of $2$, because the second
required bit of $x$ cannot be matched anywhere; placing it at position $1$ rather than
position $4$ keeps that unavoidable cost at $2$ instead of $16$.

## 6. Contrasting Instances: Both Phases Are Real

The rule is only convincing if each phase can dominate an answer. The table compares four
authored instances, where $\kappa = \mathrm{popcount}(\text{num2})$.

| `num1` (binary) | `num2` (binary) | $\kappa$ | Phase 1 matched positions | Phase 2 filled positions | $x$ | $x \oplus \text{num1}$ |
|---|---|---|---|---|---|---|
| `00001` (1) | `01100` (12) | 2 | $\{0\}$ | $\{1\}$ | 3 | 2 |
| `11001` (25) | `1001000` (72) | 2 | $\{4, 3\}$ | none | 24 | 1 |
| `0011` (3) | `0101` (5) | 2 | $\{1, 0\}$ | none | 3 | 0 |
| `1111` (15) | `0001` (1) | 1 | $\{3\}$ | none | 8 | 7 |

The second row shows phase 1 refusing to spend its two matches on the cheap low bit $0$ of
`num1 = 25`; it takes positions $4$ and $3$ instead, sacrificing the low bit and accepting
XOR cost $1$. The fourth row is the opposite regime: `num2` has fewer set bits than `num1`,
so the budget runs out during the descending phase and phase 2 never runs.

## 7. Why the Greedy Rule Is Correct

Let $c_1$ be the number of set bits of `num1` and let $\kappa$ be the required popcount of
$x$.

**Invariant of the descending phase.** Before the scan tests position $p$, the positions
already fixed in $x$ are exactly the set positions of `num1` strictly above $p$, taken in
descending order and truncated to the budget. Every mismatch created above $p$ is therefore
forced, and every position above $p$ that could be matched within budget has been matched.

**Exchange argument for phase 1.** Suppose a feasible $x$ with $\kappa$ set bits matches
`num1` at a lower set position $q$ while leaving a higher set position $p > q$ of `num1`
unmatched. Move the one from $q$ to $p$. The mismatch at $p$ disappears, saving $2^{p}$,
and a new mismatch appears at $q$, costing $2^{q}$. Because $2^{p} > 2^{q}$, the objective
strictly decreases. Hence an optimal $x$ matches the highest $\min(\kappa, c_1)$ set
positions of `num1`.

**Exchange argument for phase 2.** If $\kappa > c_1$, every set position of `num1` is
matched, so the remaining $\kappa - c_1$ ones of $x$ must occupy zero positions of `num1`,
each producing a mismatch. Suppose such a one sits at position $p$ while a lower zero
position $q < p$ of `num1` is unused. Moving the one from $p$ to $q$ replaces cost $2^{p}$
with cost $2^{q} < 2^{p}$, improving the objective and leaving the bit count unchanged.
Therefore the extra ones belong at the lowest $\kappa - c_1$ zero positions.

**Feasibility of the fill phase.** There are $30$ bit positions and $\kappa \le 29$ under
the bound `num2` $\le 10^{9}$, so $30 - c_1 \ge \kappa - c_1$: the ascending loop always has
enough zero positions to complete the budget.

Every feasible assignment of $\kappa$ ones either already agrees with the greedy choice or
admits one of the two strict improvements above, so the greedy assignment is the unique
minimiser — matching the problem's uniqueness guarantee.

## 8. Boundary and Degenerate Instances

| Situation | Input | Behaviour of the method | Output |
|---|---|---|---|
| Identical inputs | `num1 = num2 = 1000000000` | $\kappa = \mathrm{popcount}(\text{num1})$, so phase 1 copies every set bit and phase 2 has nothing left to place | `1000000000` |
| Single required bit | `num1 = 15`, `num2 = 1` | $\kappa = 1$; only the highest set bit of `num1` is matched | `8` |
| Only a high source bit | `num1 = 536870912`, `num2 = 7` | match position $29$, then fill the lowest two zero positions | `536870915` |
| Nearly full width | `num1 = 1`, `num2 = 536870911` | $\kappa = 29$; match position $0$, then fill positions $1$ through $28$ | `536870911` |
| Minimum legal inputs | `num1 = 3`, `num2 = 1` | $\kappa = 1$; the high set bit of `num1` is kept, the low one is dropped | `2` |
| One match plus one fill | `num1 = 1`, `num2 = 12` | both phases execute, the second producing the only mismatch | `3` |

Two traps live in this table. First, $x$ must be *positive*, not merely non-negative: since
`num2` $\ge 1$ guarantees $\kappa \ge 1$, the constructed $x$ always has a set bit. Second,
the budget can exceed the number of ones in `num1` by a wide margin — the fourth row uses 29
of the 30 available positions — so the fill phase must not assume `num1` supplies enough
ones.

## 9. Alternative Methods and Their Costs

| Alternative | Idea | Why it is not used |
|---|---|---|
| Enumerate every integer with $\kappa$ set bits | Generate all candidate values and evaluate each XOR | Up to $\binom{30}{15} = 155{,}117{,}520$ candidates; ignores that positions are independent under XOR |
| Digit DP over positions with a remaining-count state | Process bits from high to low, memoise on (position, budget) | Correct but unnecessary: no carry couples the positions, so the exchange argument already fixes each bit |
| Mutate `num1` in place | Clear its lowest set bits when $\kappa < c_1$, or set its lowest zero bits when $\kappa > c_1$ | Same greedy priorities and running time, but the two regimes need separate loops and are easier to get wrong |
| Sort candidate positions by weight | Sort positions descending by $2^{p}$ and match greedily | Equivalent to the directed scans, with extra bookkeeping |
| Test every $x$ below $2^{30}$ | Check the bit count and the XOR value for each integer | $\Theta(2^{30})$ work for a problem decided by at most 60 bit tests |

## 10. Complexity Derivation

Let $B$ be the bit width needed to represent the inputs. Under the stated constraints
`num1, num2` $\le 10^{9} < 2^{30}$ the relevant positions are $0$ through $29$, so
$B = 30$, and in general $B = \Theta(\log \max(\text{num1}, \text{num2}))$.

**Time.** Counting the set bits of `num2` costs $O(B)$ in a bit-serial model, or $O(1)$
with a hardware popcount. The descending match scan tests each of the $B$ positions once,
and the ascending fill scan does the same, so the total is

$$
O(B) \;=\; O(\log \max(\text{num1}, \text{num2})) .
$$

No position is revisited and no nested loop exists, so the bound is tight.

**Auxiliary space.** The method keeps only the required popcount $\kappa$, the integer being
assembled, and a loop index. Nothing is allocated per position and no table is materialised,
so auxiliary space is

$$
O(1).
$$

The returned integer is the output rather than auxiliary storage; it occupies $O(B)$ bits in
the output space, which is unavoidable for any method that returns a value of that width.