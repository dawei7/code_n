# Guided Example: Count Number of Distinct Integers After Reverse Operations

## 1. The Instance and the Operation Being Counted

The array `nums` holds positive integers. For every integer of the **original** array, its digits are reversed and the resulting integer is appended to the end of the array. Only the resulting array's number of distinct values is requested — not the array itself, and not the order in which the appended values land.

**Representative input.** `nums = [1, 13, 10, 12, 31]`

**Required output.** `6`

This five-element input is worth tracing because it contains all of the interesting set-growth cases at once: an original whose reversal collapses to a shorter number because of a trailing zero, two reversals that are already present as originals, and exactly one reversal that is genuinely new.

Let $O$ denote the set of distinct original values and let $r(x)$ denote the integer obtained by writing the decimal digits of $x$ in reverse order and reading the result as a number. If the originals are $x_1, \dots, x_n$, the distinct-value set of the final array is

$$
U = O \;\cup\; \{\, r(x_1),\, r(x_2),\, \dots,\, r(x_n) \,\}, \qquad \text{answer} = \lvert U \rvert .
$$

The contract bounds the input by $1 \le n \le 10^{5}$ and $1 \le \texttt{nums}[i] \le 10^{6}$, so a value carries at most seven decimal digits.

## 2. Reversal Is a Permutation of Digit Positions

Write a value $x$ with $m$ decimal digits as $d_{m-1} d_{m-2} \cdots d_0$, where $d_{m-1} \neq 0$ is the most significant digit and $d_0$ is the least significant one. Reversal moves each digit to the mirrored position:

$$
r(x) \;=\; \sum_{i=0}^{m-1} d_i \cdot 10^{\,m-1-i}.
$$

Two structural facts follow immediately. Reversal preserves the multiset of digits, so it also preserves the digit sum and hence the residue of the value modulo $9$. Reversal does **not** preserve the number of digits: a nonzero least significant digit keeps the length, while one or more trailing zeros become leading zeros whose positions are dropped when the result is read as a number.

| Original `x` | Digits, most significant first | Digit sequence reversed | Leading zeros dropped | Numeric reversal `r(x)` | Digits lost |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `1` | `1` | `1` | none | `1` | 0 |
| `13` | `1`, `3` | `3`, `1` | none | `31` | 0 |
| `10` | `1`, `0` | `0`, `1` | the `0` | `1` | 1 |
| `12` | `1`, `2` | `2`, `1` | none | `21` | 0 |
| `31` | `3`, `1` | `1`, `3` | none | `13` | 0 |

Row three is the decisive row of this instance. Reversal is therefore neither injective nor an involution over the positive integers: `10` and `1` both reverse to `1`, and reversing `10` twice yields `1` rather than `10`. Any reasoning that assumes reversal is its own inverse will mis-count inputs whose values end in zero.

## 3. The Union Invariant, and Why the Operation Is Not Recursive

The whole method rests on one accumulator invariant. Let $S_t$ be the accumulator after the first $t$ originals have been processed. Then

$$
S_t = O \;\cup\; \{\, r(x_1), \dots, r(x_t) \,\}, \qquad S_n = U .
$$

The invariant is maintained by two moves that never interact: the accumulator starts as $O$, and each original contributes exactly one additional candidate $r(x_t)$. Because a set ignores a value it already holds, every possible form of duplication collapses without special handling — repeated originals, repeated reversals, a reversal that coincides with an original, and palindromic values whose reversal is themselves.

Two bounds follow from the invariant. Since $U$ contains $O$, we have $\lvert U \rvert \ge \lvert O \rvert$; since $U$ is contained in the union of $n$ originals and $n$ reversals, we have $\lvert U \rvert \le 2n$. A trace that ends outside these bounds has made an arithmetic or bookkeeping mistake.

