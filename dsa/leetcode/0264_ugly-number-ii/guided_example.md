# Guided Example: Ugly Number II

We trace the step-by-step three-pointer dynamic programming merge, prime factor stream generation ($\times 2, \times 3, \times 5$), and multi-pointer duplicate advancement on representative $n^{\text{th}}$ ugly number queries:

- **Input:** $n = 10$
- **Required output:** $12$ (The first 10 ugly numbers are: $1, 2, 3, 4, 5, 6, 8, 9, 10, 12$)
- **Base Case:** $n = 1 \implies 1$
- **Eleventh Ugly Number:** $n = 11 \implies 15$ ($3 \times 5 = 15$)
- **Deduplication Coincidence:** $6$ is generated as both $3 \times 2$ and $2 \times 3$; both $p_2$ and $p_3$ advance simultaneously to prevent duplicate insertions

This instance demonstrates generating ordered mathematical sequences via multi-way stream merging, mathematically proves why every ugly number is the product of a previous ugly number with 2, 3, or 5, details the three-pointer index progression ($p_2, p_3, p_5$), and runs in optimal strictly $O(N)$ linear time with $O(N)$ space.

---

## 1. Instance & Teaching Goal

An **ugly number** is a positive integer whose prime factors are limited to 2, 3, and 5.
Given $n = 10$, find the $10^{\text{th}}$ ugly number:
```text
Sequence:  1, 2, 3, 4, 5, 6, 8, 9, 10, 12
Index:     1  2  3  4  5  6  7  8   9  10
Output: 12
```

- Testing integers sequentially ($1, 2, 3, 4, \dots$) and factoring each by $\{2, 3, 5\}$ (as in LeetCode 263) wastes enormous time on non-ugly numbers (e.g. finding the $1690^{\text{th}}$ ugly number requires testing past $2 \times 10^9$).
- Instead of checking all numbers, we **generate only ugly numbers** in strictly increasing order.
- Every ugly number $U > 1$ is formed by multiplying an earlier ugly number by 2, 3, or 5.
- This is equivalent to merging three sorted infinite streams:
  $$
  S_2 = [1 \times 2, 2 \times 2, 3 \times 2, 4 \times 2, \dots]
  $$
  $$
  S_3 = [1 \times 3, 2 \times 3, 3 \times 3, 4 \times 3, \dots]
  $$
  $$
  S_5 = [1 \times 5, 2 \times 5, 3 \times 5, 4 \times 5, \dots]
  $$
Using three pointers, we select the minimum candidate at each step in $O(1)$ time, finding the $n^{\text{th}}$ number in strictly $O(N)$ time.

---

## 2. Conceptual Foundation & Invariants

### The Three-Pointer Merge Protocol
Initialize an array $\text{ugly} = [1]$ of length $n$.
Maintain three indices pointing into $\text{ugly}$:
- $p_2 = 0$: Pointer to the next ugly number to multiply by 2.
- $p_3 = 0$: Pointer to the next ugly number to multiply by 3.
- $p_5 = 0$: Pointer to the next ugly number to multiply by 5.

For each index $i$ from $1$ to $n - 1$:
1. **Candidate Evaluation:**
   Compute the next candidate from each stream:
   $$
   c_2 = \text{ugly}[p_2] \times 2
   $$
   $$
   c_3 = \text{ugly}[p_3] \times 3
   $$
   $$
   c_5 = \text{ugly}[p_5] \times 5
   $$
2. **Select Minimum:**
   $$
   \text{next\_val} = \min(c_2, c_3, c_5)
   $$
   $$
   \text{ugly}[i] = \text{next\_val}
   $$
3. **Advance Pointer(s) with Deduplication:**
   Increment every pointer that produced $\text{next\_val}$:
   - If $\text{next\_val} == c_2$: $p_2 \leftarrow p_2 + 1$
   - If $\text{next\_val} == c_3$: $p_3 \leftarrow p_3 + 1$
   - If $\text{next\_val} == c_5$: $p_5 \leftarrow p_5 + 1$

*(Crucial Invariant: If $c_2 == c_3$, both $p_2$ and $p_3$ increment in the same step! This naturally eliminates duplicate values like $6 = 2 \times 3 = 3 \times 2$ without needing a set)*.

