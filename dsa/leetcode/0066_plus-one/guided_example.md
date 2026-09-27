# Guided Example: Plus One

We trace the step-by-step backward carry propagation on representative increment instances:

- **Cascade Carry Overflow:** $\text{digits} = [9, 9, 9] \implies [1, 0, 0, 0]$
- **Standard Terminal Case:** $\text{digits} = [1, 2, 9] \implies [1, 3, 0]$
- **Single-Digit Absorbed:** $\text{digits} = [4, 3, 2, 1] \implies [4, 3, 2, 2]$

This instance demonstrates in-place right-to-left decimal addition, terminating early when a digit does not overflow ($\text{digits}[i] \ne 9$), carry cascading across consecutive nines, and prepending a leading 1 when the entire array overflows.

---

## 1. Instance & Teaching Goal

Given a non-empty array of decimal digits representing a non-negative integer without leading zeros, increment the large integer by one and return the resulting array of digits.

Consider two contrasting behaviors:
1. **Early Absorbed Increment:** For $[1, 2, 9]$, adding 1 turns $9$ into $0$ with a carry. At the tens place, $2 + 1 = 3 < 10$. The carry is absorbed, returning $[1, 3, 0]$ immediately without touching leading digits.
2. **All-Nines Overflow:** For $[9, 9, 9]$, every digit rolls over to $0$. The carry exhausts the array bounds, requiring an additional leading digit: $[1, 0, 0, 0]$.

A naive approach converts the array to an integer, adds 1, and converts back to a string/list. However, in fixed-width integer environments (or where $N \le 100$), numbers exceed 64-bit bounds ($10^{100}$). The optimal algorithm mutates the array in place in $O(N)$ time and $O(1)$ space.

---

## 2. Conceptual Foundation & Invariants

### Right-to-Left Carry Algorithm
We iterate pointer $i$ backwards from the least significant digit $N - 1$ down to $0$:
1. **If $\text{digits}[i] < 9$:**
   - Increment: $\text{digits}[i] \leftarrow \text{digits}[i] + 1$.
   - The increment has been completely absorbed without generating a further carry.
   - Return $\text{digits}$ immediately.
2. **If $\text{digits}[i] == 9$:**
   - Roll over: $\text{digits}[i] \leftarrow 0$.
   - Carry continues to the left (next iteration $i - 1$).

### Global Array Overflow Case
If the loop completes without an early return, every digit in the original array was $9$ (e.g. $[9, 9, \dots, 9]$) and is now $0$.
- Prepend a leading $1$ to the array:
  $$
  \text{return } [1] + \text{digits}
  $$

> **Invariant.** Before index $i$, all positions to the right ($i + 1 \dots N - 1$) have been finalized to $0$, and a carry of $1$ is pending at index $i$.

---

## 3. Step-by-Step Worked Execution

### Case 1: All-Nines Overflow ($[9, 9, 9]$, $N = 3$)

- **Step 1 ($i = 2$, Units Place):**
  - $\text{digits}[2] = 9$.
  - Rollover: $\text{digits}[2] \leftarrow 0$. Carry continues left.
  - Array state: $[9, 9, \mathbf{0}]$.
- **Step 2 ($i = 1$, Tens Place):**
  - $\text{digits}[1] = 9$.
  - Rollover: $\text{digits}[1] \leftarrow 0$. Carry continues left.
  - Array state: $[9, \mathbf{0}, 0]$.
- **Step 3 ($i = 0$, Hundreds Place):**
  - $\text{digits}[0] = 9$.
  - Rollover: $\text{digits}[0] \leftarrow 0$. Carry continues left.
  - Array state: $[\mathbf{0}, 0, 0]$.
- **Post-Loop Processing:**
  - Loop finished with unabsorbed carry.
  - Prepend $1$: $[1] + [0, 0, 0] = [1, 0, 0, 0]$.
- Result: $[1, 0, 0, 0]$.

---

### Case 2: Partial Carry Cascade ($[1, 2, 9]$, $N = 3$)

- **Step 1 ($i = 2$):**
  - $\text{digits}[2] = 9 \implies \text{digits}[2] \leftarrow 0$.
  - Array state: $[1, 2, \mathbf{0}]$.
- **Step 2 ($i = 1$):**
  - $\text{digits}[1] = 2 < 9$.
  - Increment: $\text{digits}[1] \leftarrow 2 + 1 = 3$.
  - **Early Exit:** No carry generated! Return $[1, 3, 0]$ immediately.

---

## 4. Complete Execution Trace

### All-Nines Trace Table ($[9, 9, 9]$)

| Step | Index $i$ | Original Digit | Condition ($\text{val} < 9$) | Action Taken | Array State After Step | Status |
|:---:|:---:|:---:|:---:|:---|:---:|:---|
| 1 | 2 | 9 | False | Rollover to 0 | `[9, 9, 0]` | Carry continues |
| 2 | 1 | 9 | False | Rollover to 0 | `[9, 0, 0]` | Carry continues |
| 3 | 0 | 9 | False | Rollover to 0 | `[0, 0, 0]` | Loop terminates |
| Overflow | - | - | - | Prepend `[1]` | **`[1, 0, 0, 0]`** | **Final Output** |

### Comparison Across Input Types

| Input Array | Roll-overs Encountered | Terminating Index | Returned Array | Auxiliary Reallocation? |
|:---:|:---:|:---:|:---:|:---:|
| `[4, 3, 2, 1]` | 0 | $i = 3$ | `[4, 3, 2, 2]` | No (In-place) |
| `[1, 2, 9]` | 1 | $i = 1$ | `[1, 3, 0]` | No (In-place) |
| `[9]` | 1 | Post-loop | `[1, 0]` | Yes ($+1$ digit) |
| `[9, 9, 9]` | 3 | Post-loop | `[1, 0, 0, 0]` | Yes ($+1$ digit) |

---

## 5. Algorithmic Correctness

**Soundness.** Decimal addition adds 1 to the units place. If the digit is $< 9$, $d + 1 \le 9$ produces no carry, leaving all higher-order digits unchanged. If $d = 9$, $9 + 1 = 10$, setting the current digit to $0$ and carrying $1$ to position $i - 1$. This directly models arithmetic addition.

**Completeness.** The loop checks every position from $N - 1$ down to $0$. If all digits are $9$, prepending $1$ to an array of zeroes yields $10^N$, the exact value of $(10^N - 1) + 1$.

---

## 6. Traps This Instance Exposes

- **Integer Conversion Overflow:** In languages like Java or C++, converting `digits` to `long long` fails when $N > 18$ ($10^{18} > 2^{63}-1$). The array manipulation approach scales to arbitrary lengths.
- **Unnecessary Allocation on Non-Overflow Cases:** Pre-allocating a new list for every increment wastes memory; mutating `digits` in place and prepending `[1]` only upon total overflow achieves $O(1)$ extra memory for $> 99\%$ of cases.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$ worst case (when all digits are $9$). Best and average case is $O(1)$, since the units digit is $< 9$ in $9$ out of $10$ numbers, halting after a single step.
- **Auxiliary Space Complexity:** $O(1)$ in-place modification for normal cases, and $O(N)$ only when allocating the $(N+1)$-digit array upon all-nines overflow.
