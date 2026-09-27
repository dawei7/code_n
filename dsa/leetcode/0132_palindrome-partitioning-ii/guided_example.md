# Guided Example: Palindrome Partitioning II

We trace the step-by-step 1D dynamic programming minimum cut recurrence and 2D palindrome lookups on representative string instances:

- **Input:** $s = \text{"aab"}$
- **Required output:** $1$ (Optimal cut: $\text{"aa"} \mid \text{"b"}$, requiring $1$ cut)
- **Zero-Cut Base:** $s = \text{"racecar"} \implies 0$ (Entire string is palindromic)

This instance demonstrates formulating the prefix optimal cut state ($DP[i]$ as the minimal cuts for $s[0 \dots i-1]$), anchoring the base case with $DP[0] = -1$ (or direct zero assignment when the entire prefix is palindromic), evaluating suffix transitions ($DP[j] + 1$ for palindromic $s[j \dots i-1]$), and reducing complexity from exponential backtracking down to $O(N^2)$ polynomial time.

---

## 1. Instance & Teaching Goal

Given a string $s = \text{"aab"}$, partition $s$ such that every substring is a palindrome. Return the **minimum cuts** needed for such a partitioning.

Evaluating all valid partitions:
1. $\text{"a"} \mid \text{"a"} \mid \text{"b"}$: requires $2$ cuts (3 parts).
2. $\text{"aa"} \mid \text{"b"}$: requires $1$ cut (2 parts).
The minimum number of cuts needed is $\min(2, 1) = 1$.

While LeetCode 131 asks for *all* partitionings (requiring $O(N \cdot 2^N)$ backtracking), LeetCode 132 asks only for the *scalar minimum* number of cuts.
This optimal substructure enables 1D Dynamic Programming: the minimum cuts for prefix $s[0 \dots i-1]$ depend solely on the minimum cuts of shorter prefixes $s[0 \dots j-1]$ where the suffix $s[j \dots i-1]$ is a palindrome.

---

## 2. Conceptual Foundation & Invariants

### 1D Dynamic Programming Recurrence
Let $N = |s|$.
Let $DP[i]$ represent the minimum cuts needed to partition the prefix $s[0 \dots i-1]$ (length $i$).

1. **Initialization:**
   Each character isolated requires at most $i - 1$ cuts.
   Initialize:
   $$
   DP[i] = i - 1 \quad \text{for } i \in [1, N]
   $$
2. **State Transition ($i \in [1, N]$):**
   Examine every possible left split point $j \in [0, i - 1]$:
   - If substring $s[j \dots i - 1]$ is a palindrome:
     - **Case A ($j = 0$):**
       The entire prefix $s[0 \dots i - 1]$ is itself a palindrome! No cuts needed:
       $$
       DP[i] \leftarrow 0
       $$
     - **Case B ($j > 0$):**
       Place a cut right before $j$, appending the palindromic suffix $s[j \dots i - 1]$ to the optimal partition of prefix $s[0 \dots j - 1]$:
       $$
       DP[i] \leftarrow \min(DP[i], \, DP[j] + 1)
       $$

### Palindrome Precomputation
Precompute an $N \times N$ matrix $\text{is\_pal}[j][k]$:
$$
\text{is\_pal}[j][k] = (s[j] == s[k]) \land (k - j \le 2 \lor \text{is\_pal}[j + 1][k - 1])
$$
allowing $O(1)$ verification of $s[j \dots i-1]$.

> **Invariant.** For every prefix length $i \in [1, N]$, $DP[i]$ stores the mathematically minimum number of cuts needed to decompose $s[0 \dots i-1]$ into valid palindromic substrings.

---

## 3. Step-by-Step Worked Execution

We trace $s = \text{"aab"}$ ($N = 3$, indices $0, 1, 2$):

### Precompute Palindromes for $s = \text{"aab"}$
- Substring $s[0 \dots 0] = \text{"a"}$: Palindrome.
- Substring $s[1 \dots 1] = \text{"a"}$: Palindrome.
- Substring $s[2 \dots 2] = \text{"b"}$: Palindrome.
- Substring $s[0 \dots 1] = \text{"aa"}$: Palindrome ($'a' == 'a'$).
- Substring $s[1 \dots 2] = \text{"ab"}$: Not a palindrome ($'a' \ne 'b'$).
- Substring $s[0 \dots 2] = \text{"aab"}$: Not a palindrome ($'a' \ne 'b'$).

---

### Step 1: Prefix Length $i = 1$ ($s[0 \dots 0] = \text{"a"}$)
- Worst-case cuts: $DP[1] = 0$.
- $j = 0$: $s[0 \dots 0] = \text{"a"}$ is a palindrome.
- Since $j = 0$, entire prefix is a palindrome:
  $$
  DP[1] = 0
  $$