> **Invariant.** At step $i$, $\text{ugly}[0 \dots i]$ contains the first $i + 1$ ugly numbers in strictly sorted order. The candidate $\min(c_2, c_3, c_5)$ is strictly the smallest ugly number greater than $\text{ugly}[i - 1]$.

---

## 3. Step-by-Step Worked Execution

We trace the generation of the first $n = 10$ ugly numbers:
Base case: $\text{ugly}[0] = 1, \quad p_2 = 0, \quad p_3 = 0, \quad p_5 = 0$.

---

### Step 1 ($i = 1$)
- Candidates: $c_2 = 1 \times 2 = 2, \quad c_3 = 1 \times 3 = 3, \quad c_5 = 1 \times 5 = 5$.
- Minimum: $\min(2, 3, 5) = \mathbf{2}$.
- Store: $\text{ugly}[1] = 2$.
- Update pointer: $c_2 == 2 \implies p_2 \leftarrow 1$.
- Array: `[1, 2]`.

---

### Step 2 ($i = 2$)
- Candidates: $c_2 = 2 \times 2 = 4, \quad c_3 = 1 \times 3 = 3, \quad c_5 = 1 \times 5 = 5$.
- Minimum: $\min(4, 3, 5) = \mathbf{3}$.
- Store: $\text{ugly}[2] = 3$.
- Update pointer: $c_3 == 3 \implies p_3 \leftarrow 1$.
- Array: `[1, 2, 3]`.

---

### Step 3 ($i = 3$)
- Candidates: $c_2 = 2 \times 2 = 4, \quad c_3 = 2 \times 3 = 6, \quad c_5 = 1 \times 5 = 5$.
- Minimum: $\min(4, 6, 5) = \mathbf{4}$.
- Store: $\text{ugly}[3] = 4$.
- Update pointer: $c_2 == 4 \implies p_2 \leftarrow 2$.
- Array: `[1, 2, 3, 4]`.

---

### Step 4 ($i = 4$)
- Candidates: $c_2 = 3 \times 2 = 6, \quad c_3 = 2 \times 3 = 6, \quad c_5 = 1 \times 5 = 5$.
- Minimum: $\min(6, 6, 5) = \mathbf{5}$.
- Store: $\text{ugly}[4] = 5$.
- Update pointer: $c_5 == 5 \implies p_5 \leftarrow 1$.
- Array: `[1, 2, 3, 4, 5]`.

---

### Step 5 ($i = 5$) — Simultaneous Deduplication
- Candidates: $c_2 = 3 \times 2 = 6, \quad c_3 = 2 \times 3 = 6, \quad c_5 = 2 \times 5 = 10$.
- Minimum: $\min(6, 6, 10) = \mathbf{6}$.
- Store: $\text{ugly}[5] = 6$.
- Update pointers:
  - $c_2 == 6 \implies p_2 \leftarrow 3$.
  - $c_3 == 6 \implies p_3 \leftarrow 2$.
  *(Both advance, preventing $6$ from being inserted twice!)*.
- Array: `[1, 2, 3, 4, 5, 6]`.

---

### Step 6 ($i = 6$)
- Candidates: $c_2 = 4 \times 2 = 8, \quad c_3 = 3 \times 3 = 9, \quad c_5 = 2 \times 5 = 10$.
- Minimum: $\min(8, 9, 10) = \mathbf{8}$.
- Store: $\text{ugly}[6] = 8$.
- Update pointer: $p_2 \leftarrow 4$.
- Array: `[1, 2, 3, 4, 5, 6, 8]`.

---

### Step 7 ($i = 7$)
- Candidates: $c_2 = 5 \times 2 = 10, \quad c_3 = 3 \times 3 = 9, \quad c_5 = 2 \times 5 = 10$.
- Minimum: $\min(10, 9, 10) = \mathbf{9}$.
- Store: $\text{ugly}[7] = 9$.
- Update pointer: $p_3 \leftarrow 3$.
- Array: `[1, 2, 3, 4, 5, 6, 8, 9]`.

---

### Step 8 ($i = 8$) — Simultaneous Deduplication
- Candidates: $c_2 = 5 \times 2 = 10, \quad c_3 = 4 \times 3 = 12, \quad c_5 = 2 \times 5 = 10$.
- Minimum: $\min(10, 12, 10) = \mathbf{10}$.
- Store: $\text{ugly}[8] = 10$.
- Update pointers: $p_2 \leftarrow 5, \quad p_5 \leftarrow 2$.
- Array: `[1, 2, 3, 4, 5, 6, 8, 9, 10]`.

