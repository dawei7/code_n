# Guided Example: Power of Four

We trace the step-by-step bitwise power-of-two validation ($n \ \& \ (n - 1) == 0$), odd-position bitmask filtering ($n \ \& \ \text{0xAAAAAAAA} == 0$), positive domain boundary checking ($n > 0$), and constant-time power-of-four identification on representative integer instances:

- **Input:** $n = 16$
- **Required output:** `true`
  - $16 > 0$ (Positivity condition holds)
  - $16 = 10000_2$, $15 = 01111_2 \implies 16 \ \& \ 15 = 0$ (Guarantees $n$ is a power of 2, $16 = 2^4$)
  - Bit position is $4$ (Even index, $4 = 2 \times 2 \implies 16 = 4^2$)
  - Mask check: $16 \ \& \ \text{0xAAAAAAAA} = 00010000_2 \ \& \ 10101010_2 = 0$ (No bits in odd positions)
  - All conditions met $\implies \text{true}$
- **Power of Two Counterexample:** $n = 8 = 2^3$:
  - $8 \ \& \ 7 = 0$ (Is a power of 2)
  - Set bit is at position $3$ (Odd index)
  - $8 \ \& \ \text{0xAAAAAAAA} = 8 \ne 0 \implies \text{false}$
- **Non-Power Counterexample:** $n = 5 = 101_2 \implies 5 \ \& \ 4 = 4 \ne 0 \implies \text{false}$
- **Zero Base Case:** $n = 0 \implies 0 > 0$ is false $\implies \text{false}$
- **Negative Integer Base Case:** $n = -16 \implies -16 > 0$ is false $\implies \text{false}$
- **Unit Base Case:** $n = 1 = 4^0 \implies 1 > 0$, $1 \ \& \ 0 = 0$, $1 \ \& \ \text{0xAAAAAAAA} = 0 \implies \text{true}$

This instance demonstrates constant-time bit manipulation classifications, mathematically proves why powers of four correspond exactly to powers of two with their single set bit in an even index, and achieves $O(1)$ time and $O(1)$ auxiliary space complexity.

---

## 1. Instance & Teaching Goal

Given an integer $n = 16$:
Determine whether $n$ is a power of four, meaning there exists an integer $x$ such that $n = 4^x$:

```text
Powers of Four:
4^0 = 1   = 0000 0001_2  (Bit 0 set, even)
4^1 = 4   = 0000 0100_2  (Bit 2 set, even)
4^2 = 16  = 0001 0000_2  (Bit 4 set, even)
4^3 = 64  = 0100 0000_2  (Bit 6 set, even)

Non-Powers of Four:
2^1 = 2   = 0000 0010_2  (Bit 1 set, ODD)
2^3 = 8   = 0000 1000_2  (Bit 3 set, ODD)
2^5 = 32  = 0010 0000_2  (Bit 5 set, ODD)
```

### The $O(1)$ Constant-Time Requirement
While repeatedly dividing by 4 takes $O(\log_4 N)$ operations, we can resolve the query in strictly **$O(1)$ constant time** using three bitwise predicates.

---

## 2. Conceptual Foundation & Invariants

An integer $n$ is a power of four ($n = 4^x = 2^{2x}$) if and only if:
1. **Positivity:** $n > 0$.
   Negative numbers and zero are not positive powers of four.
2. **Power of Two Property:** $(n \ \& \ (n - 1)) == 0$.
   Subtracting 1 from $n$ flips the lowest set bit and all lower zeros to ones.
   Taking the bitwise AND clears that bit:
   If $n$ had exactly one set bit, the result is $0$.
3. **Even Bit Position Filter:** $(n \ \& \ \text{0xAAAAAAAA}) == 0$.
   In a 32-bit signed integer, the hexadecimal constant $\text{0xAAAAAAAA}$ is:
   $$
   10101010101010101010101010101010_2
   $$
   It has set bits at all **odd** bit indices ($1, 3, 5, \dots, 31$).
   If $n$ is a power of four, its sole set bit is at an **even** index ($0, 2, 4, \dots, 30$), so it shares zero overlapping bits with $\text{0xAAAAAAAA}$.

> **Invariant.** An integer $n$ satisfies all three conditions simultaneously if and only if $n = 4^k$ for some non-negative integer $k$.

---

## 3. Step-by-Step Worked Execution

We trace the evaluation on $n = 16$:

---

### Step 1: Positivity Verification
- Check condition: $n > 0$.
  $$
  16 > 0 \implies \mathbf{\text{True}}
  $$

---

### Step 2: Power of Two Verification
- Binary representation:
  $$
  n = 16 = 0001 \; 0000_2
  $$
  $$
  n - 1 = 15 = 0000 \; 1111_2
  $$
- Bitwise AND:
  $$
  n \ \& \ (n - 1) = 0001 \; 0000_2 \ \& \ 0000 \; 1111_2 = \mathbf{0}
  $$