---

### Step 2: Prefix Length $i = 2$ ($s[0 \dots 1] = \text{"aa"}$)
- Worst-case cuts: $DP[2] = 2 - 1 = 1$.
- Check candidates $j \in [0, 1]$:
  - $j = 0$: $s[0 \dots 1] = \text{"aa"}$ is a palindrome!
    - Entire prefix is palindromic $\implies DP[2] = 0$.
  - (No further checks needed, minimum 0 reached).
- $DP[2] = 0$.

---

### Step 3: Prefix Length $i = 3$ ($s[0 \dots 2] = \text{"aab"}$)
- Worst-case cuts: $DP[3] = 3 - 1 = 2$.
- Check candidates $j \in [0, 1, 2]$:
  - $j = 0$: $s[0 \dots 2] = \text{"aab"}$ is **not** a palindrome.
  - $j = 1$: $s[1 \dots 2] = \text{"ab"}$ is **not** a palindrome.
  - $j = 2$: $s[2 \dots 2] = \text{"b"}$ is a palindrome!
    - Suffix is palindromic. Cut placed before index 2:
      $$
      \text{cost} = DP[2] + 1 = 0 + 1 = 1
      $$
    - Update: $DP[3] = \min(2, 1) = \mathbf{1}$.

All prefixes evaluated.
Minimum cuts for complete string $s$: $DP[3] = \mathbf{1}$.

---

## 4. Complete Execution Trace

```text
String:          a       a       b
Indices:         0       1       2
Prefix i=1:     "a"      -> Palindrome!                DP[1] = 0
Prefix i=2:     "aa"     -> Palindrome!                DP[2] = 0
Prefix i=3:     "aab"    -> "aa" | "b" (DP[2] + 1)     DP[3] = 0 + 1 = 1
```

| Prefix Length $i$ | Substring $s[0 \dots i-1]$ | Initial Worst-Case | Split Index $j$ Evaluated | Suffix $s[j \dots i-1]$ | Suffix Palindrome? | Transition Formula | Resulting $DP[i]$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | `"a"` | 0 | $j = 0$ | `"a"` | Yes | Entire prefix | **0** |
| 2 | `"aa"` | 1 | $j = 0$ | `"aa"` | Yes | Entire prefix | **0** |
| 3 | `"aab"` | 2 | $j = 0$ | `"aab"` | No | - | 2 |
| 3 | `"aab"` | 2 | $j = 1$ | `"ab"` | No | - | 2 |
| **3** | **`"aab"`** | **2** | **$j = 2$** | **`"b"`** | **Yes** | **$DP[2] + 1 = 0 + 1$** | **1 (Final)** |

---

## 5. Algorithmic Correctness

**Soundness.** Suppose an optimal partition of $s[0 \dots i-1]$ ends with the palindromic substring $s[j \dots i-1]$. The total cuts required is exactly 1 (the cut separating the prefix from the suffix) plus the cuts required for $s[0 \dots j-1]$. By Bellman's Principle of Optimality, minimizing over all valid split indices $j$ where $s[j \dots i-1]$ is a palindrome guarantees the globally minimum number of cuts.

**Completeness.** All split positions $j \in [0, i-1]$ are considered. If the entire prefix is a palindrome, $j = 0$ directly sets $DP[i] = 0$. No valid partition can be overlooked.

---

## 6. Traps This Instance Exposes

- **Base Case Off-by-One:** An entire prefix that is a palindrome requires $0$ cuts (1 piece). Forgetting the $j = 0$ branch and setting $DP[0] = 0$ with $DP[j] + 1$ would erroneously calculate $0 + 1 = 1$ cut for a single palindrome! Either handle $j = 0$ as a special zero-cut case or initialize $DP[0] = -1$.
- **Redundant Palindrome Recalculation:** Checking if `s[j:i]` is a palindrome via $O(L)$ two-pointer scan inside the nested loop results in $O(N^3)$ total runtime. Precomputing the 2D boolean table or expanding around centers reduces overall time to $O(N^2)$.
- **Single Character Input:** If $|s| = 1$, the loop terminates with $DP[1] = 0$ cuts, correctly handling base cases.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N^2)$, where $N = |s|$. Precomputing the 2D palindrome table takes $O(N^2)$ time. Filling the 1D $DP$ table has $N$ states, each evaluating up to $N$ split positions in $O(1)$ time, taking $\frac{N(N+1)}{2} = O(N^2)$ operations.
- **Auxiliary Space Complexity:** $O(N^2)$ for the 2D palindrome lookup table and $O(N)$ for the 1D $DP$ array.