---

### Step 9 ($i = 9$) — Terminal Target Reached
- Candidates: $c_2 = 6 \times 2 = 12, \quad c_3 = 4 \times 3 = 12, \quad c_5 = 3 \times 5 = 15$.
- Minimum: $\min(12, 12, 15) = \mathbf{12}$.
- Store: $\text{ugly}[9] = 12$.
- Array: `[1, 2, 3, 4, 5, 6, 8, 9, 10, 12]`.

Final answer: $\text{ugly}[9] = \mathbf{12}$.

---

## 4. Complete Execution Trace

```text
n = 10
ugly = [1]
p2 = 0, p3 = 0, p5 = 0

i=1: min(1*2, 1*3, 1*5) = 2  -> p2=1 -> ugly=[1, 2]
i=2: min(2*2, 1*3, 1*5) = 3  -> p3=1 -> ugly=[1, 2, 3]
i=3: min(2*2, 2*3, 1*5) = 4  -> p2=2 -> ugly=[1, 2, 3, 4]
i=4: min(3*2, 2*3, 1*5) = 5  -> p5=1 -> ugly=[1, 2, 3, 4, 5]
i=5: min(3*2, 2*3, 2*5) = 6  -> p2=3, p3=2 -> ugly=[1, 2, 3, 4, 5, 6]
i=6: min(4*2, 3*3, 2*5) = 8  -> p2=4 -> ugly=[1, 2, 3, 4, 5, 6, 8]
i=7: min(5*2, 3*3, 2*5) = 9  -> p3=3 -> ugly=[1, 2, 3, 4, 5, 6, 8, 9]
i=8: min(5*2, 4*3, 2*5) = 10 -> p2=5, p5=2 -> ugly=[1, 2, 3, 4, 5, 6, 8, 9, 10]
i=9: min(6*2, 4*3, 3*5) = 12 -> p2=6, p3=4 -> ugly=[1, 2, 3, 4, 5, 6, 8, 9, 10, 12]

Result: 12
```

| Step $i$ | $c_2 = \text{ugly}[p_2] \times 2$ | $c_3 = \text{ugly}[p_3] \times 3$ | $c_5 = \text{ugly}[p_5] \times 5$ | Next Chosen $\min(c_2, c_3, c_5)$ | Pointer Updates | Resulting $\text{ugly}[i]$ |
|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| 1 | $1 \times 2 = 2$ | $1 \times 3 = 3$ | $1 \times 5 = 5$ | 2 | $p_2 \leftarrow 1$ | 2 |
| 2 | $2 \times 2 = 4$ | $1 \times 3 = 3$ | $1 \times 5 = 5$ | 3 | $p_3 \leftarrow 1$ | 3 |
| 3 | $2 \times 2 = 4$ | $2 \times 3 = 6$ | $1 \times 5 = 5$ | 4 | $p_2 \leftarrow 2$ | 4 |
| 4 | $3 \times 2 = 6$ | $2 \times 3 = 6$ | $1 \times 5 = 5$ | 5 | $p_5 \leftarrow 1$ | 5 |
| **5** | $3 \times 2 = \mathbf{6}$ | $2 \times 3 = \mathbf{6}$ | $2 \times 5 = 10$ | **6** | $p_2 \leftarrow 3, \; p_3 \leftarrow 2$ | **6** |
| 6 | $4 \times 2 = 8$ | $3 \times 3 = 9$ | $2 \times 5 = 10$ | 8 | $p_2 \leftarrow 4$ | 8 |
| 7 | $5 \times 2 = 10$ | $3 \times 3 = 9$ | $2 \times 5 = 10$ | 9 | $p_3 \leftarrow 3$ | 9 |
| **8** | $5 \times 2 = \mathbf{10}$ | $4 \times 3 = 12$ | $2 \times 5 = \mathbf{10}$ | **10** | $p_2 \leftarrow 5, \; p_5 \leftarrow 2$ | **10** |
| **9** | $6 \times 2 = \mathbf{12}$ | $4 \times 3 = \mathbf{12}$ | $3 \times 5 = 15$ | **12** | $p_2 \leftarrow 6, \; p_3 \leftarrow 4$ | **$\mathbf{12}$ ($10^{\text{th}}$ Ugly)** |

