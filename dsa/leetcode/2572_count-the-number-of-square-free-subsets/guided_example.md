# Guided Example: Count the Number of Square-Free Subsets

## 1. The obstruction is a repeated prime, not a large product

A subset of `nums` is square-free when the product of the elements it selects is divisible by no perfect square larger than $1$. Factoring that product is not how the problem becomes tractable. Write each element as a product of primes and the real condition appears:

$$\prod_{i \in I} \texttt{nums}[i] \ \text{is square-free} \iff \text{no prime divides two distinct elements of } I \text{ and no element contains } p^2.$$

If a prime $p$ divides both `nums[i]` and `nums[j]` for $i \ne j$, then $p^2$ divides the product. If one element already contains $p^2$, the product contains $p^2$ as well. Conversely, when the second condition never occurs and the selected elements share no prime, every prime exponent in the product is exactly $1$, so the product is square-free. The task is therefore a **compatibility problem between the prime supports of the elements**, not an arithmetic problem about products.

The representative instance used throughout this lesson is

- Input: `nums = [1, 1, 2, 6]`
- Required outcome: `11`

It is deliberately small but it carries every decisive idea at once: two copies of the value `1`, which consume no prime yet double the number of choices; the value `2` with prime support $\{2\}$; the value `6` with prime support $\{2,3\}$, which is individually legal but incompatible with `2`; and a final correction that removes the empty subset.

## 2. The ceiling on the input values collapses the prime universe

The constraint $1 \le \texttt{nums}[i] \le 30$ is the reason a compact state space exists at all. No single element can introduce a prime larger than $29$, so at most the ten primes

$$P = \{2, 3, 5, 7, 11, 13, 17, 19, 23, 29\}$$

can ever appear. Moreover each element is either intrinsically usable or intrinsically hopeless:

| Values in $1..30$ | Contains a repeated prime? | Can it appear in a square-free subset? |
|---|---|---|
| `1` | no | yes, and it contributes no prime at all |
| `2`, `3`, `5`, `7`, `11`, `13`, `17`, `19`, `23`, `29` | no | yes, its support is a single prime |
| `6`, `10`, `14`, `15`, `21`, `22`, `26` | no | yes, its support is two distinct primes |
| `30` | no | yes, its support is three distinct primes |
| `4`, `8`, `9`, `12`, `16`, `18`, `20`, `24`, `25`, `27`, `28` | yes | never, the value alone already forces a square divisor |

A value in the last row is unusable under every combination: `4` and `8` carry $2^2$, `9` and `27` carry $3^2$, `25` carries $5^2$, and `12`, `16`, `18`, `20`, `24`, `28` carry one of those squares too. Testing divisibility by $4$, $9$, and $25$ is sufficient to detect all of them because $7^2 = 49 > 30$: no larger square can fit inside a value of at most $30$.

Assign one bit to each prime of $P$:

| Bit $i$ | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|---|
| Prime $p_i$ | $2$ | $3$ | $5$ | $7$ | $11$ | $13$ | $17$ | $19$ | $23$ | $29$ |

A usable value $x$ becomes a **support mask**: the set of bits belonging to the primes that divide $x$. Every mask is a subset of a $10$-element universe, so there are exactly $2^{10} = 1024$ masks — a state space that does not depend on the input length. Note also that for square-free $x \ge 2$ the mask determines the value, because $x$ is precisely the product of the primes in its own support.

## 3. The state: how many subsets realize each used-prime set

Let $c_x$ count how many positions of `nums` hold the value $x$. The dynamic programming table is indexed by masks:

$$f[S] = \text{number of index subsets whose product has prime support exactly } S.$$

The empty subset is included in $f[0]$, and every count is kept modulo $10^9 + 7$ because the number of subsets can be astronomically large while the required output stays small.

Ones deserve separate treatment. The value `1` has an empty support, so it conflicts with nothing and can be taken or skipped freely and independently of every other decision. A subset of the $c_1$ one-positions can be combined with any admissible selection of the remaining values, which contributes a factor of $2^{c_1}$:

$$f[0] = 2^{c_1}, \qquad f[S] = 0 \ \text{for every} \ S \ne 0 .$$

Composition of the representative instance:

| Value `x` | Occurrences $c_x$ | Support mask $m(x)$ | Primes used by the support |
|---|---|---|---|
| `1` | 2 | $0$ | none |
| `2` | 1 | $1$ (bit 0) | $\{2\}$ |
| `6` | 1 | $3$ (bits 0 and 1) | $\{2,3\}$ |

## 4. Executing the recurrence on `nums = [1, 1, 2, 6]`

