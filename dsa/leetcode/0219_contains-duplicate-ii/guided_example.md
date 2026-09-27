# Guided Example: Contains Duplicate II

We trace the step-by-step fixed-capacity sliding window hash set and last-seen index mapping on representative proximity-constrained duplicate searches:

- **Input:** $\text{nums} = [1, 2, 3, 1], \quad k = 3$
- **Required output:** `true` (Elements at index $0$ and index $3$ have equal value $1$, and $|0 - 3| = 3 \le 3$)
- **Exceeded Distance Instance:** $\text{nums} = [1, 2, 3, 1, 2, 3], \quad k = 2 \implies \text{false}$ (Duplicate values are separated by distance 3, exceeding $k = 2$)
- **Immediate Neighbor Instance:** $\text{nums} = [1, 0, 1, 1], \quad k = 1 \implies \text{true}$ (Duplicate pair at indices 2 and 3 with distance $1 \le 1$)
- **Zero Distance Parameter:** $k = 0 \implies \text{false}$ (Distinct indices require $|i - j| \ge 1 > 0$)

This instance demonstrates the fixed-window set pattern ($\text{capacity} \le k$), proves why maintaining only the last $k$ elements achieves $O(N)$ time with $O(\min(N, k))$ auxiliary space, compares window eviction with last-seen index tracking, and highlights distance boundary invariants.

---

## 1. Instance & Teaching Goal

Given an integer array $\text{nums} = [1, 2, 3, 1]$ and an integer $k = 3$:
Determine whether there exist **two distinct indices** $i$ and $j$ such that:
$$
\text{nums}[i] == \text{nums}[j] \quad \text{and} \quad |i - j| \le k
$$

In LeetCode 217 (Contains Duplicate), duplicates could appear anywhere in the array.
Here, duplicates are valid **only if their index difference is at most $k$**.
- A naive comparison evaluates all pairs $(i, j)$ with $|i - j| \le k$, taking $O(N \cdot k)$ time.
- A **Sliding Window Hash Set** of size at most $k$ maintains the active elements in the interval $[i - k, i - 1]$. If the current element $\text{nums}[i]$ is already present in the window, a valid pair has been found in $O(1)$ time!
- An element falling out of the window ($i - k$) is evicted, ensuring the set never exceeds $k$ elements.

---

## 2. Conceptual Foundation & Invariants

### Method A: Fixed-Size Sliding Window Set ($O(\min(N, k))$ Space)
Maintain a set `window`:
For index $i$ from $0$ to $N - 1$:
1. **Evict Out-of-Window Elements:**
   If $i > k$:
   $$
   \text{window}.\text{remove}(\text{nums}[i - k - 1])
   $$
2. **Proximity Check:**
   If $\text{nums}[i] \in \text{window}$:
   Return `true`! (A duplicate exists within distance $\le k$).
3. **Incorporate Current Element:**
   $$
   \text{window}.\text{add}(\text{nums}[i])
   $$
If the loop finishes, return `false`.

### Method B: Last-Seen Index Map
Store `last_seen = {}` mapping value $\to$ most recent index:
For each index $i$ and value $x$:
- If $x \in \text{last\_seen}$ and $i - \text{last\_seen}[x] \le k$: return `true`.
- Update $\text{last\_seen}[x] = i$.

> **Invariant.** At index $i$, the set `window` contains precisely the elements $\{\text{nums}[j] \mid \max(0, i - k) \le j < i\}$. The size of `window` is strictly bounded by $k$.

---

## 3. Step-by-Step Worked Execution

We trace the sliding window on $\text{nums} = [1, 2, 3, 1]$ with $k = 3$:

### Step 0: Initial Setup
- $k = 3$.
- $\text{window} = \emptyset$.

---

### Step 1: Index $i = 0$ ($x = 1$)
- Eviction check: $i = 0 \not> 3$. No eviction.
- Proximity check: $1 \in \text{window} \implies$ False.
- Insert $x$: $\text{window} = \{1\}$.

---

### Step 2: Index $i = 1$ ($x = 2$)
- Eviction check: $i = 1 \not> 3$. No eviction.
- Proximity check: $2 \in \text{window} \implies$ False.
- Insert $x$: $\text{window} = \{1, 2\}$.

