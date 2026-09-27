# Guided Example: Optimal Account Balancing

We trace the step-by-step net debt aggregation ($net[u]$), non-zero balance extraction, the zero-sum subset partition duality ($\text{transfers} = m - P_{max}$), bitmask sub-mask dynamic programming ($f[i] = \min(f[j] + f[i \oplus j])$), and transaction spanning tree construction on representative financial networks:

- **Input:** $transactions = [[0, 1, 10], [2, 0, 5]]$
- **Required output:** `2`
  - Step 1: Compute net balances per person:
    - Transaction $[0, 1, 10]$: Person $0$ pays $10 \implies net[0] \mathrel{-}= 10, \; net[1] \mathrel{+}= 10$
    - Transaction $[2, 0, 5]$: Person $2$ pays $5 \implies net[2] \mathrel{-}= 5, \; net[0] \mathrel{+}= 5$
    - Net balances:
      $$
      net[0] = -10 + 5 = -5, \quad net[1] = +10, \quad net[2] = -5
      $$
  - Step 2: Extract non-zero balances:
    $$
    nums = [-5, \; 10, \; -5] \quad (m = 3)
    $$
    Check global invariant: $\sum nums = -5 + 10 - 5 = 0$.
  - Step 3: Zero-sum subset partition theorem:
    - Any isolated zero-sum component of size $k$ can be settled in exactly $k - 1$ transfers (forming a tree of debt payments).
    - If the $m$ debts partition into $P$ disjoint zero-sum components:
      $$
      \text{Total Transfers} = \sum_{j=1}^P (|S_j| - 1) = m - P
      $$
    - Minimizing total transfers is mathematically equivalent to **maximizing the number of disjoint zero-sum subsets $P$**.
    - For $nums = [-5, 10, -5]$:
      - Can we partition into 2 non-empty zero-sum subsets?
        - Subsets of size 1: $\{-5\}, \{10\}, \{-5\} \ne 0$
        - Subsets of size 2: $\{-5, 10\} = 5 \ne 0, \; \{-5, -5\} = -10 \ne 0$
        - No proper zero-sum subsets exist!
      - Thus, the maximal partition is $P = 1$ (the entire set of 3 accounts).
      - Minimum transfers:
        $$
        m - P = 3 - 1 = \mathbf{2}
        $$
  - Settle transfers:
    1. Person 0 pays Person 1: $\$5$ (Person 0 settled: $0$, Person 1 remaining: $+5$)
    2. Person 2 pays Person 1: $\$5$ (Both settled: $0$)
    All accounts balanced in exactly $2$ transfers.
- **Netted Cycle Instance:** $transactions = [[0, 1, 10], [1, 0, 1], [1, 2, 5], [2, 0, 5]]$
  - Net balances: $net[0] = -4, net[1] = +4, net[2] = 0$
  - Active accounts: $[-4, 4]$ ($m = 2$) $\implies 1$ transfer of $\$4$ from Person 0 to Person 1 $\implies \mathbf{1}$
- **All Accounts Balanced:** Net balances all $0 \implies \mathbf{0}$ transfers

This instance demonstrates network flow debt simplification, mathematically proves the duality between minimal transaction spanning trees and maximum zero-sum subset partitioning, and derives $O(3^m)$ runtime and $O(2^m)$ space bounds.

---

## 1. Instance & Teaching Goal

Given an array of transactions $[[0, 1, 10], [2, 0, 5]]$:
Each transaction $[from, to, amount]$ represents a payment of $amount$ from $from$ to $to$.
Return the **minimum number of transactions** required to settle all debts.

```text
Original Debt Flow:
  Person 2 -----$5-----> Person 0 -----$10-----> Person 1

Net Balances:
  Person 0: -5 (Owes 5)
  Person 1: +10 (Owed 10)
  Person 2: -5 (Owes 5)

Optimal Direct Settlement (2 Transfers):
  Person 0 -----$5-----> Person 1
  Person 2 -----$5-----> Person 1
```

