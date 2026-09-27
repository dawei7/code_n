# Guided Example: Permutation Sequence

We trace the step-by-step factorial number system (factoradic base) decomposition on representative sequence instances:

- **Instance 1:** $n = 3, k = 3 \implies \text{"213"}$
- **Instance 2 (Multi-digit):** $n = 4, k = 9 \implies \text{"2314"}$

This instance demonstrates mathematical permutation ranking, converting 1-based rank $k$ to 0-based block indices, quotient/remainder extraction with factorials $(n-1)!$, shrinking the available digit list, and direct $O(n^2)$ direct construction without generating previous permutations.

---

## 1. Instance & Teaching Goal

The set $[1, 2, \dots, n]$ contains a total of $n!$ unique permutations. Listed in lexicographical order for $n = 3$:
1. `"123"`
2. `"132"`
3. `"213"`
4. `"231"`
5. `"312"`
6. `"321"`

Given $n = 3$ and $k = 3$, we must return the $3^{\text{rd}}$ permutation sequence (`"213"`).

Generating all $k$ permutations using `next_permutation` takes $O(k \cdot n)$ time.
By recognizing that permutations partition naturally into equal-sized blocks of $(n-1)!$, we determine each digit directly via integer division:
$$
\text{digit\_index} = \lfloor (k - 1) / (n - 1)! \rfloor
$$
This allows us to construct the $k$-th permutation in $O(n^2)$ time with zero backtracking.

---

## 2. Conceptual Foundation & Invariants

### Factoradic Block Partitioning
When picking the first digit from $n$ candidates:
- There are $n$ possible leading digits.
- For each choice, the remaining $n - 1$ positions have $(n - 1)!$ permutations.
- Group 0 starts with the $1^{\text{st}}$ available digit, spanning ranks $0 \dots (n-1)! - 1$.
- Group 1 starts with the $2^{\text{nd}}$ available digit, spanning ranks $(n-1)! \dots 2(n-1)! - 1$.

### Iterative Construction Procedure
1. Convert $k$ from 1-based to 0-based: $k \leftarrow k - 1$.
2. Maintain a list of available digits: $\text{numbers} = [1, 2, \dots, n]$.
3. Precompute factorial table: $\text{fact}[m] = m!$.
4. For each position from $i = n - 1$ down to $0$:
   - Group size is $\text{fact}[i] = i!$.
   - Selected index is:
     $$
     \text{idx} = \lfloor k / \text{fact}[i] \rfloor
     $$
   - Append $\text{str}(\text{numbers}[\text{idx}])$ to result string.
   - Remove $\text{numbers}[\text{idx}]$ from the candidate pool.
   - Update remainder:
     $$
     k \leftarrow k \pmod{\text{fact}[i]}
     $$

> **Invariant.** At each step $i$, $k$ represents the exact 0-based offset within the sub-block of permutations formed by the remaining available digits.

---

## 3. Step-by-Step Worked Execution

We trace $n = 4, k = 9$:

### Setup
- Convert $k$: $k \leftarrow 9 - 1 = 8$.
- Available digits: $\text{numbers} = [1, 2, 3, 4]$.
- Precompute factorials:
  - $3! = 6$
  - $2! = 2$
  - $1! = 1$
  - $0! = 1$

---

### Step 1: Determine Position 0 (Out of 4)
- Remaining unfixed digits: 4. Block size for each choice is $(4 - 1)! = 3! = 6$.
- Compute index:
  $$
  \text{idx} = \lfloor 8 / 6 \rfloor = 1
  $$
- Selected digit: $\text{numbers}[1] = 2$.
- Append `'2'` to result.
- Remove $2$ from list: $\text{numbers} = [1, 3, 4]$.
- Update remainder:
  $$
  k \leftarrow 8 \pmod{6} = 2
  $$

---

### Step 2: Determine Position 1 (Out of 4)
- Remaining unfixed digits: 3. Block size is $(3 - 1)! = 2! = 2$.
- Compute index:
  $$
  \text{idx} = \lfloor 2 / 2 \rfloor = 1
  $$
- Selected digit: $\text{numbers}[1] = 3$.
- Append `'3'` to result.
- Remove $3$ from list: $\text{numbers} = [1, 4]$.
- Update remainder:
  $$
  k \leftarrow 2 \pmod{2} = 0
  $$

---

### Step 3: Determine Position 2 (Out of 4)
- Remaining unfixed digits: 2. Block size is $(2 - 1)! = 1! = 1$.
- Compute index:
  $$
  \text{idx} = \lfloor 0 / 1 \rfloor = 0
  $$
- Selected digit: $\text{numbers}[0] = 1$.
- Append `'1'` to result.
- Remove $1$ from list: $\text{numbers} = [4]$.
- Update remainder:
  $$
  k \leftarrow 0 \pmod{1} = 0
  $$

---

### Step 4: Determine Position 3 (Out of 4)
- Only $[4]$ remains. Append `'4'`.
- Result assembled: `"2314"`.

---

## 4. Complete Execution Trace

| Position | Unfixed Count | Block Factorial $i!$ | Current $k$ | Calculated Index $\lfloor k / i! \rfloor$ | Selected Digit | Remaining Pool | Updated Remainder $k \pmod{i!}$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 0 | 4 | $3! = 6$ | 8 | $\lfloor 8/6 \rfloor = \mathbf{1}$ | **2** | `[1, 3, 4]` | $8 \pmod{6} = 2$ |
| 1 | 3 | $2! = 2$ | 2 | $\lfloor 2/2 \rfloor = \mathbf{1}$ | **3** | `[1, 4]` | $2 \pmod{2} = 0$ |
| 2 | 2 | $1! = 1$ | 0 | $\lfloor 0/1 \rfloor = \mathbf{0}$ | **1** | `[4]` | $0 \pmod{1} = 0$ |
| 3 | 1 | $0! = 1$ | 0 | $\lfloor 0/1 \rfloor = \mathbf{0}$ | **4** | `[]` | 0 |

Final emitted string: `"2314"`.

---

## 5. Algorithmic Correctness

**Soundness.** Lexicographical ordering strictly sorts permutations by their first digit, then second, and so on. Since there are exactly $(n-1)!$ permutations starting with each of the available digits in sorted order, the $k$-th permutation must begin with the $\lfloor k / (n-1)! \rfloor$-th available digit. By mathematical induction, this holds at every subsequent position.

**Completeness.** At each step, one digit is removed from the candidate pool and appended to the output. After $n$ iterations, the pool is empty and all $n$ positions have been deterministically assigned.

---

## 6. Traps This Instance Exposes

- **0-Based vs 1-Based Offset:** Forgetting $k \leftarrow k - 1$ causes off-by-one errors across block boundaries (e.g. if $k = 6$, $6 / 6 = 1$, which would pick the second block instead of the last element of the first block). 0-based modulo arithmetic guarantees correct block indexing.
- **List Element Removal Overhead:** Removing an element from a Python list takes $O(n)$ time. For $n \le 9$, this is instantaneous ($9 \times 9 = 81$ operations).
- **Factorial Precomputation:** Computing factorials up to $n$ avoids repeated factorial calculations inside the loop.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n^2)$. The loop runs $n$ times. In each iteration, removing an element from the dynamic list takes $O(n)$ time. For $n \le 9$, $n^2 \le 81$ basic operations, executing in under $0.1$ milliseconds.
- **Auxiliary Space Complexity:** $O(n)$ to store the array of available digits and the result string.