Each distinct usable value $x \ge 2$ is swept once, in increasing order of $x$. At most one position holding $x$ can ever be selected, because $x \ge 2$ has a non-empty support and two copies of $x$ would repeat every prime in that support. Selecting one position out of the $c_x$ available positions gives $c_x$ possibilities, so the sweep is

$$f[S \cup m(x)] \leftarrow f[S \cup m(x)] + c_x \cdot f[S] \qquad \text{for every mask } S \text{ with } S \cap m(x) = \varnothing .$$

The destinations are exactly the masks that contain every bit of $m(x)$; the sources are exactly the masks that contain none of them. Those two families are disjoint, so a mask written during this sweep is never read as a source during the same sweep and no value can be reused. Sweeping the destinations in decreasing numeric order is the conventional way to make that property explicit.

Seeding with $f[0] = 2^{c_1} = 2^2 = 4$ and applying the two sweeps:

| Sweep stage | $f[0]$ | $f[1]$ | $f[2]$ | $f[3]$ | $\sum_S f[S]$ |
|---|---|---|---|---|---|
| seed with $2^{c_1} = 2^2$ | 4 | 0 | 0 | 0 | 4 |
| after value `2`, mask $1$, $c_2 = 1$ | 4 | 4 | 0 | 0 | 8 |
| after value `6`, mask $3$, $c_6 = 1$ | 4 | 4 | 0 | 4 | 12 |

Reading the two sweeps in detail:

- **Sweeping `2`** (support $\{2\}$): the only occupied source is $S = 0$, which is disjoint from the mask, so $f[1]$ receives $c_2 \cdot f[0] = 1 \cdot 4 = 4$. The four ones-only subsets may each be augmented by the position holding `2`. Masks $2$ and $3$ stay at $0$ because no selected value has produced prime $3$.
- **Sweeping `6`** (support $\{2,3\}$, mask $3$): $S = 0$ is still disjoint and contributes $f[3] = 1 \cdot 4 = 4$. But $S = 1$ is *not* disjoint — bit $0$ is already claimed by the value `2` — so `6` is refused as an extension of that family. This is exactly the incompatibility the problem is built on.

Every mask at the end holds a count of subsets, and exactly one of the counted subsets is the empty subset, which is not a square-free *non-empty* subset:

$$\text{answer} = \left( \sum_{S} f[S] \right) - 1 = 12 - 1 = 11 .$$

The same arithmetic, grouped by which non-one values were selected, makes the conflict concrete. Positions are indexed `0`, `1`, `2`, `3` for the values `1`, `1`, `2`, `6`:

| Selection of the non-one positions | Index subsets | Product support | Admissible |
|---|---|---|---|
| neither `2` nor `6` | $\varnothing$, `{0}`, `{1}`, `{0,1}` | $\varnothing$ | yes, 4 subsets |
| `2` only, with any sub-choice of the ones | `{2}`, `{0,2}`, `{1,2}`, `{0,1,2}` | $\{2\}$ | yes, 4 subsets |
| `6` only, with any sub-choice of the ones | `{3}`, `{0,3}`, `{1,3}`, `{0,1,3}` | $\{2,3\}$ | yes, 4 subsets |
| `2` and `6` together, with any sub-choice of the ones | `{2,3}`, `{0,2,3}`, `{1,2,3}`, `{0,1,2,3}` | $\{2,2,3\}$ | no, $4 \mid 12$ |

Four admissible groups of four, of which the first group contains the empty subset, give $4 + 4 + 4 - 1 = 11$ — the same figure the table of $f$ values produced.

## 5. Why the reasoning is correct

The invariant maintained after each sweep is:

> Once every usable value $y$ with $2 \le y < x$ has been swept, $f[S]$ equals the number of index subsets drawn from the positions holding `1` or a value below $x$ whose product has prime support exactly $S$.

It holds initially because before any sweep the only selectable positions are the $c_1$ ones, and there are $2^{c_1}$ ways to choose some of them, all realizing $S = 0$ and all counted in $f[0]$.

For the inductive step, consider the sweep of $x$. New index subsets either avoid every position holding $x$ — already counted by the inductive hypothesis — or select exactly one such position, since selecting two positions with the same value $x \ge 2$ repeats every prime in $m(x)$. A subset that selects a position of value $x$ is admissible exactly when the rest of the subset is admissible and its support $S$ is disjoint from $m(x)$, and its resulting support is then $S \cup m(x)$. For each such $S$ there are $c_x$ choices of the position, and the admissible subsets of the rest are counted by $f[S]$, so the update adds precisely $c_x \cdot f[S]$ to $f[S \cup m(x)]$ and nothing else. Because destinations contain $m(x)$ while sources avoid it, no entry is both a source and a destination within one sweep, so each new subset is counted exactly once and the invariant is restored.

