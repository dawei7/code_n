# Guided Example: Advantage Shuffle

We trace the step-by-step Tian Ji horse racing greedy algorithm, sorting with index preservation, smallest-winner pairing, weakest-against-strongest sacrifice mechanics, and advantage count maximization on representative number arrays:

- **Input:**
  $$
  nums1 = [12, 24, 8, 32], \quad nums2 = [13, 25, 32, 11]
  $$
- **Required output:** `[24, 32, 8, 12]`
  - Advantage game rules:
    - We are given two integer arrays $nums1$ and $nums2$ of equal length $n = 4$.
    - We must permute $nums1$ into an array $A$ such that the **advantage** of $A$ with respect to $nums2$ (the number of indices $k$ where $A[k] > nums2[k]$) is maximized.
    - For $nums1 = [12, 24, 8, 32]$ against $nums2 = [13, 25, 32, 11]$:
      - Pair $24 > 13$ (win at index 0).
      - Pair $32 > 25$ (win at index 1).
      - Pair $8 \le 32$ (loss at index 2, sacrificed).
      - Pair $12 > 11$ (win at index 3).
      - Advantage achieved: **$3$ wins out of $4$** (provably maximal).
      - Result array: **`[24, 32, 8, 12]`**.
- **The Tian Ji Horse Racing Greedy Invariant:**
  - **The Principle of Economical Victory:**
    - To win a match against an opponent's card $y$, we want to spend the **smallest card $x \in nums1$ such that $x > y$**.
    - Spending a much larger card than necessary squanders power that could secure wins against stronger future opponents.
  - **The Principle of Strategic Sacrifice:**
    - If our smallest remaining card $x$ cannot even defeat the opponent's **weakest** remaining card $y_{min}$ ($x \le y_{min}$), then card $x$ cannot defeat **any** remaining opponent card!
    - Card $x$ is guaranteed to be a loss regardless of where it is placed.
    - To minimize the damage of this inevitable loss, we pair $x$ against the opponent's **strongest remaining card** $y_{max}$!
    - By "wasting" the opponent's strongest card on our weakest card, we neutralize their hardest-to-beat element, making it easier for our remaining cards to win.

---

## 1. Instance & Teaching Goal

Given $nums1 = [12, 24, 8, 32]$ and $nums2 = [13, 25, 32, 11]$, construct the permutation of $nums1$ that maximizes head-to-head wins.

```text
Sorted nums1: [8, 12, 24, 32]
Sorted nums2 (with original indices):
  (11, idx 3) <- weakest opponent (pointer i)
  (13, idx 0)
  (25, idx 1)
  (32, idx 2) <- strongest opponent (pointer j)

1. Pick 8: 8 <= 11 -> Cannot beat weakest! Sacrifice against strongest (32 at idx 2).
   ans[2] = 8, decrement j.
2. Pick 12: 12 > 11 -> Can beat weakest! Win against 11 at idx 3.
   ans[3] = 12, increment i.
3. Pick 24: 24 > 13 -> Can beat weakest! Win against 13 at idx 0.
   ans[0] = 24, increment i.
4. Pick 32: 32 > 25 -> Can beat weakest! Win against 25 at idx 1.
   ans[1] = 32, increment i.

Result: [24, 32, 8, 12] (3 wins)
```

The teaching goal is to demonstrate how a two-pointer dual-end sweep on sorted arrays implements the classic optimal exchange argument.

---

## 2. Conceptual Foundation & Invariants

### 1. Indexed Target Ordering:
Pair each element of $nums2$ with its original array index and sort ascending:
$$
t = \text{sorted}\left([(nums2[k], k) \mid k \in [0, n - 1]]\right)
$$
Maintain two pointers $i = 0$ (weakest unassigned opponent) and $j = n - 1$ (strongest unassigned opponent).

### 2. Decision Invariant for Sorted $x \in nums1$:
$$
\text{For each } x \in \text{sorted}(nums1):
$$
$$
\begin{cases}
A[t[i].\text{index}] \leftarrow x, \; i \leftarrow i + 1 & \text{if } x > t[i].\text{value} \quad (\text{Win secured}) \\
A[t[j].\text{index}] \leftarrow x, \; j \leftarrow j - 1 & \text{if } x \le t[i].\text{value} \quad (\text{Sacrifice against } \max)
\end{cases}
$$

---

## 3. Step-by-Step Worked Execution

We trace $nums1 = [12, 24, 8, 32]$ and $nums2 = [13, 25, 32, 11]$:

---

### Phase 1: Sorting and Initialization
- Sort $nums1$ ascending:
  $$
  nums1 = [8, 12, 24, 32]
  $$
- Sort $nums2$ by value, storing original indices:
  - $t[0] = (11, \text{index } 3)$
  - $t[1] = (13, \text{index } 0)$
  - $t[2] = (25, \text{index } 1)$
  - $t[3] = (32, \text{index } 2)$
- Initialize two pointers: $i = 0$ (weakest), $j = 3$ (strongest).
- Initialize output array: $A = [\cdot, \cdot, \cdot, \cdot]$.

