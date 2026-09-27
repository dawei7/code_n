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

### The Same Instance Through Method B (Last-Seen Index Map)

Method B keeps no window at all. It answers the same instance by remembering, for each value, the most recent index at which that value occurred, and it is the encoding the canonical solution uses.

| Index $i$ | Element $x$ | Map before the check | Computed distance $i - \text{last\_seen}[x]$ | Distance $\le k$? | Action, and the map afterwards |
|:---:|:---:|:---|:---:|:---:|:---|
| 0 | 1 | $\{\}$ | undefined, because $x$ has no stored index yet | No | Store $\text{last\_seen}[1] = 0$; map becomes $\{1 \to 0\}$ |
| 1 | 2 | $\{1 \to 0\}$ | undefined | No | Store $\text{last\_seen}[2] = 1$; map becomes $\{1 \to 0,\ 2 \to 1\}$ |
| 2 | 3 | $\{1 \to 0,\ 2 \to 1\}$ | undefined | No | Store $\text{last\_seen}[3] = 2$; map becomes $\{1 \to 0,\ 2 \to 1,\ 3 \to 2\}$ |
| 3 | 1 | $\{1 \to 0,\ 2 \to 1,\ 3 \to 2\}$ | $3 - 0 = 3$ | Yes, $3 \le 3$ | Return `true` immediately; the map is never read again |

Two facts make this method work with a single stored index per value. First, only the **most recent** occurrence matters: if the newest occurrence of $x$ before index $i$ is farther than $k$ away, every older occurrence is farther still, so no discarded index could ever have produced an acceptable pair. Second, nothing is ever removed, so the eviction boundary $i > k$ that Method A must get exactly right simply does not exist here; the price is that the map may hold one entry per distinct value, which is $O(N)$ rather than $O(\min(N, k))$.

### Contrast: Exceeded Distance in $[1, 2, 3, 1, 2, 3], k = 2$
- $i = 0$: add 1 $\implies \{1\}$
- $i = 1$: add 2 $\implies \{1, 2\}$
- $i = 2$: add 3 $\implies \{1, 2, 3\}$
- $i = 3$ ($x = 1$): Evict $\text{nums}[3 - 2 - 1] = \text{nums}[0] = 1$!
  - Window becomes $\{2, 3\}$.
  - $1 \notin \{2, 3\}$!
  - Add 1 $\implies \{2, 3, 1\}$.
- Element 1 at index 3 is separated by distance $3 > 2$ from index 0, so it is correctly rejected!

The remaining indices are worth finishing, because each one rejects for the same reason: the matching occurrence has just been evicted at the very step its partner arrives.

| Index $i$ | Element $x$ | Evicted value $\text{nums}[i - k - 1]$ | Window before the check | Is $x$ in the window? | Window after the step |
|:---:|:---:|:---|:---|:---:|:---|
| 0 | 1 | none, because $i - k - 1 = -3$ | $\emptyset$ | No | $\{1\}$ |
| 1 | 2 | none, because $i - k - 1 = -2$ | $\{1\}$ | No | $\{1, 2\}$ |
| 2 | 3 | none, because $i - k - 1 = -1$ | $\{1, 2\}$ | No | $\{1, 2, 3\}$ |
| 3 | 1 | $\text{nums}[0] = 1$ | $\{2, 3\}$ | No: the only earlier $1$ left the window in this very step | $\{2, 3, 1\}$ |
| 4 | 2 | $\text{nums}[1] = 2$ | $\{3, 1\}$ | No: the earlier $2$ sat at index $1$ | $\{3, 1, 2\}$ |
| 5 | 3 | $\text{nums}[2] = 3$ | $\{1, 2\}$ | No: the earlier $3$ sat at index $2$ | $\{1, 2, 3\}$, and the loop ends with `false` |

Every duplicate pair in this array is separated by exactly $3 = k + 1$: the pairs are $(0, 3)$ for value $1$, $(1, 4)$ for value $2$, and $(2, 5)$ for value $3$. Method B reaches the identical verdict by the mirror-image test, since each distance it computes is also $3 > 2$. Removing the eviction step, or evicting with index $i - k$ instead of $i - k - 1$, would keep each partner alive for one extra step and flip this answer to `true` — the single most common way to fail this problem.