- Check condition: $(n \ \& \ (n - 1)) == 0 \implies \mathbf{\text{True}}$.
- *Deduction: $n$ has exactly one set bit and is a valid power of two ($16 = 2^4$).*

---

### Step 3: Odd-Position Mask Filtering
- Bitmask $\text{0xAAAAAAAA}$:
  $$
  \text{Mask} = 1010 \; 1010 \; 1010 \; 1010 \; 1010 \; 1010 \; 1010 \; 1010_2
  $$
- Bitwise AND with $n = 16$:
  $$
  16 \ \& \ \text{0xAAAAAAAA} = 0000 \; 0000 \; 0000 \; 0000 \; 0000 \; 0000 \; 0001 \; 0000_2 \ \& \ \dots \; 1010 \; 1010_2 = \mathbf{0}
  $$
- Check condition: $(n \ \& \ \text{0xAAAAAAAA}) == 0 \implies \mathbf{\text{True}}$.
- *Deduction: The single set bit is at position 4 (even), confirming that $n$ is an even power of two ($2^{2 \times 2} = 4^2$).*

---

### Step 4: Final Predicate Conjunction
All three boolean clauses evaluate to `True`:
$$
\text{True} \land \text{True} \land \text{True} = \mathbf{\text{True}}
$$

---

## 4. Complete Execution Trace

```text
Testing n = 16 (Binary: 0001 0000)
1. n > 0                       : 16 > 0           -> True
2. (n & (n - 1)) == 0          : 16 & 15 == 0     -> True (Power of 2)
3. (n & 0xAAAAAAAA) == 0       : 16 & 0xAA.. == 0 -> True (Even bit position 4)
Result: True

Testing n = 8 (Binary: 0000 1000)
1. n > 0                       : 8 > 0            -> True
2. (n & (n - 1)) == 0          : 8 & 7 == 0       -> True (Power of 2)
3. (n & 0xAAAAAAAA) == 0       : 8 & 0xAA.. == 8  -> False (Odd bit position 3)
Result: False
```

| Candidate $n$ | Binary Form | $n > 0$? | $n \ \& \ (n - 1)$ | Power of 2? | $n \ \& \ \text{0xAAAAAAAA}$ | Even Bit Position? | Final Output |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 16 | $0001 \; 0000_2$ | True | $0$ | Yes | $0$ | Yes (bit 4) | **`true`** |
| 8 | $0000 \; 1000_2$ | True | $0$ | Yes | $8 \ne 0$ | No (bit 3) | `false` |
| 5 | $0000 \; 0101_2$ | True | $4 \ne 0$ | No | - | - | `false` |
| 4 | $0000 \; 0100_2$ | True | $0$ | Yes | $0$ | Yes (bit 2) | **`true`** |
| 1 | $0000 \; 0001_2$ | True | $0$ | Yes | $0$ | Yes (bit 0) | **`true`** |
| 0 | $0000 \; 0000_2$ | False | - | - | - | - | `false` |
| -16 | Negative | False | - | - | - | - | `false` |

---

## 5. Algorithmic Correctness

**Soundness.** Since $4^x = 2^{2x}$, every power of four is a power of two whose unique set bit lies at index $2x$ (which is always an even index $\in \{0, 2, 4, 6, \dots\}$). The predicate $n \ \& \ (n - 1) == 0$ proves that $n = 2^k$ for some non-negative integer $k$. The predicate $n \ \& \ \text{0xAAAAAAAA} == 0$ proves that $k$ is not odd. Together with $n > 0$, these conditions uniquely characterize the set $\{4^0, 4^1, 4^2, \dots\}$.

**Completeness.** Any positive power of four $n = 4^x$ satisfies $n > 0$, has binary weight 1, and has its set bit at index $2x$. Thus, all valid powers of four evaluate all three checks to true, with zero false negatives.

---

## 6. Traps This Instance Exposes

- **Zero and $n \ \& \ (n - 1)$:** For $n = 0$, $n \ \& \ (n - 1) = 0 \ \& \ (-1) = 0$. Without the $n > 0$ check, 0 would falsely pass as a power of two.
- **Operator Precedence:** In Python, equality `==` has higher precedence than bitwise AND `&`. The expression `n & (n - 1) == 0` is parsed as `n & ((n - 1) == 0)`. Parenthesizing as `(n & (n - 1)) == 0` is mandatory.
- **Power of Two vs Power of Four:** Numbers like $2, 8, 32, 128$ are powers of two but NOT powers of four. The bitmask `0xAAAAAAAA` isolates odd positions to filter them out.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$. The solution performs three constant-time scalar bitwise operations and comparisons.
- **Auxiliary Space Complexity:** $O(1)$ constant auxiliary memory using zero additional data structures.
