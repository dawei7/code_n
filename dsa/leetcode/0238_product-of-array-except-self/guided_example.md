# Guided Example: Product of Array Except Self

We trace the step-by-step prefix product forwarding, suffix product backward folding, and division-free $O(1)$ auxiliary space aggregation on representative integer arrays:

- **Input:** $\text{nums} = [1, 2, 3, 4]$
- **Required output:** $[24, 12, 8, 6]$
- **Single Zero Instance:** $\text{nums} = [-1, 1, 0, -3, 3] \implies [0, 0, 9, 0, 0]$ (Zero cancels all products except its own index)
- **Multiple Zeroes Instance:** $\text{nums} = [0, 4, 0] \implies [0, 0, 0]$ (Every entry contains at least one zero factor)
- **Two Element Instance:** $\text{nums} = [2, 5] \implies [5, 2]$

This instance demonstrates prefix-suffix product factorization ($\text{ans}[i] = \text{prefix}[i] \times \text{suffix}[i]$), strictly enforces the constraint prohibiting arithmetic division (`/`), explains reusing the output array for prefix storage to achieve $O(1)$ extra space, and runs in two linear passes ($2N$ operations, $O(N)$ time).

---

## 1. Instance & Teaching Goal

Given an integer array $\text{nums} = [1, 2, 3, 4]$ of length $N = 4$:
Compute $\text{ans}[i] = \prod_{j \ne i} \text{nums}[j]$ for each index $i$:
- $\text{ans}[0] = 2 \times 3 \times 4 = 24$
- $\text{ans}[1] = 1 \times 3 \times 4 = 12$
- $\text{ans}[2] = 1 \times 2 \times 4 = 8$
- $\text{ans}[3] = 1 \times 2 \times 3 = 6$
Output: `[24, 12, 8, 6]`.

### The Division Prohibition Constraint
If division were allowed, one could compute the total product $P = 1 \times 2 \times 3 \times 4 = 24$ and divide $\text{ans}[i] = P / \text{nums}[i]$.
However:
1. **Division is explicitly forbidden** by the problem specification.
2. Even if allowed, division breaks down whenever `nums` contains one or more zeroes ($P / 0$ causes a division-by-zero crash).
By recognizing that every excluded product factors into the product of elements strictly to the left times elements strictly to the right:
$$
\text{ans}[i] = \left(\prod_{j < i} \text{nums}[j]\right) \times \left(\prod_{j > i} \text{nums}[j]\right) = \text{prefix}[i] \times \text{suffix}[i]
$$
we compute all answers in $O(N)$ time without division.

---

## 2. Conceptual Foundation & Invariants

### Output-Reused Prefix-Suffix Protocol
We avoid allocating separate $O(N)$ prefix and suffix arrays by storing prefix products directly inside the return array $\text{ans}$ and accumulating suffix products on-the-fly using a single scalar variable `suffix`:

### Pass 1: Left-to-Right Prefix Accumulation
Initialize $\text{prefix} = 1$:
For $i = 0$ to $N - 1$:
1. Record prefix product of elements before index $i$:
   $$
   \text{ans}[i] \leftarrow \text{prefix}
   $$
2. Incorporate $\text{nums}[i]$ into `prefix` for subsequent indices:
   $$
   \text{prefix} \leftarrow \text{prefix} \times \text{nums}[i]
   $$
*(After Pass 1, $\text{ans}[i]$ holds $\prod_{j=0}^{i-1} \text{nums}[j]$)*.

### Pass 2: Right-to-Left Suffix Accumulation
Initialize $\text{suffix} = 1$:
For $i = N - 1$ down to $0$:
1. Multiply the stored prefix product by the current suffix product:
   $$
   \text{ans}[i] \leftarrow \text{ans}[i] \times \text{suffix}
   $$
2. Incorporate $\text{nums}[i]$ into `suffix` for preceding indices:
   $$
   \text{suffix} \leftarrow \text{suffix} \times \text{nums}[i]
   $$

> **Invariant.** After Pass 1, $\text{ans}[i]$ stores the exact product of all elements to the left of $i$. During Pass 2, `suffix` holds the exact product of all elements to the right of $i$, so $\text{ans}[i] \times \text{suffix}$ yields the final product except self.

---

## 3. Step-by-Step Worked Execution

We trace the two passes on $\text{nums} = [1, 2, 3, 4]$ ($N = 4$):

### Pass 1: Forward Prefix Pass
Start with $\text{prefix} = 1, \quad \text{ans} = [0, 0, 0, 0]$.

- **Index $i = 0$ ($\text{nums}[0] = 1$):**
  - Stash prefix: $\text{ans}[0] = 1$.
  - Update prefix: $\text{prefix} \leftarrow 1 \times \text{nums}[0] = 1 \times 1 = 1$.
- **Index $i = 1$ ($\text{nums}[1] = 2$):**
  - Stash prefix: $\text{ans}[1] = 1$.
  - Update prefix: $\text{prefix} \leftarrow 1 \times \text{nums}[1] = 1 \times 2 = 2$.
- **Index $i = 2$ ($\text{nums}[2] = 3$):**
  - Stash prefix: $\text{ans}[2] = 2$.
  - Update prefix: $\text{prefix} \leftarrow 2 \times \text{nums}[2] = 2 \times 3 = 6$.
- **Index $i = 3$ ($\text{nums}[3] = 4$):**
  - Stash prefix: $\text{ans}[3] = 6$.
  - Update prefix: $\text{prefix} \leftarrow 6 \times \text{nums}[3] = 6 \times 4 = 24$.