### The Zero-Sum Partition Duality
- Debt settlement does not depend on who originally transacted with whom. Only the **net balance** of each participant matters.
- In any valid settlement:
  - If a group of $k$ accounts sums to zero ($\sum_{i \in S} net[i] = 0$), debts within this group can be completely cleared by creating a **spanning tree** of transfers connecting the $k$ accounts.
  - A spanning tree on $k$ vertices contains exactly $k - 1$ edges (transfers).
- If the entire set of $m$ active accounts is decomposed into $P$ disjoint zero-sum subsets:
  $$
  \text{Transfers} = \sum_{j=1}^P (|S_j| - 1) = \sum |S_j| - \sum_{j=1}^P 1 = m - P
  $$
- Therefore:
  $$
  \min(\text{Transfers}) \iff \max(P)
  $$
  Minimizing transactions is equivalent to finding the **maximum number of disjoint zero-sum subsets**!

---

## 2. Conceptual Foundation & Invariants

### 1. Net Balance Condensation:
Initialize balance map $g$:
- For each transaction $(f, t, x)$:
  $$
  g[f] \leftarrow g[f] - x, \quad g[t] \leftarrow g[t] + x
  $$
- Discard all accounts with $g[u] == 0$.
- Let $nums = [x \in g.\text{values}() \mid x \ne 0]$ have size $m$.

### 2. Bitmask Sub-Mask Dynamic Programming:
Let $f[mask]$ be the minimum number of transactions to settle the subset of accounts indicated by the 1-bits in $mask$:
1. If the elements in $mask$ do not sum to 0 ($\sum_{j \in mask} nums[j] \ne 0$):
   $mask$ cannot be settled independently.
2. If $\sum_{j \in mask} nums[j] == 0$:
   - Base configuration: A single spanning tree requires:
     $$
     f[mask] = \text{popcount}(mask) - 1
     $$
   - Sub-mask decomposition: Check if $mask$ can be split into two smaller zero-sum subsets $sub$ and $mask \setminus sub$:
     $$
     f[mask] = \min_{sub \subset mask} (f[sub] + f[mask \oplus sub])
     $$
3. Result: $f[(1 \ll m) - 1]$.

> **Zero-Sum Invariant.** A debt cluster can settle completely without external cash flow if and only if its algebraic net sum is zero. Every independent zero-sum cluster reduces the total global transfer count by 1.

---

## 3. Step-by-Step Worked Execution

We trace $transactions = [[0, 1, 10], [2, 0, 5]]$:

---

### Step 1: Net Balance Aggregation
- Transaction 1: $0 \to 1$ (\$10):
  $$
  g[0] = -10, \quad g[1] = +10
  $$
- Transaction 2: $2 \to 0$ (\$5):
  $$
  g[2] = -5, \quad g[0] = -10 + 5 = -5
  $$
Net balances:
$$
g = \{0: -5, \; 1: +10, \; 2: -5\}
$$
Non-zero array:
$$
nums = [-5, \; 10, \; -5] \quad (m = 3)
$$

---

### Step 2: Bitmask DP Table Construction ($2^3 = 8$ states)
Let bit 0 correspond to $-5$, bit 1 to $+10$, bit 2 to $-5$.

- **Singletons (1 bit set):**
  - $mask = 001_2: \sum = -5 \ne 0$
  - $mask = 010_2: \sum = 10 \ne 0$
  - $mask = 100_2: \sum = -5 \ne 0$
- **Pairs (2 bits set):**
  - $mask = 011_2$ (bits 0, 1): $-5 + 10 = 5 \ne 0$
  - $mask = 101_2$ (bits 0, 2): $-5 - 5 = -10 \ne 0$
  - $mask = 110_2$ (bits 1, 2): $10 - 5 = 5 \ne 0$