**Scope is part of the contract.** The reversal is applied to the original integers only, never to the values it appends. This is not a shortcut that merely saves work — it is what makes the task well defined. Applying reversal repeatedly to `12` would produce `21`, then `12` again, cycling forever; the one-pass reading guarantees exactly $n$ appended values and terminates unconditionally.

## 4. Step-by-Step Trace on the Chosen Instance

The initial accumulator is the set of distinct originals, $O = \{1, 10, 12, 13, 31\}$, whose size is $5$. Each row then contributes one reversal.

| Step `t` | Original `x_t` | Reversal `r(x_t)` | Already in the accumulator? | Accumulator size after | Member newly added |
|:---:|:---:|:---:|:---:|:---:|:---|
| 0 | — | — | — | 5 | — (`O = {1, 10, 12, 13, 31}`) |
| 1 | `1` | `1` | yes | 5 | none |
| 2 | `13` | `31` | yes | 5 | none |
| 3 | `10` | `1` | yes | 5 | none |
| 4 | `12` | `21` | no | 6 | `21` |
| 5 | `31` | `13` | yes | 6 | none |

The accumulator settles at $U = \{1, 10, 12, 13, 21, 31\}$, so the answer is `6`, which is exactly the expected output recorded for this input. Only step 4 grew the set; the other four reversals landed on values that were already present.

The same conclusion can be checked against the conceptual expanded array, which holds the five originals followed by the five appended reversals:

```text
expanded:  [1, 13, 10, 12, 31 | 1, 31, 1, 21, 13]
             \_____ originals _____/  \__ reversals __/
```

| Value | Occurrences in the expanded array | Source of each occurrence |
|:---:|:---:|:---|
| `1` | 3 | the original `1`, the reversal of `1`, and the reversal of `10` |
| `10` | 1 | the original `10` only; no reversal reaches it |
| `12` | 1 | the original `12` only; no reversal reaches it |
| `13` | 2 | the original `13` and the reversal of `31` |
| `21` | 1 | the reversal of `12` only |
| `31` | 2 | the original `31` and the reversal of `13` |

The occurrence counts total $3+1+1+2+1+2 = 10 = 2n$, confirming that the expanded array has exactly twice the input length while its distinct count is only six. The value `1` also illustrates that distinctness is a property of values, not of positions: it occupies three different slots and still counts once.

## 5. Correctness: Why the Accumulator Equals the Final Distinct Set

**Soundness.** Every element of $S_n$ is either an original value (inserted when the accumulator was seeded) or the reversal of some original occurrence (inserted while that occurrence was processed). In both cases the value appears in the final array by construction, so the accumulator contains nothing that the expanded array lacks.

**Completeness.** Conversely, every entry of the final array is either one of the originals or the reversal of one of the originals, because the operation produces exactly those $n$ appended values. Originals are all present from the seed, and the traversal visits every original occurrence, so each of the $n$ reversals is inserted at its own step. Nothing in the expanded array is left out.

Together, the two directions give $S_n = U$ as sets, so $\lvert S_n \rvert$ is precisely the number of distinct integers in the expanded array. The proof also shows why the expanded array never needs to exist in memory: it is $2n$ slots long, yet every question asked about it is answered by membership, and the accumulator retains only the distinct values.

## 6. Boundary and Trap Analysis

