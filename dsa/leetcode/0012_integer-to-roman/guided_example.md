# Guided Example: Integer to Roman

We trace the step-by-step greedy value decomposition on a representative integer instance:

- **Input:** $\text{num} = 3749$
- **Required output:** $\text{"MMMDCCXLIX"}$

This instance demonstrates thousands accumulation, hundreds expansion with subtractive transitions, tens sub-boundaries, and units resolution according to standard canonical Roman numeral conventions.

---

## 1. Instance & Teaching Goal

Roman numerals are formed by combining seven base symbols and six subtractive pairs:

| Value | Symbol / Pair | Value | Symbol / Pair |
|:---:|:---:|:---:|:---:|
| 1000 | `M` | 900 | `CM` |
| 500 | `D` | 400 | `CD` |
| 100 | `C` | 90 | `XC` |
| 50 | `L` | 40 | `XL` |
| 10 | `X` | 9 | `IX` |
| 5 | `V` | 4 | `IV` |
| 1 | `I` | | |

The objective is to convert $\text{num} = 3749$ into its unique canonical representation $\text{"MMMDCCXLIX"}$ without creating invalid subtractive pairings (such as $\text{"IL"}$ for $49$).

A naive approach splits numbers into decimal place values using separate nested branches. The optimal method maintains all 13 base and subtractive symbols in descending value order, greedily subtracting the largest applicable symbol until the remaining value reaches $0$.

---

## 2. Conceptual Foundation & Invariants

### Greedy Coin-Change Analogy
The problem can be modeled as a greedy coin-change system with 13 fixed denominations:
$$
V = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
$$
$$
S = [\text{"M"}, \text{"CM"}, \text{"D"}, \text{"CD"}, \text{"C"}, \text{"XC"}, \text{"L"}, \text{"XL"}, \text{"X"}, \text{"IX"}, \text{"V"}, \text{"IV"}, \text{"I"}]
$$

Because Roman numerals strictly partition each decimal place ($1000$s, $100$s, $10$s, $1$s), the standard system has the canonical greedy-choice property:
- Always taking the largest denomination $V[k] \le \text{remainder}$ produces the minimal number of symbols and exactly matches standard Roman positional grammar.
- Subtracting $V[k]$ leaves a remainder strictly smaller than the next higher boundary.

> **Invariant.** At each step, $\text{num} = \text{Value}(\text{accumulated string}) + \text{remainder}$, and all appended symbols appear in strictly non-increasing denomination rank.

---

## 3. Step-by-Step Worked Execution

We process $\text{num} = 3749$ across the 13 canonical denominations in descending order:

### 1. Denomination 1000 (`M`)
- Check fit: $\lfloor 3749 / 1000 \rfloor = 3$.
- Append `'M'` three times: $\text{"MMM"}$.
- Deduct value: $3749 - 3000 = 749$.
- Remainder: $749$.

### 2. Denomination 900 (`CM`)
- Check fit: $749 < 900$.
- Skip denomination. Remainder: $749$.

### 3. Denomination 500 (`D`)
- Check fit: $\lfloor 749 / 500 \rfloor = 1$.
- Append `'D'`: $\text{"MMMD"}$.
- Deduct value: $749 - 500 = 249$.
- Remainder: $249$.

### 4. Denomination 400 (`CD`)
- Check fit: $249 < 400$.
- Skip denomination. Remainder: $249$.

### 5. Denomination 100 (`C`)
- Check fit: $\lfloor 249 / 100 \rfloor = 2$.
- Append `'C'` twice: $\text{"MMMDCC"}$.
- Deduct value: $249 - 200 = 49$.
- Remainder: $49$.

### 6. Denominations 90 (`XC`) and 50 (`L`)
- Check fit: $49 < 90$ and $49 < 50$.
- Skip both. Remainder: $49$.

### 7. Denomination 40 (`XL`)
- Check fit: $\lfloor 49 / 40 \rfloor = 1$.
- Append $\text{"XL"}$: $\text{"MMMDCCXL"}$.
- Deduct value: $49 - 40 = 9$.
- Remainder: $9$.

