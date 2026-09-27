# Guided Example: Climbing Stairs

We trace the step-by-step state transition and Fibonacci recurrence evaluation on a representative staircase instance:

- **Input:** $n = 5$
- **Required output:** $8$

This instance demonstrates decomposing choices into mutually exclusive previous steps ($i - 1$ and $i - 2$), mapping step climbing to the Fibonacci recurrence ($DP[i] = DP[i-1] + DP[i-2]$), space optimization to two scalar variables, and matrix exponentiation / closed-form connections.

---

## 1. Instance & Teaching Goal

You are climbing a staircase that has $n = 5$ steps. Each time you can climb either $1$ step or $2$ steps. In how many distinct ways can you climb to the top?

For $n = 5$, there are 8 distinct valid step combinations:
1. $1 + 1 + 1 + 1 + 1$
2. $1 + 1 + 1 + 2$
3. $1 + 1 + 2 + 1$
4. $1 + 2 + 1 + 1$
5. $2 + 1 + 1 + 1$
6. $1 + 2 + 2$
7. $2 + 1 + 2$
8. $2 + 2 + 1$

A naive recursive implementation recalculates overlapping subproblems, exhibiting exponential $O(2^n)$ time.
Dynamic programming observes that the very last hop to reach step $i$ must be either:
- A $1$-step hop from step $i - 1$, OR
- A $2$-step hop from step $i - 2$.
Since these two scenarios are mutually exclusive and collectively exhaustive, the number of ways to reach step $i$ is strictly $DP[i-1] + DP[i-2]$.

---

## 2. Conceptual Foundation & Invariants

### The Fibonacci Recurrence
Let $DP[i]$ be the number of distinct ways to reach step $i$.
1. **Base Cases:**
   - Step 1: Exactly 1 way ($[1]$):
     $$
     DP[1] = 1
     $$
   - Step 2: Exactly 2 ways ($[1+1]$ or $[2]$):
     $$
     DP[2] = 2
     $$
2. **Inductive Step ($i \ge 3$):**
   $$
   DP[i] = DP[i - 1] + DP[i - 2]
   $$

### Space Optimization ($O(1)$ Memory)
Because computing $DP[i]$ requires only the previous two terms, we discard the full array and maintain two variables:
$$
\text{prev2} = DP[1] = 1, \quad \text{prev1} = DP[2] = 2
$$
In each iteration:
$$
\text{current} \leftarrow \text{prev1} + \text{prev2}
$$
$$
\text{prev2} \leftarrow \text{prev1}, \quad \text{prev1} \leftarrow \text{current}
$$

> **Invariant.** At the start of step $i$, `prev1` equals $DP[i-1]$ and `prev2` equals $DP[i-2]$. After updating, `prev1` holds $DP[i]$.

---

## 3. Step-by-Step Worked Execution

We trace the calculation from $i = 1$ to $n = 5$:

- **Step 1 ($i = 1$):**
  - Base case: $DP[1] = 1$.
- **Step 2 ($i = 2$):**
  - Base case: $DP[2] = 2$.
- **Step 3 ($i = 3$):**
  - Incoming from Step 2: $DP[2] = 2$ (via $+1$ step).
  - Incoming from Step 1: $DP[1] = 1$ (via $+2$ steps).
  - $DP[3] = 2 + 1 = 3$.
- **Step 4 ($i = 4$):**
  - Incoming from Step 3: $DP[3] = 3$.
  - Incoming from Step 2: $DP[2] = 2$.
  - $DP[4] = 3 + 2 = 5$.
- **Step 5 ($i = 5$):**
  - Incoming from Step 4: $DP[4] = 5$.
  - Incoming from Step 3: $DP[3] = 3$.
  - $DP[5] = 5 + 3 = \mathbf{8}$.

Goal reached for $n = 5$: $8$ unique paths.

### The Two-Variable Shift, Step by Step

The array is unnecessary because each transition consumes only the two most recent terms. Tracking both variables through the shift shows that the invariant `prev1 = DP[i-1]`, `prev2 = DP[i-2]` is re-established by every iteration:

| Transition | `prev2` before ($DP[i-2]$) | `prev1` before ($DP[i-1]$) | $DP[i] = $ `prev1` $+$ `prev2` | `prev2` after | `prev1` after |
|:---:|:---:|:---:|:---:|:---:|:---:|
| Initialize ($i = 2$) | 1 ($DP[1]$) | 2 ($DP[2]$) | not computed yet | 1 | 2 |
| $i = 3$ | 1 | 2 | **3** | 2 | 3 |
| $i = 4$ | 2 | 3 | **5** | 3 | 5 |
| $i = 5$ | 3 | 5 | **8** | 5 | 8 |

After the final shift, `prev1` $= 8 = DP[5]$, which is the answer; the discarded `prev2` $= 5 = DP[4]$ is never needed again. Only two scalars are live at any moment, independent of $n$.

---

## 4. Complete Execution Trace

| Step $i$ | Predecessor 1 ($DP[i-1]$) | Predecessor 2 ($DP[i-2]$) | Evaluated Recurrence ($DP[i-1] + DP[i-2]$) | Computed $DP[i]$ | Unique Paths Discovered |
|:---:|:---:|:---:|:---:|:---:|:---|
| 1 | - | - | Base condition | **1** | `[1]` |
| 2 | - | - | Base condition | **2** | `[1+1]`, `[2]` |
| 3 | 2 | 1 | $2 + 1$ | **3** | `[1+1+1]`, `[1+2]`, `[2+1]` |
| 4 | 3 | 2 | $3 + 2$ | **5** | 5 combinations |
| 5 | 5 | 3 | $5 + 3$ | **8** | **8 combinations (Result)** |

---

## 5. Algorithmic Correctness

**Soundness.** Every valid sequence of steps ending at step $i$ must end with either a 1-step or a 2-step hop. A sequence ending in 1 corresponds uniquely to a valid path to $i - 1$. A sequence ending in 2 corresponds uniquely to a valid path to $i - 2$. Because the final hop size is distinct, these two sets of paths have empty intersection. Therefore, $|DP[i]| = |DP[i-1]| + |DP[i-2]|$.

**Completeness.** Starting with true base cases $DP[1] = 1$ and $DP[2] = 2$, mathematical induction guarantees that every integer step up to $n$ is evaluated and accounts for all paths.

---

## 6. Traps This Instance Exposes

- **Base Cases for Small $n$:** If $n = 1$, the algorithm must return $1$ without attempting to index $DP[2]$ or execute iterations that assume $n \ge 2$.
- **Linear Space Overhead:** Allocating a full list of length $n + 1$ takes $O(n)$ space. Storing only `prev1` and `prev2` reduces memory to $O(1)$ scalar variables.
- **Logarithmic Acceleration:** For massive $n$ ($n \approx 10^9$), the transition matrix $\begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}$ raised to the power $n-1$ via binary exponentiation calculates $DP[n]$ in $O(\log n)$ time.

Every $n$ from the case set lands on the same shifted sequence, because the number of ways to reach step $n$ is the Fibonacci number $F_{n+1}$ under $F_1 = F_2 = 1$:

| Instance | $n$ | Ways to climb | Fibonacci identity | Why the value is exact |
|:---|:---:|:---:|:---|:---|
| One stair | 1 | 1 | $F_2 = 1$ | The base case returns immediately; only the single $1$-step hop exists. |
| Two stairs | 2 | 2 | $F_3 = 2$ | Base case: the sequences are $1+1$ and $2$. |
| Three stairs | 3 | 3 | $F_4 = 3$ | First inductive step: $F_3 + F_2 = 2 + 1$. |
| Five stairs (main trace) | 5 | 8 | $F_6 = 8$ | $F_5 + F_4 = 5 + 3$; the eight sequences are listed in section 1. |
| Largest legal staircase | 45 | 1836311903 | $F_{46} = 1836311903$ | Already the largest $n$ whose count fits a signed 32-bit integer, since $F_{47} = 2971215073 > 2^{31} - 1$. |

The final row explains the constraint $1 \le n \le 45$: one more step would push the count past $2^{31} - 1 = 2147483647$, so the recurrence never has to leave signed 32-bit range.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. The loop executes $n - 2$ times, performing one scalar addition per step.
- **Auxiliary Space Complexity:** $O(1)$. Requires only two scalar variables (`prev1`, `prev2`) to track the prior terms.
