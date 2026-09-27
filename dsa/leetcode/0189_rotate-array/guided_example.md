# Guided Example: Rotate Array

We trace the step-by-step three-step in-place reversal algorithm and cyclic index transformation on representative rotated integer arrays:

- **Input:** $\text{nums} = [1, 2, 3, 4, 5, 6, 7], \quad k = 3$
- **Required output:** $[5, 6, 7, 1, 2, 3, 4]$ (Right-rotated by 3 positions)
- **Even Split Instance:** $\text{nums} = [-1, -100, 3, 99], \quad k = 2 \implies [3, 99, -1, -100]$
- **Modulus Overflow Instance:** $\text{nums} = [1, 2], \quad k = 3 \implies k = 3 \pmod 2 = 1 \implies [2, 1]$

This instance demonstrates in-place block cyclic shifting, algebraically proves why three reversals ($(A B)^R \to B^R A^R \to B A$) yield the exact rotated array, handles $k \ge N$ via modular normalization ($k \leftarrow k \pmod N$), and runs in $O(N)$ time with strictly $O(1)$ auxiliary memory.

---

## 1. Instance & Teaching Goal

Given an integer array $\text{nums} = [1, 2, 3, 4, 5, 6, 7]$ of length $N = 7$ and rotation step $k = 3$:
Rotate the array to the right by $k$ steps in-place.
Rotating right by $3$ shifts every element forward by 3 positions, wrapping around to the front:
$$
[1, 2, 3, 4, 5, 6, 7] \implies \mathbf{[5, 6, 7, 1, 2, 3, 4]}
$$

Allocating a second array $[0] \times N$ and placing $\text{new\_nums}[(i + k) \% N] = \text{nums}[i]$ is straightforward but requires $O(N)$ auxiliary space.
The **Three-Reversal Algorithm** executes this block permutation purely in-place:
1. Decompose the array into two blocks:
   $$
   A = \text{nums}[0 \dots N - k - 1] \quad (\text{first } N-k \text{ elements: } [1, 2, 3, 4])
   $$
   $$
   B = \text{nums}[N - k \dots N - 1] \quad (\text{last } k \text{ elements: } [5, 6, 7])
   $$
2. The goal is to transform $[A, B]$ into $[B, A]$.
3. By reversing the entire array and then reversing each block individually:
   $$
   [A, B]^R = [B^R, A^R] \xrightarrow{\text{reverse } B^R} [B, A^R] \xrightarrow{\text{reverse } A^R} [B, A]
   $$
This achieves the exact rotation in $O(N)$ time using only $O(1)$ extra space.

---

## 2. Conceptual Foundation & Invariants

### The Three-Reversal Protocol
Let $N = |\text{nums}|$.
1. **Modular Normalization:**
   Rotating by $N$ steps returns the array to its identical original state. Therefore, normalize $k$:
   $$
   k \leftarrow k \pmod N
   $$
   If $k == 0$, no rotation is needed; return immediately.

2. **In-Place Two-Pointer Reversal Helper:**
   Define $\text{reverse}(L, R)$:
   While $L < R$:
   $$
   \text{nums}[L], \, \text{nums}[R] \leftarrow \text{nums}[R], \, \text{nums}[L]
   $$
   $$
   L \leftarrow L + 1, \quad R \leftarrow R - 1
   $$

3. **Three Reversal Sequence:**
   - **Step 1 (Global Reversal):** Reverse all $N$ elements:
     $$
     \text{reverse}(0, N - 1)
     $$
   - **Step 2 (Prefix Reversal):** Reverse the first $k$ elements:
     $$
     \text{reverse}(0, k - 1)
     $$
   - **Step 3 (Suffix Reversal):** Reverse the remaining $N - k$ elements:
     $$
     \text{reverse}(k, N - 1)
     $$

> **Invariant.** After Step 1, block $B$ has moved to the front and block $A$ to the back, but both blocks are internally reversed. Steps 2 and 3 independently un-reverse blocks $B$ and $A$, completing the transformation.

---

## 3. Step-by-Step Worked Execution

We trace the algorithm on $\text{nums} = [1, 2, 3, 4, 5, 6, 7]$ with $k = 3$ ($N = 7$):

### Normalization
$$
k = 3 \pmod 7 = 3
$$

---

### Step 1: Reverse Entire Array ($0 \dots 6$)
Call $\text{reverse}(0, 6)$:
- Swap $(0, 6)$: $1 \leftrightarrow 7$
- Swap $(1, 5)$: $2 \leftrightarrow 6$
- Swap $(2, 4)$: $3 \leftrightarrow 5$
- Index $3$ ($4$) remains at center.

