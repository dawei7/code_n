# Guided Example: Distribute Candies

We trace the step-by-step capacity quota bounding ($n/2$), distinct type cardinalities ($|\text{set}(candyType)|$), dual-constraint upper bound minimization ($\min(n/2, |\text{set}|)$), greedy variety maximization, and closed-form linear verification on representative candy collections:

- **Input:** $candyType = [1, 1, 2, 2, 3, 3]$
- **Required output:** `3`
  - Problem setup:
    - Total candies: $n = 6$.
    - Allowance quota: Alice is allowed to eat at most $n / 2 = 6 / 2 = \mathbf{3}$ candies.
    - Goal: Maximize the number of **different types of candies** Alice can eat.
- **Dual-Constraint Capacity & Variety Analysis:**
  - Let $U = |\text{set}(candyType)|$ denote the number of unique candy types in the collection.
  - Let $C = n / 2$ denote the maximum number of candies Alice is permitted to consume.
  - Alice wants to choose a subset of $C$ candies that contains as many distinct types as possible.
  - **Constraint 1 (Intake Capacity Limit):**
    - Even if there were infinitely many candy types available, Alice can eat at most $C$ individual candies.
    - Therefore, the number of distinct types eaten can **never exceed $C = n / 2$**:
      $$
      \text{Types} \le \frac{n}{2}
      $$
  - **Constraint 2 (Physical Variety Availability):**
    - Alice cannot eat a candy type that does not exist in the bag.
    - Therefore, the number of distinct types eaten can **never exceed $U = |\text{set}(candyType)|$**:
      $$
      \text{Types} \le U
      $$
  - **Greedy Realizability Theorem:**
    - Can Alice always achieve the smaller of these two bounds?
    - **Yes!** Alice simply picks exactly **one candy from each distinct type**.
    - If $U \le C$: She takes one candy of each of the $U$ types, and fills any remaining quota $C - U$ with duplicate candies. Total unique types eaten: $U$.
    - If $U > C$: She takes one candy from each of any $C$ different types. Total unique types eaten: $C$.
    - Therefore, the exact maximum is:
      $$
      \text{Max Types} = \min\left( \frac{n}{2}, \; |\text{set}(candyType)| \right)
      $$
- **Step-by-Step Execution Trace on $[1, 1, 2, 2, 3, 3]$ ($n = 6$):**
  - **Step 1: Compute Consumption Quota:**
    $$
    C = \frac{n}{2} = \frac{6}{2} = \mathbf{3}
    $$
  - **Step 2: Compute Distinct Types Available:**
    - Unique set: $\{1, 2, 3\}$.
    - Distinct count:
      $$
      U = |\{1, 2, 3\}| = \mathbf{3}
      $$
  - **Step 3: Evaluate Minimum:**
    $$
    ans = \min(C, U) = \min(3, 3) = \mathbf{3}
    $$
    *(Alice eats one of Type 1, one of Type 2, and one of Type 3!)*
- **Capacity Bottleneck Instance ($candyType = [1, 1, 2, 3]$, $n = 4$):**
  - Allowed quota: $C = 4 / 2 = \mathbf{2}$.
  - Unique types: $\{1, 2, 3\} \implies U = \mathbf{3}$.
  - $ans = \min(2, 3) = \mathbf{2}$.
  - *(Even though 3 types exist, she can only eat 2 candies total)*.
- **Variety Bottleneck Instance ($candyType = [6, 6, 6, 6]$, $n = 4$):**
  - Allowed quota: $C = 4 / 2 = \mathbf{2}$.
  - Unique types: $\{6\} \implies U = \mathbf{1}$.
  - $ans = \min(2, 1) = \mathbf{1}$.
  - *(Even though she can eat 2 candies, only 1 type exists)*.

This instance demonstrates capacity-limited multiset variety selection, mathematically proves why the closed-form bound $\min(n/2, |\text{set}|)$ is universally achievable without search, and derives $O(N)$ runtime and $O(U)$ space bounds.

---

## 1. Instance & Teaching Goal

Given an array of candies $candyType$ of even length $n$:
Alice can eat at most $n / 2$ candies.
Return the **maximum number of unique candy types** she can eat.

