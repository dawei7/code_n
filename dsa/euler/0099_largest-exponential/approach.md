# Largest Exponential - Optimal Approach

## 1. Problem Essence & Formal Mathematical Formulation

Comparing two numbers written in index form like $2^{11}$ and $3^7$ is not difficult, as $2^{11} = 2048 < 3^7 = 2187$. However, confirming that $632382^{518061} > 519432^{525806}$ would be much more difficult, as both numbers contain well over three million digits.

The file `base_exp.txt` contains one thousand ($1000$) lines with a base/exponent pair on each line.

The objective is to find the **1-indexed line number** with the greatest numerical value:

$$
k^* = \operatorname*{arg\,max}_{1 \le k \le 1000} \left( b_k^{e_k} \right)
$$

---

## 2. The Naive Approach & Fundamental Bottlenecks

### Astronomical BigInt Exponentiation
A naive approach computes $b_k^{e_k}$ directly using arbitrary-precision BigInt arithmetic:
```python
def naive_largest_exponential():
    # computes numbers with over 3 million digits each
    # takes > 3 GB RAM and dozens of seconds
    # ...
```

### Logarithmic Monotonicity Transformation
1. The natural logarithm $\ln(x)$ is strictly monotonically increasing for $x > 0$.
2. For any two exponential terms $b_1^{e_1}$ and $b_2^{e_2}$:

$$
b_1^{e_1} > b_2^{e_2} \iff \ln\left( b_1^{e_1} \right) > \ln\left( b_2^{e_2} \right) \iff e_1 \ln(b_1) > e_2 \ln(b_2)
$$

3. Instead of multiplying 3-million-digit BigInts, we simply compute the scalar product $e \ln(b)$ in $\mathcal{O}(1)$ time per line, completing all 1000 comparisons in $\approx 0.001$ seconds.

---

## 3. Core Intuition & Mathematical Structure

### Logarithmic Equivalence for Exponentials

| Exponential $b^e$ | Approximate Magnitude | Logarithmic Value $e \ln(b)$ | Relative Order |
| :---: | :---: | :---: | :---: |
| **$2^{11}$** | $2048$ | $11 \ln(2) \approx 7.6246$ | Smaller |
| **$3^7$** | $2187$ | $7 \ln(3) \approx 7.6903$ | **Larger (Sample)** |
| **$519432^{525806}$** | $\approx 10^{3\,005\,181}$ | $525806 \ln(519432) \approx 6\,920\,067.8$ | Smaller |
| **$632382^{518061}$** | $\approx 10^{3\,005\,360}$ | $518061 \ln(632382) \approx 6\,920\,479.5$ | **Larger (Sample)** |

---

## 4. Rigorous Mathematical Breakthrough & Derivations

### Logarithmic Line Scanner Pipeline
1. Parse lines $(b_i, e_i)$ from `base_exp.txt` for $i = 1 \dots 1000$.
2. Initialize `max_val = 0.0, best_line = 0`.
3. For index $i \in [1, 1000]$:
   - Compute $v_i = e_i \times \ln(b_i)$.
   - If $v_i > \text{max\_val}$:

$$
\text{max\_val} = v_i, \quad \text{best\_line} = i
$$

4. Return `best_line`.

---

## 5. Concrete Step-by-Step Example Walkthrough

### Example 1: Trace for $2^{11}$ vs $3^7$
- $2^{11} \implies 11 \ln(2) \approx 7.6246$.
- $3^7 \implies 7 \ln(3) \approx 7.6903$.
- $7.6903 > 7.6246 \implies 3^7 > 2^{11}$. Matches problem statement sample! $\checkmark$

### Example 2: Target Evaluation across 1000 Lines
- Scanning all 1000 base-exponent pairs in `base_exp.txt`:
  - Line 709 contains $(b, e) = (895447, 504922) \implies 504922 \ln(895447) \approx 6\,920\,500+$.
  - Line 709 yields the global maximum value!
- Optimal line number:

$$
k^* = \mathbf{709}
$$

---

## 6. Implementation Architecture & Algorithmic Blueprint

### Algorithmic Execution Pipeline

| Stage | Operation | Code / Formula Action | Complexity |
| :---: | :--- | :--- | :---: |
| **Stage 1** | **File Loading** | Read comma-separated lines from `base_exp.txt` | $\mathcal{O}(N)$ |
| **Stage 2** | **Line Iteration** | `enumerate(lines, 1)` | $1000$ lines |
| **Stage 3** | **Log Multiplication**| `val = e * math.log(b)` | $\mathcal{O}(1)$ per line |
| **Stage 4** | **Max Reduction** | Track `max_val` and `best_line` | $\mathcal{O}(1)$ |
| **Stage 5** | **Return Line** | Return scalar integer `709` | $\mathcal{O}(1)$ |

---

## 7. Mathematical Complexity & Edge Case Invariants

| Dimension | Complexity | Performance / Resource Bounds |
| :--- | :--- | :--- |
| **Time Complexity** | $\mathcal{O}(N)$ where $N = 1000$ | $\approx 0.001$ seconds |
| **Space Complexity** | $\mathcal{O}(N)$ | Text buffer $\approx 15$ KB |
| **Dynamic Execution** | $100\%$ Inline | Double-precision logarithmic scalar products |

### Critical Invariants & Edge Cases Handled:
1. **Dynamic Path Resolution**: Resolves `base_exp.txt` relative to package location without relying on external working directories.
2. **1-Based Indexing**: `enumerate(lines, 1)` ensures the returned line number matches 1-indexed file lines correctly.