| Boundary situation | Instance | Result | Why the rule handles it |
|:---|:---|:---:|:---|
| Trailing zero shrinks the reversal | `[10]` | `2` | $r(10) = 1$, so $U = \{10, 1\}$; the two values have different digit lengths |
| Several originals collapse to one reversal | `[1000, 10, 1]` | `3` | the reversals are `1`, `1`, `1`; $U = \{1, 10, 1000\}$ and the $2n$ bound is far from tight |
| Palindromic value | `[121, 121]` | `1` | $r(121) = 121$, already in the seed, so the set never grows |
| Mutually reversing pair | `[71, 17]` | `2` | $r(71) = 17$ and $r(17) = 71$; the reversals reproduce the seed exactly |
| Repeated identical originals | `[2, 2, 2]` | `1` | the seed keeps one copy, and all three reversals are the same value |
| Every reversal is new | `[12, 34]` | `4` | $U = \{12, 21, 34, 43\}$; the union hits its $2n$ ceiling |
| Largest permitted value | `[1000000]` | `2` | seven digits reduce to a single digit: $r(1000000) = 1$ |
| Trailing zero on a multi-digit value | `[860]` | `2` | $r(860) = 68$; the dropped zero also shortens the number |
| Minimum length, single digit | `[7]` | `1` | a single digit is its own reversal, so no value is added |
| Recursion trap (rejected reading) | `[12]` | `2`, not a cycle | reversing appended results would oscillate `12 → 21 → 12`; the contract reverses originals only |

The subtlest row is the trailing-zero one, and the instance in section 1 exercises it at step 3: `10` reverses to `1`, which is already an original. A method that padded reversals back to a fixed width, or that treated the reversed digit string and the number as interchangeable, would count `01` as a separate value and over-report the answer.

## 7. Alternatives and Their Trade-offs

| Method | Time | Auxiliary space | Verdict |
|:---|:---:|:---:|:---|
| Seed with the originals, then insert every reversal | expected $O(nD)$ | $O(n)$ | the method derived in this lesson |
| Same union, but reverse digits arithmetically by repeated remainder and division | expected $O(nD)$ | $O(n) + O(1)$ | identical asymptotics with no digit strings; fewer temporary allocations |
| Materialise the expanded array and deduplicate it afterwards | $O(nD) + O(n)$ | $O(n)$ extra for a $2n$-element sequence | correct, but stores a redundant sequence the invariant proves unnecessary |
| Reverse only the distinct originals | expected $O(\lvert O\rvert D)$ | $O(n)$ | fewer reversals on duplicate-heavy input; needs a snapshot of the seed to avoid mutating the structure being traversed |
| Build the expanded array, sort it, then count adjacent distinct runs | $O(n \log n)$ with a digit factor | $O(n)$ | sorting buys nothing, because distinctness is a membership question rather than an ordering question |

The last row is the most instructive failure of instinct: counting distinct values feels like a sorting task, yet the seed-versus-append structure of this problem makes membership the natural operation and keeps the method linear. The arithmetic reversal alternative is worth knowing because it removes the per-value digit string entirely, at the cost of being slightly harder to read.

## 8. Time and Auxiliary-Space Complexity Derivation

Let $n = \lvert \texttt{nums} \rvert$ and let $D$ be the maximum number of decimal digits in any input value, so $D \le 7$ under the constraint `nums[i] <= 10**6`.

| Phase | Work performed | Cost |
|:---|:---|:---|
| Seed the accumulator | one insertion per original, duplicates collapse | expected $O(n)$ |
| Reverse each original | inspect and rewrite $O(D)$ digits per value | $O(nD)$ |
| Insert each reversal | one expected constant-time membership test and insertion per value | expected $O(nD)$ |
| Read the answer | the accumulator's size is maintained by the structure | $O(1)$ |
| **Time** | sum of the phases | **expected $O(nD)$, that is $O(n)$ for bounded $D$** |
| **Auxiliary space** | at most $2n$ distinct values in the accumulator, plus $O(D)$ reusable temporary digit storage | **$O(n)$** |

The digit factor is genuinely part of the cost, so it is worth stating explicitly rather than hiding it inside the hashing bound: reversal is not a constant-time operation on a number, since every digit must be moved. Under this problem's limits, however, $D \le 7$ is a fixed constant, which is why the bound is commonly quoted as $O(n)$. The set operations are expected constant time, so the total time is expected rather than worst case; the auxiliary space is dominated by the accumulator, which holds at most one value per original and at most one value per reversal, and the input array itself is never modified or extended.