Array state after Step 1:
$$
\text{nums} = [\mathbf{7, 6, 5}, \, \mathbf{4, 3, 2, 1}]
$$
*(Block $B = [5, 6, 7]$ is now at the front as $[7, 6, 5]$. Block $A = [1, 2, 3, 4]$ is at the rear as $[4, 3, 2, 1]$)*.

---

### Step 2: Reverse First $k = 3$ Elements ($0 \dots 2$)
Call $\text{reverse}(0, 2)$:
- Swap $(0, 2)$: $7 \leftrightarrow 5$
- Index $1$ ($6$) remains at center.

Array state after Step 2:
$$
\text{nums} = [\mathbf{5, 6, 7}, \, 4, 3, 2, 1]
$$
*(Block $B$ is restored to its proper forward spelling $[5, 6, 7]$ at the front of the array!)*

---

### Step 3: Reverse Suffix Elements ($3 \dots 6$)
Call $\text{reverse}(3, 6)$ on the remaining $N - k = 4$ elements:
- Swap $(3, 6)$: $4 \leftrightarrow 1$
- Swap $(4, 5)$: $3 \leftrightarrow 2$

Array state after Step 3:
$$
\text{nums} = [5, 6, 7, \, \mathbf{1, 2, 3, 4}]
$$
*(Block $A$ is restored to its proper forward spelling $[1, 2, 3, 4]$ at the rear of the array!)*

Final rotated array: $\mathbf{[5, 6, 7, 1, 2, 3, 4]}$.

---

## 4. Complete Execution Trace

```text
Initial Array:
[ 1,  2,  3,  4,  5,  6,  7 ], k = 3

Step 1: Reverse entire array (0 to 6):
[ 7,  6,  5,  4,  3,  2,  1 ]

Step 2: Reverse first k elements (0 to 2):
[ 5,  6,  7,  4,  3,  2,  1 ]

Step 3: Reverse remaining n - k elements (3 to 6):
[ 5,  6,  7,  1,  2,  3,  4 ]

Result: [5, 6, 7, 1, 2, 3, 4]
```

| Step | Operation Range $[L, R]$ | Subarray Targeted | Action Taken | Resulting Full Array $\text{nums}$ |
|:---:|:---:|:---:|:---:|:---|
| Start | - | - | Initial configuration | `[1, 2, 3, 4, 5, 6, 7]` |
| **1** | **$[0, 6]$** | **`[1, 2, 3, 4, 5, 6, 7]`** | **Reverse All** | **`[7, 6, 5, 4, 3, 2, 1]`** |
| **2** | **$[0, 2]$** | **`[7, 6, 5]`** | **Reverse First $k$** | **`[5, 6, 7, 4, 3, 2, 1]`** |
| **3** | **$[3, 6]$** | **`[4, 3, 2, 1]`** | **Reverse Suffix** | **`[5, 6, 7, 1, 2, 3, 4]` (Final)** |

---

## 5. Algorithmic Correctness

**Soundness.** Let the original array be the concatenation of words $A$ and $B$, where $|A| = N - k$ and $|B| = k$. The right rotation of $A B$ by $k$ positions is $B A$. Reversing $A B$ yields $(A B)^R = B^R A^R$. Reversing the first $k$ elements yields $(B^R)^R A^R = B A^R$. Reversing the final $N - k$ elements yields $B (A^R)^R = B A$.

**Completeness.** Since $k \pmod N$ maps any non-negative integer $k$ into the valid interval $[0, N - 1]$, all rotation magnitudes (including $k > N$ and $k = 0$) are mapped to their canonical equivalence class.

---

## 6. Traps This Instance Exposes

- **Failing to Compute $k \pmod N$:** When $k > N$ (e.g. $N = 2, k = 3$), attempting to reverse indices up to $k - 1 = 2$ causes an out-of-bounds error. Always execute `k %= len(nums)`.
- **Using Slicing Reassignment in Python:** Writing `nums = nums[-k:] + nums[:-k]` creates a new list and rebinds the local variable `nums`, leaving the caller's list unchanged! In-place modification requires `nums[:] = ...` or manual swaps.
- **Cyclic Replacement Index Jumps:** The alternative $O(1)$ space algorithm jumps through index cycles $(i + k) \pmod N$. However, when $\gcd(N, k) > 1$, multiple disjoint cycles exist, requiring complex cycle counting. The three-reversal method is far less error-prone.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N$ is the number of elements in `nums`. Step 1 performs $\lfloor N/2 \rfloor$ swaps, Step 2 performs $\lfloor k/2 \rfloor$ swaps, and Step 3 performs $\lfloor (N-k)/2 \rfloor$ swaps. Total swaps are exactly $N$, running in strictly $O(N)$ linear time.
- **Auxiliary Space Complexity:** $O(1)$ constant memory, modifying elements entirely in-place.