**State after Pass 1:** $\text{ans} = [1, 1, 2, 6]$.
*(Notice $\text{ans}[i]$ is the product of all elements left of $i$)*.

---

### Pass 2: Backward Suffix Pass
Start with $\text{suffix} = 1$.

- **Index $i = 3$ ($\text{nums}[3] = 4$):**
  - Combine: $\text{ans}[3] \leftarrow \text{ans}[3] \times \text{suffix} = 6 \times 1 = \mathbf{6}$.
  - Update suffix: $\text{suffix} \leftarrow 1 \times \text{nums}[3] = 1 \times 4 = 4$.
- **Index $i = 2$ ($\text{nums}[2] = 3$):**
  - Combine: $\text{ans}[2] \leftarrow \text{ans}[2] \times \text{suffix} = 2 \times 4 = \mathbf{8}$.
  - Update suffix: $\text{suffix} \leftarrow 4 \times \text{nums}[2] = 4 \times 3 = 12$.
- **Index $i = 1$ ($\text{nums}[1] = 2$):**
  - Combine: $\text{ans}[1] \leftarrow \text{ans}[1] \times \text{suffix} = 1 \times 12 = \mathbf{12}$.
  - Update suffix: $\text{suffix} \leftarrow 12 \times \text{nums}[1] = 12 \times 2 = 24$.
- **Index $i = 0$ ($\text{nums}[0] = 1$):**
  - Combine: $\text{ans}[0] \leftarrow \text{ans}[0] \times \text{suffix} = 1 \times 24 = \mathbf{24}$.
  - Update suffix: $\text{suffix} \leftarrow 24 \times \text{nums}[0] = 24 \times 1 = 24$.

**Final Result:** $\text{ans} = [24, 12, 8, 6]$.

---

## 4. Complete Execution Trace

```text
Input: nums = [1, 2, 3, 4]

Pass 1 (Left to Right Prefix):
i = 0: ans[0] = 1,  prefix becomes 1 * 1 = 1
i = 1: ans[1] = 1,  prefix becomes 1 * 2 = 2
i = 2: ans[2] = 2,  prefix becomes 2 * 3 = 6
i = 3: ans[3] = 6,  prefix becomes 6 * 4 = 24
ans array after Pass 1: [1, 1, 2, 6]

Pass 2 (Right to Left Suffix):
i = 3: ans[3] = 6 * 1  = 6,  suffix becomes 1 * 4  = 4
i = 2: ans[2] = 2 * 4  = 8,  suffix becomes 4 * 3  = 12
i = 1: ans[1] = 1 * 12 = 12, suffix becomes 12 * 2 = 24
i = 0: ans[0] = 1 * 24 = 24, suffix becomes 24 * 1 = 24

Final Output: [24, 12, 8, 6]
```

| Index $i$ | $\text{nums}[i]$ | Stored Prefix $\text{ans}[i]$ | Current Suffix | Combined Value ($\text{prefix} \times \text{suffix}$) | Updated Suffix | Final $\text{ans}[i]$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **0** | 1 | 1 | 24 | $1 \times 24$ | 24 | **24** |
| **1** | 2 | 1 | 12 | $1 \times 12$ | 24 | **12** |
| **2** | 3 | 2 | 4 | $2 \times 4$ | 12 | **8** |
| **3** | 4 | 6 | 1 | $6 \times 1$ | 4 | **6** |

---

## 5. Algorithmic Correctness

**Soundness.** For any index $i$, the set of indices $\{0, \dots, N - 1\} \setminus \{i\}$ is the disjoint union of $\{0, \dots, i - 1\}$ and $\{i + 1, \dots, N - 1\}$. By associativity and commutativity of multiplication over integers, $\prod_{j \ne i} \text{nums}[j] = \left(\prod_{j=0}^{i-1} \text{nums}[j]\right) \times \left(\prod_{j=i+1}^{N-1} \text{nums}[j]\right)$. Pass 1 computes the exact left product, and Pass 2 multiplies it by the exact right product.

**Completeness.** Every index $i \in [0, N - 1]$ is processed. The empty product identity ($1$) ensures boundary indices $0$ and $N - 1$ receive the full products of their respective single-sided complements without zeroing or out-of-bounds access.

---

## 6. Traps This Instance Exposes

- **Using the Division Operator (`/` or `//`):** Even when passing test cases locally, using division violates the core interview constraint. Furthermore, if `nums` contains `0`, division by zero crashes or requires cumbersome branch handling. The two-pass multiplication naturally handles single or multiple zeroes without any conditional branching.
- **Accidental Inclusion of Self:** Stashing `ans[i] = prefix` must occur **before** updating `prefix *= nums[i]`. If reversed, $\text{ans}[i]$ includes $\text{nums}[i]$, which violates the "except self" requirement.
- **Space Overhead:** Creating both `left = [0]*n` and `right = [0]*n` takes $2N$ auxiliary space. Reusing `ans` for the prefix and folding the suffix on-the-fly reduces auxiliary space to $O(1)$.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N$ is the length of `nums`. Pass 1 performs $N$ multiplications, and Pass 2 performs $2N$ multiplications. Total runtime is strictly $3N = O(N)$ arithmetic operations.
- **Auxiliary Space Complexity:** $O(1)$ auxiliary space. The output array `ans` does not count toward auxiliary space complexity per problem guidelines, and only two scalar variables (`prefix`, `suffix`) are allocated.
