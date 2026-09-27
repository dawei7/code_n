# Guided Example: Lexicographical Numbers

We trace the step-by-step decimal trie preorder traversal without recursion, child descent multiplication ($v \times 10 \le n$), sibling incrementation ($v + 1$), digit-exhaustion backtracking ($v //= 10$ on $v \% 10 == 9$ or $v + 1 > n$), and constant-extra-space iteration on representative numerical ranges:

- **Input:** $n = 13$
- **Required output:** `[1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]`
  - Step-by-step state evolution:
    - Step 1: Emit $1 \implies 1 \times 10 \le 13 \implies$ descend to $10$
    - Step 2: Emit $10 \implies 10 \times 10 > 13 \implies$ advance to sibling $10 + 1 = 11$
    - Step 3: Emit $11 \implies 11 \times 10 > 13 \implies$ advance to sibling $11 + 1 = 12$
    - Step 4: Emit $12 \implies 12 \times 10 > 13 \implies$ advance to sibling $12 + 1 = 13$
    - Step 5: Emit $13 \implies 13 + 1 > 13 \implies$ backtrack up: $13 // 10 = 1$, advance to sibling $1 + 1 = 2$
    - Step 6 to 13: Emits $2, 3, 4, 5, 6, 7, 8, 9$ in order
  - Complete 13-element lexicographical sequence produced
- **Two-Digit Limit:** $n = 20 \implies [1, 10, 11, \dots, 19, 2, 20, 3, \dots, 9]$
- **Single-Digit Range:** $n = 5 \implies [1, 2, 3, 4, 5]$

This instance demonstrates in-place depth-first traversal of an implicit 10-ary prefix tree, mathematically proves why pre-order DFS matches dictionary word sorting, avoids $O(N \log N)$ string conversion or recursion stacks, and achieves $O(N)$ time and $O(1)$ auxiliary space.

---

## 1. Instance & Teaching Goal

Given an integer $n = 13$:
Return all integers in the range $[1, n]$ sorted in **lexicographical order** (as strings):
$$
\text{"1"} < \text{"10"} < \text{"11"} < \text{"12"} < \text{"13"} < \text{"2"} < \text{"3"} < \dots < \text{"9"}
$$
The problem requires $O(N)$ linear time and strictly **$O(1)$ auxiliary memory** (excluding the returned list).

```text
The Implicit 10-Ary Decimal Trie:
               Root
         /   /   \   \
        1   2 ... 9  (10 branches each)
       /
     10 11 12 13 (14..19 exceed n=13)

Lexicographical order is EXACTLY Preorder Depth-First Search:
Visit Node -> Visit Child (v * 10) -> Sibling (v + 1) -> Backtrack (v // 10)

Result: [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]
```

---

## 2. Conceptual Foundation & Invariants

### 1. The Preorder DFS State Machine
We maintain a single integer state variable $v$, initialized to $v = 1$.
At each of the $n$ iterations:
1. Append current $v$ to $ans$.
2. **Transition to the Next Lexicographical Integer:**
   - **Case A (Descend to Smallest Child):**
     If $v \times 10 \le n$:
     $$
     v \leftarrow v \times 10
     $$
     (e.g. from $1 \to 10$, $10 \to 100$).
   - **Case B (Advance to Sibling or Backtrack to Ancestor):**
     If $v \times 10 > n$, we cannot descend. We attempt to increment $v \leftarrow v + 1$.
     However, if $v \% 10 == 9$ (all children under parent exhausted) OR $v + 1 > n$ (sibling exceeds ceiling $n$):
     We must ascend up the tree:
     $$
     \text{while } (v \% 10 == 9 \lor v + 1 > n): \quad v \leftarrow \lfloor v / 10 \rfloor
     $$
     Then take the unvisited sibling:
     $$
     v \leftarrow v + 1
     $$

> **Invariant.** The sequence of generated integers strictly corresponds to the preorder traversal order of the 10-ary decimal tree restricted to nodes $\le n$.

---

## 3. Step-by-Step Worked Execution

We trace $n = 13$:
Initial: $v = 1, ans = []$.

---

### Step 1: $v = 1$
- Emit: $ans = [\mathbf{1}]$.
- Check descent: $1 \times 10 = 10 \le 13$ (**True**).
- Descend:
  $$
  v \leftarrow 1 \times 10 = \mathbf{10}
  $$

---

### Step 2: $v = 10$
- Emit: $ans = [1, \; \mathbf{10}]$.
- Check descent: $10 \times 10 = 100 > 13$ (**False**).
- Advance:
  - $10 \% 10 = 0 \ne 9$ and $10 + 1 = 11 \le 13$. No backtracking needed.
  $$
  v \leftarrow 10 + 1 = \mathbf{11}
  $$

---

### Step 3: $v = 11$
- Emit: $ans = [1, 10, \; \mathbf{11}]$.
- Descent: $110 > 13$ (False).
- Advance: $11 + 1 = 12 \le 13 \implies v \leftarrow \mathbf{12}$.

---

### Step 4: $v = 12$
- Emit: $ans = [1, 10, 11, \; \mathbf{12}]$.
- Descent: $120 > 13$ (False).
- Advance: $12 + 1 = 13 \le 13 \implies v \leftarrow \mathbf{13}$.

---

### Step 5: $v = 13$ — Boundary Backtracking Triggered!
- Emit: $ans = [1, 10, 11, 12, \; \mathbf{13}]$.
- Descent: $130 > 13$ (False).
- Check sibling condition:
  $$
  v + 1 = 14 > 13 \implies \text{Exceeds limit } n!
  $$
- **Backtrack:**
  $$
  v \leftarrow \lfloor 13 / 10 \rfloor = \mathbf{1}
  $$
- Check parent $v = 1$:
  - $1 \% 10 = 1 \ne 9$ and $1 + 1 = 2 \le 13$ (Valid!).
- Advance parent to next root branch:
  $$
  v \leftarrow 1 + 1 = \mathbf{2}
  $$

---

### Step 6 to 13: Processing Roots $2 \dots 9$
- For each $v \in [2, 9]$:
  - $v \times 10 \ge 20 > 13$ (Cannot descend).
  - $v + 1 \le 10$, but since $v < 9$, advance $v \leftarrow v + 1$.
  - Sequentially emits $2, 3, 4, 5, 6, 7, 8, 9$.

---

### Step 14: Termination
Exactly $n = 13$ elements emitted. Return:
$$
\mathbf{[1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]}
$$

---

## 4. Complete Execution Trace

```text
n = 13
v = 1: append 1  -> 1*10 <= 13   -> v = 10
v = 10: append 10 -> 10*10 > 13   -> v = 11
v = 11: append 11 -> 11*10 > 13   -> v = 12
v = 12: append 12 -> 12*10 > 13   -> v = 13
v = 13: append 13 -> 13+1 > 13    -> backtrack: v=13//10=1 -> v = 1+1 = 2
v = 2: append 2  -> v = 3
v = 3: append 3  -> v = 4
...
v = 9: append 9  -> 13 elements collected -> Terminate
```

| Step | Value Emitted $v$ | Branch Evaluated | Decision Rule Applied | Next State $v$ | Total Collected |
|:---:|:---:|:---:|:---|:---:|:---:|
| 1 | 1 | $1 \times 10 \le 13$ | Descend to child | 10 | 1 |
| 2 | 10 | $10 \times 10 > 13$ | Sibling $+1$ | 11 | 2 |
| 3 | 11 | $11 \times 10 > 13$ | Sibling $+1$ | 12 | 3 |
| 4 | 12 | $12 \times 10 > 13$ | Sibling $+1$ | 13 | 4 |
| **5** | **13** | **$13 + 1 > 13$** | **Backtrack: $13 // 10 = 1$, then $+1$** | **2** | **5** |
| 6 | 2 | $20 > 13$ | Sibling $+1$ | 3 | 6 |
| 7..13| $3 \dots 9$ | $> 13$ | Sibling $+1$ | $4 \dots 10$ | **13 (Final)** |

---

## 5. Algorithmic Correctness

**Soundness.** Lexicographical string comparison between integers $u$ and $w$ checks characters from left to right. If $w = u \cdot 10 + d$, then $w$ begins with the exact prefix $u$, so $u < w < u + 1$ lexicographically. Thus, exploring $u \cdot 10$ before $u + 1$ precisely mimics alphabetical order. Ascending when digits reach 9 or exceed $n$ ensures every path stays within valid bounds $[1, n]$.

**Completeness.** The decimal trie contains all positive integers. By performing an exhaustive DFS traversal with pruning at $> n$, every integer in $[1, n]$ is visited exactly once, with zero omissions or duplicates.

---

## 6. Traps This Instance Exposes

- **Converting to String and Sorting:** Converting all $N$ numbers to strings and sorting them costs $O(N \log N)$ time and $O(N)$ string memory, failing the problem's strict $O(N)$ time and $O(1)$ extra space requirements.
- **Recursive Call Stack:** A standard recursive DFS uses $O(\log_{10} N)$ stack space. Simulating the traversal iteratively with scalar $v$ achieves true $O(1)$ auxiliary space.
- **Double Backtracking Condition:** Backtracking must occur both when $v \% 10 == 9$ (end of digit block) AND when $v + 1 > n$ (boundary ceiling reached). Omitting either condition causes out-of-bounds numbers or infinite loops.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N = n$.
  - Exactly $N$ numbers are appended to the answer list.
  - In each step, $v$ either multiplies by 10 or divides by 10.
  - Across the entire traversal, each digit is appended and removed at most twice.
  - Amortized cost per number is $O(1)$, yielding strictly $O(N)$ total time.
- **Auxiliary Space Complexity:** $O(1)$ auxiliary space, storing only the single integer scalar $v$.
