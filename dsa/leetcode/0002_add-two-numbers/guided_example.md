# Guided Example: Add Two Numbers

We will compute the sum of two numbers represented by linked lists in reverse digit order:

- **Input:** $l_1 = [9, 9, 9]$, $l_2 = [1]$
- **Numerical meaning:** $999 + 1 = 1000$
- **Required output:** `[0, 0, 0, 1]`

This instance is chosen because it exposes the three essential subtleties of digit-wise addition: unequal input lengths, cascading carry propagation across multiple positions, and a final lingering carry that appends a newly created node after both input lists have been exhausted.

---

## 1. Instance & Teaching Goal

Each node represents one decimal digit in least-significant-first order. Positional addition must proceed column by column from lowest to highest power of $10$:

$$
\text{Column sum} = \text{digit}_1 + \text{digit}_2 + \text{carry}_{\text{in}}
$$

From this column sum, two values are determined at each position:

$$
\text{New digit} = \text{Column sum} \pmod{10}, \qquad \text{carry}_{\text{out}} = \left\lfloor \frac{\text{Column sum}}{10} \right\rfloor
$$

A correct method must continue processing as long as *either* list has remaining nodes or the carry is non-zero.

---

## 2. Conceptual Foundation & Invariants

We traverse the lists in lockstep while accumulating digits into a new resultant list. We maintain an integer accumulator $\text{carry} \in \{0, 1\}$.

| Position (Power of 10) | $10^0$ | $10^1$ | $10^2$ | $10^3$ |
|---|---|---|---|---|
| $l_1$ digit | 9 | 9 | 9 | $\varnothing$ |
| $l_2$ digit | 1 | $\varnothing$ | $\varnothing$ | $\varnothing$ |

> **Invariant.** At step $k$, all column additions up to $10^{k-1}$ have been finalized into the output chain, and $\text{carry}$ holds the exact quotient from the $(k-1)$-th digit sum.

---

## 3. Step-by-Step Worked Execution

### Step 1: Position $10^0$ (Units)

- **Available digits:** $l_1 = 9$, $l_2 = 1$, $\text{carry}_{\text{in}} = 0$.
- **Sum calculation:** $9 + 1 + 0 = 10$.
- **Output digit:** $10 \pmod{10} = 0$.
- **New carry:** $\lfloor 10 / 10 \rfloor = 1$.

| State Parameter | Value |
|---|---|
| Active $l_1$ Node | $9 \to \text{next}$ |
| Active $l_2$ Node | $1 \to \varnothing$ |
| Result List Built | `[0]` |
| Carry Forward | $1$ |

---

### Step 2: Position $10^1$ (Tens)

- **Available digits:** $l_1 = 9$, $l_2 = \varnothing$ (treated as $0$), $\text{carry}_{\text{in}} = 1$.
- **Sum calculation:** $9 + 0 + 1 = 10$.
- **Output digit:** $10 \pmod{10} = 0$.
- **New carry:** $\lfloor 10 / 10 \rfloor = 1$.

| State Parameter | Value |
|---|---|
| Active $l_1$ Node | $9 \to \text{next}$ |
| Active $l_2$ Node | $\varnothing$ |
| Result List Built | $[0 \to 0]$ |
| Carry Forward | $1$ |

---

### Step 3: Position $10^2$ (Hundreds)

- **Available digits:** $l_1 = 9$, $l_2 = \varnothing$ (treated as $0$), $\text{carry}_{\text{in}} = 1$.
- **Sum calculation:** $9 + 0 + 1 = 10$.
- **Output digit:** $10 \pmod{10} = 0$.
- **New carry:** $\lfloor 10 / 10 \rfloor = 1$.

| State Parameter | Value |
|---|---|
| Active $l_1$ Node | $\varnothing$ |
| Active $l_2$ Node | $\varnothing$ |
| Result List Built | $[0 \to 0 \to 0]$ |
| Carry Forward | $1$ |

Both input lists are now fully exhausted.

---

### Step 4: Position $10^3$ (Lingering Carry)

Although both $l_1$ and $l_2$ are $\varnothing$, the carry forward is $1 \neq 0$.

- **Sum calculation:** $0 + 0 + 1 = 1$.
- **Output digit:** $1 \pmod{10} = 1$.
- **New carry:** $\lfloor 1 / 10 \rfloor = 0$.

| State Parameter | Value |
|---|---|
| Active $l_1$ Node | $\varnothing$ |
| Active $l_2$ Node | $\varnothing$ |
| Result List Built | $[0 \to 0 \to 0 \to 1]$ |
| Carry Forward | $0$ |

All lists and carries are zero. Termination condition satisfied.

---

## 4. Complete Execution Trace

| Step | Power of 10 | $l_1$ Val | $l_2$ Val | Carry In | Total Sum | Emit Digit | Carry Out | Current Output |
|---|---|---|---|---|---|---|---|---|
| 1 | $10^0$ | 9 | 1 | 0 | 10 | 0 | 1 | `[0]` |
| 2 | $10^1$ | 9 | 0 | 1 | 10 | 0 | 1 | `[0, 0]` |
| 3 | $10^2$ | 9 | 0 | 1 | 10 | 0 | 1 | `[0, 0, 0]` |
| 4 | $10^3$ | 0 | 0 | 1 | 1 | 1 | 0 | `[0, 0, 0, 1]` |

---

## 5. Algorithmic Correctness

**Soundness.** Every emitted digit is uniquely determined by elementary base-10 arithmetic. The carry never exceeds $1$ because the maximum possible sum at any digit position is:

$$
9 + 9 + 1 = 19 \implies \lfloor 19 / 10 \rfloor = 1
$$

Thus, no digit exceeds $9$ and the output chain is mathematically identical to standard column addition.

**Completeness.** By advancing the pointer whenever a node is present and continuing the loop condition $\text{while } (l_1 \neq \varnothing \lor l_2 \neq \varnothing \lor \text{carry} \neq 0)$, no trailing digits or residual carry nodes can be omitted.

---

## 6. Traps This Instance Exposes

- **Premature Loop Termination:** Ending the iteration when either $l_1$ or $l_2$ becomes empty would miss the tens and hundreds digits.
- **Forgetting the Final Carry:** Ending when both lists are empty without checking $\text{carry} > 0$ yields $000$ instead of $1000$, discarding the highest-order digit.
- **Modifying Input In-Place:** Reusing $l_1$ or $l_2$ nodes fails when the output requires more nodes than the longer input list.
- **Dummy Head Omission:** Managing list construction without a sentinel dummy head introduces unnecessary null-pointer branching on the first node.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(\max(N, M))$ where $N$ and $M$ are the lengths of $l_1$ and $l_2$. The loop executes at most $\max(N, M) + 1$ times.
- **Auxiliary Space Complexity:** $O(1)$ auxiliary space beyond the newly allocated nodes required to represent the sum.
