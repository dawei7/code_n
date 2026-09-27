# Guided Example: Largest Number

We trace the step-by-step pairwise concatenation ordering, total-order transitivity proof, and zero-normalization on representative integer arrays:

- **Input:** $\text{nums} = [3, 30, 34, 5, 9]$
- **Required output:** `"9534330"` (Arranged in order $[9, 5, 34, 3, 30]$)
- **All-Zeroes Edge Instance:** $\text{nums} = [0, 0] \implies \text{"0"}$ (Must not return `"00"`)
- **Prefix Reversal Instance:** $\text{nums} = [10, 2] \implies \text{"210"}$ ($210 > 102$)

This instance demonstrates custom comparison sorting via concatenation duality ($A + B \gtrless B + A$), proves why standard numeric or lexicographic sort fails on prefix collisions (e.g. $3$ vs $30$), establishes transitivity via periodic fractional expansion, and operates in $O(N \log N \cdot L)$ time.

---

## 1. Instance & Teaching Goal

Given a list of non-negative integers:
$$
\text{nums} = [3, 30, 34, 5, 9]
$$
Arrange them such that their concatenated decimal representation forms the mathematically largest possible integer:
$$
\mathbf{\text{"9534330"}}
$$

Standard sorting strategies fail:
1. **Numeric Descending Sort:**
   $34 > 9 \implies$ would place $34$ before $9$, giving $349\dots$, whereas $934\dots$ is strictly larger.
2. **Standard Lexicographical Sort:**
   Comparing `"3"` vs `"30"` lexicographically yields $\text{"30"} > \text{"3"}$ in some implementations (or $\text{"3"} < \text{"30"}$), producing `"303"`.
   However, concatenating $3$ before $30$ yields $330$, which is strictly greater than $303$ ($330 > 303$).

To guarantee that the concatenated number is globally maximized:
For any two numbers $A$ and $B$, evaluate their order by comparing their two possible concatenations:
$$
A \succ B \iff A + B > B + A
$$
Because both strings $A + B$ and $B + A$ have identical length, direct lexicographical comparison is equivalent to numerical comparison.

---

## 2. Conceptual Foundation & Invariants

### The Concatenation Ordering Protocol
Let $a$ and $b$ be the string representations of two integers.
Define the comparator:
$$
\text{cmp}(a, b) =
\begin{cases}
-1 & \text{if } a + b > b + a \quad (a \text{ precedes } b) \\
1 & \text{if } a + b < b + a \quad (b \text{ precedes } a) \\
0 & \text{if } a + b == b + a \quad (\text{equivalent})
\end{cases}
$$

### Mathematical Proof of Transitivity (Total Order)
Does $A \succ B$ and $B \succ C$ guarantee $A \succ C$?
Let $l(X)$ denote the number of digits in $X$.
The concatenation $A + B$ numerically evaluates to:
$$
A \cdot 10^{l(B)} + B
$$
The inequality $A + B > B + A$ is equivalent to:
$$
A \cdot 10^{l(B)} + B > B \cdot 10^{l(A)} + A \iff A(10^{l(B)} - 1) > B(10^{l(A)} - 1) \iff \frac{A}{10^{l(A)} - 1} > \frac{B}{10^{l(B)} - 1}
$$
Notice that $\frac{X}{10^{l(X)} - 1}$ is the exact repeating decimal fraction $0.\overline{X} = 0.XXXX\dots$!
Because real number comparison $>$ over infinite periodic decimals is a strict total order, the concatenation relation is:
1. **Transitive:** If $A \succ B$ and $B \succ C$, then $A \succ C$.
2. **Antisymmetric & Irreflexive.**
Therefore, sorting $\text{nums}$ using this comparator yields the unique global optimum!

### The Sort Order as a Ranking of Repeating Decimals

The transitivity argument becomes concrete once each element is replaced by its real-valued key. Every element of the traced instance maps to a repeating decimal, and the correct order is exactly the descending order of those values:

| Element $X$ | Digits $l(X)$ | Key $\frac{X}{10^{l(X)} - 1}$ | Repeating decimal | Rank in the answer |
|:---:|:---:|:---:|:---:|:---:|
| 9 | 1 | $9 / 9 = 1$ | $0.\overline{9}$ | 1 |
| 5 | 1 | $5 / 9$ | $0.\overline{5} = 0.5555\dots$ | 2 |
| 34 | 2 | $34 / 99$ | $0.\overline{34} = 0.3434\dots$ | 3 |
| 3 | 1 | $3 / 9 = 1/3$ | $0.\overline{3} = 0.3333\dots$ | 4 |
| 30 | 2 | $30 / 99 = 10/33$ | $0.\overline{30} = 0.3030\dots$ | 5 |

