# Names Scores - Optimal Approach

## 1. Problem Essence & Formal Mathematical Formulation

Let $\mathcal{N} = \{ S_1, S_2, \dots, S_N \}$ denote a set of $N = 5163$ first names written in uppercase Latin letters.
Let $\pi$ be the permutation that sorts $\mathcal{N}$ in strict lexicographical (alphabetical) order:

$$
S_{\pi(1)} <_{\text{lex}} S_{\pi(2)} <_{\text{lex}} \dots <_{\text{lex}} S_{\pi(N)}
$$

For any name string $S$, define its alphabetical value $V(S)$ as the sum of the alphabetical positions of its letters:

$$
V(S) = \sum_{i=1}^{|S|} (\operatorname{ord}(S[i]) - 64) \quad \text{where } \text{A} = 1, \dots, \text{Z} = 26
$$

The **name score** of the $k$-th sorted name $S_{\pi(k)}$ is the product of its 1-based rank $k$ and its alphabetical value:

$$
\operatorname{Score}(k) = k \cdot V(S_{\pi(k)})
$$

The objective is to compute the total sum of all name scores in the dataset:

$$
\text{TotalScore} = \sum_{k=1}^N k \cdot V(S_{\pi(k)})
$$

---

## 2. The Naive Approach & Fundamental Bottlenecks

### Unsorted File Traversal
A naive approach calculates letter values without sorting or using an incorrect collation (such as case-sensitive ASCII sorting with quotes included):
```python
# Fails because rank k must strictly reflect sorted alphabetical position
```

### Computational Requirements
1. **Global Sorting Requirement**: Ranks $k \in [1, 5163]$ require sorting all $5163$ names alphabetically ($\mathcal{O}(N \log N \cdot L)$).
2. **Character Value Arithmetic**: ASCII offset `ord(c) - 64` maps uppercase characters $\text{'A'}\dots\text{'Z'}$ to $1\dots26$ in $\mathcal{O}(1)$ time.

---

## 3. Core Intuition & Mathematical Structure

### Letter Mapping & Name Value Decomposition

| Letter | ASCII Code | Offset $\operatorname{ord}(c) - 64$ | Example Name | Letter Values | Alphabetical Value $V(S)$ |
| :---: | :---: | :---: | :---: | :--- | :---: |
| **A** | $65$ | $1$ | `"COLIN"` | $\text{C}=3, \text{O}=15, \text{L}=12, \text{I}=9, \text{N}=14$ | $3+15+12+9+14 = \mathbf{53}$ |
| **B** | $66$ | $2$ | `"MARY"` | $\text{M}=13, \text{A}=1, \text{R}=18, \text{Y}=25$ | $13+1+18+25 = \mathbf{57}$ |
| **Z** | $90$ | $26$ | `"PATRICIA"` | $\text{P}=16, \text{A}=1, \text{T}=20, \text{R}=18, \text{I}=9, \text{C}=3, \text{I}=9, \text{A}=1$ | $\mathbf{77}$ |

---

## 4. Rigorous Mathematical Breakthrough & Derivations

### Sorting & Linear Reduction
1. Parse the comma-separated text into individual strings, stripping enclosing quotation marks.
2. Sort the array of $5163$ names in alphabetical order using standard lexicographical comparison.
3. For each name $S_k$ at 1-based index $k \in [1, 5163]$:

$$
\text{Score}(k) = k \sum_{c \in S_k} (\operatorname{ord}(c) - 64)
$$

4. Accumulate all scores into the exact total integer $\text{TotalScore}$.

---

## 5. Concrete Step-by-Step Example Walkthrough

### Example 1: Trace for `"COLIN"`
- In the sorted list of $5163$ names, `"COLIN"` appears at position $k = 938$.
- Letter values for $\text{COLIN}$:
  - $\text{C} = 3$
  - $\text{O} = 15$
  - $\text{L} = 12$
  - $\text{I} = 9$
  - $\text{N} = 14$
  - Value: $V(\text{"COLIN"}) = 3 + 15 + 12 + 9 + 14 = 53$.
- Name score:

$$
\operatorname{Score}(938) = 938 \times 53 = \mathbf{49\,714} \quad \checkmark
$$

### Example 2: Total Dataset Evaluation ($N = 5163$)
Accumulating across all $5163$ sorted names:

$$
\text{TotalScore} = \mathbf{871\,198\,282}
$$

---

## 6. Implementation Architecture & Algorithmic Blueprint

### Algorithmic Execution Pipeline

| Stage | Operation | Code / Formula Action | Complexity |
| :---: | :--- | :--- | :---: |
| **Stage 1** | **File Loading** | Read `names.txt` relative to package directory | $\mathcal{O}(\text{file size})$ |
| **Stage 2** | **Parsing & Stripping** | Split commas and strip quotes `"` | $\mathcal{O}(N \cdot L)$ |
| **Stage 3** | **Lexicographical Sort** | `sorted(names)` via Timsort | $\mathcal{O}(N \log N \cdot L)$ |
| **Stage 4** | **Rank Scoring** | `for idx, name in enumerate(names, 1): score += idx * V(name)` | $\mathcal{O}(N \cdot L)$ |
| **Stage 5** | **Return Total** | Return scalar integer $871198282$ | $\mathcal{O}(1)$ |

---

## 7. Mathematical Complexity & Edge Case Invariants

| Dimension | Complexity | Performance / Resource Bounds |
| :--- | :--- | :--- |
| **Time Complexity** | $\mathcal{O}(N \log N \cdot L)$ | $\approx 0.005$ seconds for $5163$ names |
| **Space Complexity** | $\mathcal{O}(N \cdot L)$ | Array of $5163$ strings $\approx 50$ KB |
| **Dynamic Execution** | $100\%$ Inline | Exact file parsing, sorting, and scoring |

### Critical Invariants & Edge Cases Handled:
1. **1-Based Indexing**: Ranks are strictly 1-based ($k = 1, 2, \dots, N$) as specified.
2. **Offline Local Path Resolution**: Resolves `names.txt` relative to `__file__` without hardcoding absolute user machine paths.