### Producer Table: Where Each Value Comes From

The step table shows what happens at each index; the table below inverts the
view and asks, for each value, which streams are capable of producing it. Every
value's producing slots are strictly smaller than its own slot, which is the
dependency that makes the sequence a dynamic program rather than a search.

| Value | Slot `ugly[i]` | From the $\times 2$ stream | From the $\times 3$ stream | From the $\times 5$ stream | Producing streams | Pointers advanced |
|:---:|:---:|:---|:---|:---|:---:|:---|
| 2 | 1 | `ugly[0] × 2 = 1 × 2` | — | — | 1 | $p_2$ |
| 3 | 2 | — | `ugly[0] × 3 = 1 × 3` | — | 1 | $p_3$ |
| 4 | 3 | `ugly[1] × 2 = 2 × 2` | — | — | 1 | $p_2$ |
| 5 | 4 | — | — | `ugly[0] × 5 = 1 × 5` | 1 | $p_5$ |
| 6 | 5 | `ugly[2] × 2 = 3 × 2` | `ugly[1] × 3 = 2 × 3` | — | 2 | $p_2$ and $p_3$ |
| 8 | 6 | `ugly[3] × 2 = 4 × 2` | — | — | 1 | $p_2$ |
| 9 | 7 | — | `ugly[2] × 3 = 3 × 3` | — | 1 | $p_3$ |
| 10 | 8 | `ugly[4] × 2 = 5 × 2` | — | `ugly[1] × 5 = 2 × 5` | 2 | $p_2$ and $p_5$ |
| 12 | 9 | `ugly[5] × 2 = 6 × 2` | `ugly[3] × 3 = 4 × 3` | — | 2 | $p_2$ and $p_3$ |
| 15 | 10 | — | `ugly[4] × 3 = 5 × 3` | `ugly[2] × 5 = 3 × 5` | 2 | $p_3$ and $p_5$ |
| 30 | 17 | `ugly[10] × 2 = 15 × 2` | `ugly[8] × 3 = 10 × 3` | `ugly[5] × 5 = 6 × 5` | 3 | $p_2$, $p_3$ and $p_5$ |

Two conclusions follow directly. First, a value has several producers exactly
when it admits more than one factorization over $\{2, 3, 5\}$: $6 = 3 \cdot 2 =
2 \cdot 3$ has two, and $30 = 15 \cdot 2 = 10 \cdot 3 = 6 \cdot 5$ has all three,
which is why the minimum test must be a sequence of independent comparisons
rather than a branch chain. Second, ties are the common case rather than a rare
coincidence: among the $99$ non-unit values in the first hundred entries of the
sequence, $79$ are produced by more than one stream.

---

## 5. Algorithmic Correctness

**Soundness.** Since $\text{ugly}[0] = 1$ is ugly, and every subsequent entry is formed by multiplying an existing ugly number by 2, 3, or 5, every element in `ugly` has prime factors restricted exclusively to $\{2, 3, 5\}$.

**Completeness.** Suppose there exists an ugly number $X$ smaller than the chosen minimum that was missed. Since $X > 1$, $X$ must be divisible by at least one of $\{2, 3, 5\}$. Thus $X / 2, X / 3,$ or $X / 5$ is a smaller ugly number that must already appear in the sequence. Because $p_2, p_3, p_5$ point to the earliest unused multipliers, $X$ would have been generated as a candidate. Since $\min(c_2, c_3, c_5)$ selects the globally smallest candidate at each step, no ugly number is ever skipped.

---

## 6. Traps This Instance Exposes

- **Using `elif` Instead of Separate `if` Statements:** If you write `if next_val == c2: p2 += 1 elif next_val == c3: ...`, when $c_2 == c_3 == 6$, only $p_2$ advances! In the next round, $c_3$ would still produce $6$, inserting a duplicate $6$ into the array! Using separate `if` statements guarantees that all matching pointers advance simultaneously.
- **Heap Overhead:** A min-heap (priority queue) can also generate ugly numbers, but popping and inserting takes $O(\log K)$ time per element and requires a hash set to deduplicate. The three-pointer DP approach runs in $O(1)$ time per element without any hashing overhead.
- **32-Bit Overflow in Unbounded Calculations:** For $n = 1690$, the answer is $2,123,366,400$, which fits in a 32-bit signed integer (`INT_MAX` is $2,147,483,647$). In languages like C++, candidate multiplication can temporarily exceed 32 bits, requiring 64-bit `long long` for intermediate products.