---

### Step 3: Index $i = 2$ ($x = 3$)
- Eviction check: $i = 2 \not> 3$. No eviction.
- Proximity check: $3 \in \text{window} \implies$ False.
- Insert $x$: $\text{window} = \{1, 2, 3\}$.

---

### Step 4: Index $i = 3$ ($x = 1$, Duplicate Found!)
- Eviction check: $i = 3 \not> 3$. No eviction.
- Proximity check: $1 \in \text{window} \implies$ **True!**
- Element $1$ exists within the active distance-$3$ window (it was placed at index $0$, and $|3 - 0| = 3 \le 3$).
- **Return `true`.**

---

## 4. Complete Execution Trace

```text
nums = [1, 2, 3, 1], k = 3

i = 0: x = 1 -> not in window -> window = {1}
i = 1: x = 2 -> not in window -> window = {1, 2}
i = 2: x = 3 -> not in window -> window = {1, 2, 3}
i = 3: x = 1 -> 1 IS IN WINDOW! -> RETURN TRUE
```

| Index $i$ | Element $x$ | Evicted Element ($i - k - 1$) | Window State Before Check | Proximity Match? | Return Action |
|:---:|:---:|:---:|:---|:---:|:---:|
| 0 | 1 | - | $\emptyset$ | No | Add 1 |
| 1 | 2 | - | $\{1\}$ | No | Add 2 |
| 2 | 3 | - | $\{1, 2\}$ | No | Add 3 |
| **3** | **1** | **-** | **$\{1, 2, 3\}$** | **Yes (1 in window)** | **`true` (Distance $3 \le 3$)** |

### Contrast: Exceeded Distance in $[1, 2, 3, 1, 2, 3], k = 2$
- $i = 0$: add 1 $\implies \{1\}$
- $i = 1$: add 2 $\implies \{1, 2\}$
- $i = 2$: add 3 $\implies \{1, 2, 3\}$
- $i = 3$ ($x = 1$): Evict $\text{nums}[3 - 2 - 1] = \text{nums}[0] = 1$!
  - Window becomes $\{2, 3\}$.
  - $1 \notin \{2, 3\}$!
  - Add 1 $\implies \{2, 3, 1\}$.
- Element 1 at index 3 is separated by distance $3 > 2$ from index 0, so it is correctly rejected!

---

## 5. Algorithmic Correctness

**Soundness.** Every element in `window` was inserted at an index $j$ satisfying $i - k \le j < i$, meaning $|i - j| \le k$. If $\text{nums}[i] \in \text{window}$, then $\text{nums}[i] == \text{nums}[j]$ with $|i - j| \le k$, satisfying both conditions.

**Completeness.** Suppose there exists a valid pair with $\text{nums}[i] == \text{nums}[j]$ and $i - j \le k$ ($j < i$). Because elements are only evicted when the cursor reaches index $j + k + 1$, element $\text{nums}[j]$ remains in `window` when index $i \le j + k$ is processed. Thus, the duplicate is guaranteed to be detected.

---

## 6. Traps This Instance Exposes

- **Evicting at $i \ge k$ vs $i > k$:** If $k = 3$, at index $i = 3$ the window must contain indices $0, 1, 2$ (length 3). Element at index 0 must NOT be removed until index $i = 4$ ($4 - 3 - 1 = 0$). Evicting too early drops valid distance-$k$ pairs.
- **Using $k = 0$:** Distinct indices require $i \ne j \implies |i - j| \ge 1$. If $k = 0$, no two distinct indices can satisfy $|i - j| \le 0$. The method must immediately return `false`.
- **Duplicate Elements Inside Window:** If `window` is a set and contains duplicate values, removing $\text{nums}[i - k - 1]$ might drop an element that also appeared at a later index inside the window. Using the **Last-Seen Index Map** (`last_seen[x] = i`) is completely immune to this duplicate eviction issue because it stores the *most recent* index.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N$ is the number of elements in `nums`. Each element is added and removed from the hash set at most once, with $O(1)$ average hash table operations per step.
- **Auxiliary Space Complexity:** $O(\min(N, k))$ auxiliary space for the sliding window set, which never holds more than $k$ elements at any time.