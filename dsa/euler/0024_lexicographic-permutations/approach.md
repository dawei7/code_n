# Lexicographic Permutations - Optimal Approach

## 1. Problem Essence & Formal Mathematical Formulation

Let $A = \{0, 1, 2, 3, 4, 5, 6, 7, 8, 9\}$ denote the ordered set of $N = 10$ decimal digits.
There are $N! = 10! = 3\,628\,800$ distinct permutations of $A$.

Let $\pi_0, \pi_1, \dots, \pi_{N!-1}$ denote the sequence of all permutations sorted in strict lexicographical order:

$$
\pi_0 <_{\text{lex}} \pi_1 <_{\text{lex}} \dots <_{\text{lex}} \pi_{N!-1}
$$

where $\pi_0 = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)$.

The objective is to compute the $1\,000\,000$-th lexicographical permutation (which corresponds to 0-indexed rank $k = 999\,999$):

$$
\mathbf{P} = \pi_{999999}
$$

---

## 2. The Naive Approach & Fundamental Bottlenecks

### Sequential Permutation Enumeration
A naive algorithm generates all permutations sequentially (e.g. using Heap's Algorithm or `itertools.islice(permutations(...), 999999, None)`):
```python
import itertools
def naive_nth_perm(target):
    return "".join(map(str, next(itertools.islice(itertools.permutations(range(10)), target - 1, None))))
```

### Computational Inefficiencies
1. **Generating 999,999 Unneeded States**: Creating and traversing $10^6$ permutations wastes CPU cycles.
2. **Direct Factoradix Decomposition**: The Factorial Number System allows computing the exact permutation directly in $\mathcal{O}(N^2)$ time with only $10$ division steps ($\approx 0.00005$ seconds).

---

## 3. Core Intuition & Mathematical Structure

### The Factorial Number System (Factoradix)
Any integer rank $k \in [0, N! - 1]$ has a unique representation in the factorial number system:

$$
k = \sum_{i=0}^{N-1} d_i \cdot i! = d_{N-1}(N-1)! + d_{N-2}(N-2)! + \dots + d_1(1!) + d_0(0!)
$$

where each factoradix digit satisfies $0 \le d_i \le i$.

### Step-by-Step Factoradix Decomposition for $k = 999\,999$

| Step $i$ | Factorial $i!$ | Quotient $d_i = \lfloor k / i! \rfloor$ | New Rank $k \leftarrow k \bmod i!$ | Available Digits Pool $A$ | Extracted Digit $A[d_i]$ |
| :---: | :---: | :---: | :---: | :--- | :---: |
| **$9$** | $362\,880$ | $\lfloor 999999 / 362880 \rfloor = \mathbf{2}$ | $274\,239$ | $[0, 1, \mathbf{2}, 3, 4, 5, 6, 7, 8, 9]$ | **$2$** |
| **$8$** | $40\,320$ | $\lfloor 274239 / 40320 \rfloor = \mathbf{6}$ | $32\,319$ | $[0, 1, 3, 4, 5, 6, \mathbf{7}, 8, 9]$ | **$7$** |
| **$7$** | $5\,040$ | $\lfloor 32319 / 5040 \rfloor = \mathbf{6}$ | $2\,079$ | $[0, 1, 3, 4, 5, 6, \mathbf{8}, 9]$ | **$8$** |
| **$6$** | $720$ | $\lfloor 2079 / 720 \rfloor = \mathbf{2}$ | $639$ | $[0, 1, \mathbf{3}, 4, 5, 6, 9]$ | **$3$** |
| **$5$** | $120$ | $\lfloor 639 / 120 \rfloor = \mathbf{5}$ | $39$ | $[0, 1, 4, 5, 6, \mathbf{9}]$ | **$9$** |
| **$4$** | $24$ | $\lfloor 39 / 24 \rfloor = \mathbf{1}$ | $15$ | $[0, \mathbf{1}, 4, 5, 6]$ | **$1$** |
| **$3$** | $6$ | $\lfloor 15 / 6 \rfloor = \mathbf{2}$ | $3$ | $[0, 4, \mathbf{5}, 6]$ | **$5$** |
| **$2$** | $2$ | $\lfloor 3 / 2 \rfloor = \mathbf{1}$ | $1$ | $[0, \mathbf{4}, 6]$ | **$4$** |
| **$1$** | $1$ | $\lfloor 1 / 1 \rfloor = \mathbf{1}$ | $0$ | $[0, \mathbf{6}]$ | **$6$** |
| **$0$** | $1$ | $\lfloor 0 / 1 \rfloor = \mathbf{0}$ | $0$ | $[\mathbf{0}]$ | **$0$** |

---

## 4. Rigorous Mathematical Breakthrough & Derivations

### Factoradix Permutation Extraction Algorithm
1. Start with the ordered pool of available digits $A = [0, 1, 2, \dots, 9]$ and 0-indexed rank $k = \text{target} - 1$.
2. For each index $i$ from $N-1$ down to $0$:

$$
d_i = \lfloor k / i! \rfloor, \quad k \leftarrow k \bmod i!
$$

3. Remove and append the element at index $d_i$ from $A$:

$$
\text{selected} = A.\operatorname{pop}(d_i)
$$

4. Concatenating the selected digits yields the exact lexicographical permutation.

---

## 5. Concrete Step-by-Step Example Walkthrough

### Example 1: Evaluation for $\{0, 1, 2\}$ at 1-Indexed Rank 4 ($k = 3$)
- $i = 2$ ($2! = 2$): $d_2 = \lfloor 3 / 2 \rfloor = 1, k \leftarrow 1$. Pop $A[1] = 1$. Remaining $A = [0, 2]$.
- $i = 1$ ($1! = 1$): $d_1 = \lfloor 1 / 1 \rfloor = 1, k \leftarrow 0$. Pop $A[1] = 2$. Remaining $A = [0]$.
- $i = 0$ ($0! = 1$): $d_0 = \lfloor 0 / 1 \rfloor = 0, k \leftarrow 0$. Pop $A[0] = 0$.
- Result: **$120$**. Matches sample! $\checkmark$

### Example 2: Target Evaluation for 1,000,000th Permutation
As traced in the table above:

$$
\mathbf{P} = \mathbf{2783915460}
$$

---

## 6. Implementation Architecture & Algorithmic Blueprint

### Algorithmic Execution Pipeline

| Stage | Operation | Code / Formula Action | Complexity |
| :---: | :--- | :--- | :---: |
| **Stage 1** | **Rank Normalization** | Set $k = \text{target} - 1 = 999\,999$, `digits = list(range(10))` | $\mathcal{O}(N)$ |
| **Stage 2** | **Factoradix Extraction** | For $i \in [9, 0]$ step $-1$: $d = k // i!, k = k \% i!$ | $10$ steps |
| **Stage 3** | **Element Pop** | `result.append(str(digits.pop(d)))` | $\mathcal{O}(N)$ |
| **Stage 4** | **Integer Concatenation** | `int("".join(result))` | $\mathcal{O}(N)$ |
| **Stage 5** | **Return Result** | Return scalar integer $2783915460$ | $\mathcal{O}(1)$ |

---

## 7. Mathematical Complexity & Edge Case Invariants

| Dimension | Complexity | Performance / Resource Bounds |
| :--- | :--- | :--- |
| **Time Complexity** | $\mathcal{O}(N^2)$ | $\approx 0.00005$ seconds for $N = 10$ |
| **Space Complexity** | $\mathcal{O}(N)$ | $10$-element digit list |
| **Dynamic Execution** | $100\%$ Inline | Factorial number system conversion |

### Critical Invariants & Edge Cases Handled:
1. **0-Indexing Offset**: Converting 1-indexed target ($10^6$) to 0-indexed rank ($999\,999$) ensures the first permutation $\pi_0$ corresponds to rank 0.
2. **Strict Range $0 \le d_i \le i$**: Quotient $d_i$ never exceeds the current length of $A$, guaranteeing index validity.