### Boundary Table of the Sequence Limits

The values below were produced by the same three-pointer loop the lesson traces.
They mark where the sequence stops being an arithmetic exercise and starts
testing the contract.

| Boundary or quantity | Value | What it establishes |
|:---|:---:|:---|
| Smallest legal query, $n = 1$ | 1 | The generation loop runs zero times, so the answer is the seeded $\text{ugly}[0]$ and no pointer ever advances |
| Traced target, $n = 10$ | 12 | Two ties ($6$ and $10$) already occur inside the worked window, so deduplication is exercised by the representative instance |
| Next entry, $n = 11$ | 15 | $15 = 5 \times 3 = 3 \times 5$ is a tie on the very next step, confirming ties are ordinary rather than exceptional |
| Authored case, $n = 15$ | 24 | $24 = 12 \times 2 = 8 \times 3$: another double-producing entry, both producers already present in the array |
| Authored case, $n = 100$ | 1536 | Over this prefix $79$ of the $99$ non-unit values have more than one producer, so a branch chain that advances only one pointer corrupts the sequence early |
| Largest legal query, $n = 1690$ | 2123366400 | Fits inside a signed 32-bit integer, and is the $1690^{\text{th}}$ of exactly $1691$ ugly numbers below $2^{31}$ |
| One past the legal range, $n = 1691$ | 2125764000 | Still below `INT_MAX`, so the $1690$ ceiling comes from the problem statement and not from the integer type |
| Largest live candidate while reaching $n = 1690$ | 8062156800 | Candidate products are not bounded by the answer: they overshoot `INT_MAX` by nearly four times, which is why fixed-width languages need 64-bit intermediates |

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N = n$. Each iteration of the loop from $1$ to $n - 1$ computes 3 products, takes the minimum of 3 values, and performs at most 3 pointer increments. All operations in the loop body are strictly $O(1)$. Total time is $O(N)$ linear time.
- **Auxiliary Space Complexity:** $O(N)$ auxiliary memory to store the array of $n$ ugly numbers.

### Alternatives and Their Costs

Every strategy below reaches the same sequence; they differ in whether they pay a
logarithm per entry, how many candidates they keep alive, and whether they solve
only the query that was asked.

| Strategy | Mechanism | Time | Auxiliary space | Tradeoff or failure mode |
|:---|:---|:---:|:---:|:---|
| Three-pointer merge (the method traced) | Keep the generated sequence and three indices; take the minimum of the three products and advance every tying pointer | $O(N)$ | $O(N)$ | One comparison per entry and no hashing; the whole correctness burden sits on advancing *all* tied pointers |
| Min-heap with a seen set | Seed a heap with $1$, repeatedly pop the smallest and push its three products when unseen | $O(N \log N)$ | $O(N)$ | Correct and short, but every push, pop, and membership test costs a logarithm that the three-pointer form avoids |
| Min-heap without a seen set | Push all three products unconditionally | $O(N \log N)$ with a larger constant | More than $N$ heap entries | The frontier grows by three per pop and tied values are stored repeatedly, so the heap holds many duplicates of the same candidate |
| Test each integer for ugliness | Count the ugly numbers in increasing order with the factored-residual test until the count reaches $n$ | $O(M)$ where $M$ is the answer value, each test costing $O(\log M)$ | $O(1)$ | At $n = 1690$ it inspects more than two billion integers and discards essentially all of them |
| Closure over a pre-chosen bound | Build the sorted set of all ugly numbers up to an upper limit, then index into it | $O(u \log u)$ for $u$ values | $O(u)$ | Answers a much larger question than asked, and the limit has to be known before the query is seen |

The three-pointer merge is the only row whose work is proportional to the number
of entries actually requested, and it is the reason the required bound is $O(N)$
rather than $O(N \log N)$: the three streams are each already sorted, so the
merge needs no priority queue to stay in order.
