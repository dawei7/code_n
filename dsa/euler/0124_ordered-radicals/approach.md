# Ordered Radicals - Optimal Approach

## 1. Problem Essence & Formal Mathematical Formulation

The radical of $n$, $\text{rad}(n)$, is the product of distinct prime factors of $n$. For example:

$$
504 = 2^3 \times 3^2 \times 7 \implies \text{rad}(504) = 2 \times 3 \times 7 = 42
$$

If we calculate $\text{rad}(n)$ for $1 \le n \le 10$, then sort them on $\text{rad}(n)$, and sorting on $n$ where the radicals are equal, we get:
- For $n \le 10$: $E(4) = 8$ (since $\text{rad}(8) = 2$, 4th sorted term), $E(6) = 9$ (since $\text{rad}(9) = 3$).

Let $E(k)$ be the $k$-th element in the sorted $n$ column for $1 \le n \le 100\,000$.

The objective is to find **$E(10\,000)$**:

$$
E(10000) = \operatorname{sorted}([(\text{rad}(n), n) \text{ for } n \in [1, 100000]])[9999][1]
$$

---

## 2. The Naive Approach & Fundamental Bottlenecks

### Individual Prime Factorization per Number
A naive approach factorizes each number $n = 1 \dots 100\,000$ with trial division:
```python
def naive_radicals(n):
    # Runs trial division 100,000 times, causing redundant work
    # ...
```

### Multiplicative Sieve for Radicals
1. Allocate array `rad = [1] * (N + 1)`.
2. For each prime $p \in [2, N]$ (identified when `rad[p] == 1`):
   - Multiply `rad[j] *= p` for all multiples $j = p, 2p, 3p \dots \le N$.
3. The total operations count for the sieve is $\sum_{p \le N} \frac{N}{p} = \mathcal{O}(N \log \log N) \approx 3 \times 10^5$ operations.
4. Construct tuples $(\text{rad}(n), n)$ and sort lexicographically in $\mathcal{O}(N \log N)$ time, completing in $\approx 0.03$ seconds.

---

## 3. Core Intuition & Mathematical Structure

### Ordered Radical Table for $n = 1 \dots 10$ ($N = 10$ Sample)

| Unsorted $n$ | Radical $\text{rad}(n)$ | Sorted Index $k$ | Sorted $n$ ($E(k)$) | Sorted Radical $\text{rad}(E(k))$ |
| :---: | :---: | :---: | :---: | :---: |
| **$1$** | $1$ | **$1$** | $1$ | $1$ |
| **$2$** | $2$ | **$2$** | $2$ | $2$ |
| **$3$** | $3$ | **$3$** | $4$ | $2$ |
| **$4$** | $2$ | **$4$** | $\mathbf{8}$ | $\mathbf{2}$ **(Sample $E(4)$)** |
| **$5$** | $5$ | **$5$** | $3$ | $3$ |
| **$6$** | $6$ | **$6$** | $\mathbf{9}$ | $\mathbf{3}$ **(Sample $E(6)$)** |
| **$7$** | $7$ | **$7$** | $5$ | $5$ |
| **$8$** | $2$ | **$8$** | $6$ | $6$ |
| **$9$** | $3$ | **$9$** | $7$ | $7$ |
| **$10$** | $10$ | **$10$** | $10$ | $10$ |

---

## 4. Rigorous Mathematical Breakthrough & Derivations

### Multiplicative Sieve Pipeline
1. Initialize array `rad = [1] * (limit + 1)`.
2. For $i = 2 \dots 100\,000$:
   - If `rad[i] == 1`:
     - For $j = i, 2i, 3i \dots \le 100\,000$:
       - `rad[j] *= i`
3. Build list `elements = [(rad[n], n) for n in range(1, limit + 1)]`.
4. `elements.sort()` (Python's Timsort orders primarily by `rad[n]`, secondarily by `n`).
5. Return `elements[9999][1] = 21417`.

---

## 5. Concrete Step-by-Step Example Walkthrough

### Example 1: Sample for $n \le 10$
- Sorted array:
  - $(1, 1), (2, 2), (2, 4), (2, 8), (3, 3), (3, 9), (5, 5), (6, 6), (7, 7), (10, 10)$.
- $E(4) = \mathbf{8}$ (4th element is $(2, 8)$). Matches problem statement sample! $\checkmark$
- $E(6) = \mathbf{9}$ (6th element is $(3, 9)$). Matches problem statement sample! $\checkmark$

### Example 2: Target Evaluation for $N = 100\,000, k = 10\,000$
- At sorted index $10\,000$ (0-indexed position 9999):

$$
\text{Tuple: } (194, 21417) \implies E(10\,000) = \mathbf{21\,417}
$$

---

## 6. Implementation Architecture & Algorithmic Blueprint

### Algorithmic Execution Pipeline

| Stage | Operation | Code / Formula Action | Complexity |
| :---: | :--- | :--- | :---: |
| **Stage 1** | **Radical Sieve** | Sieve radical factors $\prod p_i$ | $\mathcal{O}(N \log \log N)$ |
| **Stage 2** | **Tuple List** | `[(rad[n], n) for n in range(1, limit + 1)]` | $\mathcal{O}(N)$ |
| **Stage 3** | **Lexicographical Sort**| `elements.sort()` | $\mathcal{O}(N \log N)$ |
| **Stage 4** | **Element Extraction** | `elements[target_k - 1][1]` | $\mathcal{O}(1)$ |
| **Stage 5** | **Return Value** | Return scalar integer $21417$ | $\mathcal{O}(1)$ |

---

## 7. Mathematical Complexity & Edge Case Invariants

| Dimension | Complexity | Performance / Resource Bounds |
| :--- | :--- | :--- |
| **Time Complexity** | $\mathcal{O}(N \log N)$ where $N = 100\,000$ | $\approx 0.03$ seconds |
| **Space Complexity** | $\mathcal{O}(N)$ | Radical array & tuple list $\approx 3$ MB |
| **Dynamic Execution** | $100\%$ Inline | Multiplicative sieve with lexicographical sorting |

### Critical Invariants & Edge Cases Handled:
1. **Secondary Tie-Breaking**: Python's native tuple comparison `(rad(n), n)` breaks ties naturally using $n$ in ascending order.
2. **1-Based Indexing**: Extracting index `target_k - 1` (9999) correctly accounts for 1-indexed problem requirements.