Completeness follows from the same bijection read backwards: any square-free non-empty index subset determines a set of ones, which is free, and a set of non-one values whose supports are pairwise disjoint; the sweep order visits those values in increasing order, so the subset is counted in the state equal to the union of their supports. Summing $f[S]$ over all $1024$ masks therefore counts every square-free index subset exactly once, including the empty one, and subtracting $1$ removes exactly that single empty subset. Since subsets are distinguished by the chosen indices rather than by the chosen values, two positions holding the same value must be counted as two separate choices — which is why the multiplicity $c_x$ multiplies instead of being ignored.

## 6. Traps this instance exposes

| Trap | What it looks like on this instance | Correct treatment |
|---|---|---|
| Assuming individually legal elements combine legally | `2` alone and `6` alone are both square-free, yet `[2,6]` has product $12 = 2^2 \cdot 3$ | Check compatibility between supports before selecting, never the individual elements alone |
| Missing an intrinsic square factor | a value such as `4`, `9`, or `25` can never be rescued by any companion | Exclude such values from the sweep entirely, as if $c_x = 0$ |
| Treating equal values as one single choice | three copies of `2` produce `3` singleton subsets, not `1` | Multiply by $c_x$ once per distinct value |
| Charging `1` against the prime budget | `1` occupies no bit, so any number of ones may be taken | Seed $f[0]$ with the free factor $2^{c_1}$ |
| Reusing a value inside its own sweep | reading back a mask just written would let `2` be taken twice | Keep sources, which avoid $m(x)$, disjoint from destinations, which contain it |
| Forgetting the empty subset | $\sum_S f[S] = 12$ here, but the required answer is `11` | Subtract exactly one, the subset that deletes every element |
| Doing exact big-integer arithmetic | a long all-ones input has $2^{32}$ subsets, far beyond a machine integer | Reduce every addition and the seed $2^{c_1}$ modulo $10^9 + 7$ |

The instance's arithmetic can be cross-checked against boundary inputs whose outcomes isolate one idea each:

| Input | Expected output | Why the method produces it |
|---|---|---|
| `[3, 4, 4, 5]` | `3` | `4` is unusable; supports $\{3\}$ and $\{5\}$ are disjoint, giving `3`, `5`, `15` |
| `[2, 3, 5]` | `7` | three mutually disjoint supports, so all $2^3 - 1$ non-empty subsets qualify |
| `[1]` | `1` | $f[0] = 2^1$, minus the empty subset |
| `[4]` | `0` | every value is unusable, $f[0] = 2^0 = 1$, and $1 - 1 = 0$ |
| `[2, 2, 2]` | `3` | one distinct value with $c_2 = 3$, so three singleton choices |
| `[6, 10, 15]` | `3` | every pair shares a prime ($2$, $3$, $5$ respectively), so only the three singletons survive |
| `[1, 1, 4, 9, 25]` | `3` | $2^2 - 1$, with every unusable value skipped |
| `[1, 1, 2, 6]` | `11` | the full trace above |
| thirty-two copies of `1` | `294967267` | $2^{32} - 1 \pmod{10^9 + 7}$, since every non-empty subset of ones is square-free |

## 7. Time and auxiliary space

Let $P = 10$ be the number of primes that can divide a value of at most $30$, and $M = 2^{P} = 1024$ the number of masks.

- Counting occurrences costs one pass over the input: $O(n)$.
- Each usable value triggers one sweep over all $M$ masks, and at most $30$ distinct values exist in range, so the sweeps cost $O(30 \cdot 2^{10})$ elementary operations. Deriving a value's mask by testing the ten primes is $O(10)$ per distinct value.
- The total running time is $O(n + 30 \cdot 2^{10})$, whose second term is effectively constant. The length constraint $\texttt{nums.length} \le 1000$ is therefore never the binding one; the ceiling $\texttt{nums}[i] \le 30$ is, because it fixes the prime universe and hence the state space.
- Auxiliary space is the table itself, $O(2^{10})$ counts, plus the $O(30)$ table of values and multiplicities. No recursion, no per-value history, and no stored subsets are needed, because the multiplicities $c_x$ summarize everything the input contributes.

Notice how the input length enters the model only through those multiplicities: $n$ affects the exponent $2^{c_1}$ and each factor $c_x$, but never the size of the state space.