- **Full Mask ($mask = 111_2$, 3 bits set):**
  - Sum of elements:
    $$
    s = (-5) + 10 + (-5) = \mathbf{0}
    $$
  - Base spanning tree cost:
    $$
    f[111_2] = \text{popcount}(111_2) - 1 = 3 - 1 = \mathbf{2}
    $$
  - Test sub-mask splits ($sub \subset 111_2$):
    - Sub-mask $001_2$: remainder $110_2$. $f[001_2] = \infty \implies \infty$
    - Sub-mask $010_2$: remainder $101_2$. $f[010_2] = \infty \implies \infty$
    - Sub-mask $011_2$: remainder $100_2$. $f[011_2] = \infty \implies \infty$
    - No sub-mask has sum 0. Minimum remains $2$.

---

### Step 3: Result Extraction
The full mask $111_2$ (all accounts) settles in:
$$
f[111_2] = \mathbf{2}
$$

---

## 4. Complete Execution Trace

| State Mask | Binary Mask | Accounts Included | Net Balance Sum | Can Settle? | Spanning Tree Cost | Min Sub-Mask Split | Table Value $f[mask]$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $0$ | $000_2$ | None | $0$ | Yes | $0$ | — | $0$ |
| $1$ | $001_2$ | $\{-5\}$ | $-5$ | No | $\infty$ | — | $\infty$ |
| $2$ | $010_2$ | $\{+10\}$ | $+10$ | No | $\infty$ | — | $\infty$ |
| $3$ | $011_2$ | $\{-5, +10\}$ | $+5$ | No | $\infty$ | — | $\infty$ |
| $4$ | $100_2$ | $\{-5\}$ | $-5$ | No | $\infty$ | — | $\infty$ |
| $5$ | $101_2$ | $\{-5, -5\}$ | $-10$ | No | $\infty$ | — | $\infty$ |
| $6$ | $110_2$ | $\{+10, -5\}$ | $+5$ | No | $\infty$ | — | $\infty$ |
| **$7$** | **$111_2$** | **$\{-5, +10, -5\}$** | **$0$** | **Yes** | **$3 - 1 = 2$** | None ($P=1$) | **$2$** |

---

## 5. Boundary Cases & Failure Modes

- **Already Settled ($transactions = [[0, 1, 10], [1, 0, 10]]$):** Net balances are $0$. Non-zero list is empty ($m = 0$) $\implies f[0] = \mathbf{0}$.
- **Two Independent Equal Pairs ($nums = [-5, 5, -10, 10]$):**
  - Two zero-sum pairs: $\{-5, 5\}$ and $\{-10, 10\}$.
  - $P = 2$ disjoint subsets.
  - Total transfers: $m - P = 4 - 2 = \mathbf{2}$.
- **Chain of Debt ($A \to B \to C$):** Balances $[-5, 0, +5] \implies$ Net array $[-5, +5]$. $m = 2, P = 1 \implies 2 - 1 = \mathbf{1}$ transfer directly from $A$ to $C$.

---

## 6. Traps & Common Anti-Patterns

- **Greedy Matching (Largest with Smallest):** Greedily pairing the largest positive with the largest negative does not always maximize zero-sum partitions. For example, with $[-4, -3, -2, 4, 5]$, pairing $+5$ with $-4$ leaves remainder $+1$, whereas pairing $\{-5, 3, 2\}$ and $\{-4, 4\}$ produces 2 zero-sum groups ($5 - 2 = 3$ transfers). Bitmask DP guarantees global optimality.
- **Iterating Over Irrelevant Non-Zero Nodes:** Including individuals whose net balance is already 0 exponentially inflates the $2^m$ search space. Filtering out $net == 0$ accounts initially is essential.
- **Unbounded Bitmask Size:** If $m > 16$, $3^m$ sub-mask iteration exceeds time limits. For this problem, constraints guarantee $m \le 12$, making $3^{12} \approx 5.3 \times 10^5$ operations fast.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Aggregating balances takes $O(T)$ where $T$ is the number of transactions.
  - Sub-mask enumeration over all bitmasks takes:
    $$
    \sum_{k=0}^m \binom{m}{k} 2^k = (1 + 2)^m = 3^m \text{ operations}
    $$
  - For $m \le 12$, $3^{12} = 531,441$ operations, running in $< 25$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(2^m)$ to store the DP table $f$. For $m = 12$, $2^{12} = 4096$ words.
