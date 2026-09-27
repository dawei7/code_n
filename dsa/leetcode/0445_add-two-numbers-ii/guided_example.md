# Guided Example: Add Two Numbers II

We trace the step-by-step digit stack extraction (reversing order without mutating nodes), base-10 full-adder column-by-column addition, carry propagation ($\lfloor s / 10 \rfloor$), and head-prepending linked list construction on representative MSB-first numbers:

- **Input:**
  - $l_1 = 7 \to 2 \to 4 \to 3$ (Represents $7243$)
  - $l_2 = 5 \to 6 \to 4$ (Represents $564$)
- **Required output:** $7 \to 8 \to 0 \to 7$ (Represents $7243 + 564 = 7807$)
- **Execution trace:**
  - Phase 1: Populate LIFO stacks by traversing input lists:
    - Stack 1: $s_1 = [7, 2, 4, 3]$ (top is unit digit $3$)
    - Stack 2: $s_2 = [5, 6, 4]$ (top is unit digit $4$)
  - Phase 2: Pop and add with carry:
    - Initial state: $carry = 0, \; head = \text{None}$
    - **Position $10^0$ (Units):**
      - Digits: $d_1 = 3, d_2 = 4, carry = 0$
      - Sum: $3 + 4 + 0 = 7 \implies val = 7, carry = 0$
      - Prepend node: $7 \to \text{None}$
    - **Position $10^1$ (Tens):**
      - Digits: $d_1 = 4, d_2 = 6, carry = 0$
      - Sum: $4 + 6 + 0 = 10 \implies val = 0, carry = 1$
      - Prepend node: $0 \to 7 \to \text{None}$
    - **Position $10^2$ (Hundreds):**
      - Digits: $d_1 = 2, d_2 = 5, carry = 1$
      - Sum: $2 + 5 + 1 = 8 \implies val = 8, carry = 0$
      - Prepend node: $8 \to 0 \to 7 \to \text{None}$
    - **Position $10^3$ (Thousands):**
      - Digits: $d_1 = 7, d_2 = 0, carry = 0$
      - Sum: $7 + 0 + 0 = 7 \implies val = 7, carry = 0$
      - Prepend node: $7 \to 8 \to 0 \to 7 \to \text{None}$
  - Stacks empty and $carry = 0$. Terminate.
  - Final reconstructed head: $7 \to 8 \to 0 \to 7$
- **Carry Overflow Expanding Length:** $l_1 = [5], l_2 = [5] \implies 5 + 5 = 10 \implies [1, 0]$ (length increases from 1 to 2)
- **Zero Operands:** $l_1 = [0], l_2 = [0] \implies [0]$

This instance demonstrates LIFO stack inversion to align least significant digits without mutating the input linked lists, mathematically proves full-adder correctness, and derives $O(M + N)$ runtime and $O(M + N)$ space bounds.

---

## 1. Instance & Teaching Goal

Given two non-empty linked lists representing two non-negative integers:
The most significant digit (MSB) comes first, and each node contains a single decimal digit ($0 \dots 9$).
Add the two numbers and return the sum as a linked list in MSB-first order **without reversing the input lists**.

```text
Input Lists (MSB-first):
  l1:  ( 7 ) -> ( 2 ) -> ( 4 ) -> ( 3 )   [7243]
  l2:           ( 5 ) -> ( 6 ) -> ( 4 )   [ 564]

Alignment from Least Significant to Most Significant:
  Thousands (10^3):  7      = 7
  Hundreds  (10^2):  2 + 5  = 7 + 1 (carry) = 8
  Tens      (10^1):  4 + 6  = 10 -> digit 0, carry 1
  Units     (10^0):  3 + 4  = 7

Output List: ( 7 ) -> ( 8 ) -> ( 0 ) -> ( 7 )   [7807]
```

### The Alignment Challenge
Addition requires aligning numbers by their **least significant digit** (units place), because carries propagate from right to left (low power of 10 to high power of 10).
However, a singly linked list only permits forward traversal from MSB to LSB.
- **The Non-Mutating Stack Solution:** By pushing the digits of each list onto a LIFO stack, popping from the stacks yields digits in reverse order (units place first, then tens, then hundreds).
- As each sum digit is computed, prepending a new node to the front of the result list automatically builds the final MSB-first linked list without any list reversal steps.

---

## 2. Conceptual Foundation & Invariants

### 1. The Stack Inversion Mechanism:
- Traverse $l_1$, pushing every digit into stack $s_1$: $[d_{MSB}, \dots, d_{LSB}]$.
- Traverse $l_2$, pushing every digit into stack $s_2$: $[d'_{MSB}, \dots, d'_{LSB}]$.
- Popping elements from $s_1$ and $s_2$ yields $d_{LSB}$ and $d'_{LSB}$ first, perfectly aligning both numbers at their units digits regardless of length differences.

### 2. Full-Adder Decimal Transitions:
At each step while $s_1$ is not empty, $s_2$ is not empty, or $carry > 0$:
1. Pop $d_1 = s_1.\text{pop}()$ if $s_1$ non-empty, else $0$.
2. Pop $d_2 = s_2.\text{pop}()$ if $s_2$ non-empty, else $0$.
3. Compute total column sum:
   $$
   total = d_1 + d_2 + carry
   $$
4. Decompose:
   $$
   carry \leftarrow \lfloor total / 10 \rfloor, \quad digit \leftarrow total \pmod{10}
   $$
5. Prepend new node before current head:
   $$
   head \leftarrow \text{ListNode}(digit, \; next = head)
   $$

