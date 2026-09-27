# Guided Example: Longest Increasing Subsequence

We trace the step-by-step patience sorting tails array maintenance, greedy tail minimization, logarithmic bisection insertion (`bisect_left`), and subsequence length expansion on representative integer sequences:

- **Input:** $\text{nums} = [10, 9, 2, 5, 3, 7, 101, 18]$
- **Required output:** $4$ (One optimal strictly increasing subsequence is $[2, 3, 7, 101]$ or $[2, 3, 7, 18]$, with length $4$)
- **Identical Elements Instance:** $\text{nums} = [7, 7, 7, 7] \implies 1$ (Strict inequality requirement; identical elements overwrite the length-1 tail)
- **Decreasing Sequence Base Case:** $\text{nums} = [5, 4, 3, 2, 1] \implies 1$ (Each element replaces $\text{tails}[0]$; length never exceeds 1)
- **Already Sorted Optimal Sequence:** $\text{nums} = [1, 2, 3, 4] \implies 4$ (Every element appends to `tails`)

This instance demonstrates Patience Sorting with binary search, mathematically proves why the array of minimum subsequence tails is strictly increasing ($\text{tails}[0] < \text{tails}[1] < \dots$), contrasts the $O(N^2)$ dynamic programming recurrence against the optimal $O(N \log N)$ bisection approach, and analyzes auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given an integer array:
$$
\text{nums} = [10, 9, 2, 5, 3, 7, 101, 18]
$$
Find the length of the **longest strictly increasing subsequence (LIS)**.
Subsequences need not be contiguous:
- Candidate: $[10, 101]$ (length 2)
- Candidate: $[2, 5, 7, 101]$ (length 4)
- Candidate: $[2, 3, 7, 18]$ (length 4)
Maximum possible length: $\mathbf{4}$.

### Why the $O(N^2)$ DP is Suboptimal
Standard DP defines $dp[i]$ as the length of the LIS ending at index $i$:
$$
dp[i] = 1 + \max_{j < i, \, \text{nums}[j] < \text{nums}[i]} dp[j]
$$
This requires scanning all preceding $j < i$, costing $O(N^2)$ time.
By reframing the problem as **Patience Sorting** (tracking minimum tail values for each length), we can use binary search to determine each element's contribution in $O(\log N)$ time, achieving **$O(N \log N)$** overall.

---

## 2. Conceptual Foundation & Invariants

### The `tails` Array Definition
Let $\text{tails}[k]$ be the **smallest ending value** (tail) of all valid increasing subsequences of length $k + 1$ found so far.

```text
Suppose subsequences of length 2 found so far are:
[10, 101] -> tail = 101
[2, 5]    -> tail = 5
[2, 3]    -> tail = 3

The smallest tail for length 2 is 3.
Storing 3 is optimal because any future number > 3 can extend this subsequence,
whereas a number like 4 could extend [2, 3] but NOT [2, 5] or [10, 101]!
```

### Strict Monotonicity Invariant:
$$
\text{tails}[0] < \text{tails}[1] < \text{tails}[2] < \dots < \text{tails}[L-1]
$$
**Proof:**
Suppose an increasing subsequence of length $k + 1$ ends at value $T = \text{tails}[k]$.
Its penultimate element $T'$ forms an increasing subsequence of length $k$ with $T' < T$.
By definition, $\text{tails}[k - 1]$ is the *minimum* possible tail of all length-$k$ subsequences, so:
$$
\text{tails}[k - 1] \le T' < T = \text{tails}[k] \implies \text{tails}[k - 1] < \text{tails}[k]
$$
Because `tails` is strictly sorted, we can use binary search (`bisect_left`)!

### Transition Protocol for Number $x$:
1. Binary search index $idx$ in `tails` such that $\text{tails}[idx] \ge x$ (`bisect_left`):
   - **Case 1 ($idx == \text{len}(\text{tails})$):**
     $x$ is strictly greater than all recorded tails.
     $x$ extends the longest subsequence found so far:
     $$
     \text{tails.append}(x)
     $$
   - **Case 2 ($idx < \text{len}(\text{tails})$):**
     $x$ is $\le \text{tails}[idx]$.
     Update $\text{tails}[idx] \leftarrow x$ to establish a strictly smaller (or equal) tail for length $idx + 1$.
2. The length of the LIS is $\text{len}(\text{tails})$.

> **Invariant.** After processing each element, `tails[k]` stores the minimal possible tail value for any increasing subsequence of length $k + 1$ formed by elements seen so far.

---

## 3. Step-by-Step Worked Execution

We trace the algorithm on $\text{nums} = [10, 9, 2, 5, 3, 7, 101, 18]$:
Initialize `tails = []`.

---

### Step 1: Process $x = 10$
- `tails` is empty.
- Append $10$: $\text{tails} = [10]$.
- Longest length: 1.

---

### Step 2: Process $x = 9$
- Binary search $9$ in $[10] \implies idx = 0$ ($9 < 10$).
- Greedily replace $\text{tails}[0] = 9$.
- $\text{tails} = [9]$. (A length-1 subsequence ending in 9 is better than one ending in 10).

---

### Step 3: Process $x = 2$
- Binary search $2$ in $[9] \implies idx = 0$ ($2 < 9$).
- Replace $\text{tails}[0] = 2$.
- $\text{tails} = [2]$.