### 8. Denomination 10 (`X`)
- Check fit: $9 < 10$.
- Skip denomination. Remainder: $9$.

### 9. Denomination 9 (`IX`)
- Check fit: $\lfloor 9 / 9 \rfloor = 1$.
- Append $\text{"IX"}$: $\text{"MMMDCCXLIX"}$.
- Deduct value: $9 - 9 = 0$.
- Remainder: $0$.

### 10. Remaining Denominations (5, 4, 1)
- Remainder is $0$; all remaining denominations are bypassed.

---

## 4. Complete Execution Trace

| Denomination Value | Roman Token | Remainder Before | Multiplicity ($\lfloor \text{rem} / V \rfloor$) | Value Deducted | Resulting String Buffer | Remainder After |
|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| 1000 | `M` | 3749 | 3 | 3000 | $\text{"MMM"}$ | 749 |
| 900 | `CM` | 749 | 0 | 0 | $\text{"MMM"}$ | 749 |
| 500 | `D` | 749 | 1 | 500 | $\text{"MMMD"}$ | 249 |
| 400 | `CD` | 249 | 0 | 0 | $\text{"MMMD"}$ | 249 |
| 100 | `C` | 249 | 2 | 200 | $\text{"MMMDCC"}$ | 49 |
| 90 | `XC` | 49 | 0 | 0 | $\text{"MMMDCC"}$ | 49 |
| 50 | `L` | 49 | 0 | 0 | $\text{"MMMDCC"}$ | 49 |
| 40 | `XL` | 49 | 1 | 40 | $\text{"MMMDCCXL"}$ | 9 |
| 10 | `X` | 9 | 0 | 0 | $\text{"MMMDCCXL"}$ | 9 |
| 9 | `IX` | 9 | 1 | 9 | $\text{"MMMDCCXLIX"}$ | **0** |
| 5 | `V` | 0 | 0 | 0 | $\text{"MMMDCCXLIX"}$ | 0 |
| 4 | `IV` | 0 | 0 | 0 | $\text{"MMMDCCXLIX"}$ | 0 |
| 1 | `I` | 0 | 0 | 0 | $\text{"MMMDCCXLIX"}$ | 0 |

---

## 5. Algorithmic Correctness

**Soundness.** Every subtractive combination (`CM`, `CD`, `XC`, `XL`, `IX`, `IV`) is explicitly included in the denomination list. By predefining these composite tokens, greedy subtraction treats composite symbols as atomic values, preventing illegal non-standard forms like `IIII` (4) or `IC` (99). The final string evaluates numerically to the exact input integer.

**Completeness.** Since the smallest denomination is $1$ (`I`), any positive integer remainder can always be resolved to $0$. Under the constraint $1 \le \text{num} \le 3999$, the algorithm terminates in a finite number of steps with an exact zero remainder.

---

## 6. Traps This Instance Exposes

- **Illegal Subtractive Combinations:** Roman subtractive rules only permit powers of 10 to precede the next two higher symbols (e.g. $I$ before $V$ or $X$; $X$ before $L$ or $C$; $C$ before $D$ or $M$). Writing $49$ as $IL$ ($50 - 1$) is strictly forbidden; it must be decomposed place by place as $40 + 9 = \text{"XL"} + \text{"IX"} = \text{"XLIX"}$.
- **Repetition Limits:** No symbol may be repeated four times consecutively. The 13-token table inherently avoids four consecutive identical symbols because $4$ and $9$ in every power of 10 are represented by subtractive pairs ($4 \to \text{"IV"}$, $9 \to \text{"IX"}$, $40 \to \text{"XL"}$, $90 \to \text{"XC"}$, $400 \to \text{"CD"}$, $900 \to \text{"CM"}$).

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$. There are 13 fixed denominations. In the worst case ($3888 = \text{"MMMDCCCLXXXVIII"}$), the algorithm appends at most 15 characters. Because the number of steps is strictly bounded by a constant for all inputs $\le 3999$, the runtime is $O(1)$.
- **Auxiliary Space Complexity:** $O(1)$. Memory consumption is bounded by the static 13-denomination lookup tables and an output string of length at most 15.