> **Prefix Prepending Invariant.** Creating each new node as the predecessor of the previous partial list builds the final linked list in strictly MSB-to-LSB order without reversing pointers.

---

## 3. Step-by-Step Worked Execution

We trace $l_1 = [7, 2, 4, 3]$ and $l_2 = [5, 6, 4]$:

---

### Step 1: Populate Stacks
- Read $l_1$: $s_1 = [7, 2, 4, 3]$. Size $= 4$.
- Read $l_2$: $s_2 = [5, 6, 4]$. Size $= 3$.
- Initialize: $carry = 0, \; head = \text{None}$.

---

### Step 2: Units Column ($10^0$)
- Pop $s_1$: $d_1 = 3$.
- Pop $s_2$: $d_2 = 4$.
- Carry: $0$.
- Sum: $3 + 4 + 0 = \mathbf{7}$.
- New carry: $\lfloor 7 / 10 \rfloor = \mathbf{0}$.
- Node value: $7 \pmod{10} = \mathbf{7}$.
- Prepend: $head = \text{ListNode}(7, \text{None}) \implies (7)$.

---

### Step 3: Tens Column ($10^1$)
- Pop $s_1$: $d_1 = 4$.
- Pop $s_2$: $d_2 = 6$.
- Carry: $0$.
- Sum: $4 + 6 + 0 = \mathbf{10}$.
- New carry: $\lfloor 10 / 10 \rfloor = \mathbf{1}$.
- Node value: $10 \pmod{10} = \mathbf{0}$.
- Prepend: $head = \text{ListNode}(0, head) \implies (0) \to (7)$.

---

### Step 4: Hundreds Column ($10^2$)
- Pop $s_1$: $d_1 = 2$.
- Pop $s_2$: $d_2 = 5$.
- Carry: $1$.
- Sum: $2 + 5 + 1 = \mathbf{8}$.
- New carry: $\lfloor 8 / 10 \rfloor = \mathbf{0}$.
- Node value: $8 \pmod{10} = \mathbf{8}$.
- Prepend: $head = \text{ListNode}(8, head) \implies (8) \to (0) \to (7)$.

---

### Step 5: Thousands Column ($10^3$)
- Pop $s_1$: $d_1 = 7$.
- $s_2$ is empty $\implies d_2 = 0$.
- Carry: $0$.
- Sum: $7 + 0 + 0 = \mathbf{7}$.
- New carry: $\lfloor 7 / 10 \rfloor = \mathbf{0}$.
- Node value: $7 \pmod{10} = \mathbf{7}$.
- Prepend: $head = \text{ListNode}(7, head) \implies (7) \to (8) \to (0) \to (7)$.

---

### Termination:
Both stacks are empty and $carry = 0$.
Return $head$: **$(7) \to (8) \to (0) \to (7)$**.

---

## 4. Complete Execution Trace

| Column Power | $s_1$ Top | $s_2$ Top | In-Carry | Column Sum | Out-Carry | Digit Emitted | Linked List Formed So Far |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| **$10^0$** | $3$ | $4$ | $0$ | $7$ | $0$ | **$7$** | `(7)` |
| **$10^1$** | $4$ | $6$ | $0$ | $10$ | **$1$** | **$0$** | `(0) -> (7)` |
| **$10^2$** | $2$ | $5$ | $1$ | $8$ | $0$ | **$8$** | `(8) -> (0) -> (7)` |
| **$10^3$** | $7$ | $0$ (empty) | $0$ | $7$ | $0$ | **$7$** | `(7) -> (8) -> (0) -> (7)` |
| **Done** | Empty | Empty | $0$ | — | — | — | **Final Head: 7** |

---

## 5. Boundary Cases & Failure Modes

- **Carry Generates New MSB ($[9, 9] + [1] = [1, 0, 0]$):** After both stacks are exhausted, $carry = 1$ remains. The loop executes one final iteration for $carry$, prepending Node $1$ as the new head.
- **Both Lists Zero ($[0] + [0] = [0]$):** Single addition $0 + 0 + 0 = 0 \implies [0]$.
- **Highly Asymmetric Lengths ($[1, 0, 0, 0] + [1] = [1, 0, 0, 1]$):** Stacks naturally handle missing digits by falling back to $0$, propagating values without index alignment errors.

---

## 6. Traps & Common Anti-Patterns

- **Mutating Input Lists When Forbidden:** Reversing $l_1$ and $l_2$ modifies the caller's data structure and violates problem constraints if read-only access is requested. Stacks maintain non-destructive access.
- **Converting to Native BigInteger / 64-Bit Integers:** In languages with fixed integer types (C++, Java), converting lists with up to 100 nodes to integers causes arithmetic overflow. Digit-by-digit simulation handles unbounded lengths safely.
- **Forgetting Final Carry:** Failing to include `or carry` in the while loop condition drops the most significant carry when adding numbers like $50 + 50 = 100$ (producing $00$ instead of $100$).

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Pushing $l_1$ of length $M$ onto $s_1$ takes $O(M)$ time.
  - Pushing $l_2$ of length $N$ onto $s_2$ takes $O(N)$ time.
  - The addition loop executes $\max(M, N) + 1$ times in $O(1)$ operations per step.
  - Total Time: $\mathcal{O}(M + N)$.
- **Auxiliary Space Complexity:**
  - The two stacks store $M$ and $N$ integers.
  - Total Auxiliary Space: $\mathcal{O}(M + N)$.