---

### Step 4: Process $x = 5$
- Binary search $5$ in $[2] \implies idx = 1$ ($5 > 2$).
- $idx == \text{len}(\text{tails}) \implies$ Append $5$!
- $\text{tails} = [2, 5]$.
- Longest length: 2 (Subsequence $[2, 5]$).

---

### Step 5: Process $x = 3$
- Binary search $3$ in $[2, 5] \implies idx = 1$ ($2 < 3 < 5$).
- Replace $\text{tails}[1] = 3$.
- $\text{tails} = [2, 3]$.
- (Subsequence $[2, 3]$ now represents the best length-2 chain).

---

### Step 6: Process $x = 7$
- Binary search $7$ in $[2, 3] \implies idx = 2$ ($7 > 3$).
- Append $7$: $\text{tails} = [2, 3, 7]$.
- Longest length: 3 (Subsequence $[2, 3, 7]$).

---

### Step 7: Process $x = 101$
- Binary search $101$ in $[2, 3, 7] \implies idx = 3$ ($101 > 7$).
- Append $101$: $\text{tails} = [2, 3, 7, 101]$.
- Longest length: 4 (Subsequence $[2, 3, 7, 101]$).

---

### Step 8: Process $x = 18$
- Binary search $18$ in $[2, 3, 7, 101] \implies idx = 3$ ($7 < 18 < 101$).
- Replace $\text{tails}[3] = 18$.
- $\text{tails} = [2, 3, 7, 18]$.
- (Length remains 4, but tail of length-4 sequence is improved from 101 down to 18).

---

### Final Result
Total elements in `tails`: $\text{len}(\text{tails}) = \mathbf{4}$.

---

## 4. Complete Execution Trace

```text
nums = [10, 9, 2, 5, 3, 7, 101, 18]

x = 10:  append 10        -> tails = [10]
x = 9:   replace tails[0] -> tails = [9]
x = 2:   replace tails[0] -> tails = [2]
x = 5:   append 5         -> tails = [2, 5]
x = 3:   replace tails[1] -> tails = [2, 3]
x = 7:   append 7         -> tails = [2, 3, 7]
x = 101: append 101       -> tails = [2, 3, 7, 101]
x = 18:  replace tails[3] -> tails = [2, 3, 7, 18]

Length of tails: 4
```

| Step $i$ | Current Number $x$ | Insertion Index $idx$ (`bisect_left`) | Operation Performed | `tails` Array After Step | Current LIS Length |
|:---:|:---:|:---:|:---|:---|:---:|
| 1 | 10 | 0 | Append 10 | `[10]` | 1 |
| 2 | 9 | 0 | Replace $\text{tails}[0]$ with 9 | `[9]` | 1 |
| 3 | 2 | 0 | Replace $\text{tails}[0]$ with 2 | `[2]` | 1 |
| **4** | **5** | **1** | **Append 5** | **`[2, 5]`** | **2** |
| 5 | 3 | 1 | Replace $\text{tails}[1]$ with 3 | `[2, 3]` | 2 |
| **6** | **7** | **2** | **Append 7** | **`[2, 3, 7]`** | **3** |
| **7** | **101** | **3** | **Append 101** | **`[2, 3, 7, 101]`** | **4** |
| 8 | 18 | 3 | Replace $\text{tails}[3]$ with 18 | `[2, 3, 7, 18]` | **4** |
| **End** | - | - | - | **Final length: 4** | **$\mathbf{4}$** |

---

## 5. Algorithmic Correctness

**Soundness.** Every element in `tails` corresponds to the actual tail of an existing strictly increasing subsequence. When an element is appended, it is strictly greater than the tail of length $L - 1$, validly forming a subsequence of length $L$. Replacing $\text{tails}[idx]$ with a smaller value $x$ tightens the lower bound for length $idx + 1$, maintaining the strict monotonicity of `tails`.

**Completeness.** By induction on the sequence length, `tails[k]` maintains the minimum possible ending element for any increasing subsequence of length $k + 1$. Thus, no longer subsequence can ever be missed, and the final length of `tails` equals the exact maximum length of all valid increasing subsequences.

---

## 6. Traps This Instance Exposes

- **`tails` is NOT the LIS Itself:** A common misconception is that `tails` contains the actual subsequence. In this trace, `tails = [2, 3, 7, 18]` happens to match, but on `[2, 5, 3, 1]`, `tails` ends as `[1, 3]`, which was never a valid subsequence in the original order! `tails` accurately tracks **subsequence lengths**, not the original element sequence.
- **Strictly Increasing vs Non-Decreasing:** Because the problem demands *strictly increasing* elements, duplicate values cannot extend a subsequence. Using `bisect_left` ensures an existing equal value is replaced rather than appended. (For non-decreasing LIS, one would use `bisect_right`).
- **Overwriting Tails:** Replacing an element in `tails` does not alter the maximum length achieved so far; it only increases future capacity to extend subsequences.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N \log N)$, where $N$ is the number of elements in `nums`. The outer loop runs $N$ times. In each iteration, binary search (`bisect_left`) over `tails` (of size at most $N$) takes $O(\log N)$ time. Total runtime is strictly $O(N \log N)$.
- **Auxiliary Space Complexity:** $O(N)$ auxiliary memory to store the `tails` array, which contains at most $N$ elements.