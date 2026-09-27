# Guided Example: Maximum XOR of Two Numbers in an Array

We trace the step-by-step bitwise binary trie construction, most-significant-bit (MSB) greedy opposite-branch descent, dynamic prefix masking, and pair maximum synthesis on representative numerical arrays:

- **Input:** $nums = [3, 10, 5, 25, 2, 8]$
- **Required output:** `28`
  - Binary representations (5-bit window, $2^4 \dots 2^0$):
    - $3 = 00011_2, \quad 10 = 01010_2, \quad 5 = 00101_2$
    - $25 = 11001_2, \quad 2 = 00010_2, \quad 8 = 01000_2$
  - Querying with $x = 5$ ($00101_2$) against the Trie:
    - Bit 4 (value $2^4 = 16$, $x$ has $0$): Desired bit is $1$. Trie contains branch $1$ (from $25$) $\implies$ Take branch $1$, add $16$. Running XOR = $16$.
    - Bit 3 (value $2^3 = 8$, $x$ has $0$): Desired bit is $1$. Branch $1$ exists (from $25$) $\implies$ Take branch $1$, add $8$. Running XOR = $24$.
    - Bit 2 (value $2^2 = 4$, $x$ has $1$): Desired bit is $0$. Branch $0$ exists (from $25$) $\implies$ Take branch $0$, add $4$. Running XOR = $28$.
    - Bit 1 (value $2^1 = 2$, $x$ has $0$): Desired bit is $1$. Branch $1$ unavailable (only branch $0$ exists) $\implies$ Forced to branch $0$, add $0$. Running XOR = $28$.
    - Bit 0 (value $2^0 = 1$, $x$ has $1$): Desired bit is $0$. Branch $0$ unavailable $\implies$ Forced to branch $1$, add $0$. Running XOR = $28$.
  - Maximum XOR discovered:
    $$
    5 \oplus 25 = 00101_2 \oplus 11001_2 = 11100_2 = \mathbf{28}
    $$
- **Single Element / Zero Instance:** $nums = [0] \implies 0 \oplus 0 = \mathbf{0}$
- **Two Identical Elements:** $nums = [7, 7] \implies 7 \oplus 7 = \mathbf{0}$

This instance demonstrates bitwise prefix trees (0-1 Trie), mathematically proves why the strict greedy choice at the most significant bit dominates all lower bits combined ($2^k > \sum_{j=0}^{k-1} 2^j$), and derives $O(31 \cdot N)$ runtime and $O(31 \cdot N)$ space bounds.

---

## 1. Instance & Teaching Goal

Given an integer array $nums = [3, 10, 5, 25, 2, 8]$:
Find the maximum result of $nums[i] \oplus nums[j]$ for any pair of elements:

```text
Numbers in Binary (5 bits):
   3:  0 0 0 1 1
  10:  0 1 0 1 0
   5:  0 0 1 0 1
  25:  1 1 0 0 1
   2:  0 0 0 1 0
   8:  0 1 0 0 0

Optimal Pairing:
    5:  0  0  1  0  1
 ^ 25:  1  1  0  0  1
---------------------
   28:  1  1  1  0  0  (16 + 8 + 4 = 28)
```

### The Strict Dominance of Higher Bits
In binary arithmetic, setting the $k$-th bit to $1$ contributes $2^k$.
Because:
$$
2^k > \sum_{j=0}^{k-1} 2^j = 2^k - 1
$$
A number with a $1$ at bit $k$ is strictly larger than any number that has a $0$ at bit $k$, even if that other number has $1$s at all lower bits $k-1, \dots, 0$.
Therefore, when maximizing XOR, **we must greedily prioritize securing a $1$ at the most significant possible bit position**, never sacrificing a higher bit to gain lower bits.

---

## 2. Conceptual Foundation & Invariants

### 1. The Binary Trie (0-1 Prefix Tree):
Every 31-bit non-negative integer is represented as a root-to-leaf path of length 31, where each step chooses branch $0$ or branch $1$.
- Root represents the start before bit 30.
- Level $i$ represents decision for bit $i$.
- Inserting all $N$ numbers creates a compact prefix tree encoding all shared bit patterns.

### 2. Greedy Complement Search:
To find the element $y$ that maximizes $x \oplus y$:
- Traverse down the Trie from bit 30 down to bit 0.
- At bit $i$, let $b = (x \gg i) \ \& \ 1$.
- The optimal opposite bit is $\bar{b} = b \oplus 1$.
- If the current Trie node has a child on branch $\bar{b}$:
  - We step to that child.
  - Bit $i$ of the XOR sum becomes $1$: $ans \leftarrow ans \ | \ (1 \ll i)$.
- Else:
  - Branch $\bar{b}$ does not exist. We are forced to take branch $b$.
  - Bit $i$ of the XOR sum becomes $0$.

> **Greedy Invariant.** At any bit level $i$, if a path exists with bit $i$ equal to $b \oplus 1$, taking that branch guarantees a higher total XOR than any alternative choice, because $2^i > \sum_{j=0}^{i-1} 2^j$.

---

## 3. Step-by-Step Worked Execution

We trace the query for $x = 5$ ($00101_2$) against the Trie containing $\{3, 10, 5, 25, 2, 8\}$:

---