This table explains the instance's decisive comparison without any concatenation at all. The key for $34$ is $0.3434\dots$ while the key for $3$ is $0.3333\dots$, so $34$ precedes $3$ by a margin of only about $0.0101$; and $3$ precedes $30$ because $0.3333\dots > 0.3030\dots$. Two elements with the same key, such as two copies of $8308$, are interchangeable, which is why the comparator may report them as equivalent.

### Normalization Gating (All-Zeroes Trap)
If $\text{nums} = [0, 0, 0]$, sorting yields `['0', '0', '0']`.
Concatenating gives `"000"`, which is not a standard integer string.
If the leading character of the sorted concatenation is `'0'`, the entire number must be collapsed to `"0"`.

> **Invariant.** In the sorted array, no adjacent pair $(A, B)$ can be swapped to increase the total number. Since any permutation can be achieved via adjacent swaps, the sorted sequence achieves the global maximum.

---

## 3. Step-by-Step Worked Execution

We trace the sorting on $\text{nums} = [3, 30, 34, 5, 9]$:

### Step 1: String Conversion
Convert to string representations:
$$
S = [\text{"3"}, \text{"30"}, \text{"34"}, \text{"5"}, \text{"9"}]
$$

---

### Step 2: Pairwise Concatenation Comparisons
1. **Compare `"9"` with `"5"`:**
   - $9 + 5 = \text{"95"}$
   - $5 + 9 = \text{"59"}$
   - $\text{"95"} > \text{"59"} \implies \mathbf{\text{"9"} \succ \text{"5"}}$.
2. **Compare `"5"` with `"34"`:**
   - $5 + 34 = \text{"534"}$
   - $34 + 5 = \text{"345"}$
   - $\text{"534"} > \text{"345"} \implies \mathbf{\text{"5"} \succ \text{"34"}}$.
3. **Compare `"34"` with `"3"`:**
   - $34 + 3 = \text{"343"}$
   - $3 + 34 = \text{"334"}$
   - $\text{"343"} > \text{"334"} \implies \mathbf{\text{"34"} \succ \text{"3"}}$.
4. **Compare `"3"` with `"30"` (The Classic Trap):**
   - $3 + 30 = \text{"330"}$
   - $30 + 3 = \text{"303"}$
   - $\text{"330"} > \text{"303"} \implies \mathbf{\text{"3"} \succ \text{"30"}}$.

---

### Step 3: Sorted Array
Sorting with comparator yields:
$$
S_{\text{sorted}} = [\text{"9"}, \, \text{"5"}, \, \text{"34"}, \, \text{"3"}, \, \text{"30"}]
$$

---

### Step 4: Concatenation and Zero Normalization
- Concatenate strings:
  $$
  \text{"9"} + \text{"5"} + \text{"34"} + \text{"3"} + \text{"30"} = \mathbf{\text{"9534330"}}
  $$
- Leading character is `'9'` ($\ne \text{'0'}$), no zero normalization needed.
- Return $\mathbf{\text{"9534330"}}$.

---

## 4. Complete Execution Trace

```text
Elements: 3, 30, 34, 5, 9

Comparison Tests:
  "9" vs "5":   95 > 59   -> "9" precedes "5"
  "5" vs "34":  534 > 345 -> "5" precedes "34"
  "34" vs "3":  343 > 334 -> "34" precedes "3"
  "3" vs "30":  330 > 303 -> "3" precedes "30"

Sorted Order: ["9", "5", "34", "3", "30"]
Concatenated Result: "9534330"
```

| Pair $(A, B)$ | Concatenation $A + B$ | Concatenation $B + A$ | Comparison $A+B \gtrless B+A$ | Preferred Precedence |
|:---:|:---:|:---:|:---:|:---:|
| $(9, 5)$ | `"95"` | `"59"` | $\text{"95"} > \text{"59"}$ | $9 \succ 5$ |
| $(5, 34)$ | `"534"` | `"345"` | $\text{"534"} > \text{"345"}$ | $5 \succ 34$ |
| $(34, 3)$ | `"343"` | `"334"` | $\text{"343"} > \text{"334"}$ | $34 \succ 3$ |
| **$(3, 30)$** | **`"330"`** | **`"303"`** | **$\text{"330"} > \text{"303"}$** | **$3 \succ 30$** |

The four comparisons above are the ones the sorted order makes visible. A comparison sort is only trustworthy on this instance if *every* pair agrees with the final order, so the complete verdict set is worth recording — these are all ten unordered pairs, and each one points the same direction as the sorted sequence, which is what rules out a cyclic comparator:

| Unordered pair | $A + B$ | $B + A$ | Larger concatenation | Verdict | Positions in the answer |
|:---:|:---:|:---:|:---|:---|:---|
| $(9, 5)$ | `"95"` | `"59"` | `"95"` | $9 \succ 5$ | 1 and 2 |
| $(9, 34)$ | `"934"` | `"349"` | `"934"` | $9 \succ 34$ | 1 and 3 |
| $(9, 3)$ | `"93"` | `"39"` | `"93"` | $9 \succ 3$ | 1 and 4 |
| $(9, 30)$ | `"930"` | `"309"` | `"930"` | $9 \succ 30$ | 1 and 5 |
| $(5, 34)$ | `"534"` | `"345"` | `"534"` | $5 \succ 34$ | 2 and 3 |
| $(5, 3)$ | `"53"` | `"35"` | `"53"` | $5 \succ 3$ | 2 and 4 |
| $(5, 30)$ | `"530"` | `"305"` | `"530"` | $5 \succ 30$ | 2 and 5 |
| $(34, 3)$ | `"343"` | `"334"` | `"343"` | $34 \succ 3$ | 3 and 4 |
| $(34, 30)$ | `"3430"` | `"3034"` | `"3430"` | $34 \succ 30$ | 3 and 5 |
| $(3, 30)$ | `"330"` | `"303"` | `"330"` | $3 \succ 30$ | 4 and 5 |

Every pair resolves to one of the two elements, never to a tie, so on this instance the comparator induces a strict ranking $9 \succ 5 \succ 34 \succ 3 \succ 30$. Note that the table contains comparisons the sort never had to perform explicitly, such as $(9, 30)$ and $(5, 3)$; their agreement with the final order is the empirical shadow of the transitivity proved above.

---

## 5. Algorithmic Correctness

**Soundness.** Suppose an optimal string $S^*$ had an adjacent pair $A B$ where $A + B < B + A$. Swapping $A$ and $B$ to $B A$ strictly increases the numerical value of the substring $A B$, while leaving the prefix before $A$ and the suffix after $B$ unchanged. This contradicts the optimality of $S^*$. Therefore, every adjacent pair must satisfy $A + B \ge B + A$.

**Completeness.** Since the relation $A \succ B \iff \frac{A}{10^{l(A)} - 1} > \frac{B}{10^{l(B)} - 1}$ is a strict total order, comparison-based sorting algorithms (such as Timsort) are guaranteed to find the unique global maximum without cycles.

---

## 6. Traps This Instance Exposes

- **The Multiple Zeroes Trap:** If $\text{nums} = [0, 0]$, naive concatenation produces `"00"`. Check `if result[0] == '0': return "0"`.
- **The Prefix Trap ($3$ vs $30$):** Naive alphabetical sorting or integer sorting misorders $3$ and $30$. Concatenation testing $330 > 303$ handles arbitrary length differences without manual prefix alignment.
- **Python 3 `cmp_to_key`:** Python 3's `sort()` only accepts a unary `key` function. Using `functools.cmp_to_key` allows passing a binary comparator `lambda a, b: -1 if a + b > b + a else (1 if a + b < b + a else 0)`.

### Boundary Instances the Comparator Must Survive

The traced instance contains no zero and no duplicate, so the two failure modes that actually break submitted solutions are absent from it. They are worth tabulating against the authored cases:

| Instance | Sorted order produced | Required result | Why this instance is the one that catches the bug |
|:---|:---|:---|:---|
| `[0, 0]` | `["0", "0"]` | `"0"` | every pair ties under the comparator, so the join begins with `'0'` and the entire answer must be collapsed to a single zero instead of `"00"` |
| `[10, 2]` | `["2", "10"]` | `"210"` | numeric descending order would emit `"102"`; the concatenation test moves the shorter `"2"` ahead of `"10"` |
| `[12, 121]` | `["12", "121"]` | `"12121"` | one string is a prefix of the other, and the *shorter* one leads because `"12" + "121" = "12121"` beats `"121" + "12" = "12112"`; intuition about the longer prefix is exactly what misleads here |
| `[8308, 8308, 830]` | `["8308", "8308", "830"]` | `"83088308830"` | equal elements tie, so the comparator may leave them in either relative order, and the prefix rule still places `830` after both copies |
| `[7]` | `["7"]` | `"7"` | with a single element there is nothing to compare, but the zero-normalization guard still reads the first character and must not fire |

The first row is the only one where the join itself is invalid rather than merely suboptimal: `"00"` is not the decimal representation of any integer, so the guard is a correctness condition, not a cosmetic cleanup.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N \log N \cdot L)$, where $N$ is the number of integers in `nums` and $L$ is the maximum number of digits in an element ($L \le 10$ for 32-bit integers). Sorting performs $O(N \log N)$ comparisons, each requiring $O(L)$ string concatenation and comparison.
- **Auxiliary Space Complexity:** $O(N \cdot L)$ auxiliary memory to store the string representations and the final joined result.