---

## 5. Algorithmic Correctness

**Soundness.** Every element in `window` was inserted at an index $j$ satisfying $i - k \le j < i$, meaning $|i - j| \le k$. If $\text{nums}[i] \in \text{window}$, then $\text{nums}[i] == \text{nums}[j]$ with $|i - j| \le k$, satisfying both conditions.

**Completeness.** Suppose there exists a valid pair with $\text{nums}[i] == \text{nums}[j]$ and $i - j \le k$ ($j < i$). Because elements are only evicted when the cursor reaches index $j + k + 1$, element $\text{nums}[j]$ remains in `window` when index $i \le j + k$ is processed. Thus, the duplicate is guaranteed to be detected.

---

## 6. Traps This Instance Exposes

- **Evicting at $i \ge k$ vs $i > k$:** If $k = 3$, at index $i = 3$ the window must contain indices $0, 1, 2$ (length 3). Element at index 0 must NOT be removed until index $i = 4$ ($4 - 3 - 1 = 0$). Evicting too early drops valid distance-$k$ pairs.
- **Using $k = 0$:** Distinct indices require $i \ne j \implies |i - j| \ge 1$. If $k = 0$, no two distinct indices can satisfy $|i - j| \le 0$. The method must immediately return `false`.
- **Duplicate Elements Inside Window:** If `window` is a set and contains duplicate values, removing $\text{nums}[i - k - 1]$ might drop an element that also appeared at a later index inside the window. Using the **Last-Seen Index Map** (`last_seen[x] = i`) is completely immune to this duplicate eviction issue because it stores the *most recent* index.

**A precision about that third trap.** Because the membership test returns `true` before any insert, the window can never hold two copies of one value, so the mis-eviction it warns about cannot actually occur: the search ends at the step where the second copy would have been added. The genuine distinction between the two methods is therefore memory and bookkeeping, not immunity from a corrupted window. The map is still the safer default for this problem, because it removes the eviction boundary from the reasoning altogether and stores exactly the one index that can still matter.

**Alternative formulations, compared on this instance.** All four methods below answer `true` for $\text{nums} = [1, 2, 3, 1]$ with $k = 3$; they differ in cost and in what has to be exactly right.

| Approach | Mechanism | Time | Auxiliary space | Failure mode or tradeoff |
|:---|:---|:---:|:---:|:---|
| All-pairs scan over the distance band | For each $i$, compare $\text{nums}[i]$ with every $\text{nums}[j]$ such that $\max(0, i - k) \le j < i$ | $O(N \cdot k)$ | $O(1)$ | Correct but about $5 \times 10^{9}$ comparisons at the stated limit $N = k = 10^{5}$; the four-element instance conceals that cost entirely |
| Sliding window set (Method A) | Hold the distinct values of $[i - k, i - 1]$, evicting $\text{nums}[i - k - 1]$ once $i > k$ | $O(N)$ | $O(\min(N, k))$ | Leans entirely on the eviction boundary being exactly $i > k$; evicting at $i \ge k$ would discard index $0$ before index $3$ is read and would wrongly answer `false` here |
| Last-seen index map (Method B, the canonical method) | Store the newest index per value and test $i - \text{last\_seen}[x] \le k$ | $O(N)$ | $O(N)$, one entry per distinct value | No eviction rule and no window state to keep consistent, so the distance-$k$ boundary is tested directly; the tradeoff is memory that scales with distinct values instead of with $k$ |
| Sort by value, then compare neighbours | Sort the pairs $(\text{value}, \text{index})$ and test the index distance of consecutive occurrences within each run of equal values | $O(N \log N)$ | $O(N)$ | Sound, because inside one value's sorted occurrence list the closest pair in index order must be neighbours; it reorders the input and forbids early exit, so it still pays for a full sort even though the match sits at index $3$ |

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N$ is the number of elements in `nums`. Each element is added and removed from the hash set at most once, with $O(1)$ average hash table operations per step.
- **Auxiliary Space Complexity:** $O(\min(N, k))$ auxiliary space for the sliding window set, which never holds more than $k$ elements at any time.