### Step 1: Bit 4 ($2^4 = 16$)
- Target bit of $x$: $b = 0$.
- Desired opposite: $\bar{b} = 1$.
- Check Trie root: Branch $1$ exists (leads to $25 = 11001_2$).
- Decision:
  - Take Branch $1$.
  - Bit contribution: $+16$.
  - Cumulative XOR: $ans = \mathbf{16}$.
  - Current Trie Node: Node after prefix `1`.

---

### Step 2: Bit 3 ($2^3 = 8$)
- Target bit of $x$: $b = 0$.
- Desired opposite: $\bar{b} = 1$.
- Check current node: Branch $1$ exists (leads to $25 = 11001_2$).
- Decision:
  - Take Branch $1$.
  - Bit contribution: $+8$.
  - Cumulative XOR: $16 + 8 = \mathbf{24}$.
  - Current Trie Node: Node after prefix `11`.

---

### Step 3: Bit 2 ($2^2 = 4$)
- Target bit of $x$: $b = 1$.
- Desired opposite: $\bar{b} = 0$.
- Check current node: Branch $0$ exists (leads to $25 = 11001_2$).
- Decision:
  - Take Branch $0$.
  - Bit contribution: $+4$.
  - Cumulative XOR: $24 + 4 = \mathbf{28}$.
  - Current Trie Node: Node after prefix `110`.

---

### Step 4: Bit 1 ($2^1 = 2$)
- Target bit of $x$: $b = 0$.
- Desired opposite: $\bar{b} = 1$.
- Check current node: Does prefix `110` have a child on branch $1$?
  - The only number under `110` is $25$ ($11001_2$), whose bit 1 is $0$.
  - Branch $1$ is missing!
- Decision:
  - Forced to take Branch $0$.
  - Bit contribution: $+0$.
  - Cumulative XOR: $28 + 0 = \mathbf{28}$.
  - Current Trie Node: Node after prefix `1100`.

---

### Step 5: Bit 0 ($2^0 = 1$)
- Target bit of $x$: $b = 1$.
- Desired opposite: $\bar{b} = 0$.
- Check current node: Does prefix `1100` have a child on branch $0$?
  - The number is $25$ ($11001_2$), whose bit 0 is $1$.
  - Branch $0$ is missing!
- Decision:
  - Forced to take Branch $1$.
  - Bit contribution: $+0$.
  - Cumulative XOR: $28 + 0 = \mathbf{28}$.
  - Reached leaf node: Value $25$.

---

### Terminal Evaluation:
Query with $x = 5$ paired with $y = 25$ produces maximal XOR $5 \oplus 25 = \mathbf{28}$.

---

## 4. Complete Execution Trace

| Bit Level $i$ | Place Value $2^i$ | Value Bit $x_i$ | Desired Bit $\bar{x}_i$ | Trie Branch Available? | Branch Chosen | Bit Set in XOR? | Cumulative XOR |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **4** | $16$ | $0$ | **$1$** | **Yes** (Node `1`) | $1$ | **Yes (+16)** | $16$ |
| **3** | $8$ | $0$ | **$1$** | **Yes** (Node `11`) | $1$ | **Yes (+8)** | $24$ |
| **2** | $4$ | $1$ | **$0$** | **Yes** (Node `110`) | $0$ | **Yes (+4)** | $28$ |
| **1** | $2$ | $0$ | $1$ | **No** (only `0` exists) | $0$ | No (+0) | $28$ |
| **0** | $1$ | $1$ | $0$ | **No** (only `1` exists) | $1$ | No (+0) | **$28$** |

---

## 5. Boundary Cases & Failure Modes

- **Single Element ($nums = [0]$):** Paired with itself: $0 \oplus 0 = \mathbf{0}$.
- **All Equal Numbers ($nums = [4, 4, 4]$):** Any pair yields $4 \oplus 4 = \mathbf{0}$.
- **Numbers with Disjoint Bits ($nums = [1, 2]$):** $01_2 \oplus 10_2 = 11_2 = \mathbf{3}$.
- **Large Numbers Up to $2^{31}-1$:** The 31-bit search depth handles full signed 32-bit positive integers without overflow.

---

## 6. Traps & Common Anti-Patterns

- **Brute-Force Pair Comparison ($O(N^2)$):** Comparing all pairs takes $O(N^2)$ time. For $N = 2 \times 10^5$, $N^2 = 4 \times 10^{10}$ operations, which causes severe Time Limit Exceeded. The Trie solution processes each element in $31$ operations, totaling $\approx 6 \times 10^6$ operations.
- **Fixed-Depth Bit Traversal:** Hardcoding bit count to less than 30 truncates large numbers ($nums[i] \le 2^{31}-1$). The Trie must iterate from bit 30 down to 0.
- **Dynamic Memory Overhead:** In Python or Java, creating dynamic node objects can be optimized with flat integer array trees (`trie[node][bit]`), reducing cache misses and execution time.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Let $B = 31$ be the number of bits in non-negative 32-bit integers.
  - Inserting $N$ numbers into the Trie takes $O(N \cdot B)$ time.
  - Querying the Trie for each of the $N$ numbers takes $O(N \cdot B)$ time.
  - Total Time: $\mathcal{O}(B \cdot N) = \mathcal{O}(N)$. For $N = 2 \times 10^5$, $31 \times 200000 \approx 6.2 \times 10^6$ operations (executes in $\approx 100$ ms).
- **Auxiliary Space Complexity:**
  - The Trie contains at most $N \cdot B$ nodes.
  - Total Auxiliary Space: $\mathcal{O}(B \cdot N) = \mathcal{O}(N)$.