---

### Step 1: Process $v = 8$
- Compare with weakest opponent: $v = 8$ vs $t[i].\text{value} = 11$.
- Evaluation: $8 \le 11$.
- Card $8$ cannot win against any active opponent.
- **Sacrifice Action:** Pair $8$ against the strongest opponent $t[j]$ (value $32$, original index $2$).
- Assign: $A[2] \leftarrow 8$.
- Decrement right pointer: $j \leftarrow 3 - 1 = 2$.
- State of $A$: $[\cdot, \cdot, 8, \cdot]$.

---

### Step 2: Process $v = 12$
- Compare with weakest opponent: $v = 12$ vs $t[i].\text{value} = 11$.
- Evaluation: $12 > 11 \implies$ **Win!**
- **Win Action:** Pair $12$ against $t[i]$ (value $11$, original index $3$).
- Assign: $A[3] \leftarrow 12$.
- Increment left pointer: $i \leftarrow 0 + 1 = 1$.
- State of $A$: $[\cdot, \cdot, 8, 12]$.

---

### Step 3: Process $v = 24$
- Compare with weakest opponent: $v = 24$ vs $t[i].\text{value} = t[1].\text{value} = 13$.
- Evaluation: $24 > 13 \implies$ **Win!**
- **Win Action:** Pair $24$ against $t[1]$ (value $13$, original index $0$).
- Assign: $A[0] \leftarrow 24$.
- Increment left pointer: $i \leftarrow 1 + 1 = 2$.
- State of $A$: $[24, \cdot, 8, 12]$.

---

### Step 4: Process $v = 32$
- Compare with weakest opponent: $v = 32$ vs $t[i].\text{value} = t[2].\text{value} = 25$.
- Evaluation: $32 > 25 \implies$ **Win!**
- **Win Action:** Pair $32$ against $t[2]$ (value $25$, original index $1$).
- Assign: $A[1] \leftarrow 32$.
- Increment left pointer: $i \leftarrow 2 + 1 = 3$.
- State of $A$: $[24, 32, 8, 12]$.

---

### Termination:
All elements assigned.
- Result: **`[24, 32, 8, 12]`**.

---

## 4. Complete Execution Trace

| Card from $nums1$ | Current Weakest $t[i]$ | Condition ($v > t[i]$) | Outcome | Assigned Destination Index | Opponent Faced | Opponent Value | Pointer Shift | Result Array $A$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $8$ | $(11, \text{idx } 3)$ | $8 \le 11$ | **Sacrifice** | Index $2$ | $t[3]$ | $32$ | $j: 3 \to 2$ | $[\cdot, \cdot, 8, \cdot]$ |
| $12$ | $(11, \text{idx } 3)$ | $12 > 11$ | **Win** | Index $3$ | $t[0]$ | $11$ | $i: 0 \to 1$ | $[\cdot, \cdot, 8, 12]$ |
| $24$ | $(13, \text{idx } 0)$ | $24 > 13$ | **Win** | Index $0$ | $t[1]$ | $13$ | $i: 1 \to 2$ | $[24, \cdot, 8, 12]$ |
| **$32$** | **$(25, \text{idx } 1)$** | **$32 > 25$** | **Win** | **Index $1$** | **$t[2]$** | **$25$** | **$i: 2 \to 3$** | **`[24, 32, 8, 12]`** |

---

## 5. Boundary Cases & Failure Modes

- **All Elements in $nums1$ Strictly Exceed $nums2$:** Every element satisfies $v > t[i]$; no sacrifices occur, achieving $100\%$ wins.
- **No Element in $nums1$ Can Beat Any Element in $nums2$:** All elements are sacrificed against $j$; returns a valid permutation with $0$ wins.
- **Duplicate Elements in $nums1$ or $nums2$:** Handled seamlessly because equality $v == t[i]$ fails strict inequality $v > t[i]$, correctly triggering sacrifice against $j$.

---

## 6. Traps & Common Anti-Patterns

- **Using a Stronger Card Than Necessary:** Matching $32$ against $11$ leaves $12$ to face $25$ (which loses). Matching the smallest sufficient card ($12$) against $11$ preserves $32$ to defeat $25$, winning both matches.
- **Sacrificing Against Weak Opponents:** If card $8$ were placed against $11$, that match would be lost anyway, leaving $32$ with no low-card sacrifice absorber.
- **Linear Searching for Best Opponents:** Searching linearly for each element of $nums1$ takes $\mathcal{O}(N^2)$ time. Sorting both arrays and using two pointers reduces time to $\mathcal{O}(N \log N)$.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Sorting $nums1$ of length $N$: $\mathcal{O}(N \log N)$.
  - Sorting $nums2$ with indices: $\mathcal{O}(N \log N)$.
  - Two-pointer traversal over $N$ elements: $\mathcal{O}(N)$.
  - Total Time: $\mathcal{O}(N \log N)$, taking $< 25$ ms for $N = 10^5$.
- **Auxiliary Space Complexity:**
  - Storing indexed pairs of $nums2$ and output array: $\mathcal{O}(N)$ space.