```text
Input: [ 1,  1,  2,  2,  3,  3 ]

Total candies = 6 -> Can eat at most 3 candies.
Available unique types: { 1, 2, 3 } (3 types)

Greedy choice: Eat one of each type -> { 1, 2, 3 }
Distinct types eaten = 3
```

### The Capacity vs Variety Minimax Principle
- The answer is fundamentally bounded by two bottlenecks:
  1. **Quota Bottleneck ($n / 2$):** She cannot eat more unique types than the total number of candies she is allowed to consume.
  2. **Inventory Bottleneck ($|\text{set}|$):** She cannot eat more unique types than the number of distinct varieties present in the array.
- Since she can always prioritize choosing one candy from each unique variety before repeating any type, the answer is unconditionally $\min(n/2, |\text{set}|)$.

---

## 2. Conceptual Foundation & Invariants

### 1. The Closed-Form Formula:
$$
\text{Max Unique Types} = \min\left( \lfloor n / 2 \rfloor, \; |\text{Unique Types}| \right)
$$

### 2. Proof of Achievability:
- Let $k = \min(n/2, U)$.
- Alice selects 1 candy from each of $k$ distinct types.
- If $k < n/2$ (meaning $U < n/2$), she satisfies her remaining quota of $n/2 - k$ candies by taking duplicates of the already selected types.
- The number of distinct types consumed is exactly $k$.

> **Pigeonhole Saturation Invariant.** When variety exceeds capacity ($U \ge n/2$), every candy consumed can be of a distinct variety, perfectly saturating the intake quota.

---

## 3. Step-by-Step Worked Execution

We trace $candyType = [1, 1, 2, 2, 3, 3]$:

---

### Step 1: Calculate Quota
$$
n = 6 \implies \text{Quota} = 6 // 2 = \mathbf{3}
$$

---

### Step 2: Extract Unique Types
- Elements: $1, 1, 2, 2, 3, 3$.
- Unique set: $\{1, 2, 3\}$.
- Cardinality:
  $$
  U = \mathbf{3}
  $$

---

### Step 3: Compute Minimum
$$
ans = \min(3, 3) = \mathbf{3}
$$

---

## 4. Complete Execution Trace

| Input $candyType$ | Total Candies $n$ | Allowed Quota $n/2$ | Unique Set $\text{set}(candyType)$ | Unique Count $U$ | Result $\min(n/2, U)$ |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `[1, 1, 2, 2, 3, 3]` | $6$ | $3$ | $\{1, 2, 3\}$ | $3$ | **`3`** |
| `[1, 1, 2, 3]` | $4$ | $2$ | $\{1, 2, 3\}$ | $3$ | **`2`** |
| `[6, 6, 6, 6]` | $4$ | $2$ | $\{6\}$ | $1$ | **`1`** |
| `[1, 2, 3, 4, 5, 6]` | $6$ | $3$ | $\{1, 2, 3, 4, 5, 6\}$ | $6$ | **`3`** |

---

## 5. Boundary Cases & Failure Modes

- **All Candies of Same Type ($[1, 1, 1, 1]$):** $U = 1 \implies \min(2, 1) = \mathbf{1}$.
- **All Candies Distinct ($[1, 2, 3, 4]$):** $U = 4 \implies \min(2, 4) = \mathbf{2}$.
- **Negative Candy Types ($[-100, 100]$):** Sets handle arbitrary signed integers seamlessly.
- **Large $N = 10^5$:** Inserting into a hash set takes linear $O(N)$ time.

---

## 6. Traps & Common Anti-Patterns

- **Sorting and Counting Unique Elements ($O(N \log N)$):** Sorting the entire array is unnecessary when a hash set or boolean presence array determines the cardinality in $O(N)$ time.
- **Simulating the Candy Selection:** Iterating through candies and picking duplicates with complex greedy queues is redundant. The mathematical minimum directly gives the exact optimal value.
- **Using Floating-Point Division:** Using `n / 2` instead of `n >> 1` or integer division can yield floats in some environments.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Constructing the hash set of $N$ elements takes $\mathcal{O}(N)$ average operations.
  - Taking `len()` and `min()` takes $\mathcal{O}(1)$ time.
  - Total Time: strictly linear $\mathcal{O}(N)$. For $N = 10^5$, completes in $< 5$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(U)$ space for the hash set where $U \le N$ is the number of distinct candy types.
