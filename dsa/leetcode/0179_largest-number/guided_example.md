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

---

## 5. Algorithmic Correctness

**Soundness.** Suppose an optimal string $S^*$ had an adjacent pair $A B$ where $A + B < B + A$. Swapping $A$ and $B$ to $B A$ strictly increases the numerical value of the substring $A B$, while leaving the prefix before $A$ and the suffix after $B$ unchanged. This contradicts the optimality of $S^*$. Therefore, every adjacent pair must satisfy $A + B \ge B + A$.

**Completeness.** Since the relation $A \succ B \iff \frac{A}{10^{l(A)} - 1} > \frac{B}{10^{l(B)} - 1}$ is a strict total order, comparison-based sorting algorithms (such as Timsort) are guaranteed to find the unique global maximum without cycles.

---

## 6. Traps This Instance Exposes

- **The Multiple Zeroes Trap:** If $\text{nums} = [0, 0]$, naive concatenation produces `"00"`. Check `if result[0] == '0': return "0"`.
- **The Prefix Trap ($3$ vs $30$):** Naive alphabetical sorting or integer sorting misorders $3$ and $30$. Concatenation testing $330 > 303$ handles arbitrary length differences without manual prefix alignment.
- **Python 3 `cmp_to_key`:** Python 3's `sort()` only accepts a unary `key` function. Using `functools.cmp_to_key` allows passing a binary comparator `lambda a, b: -1 if a + b > b + a else (1 if a + b < b + a else 0)`.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N \log N \cdot L)$, where $N$ is the number of integers in `nums` and $L$ is the maximum number of digits in an element ($L \le 10$ for 32-bit integers). Sorting performs $O(N \log N)$ comparisons, each requiring $O(L)$ string concatenation and comparison.
- **Auxiliary Space Complexity:** $O(N \cdot L)$ auxiliary memory to store the string representations and the final joined result.
