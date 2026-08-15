# Passcode Derivation - Optimal Approach

## 1. Problem Essence & Formal Mathematical Formulation

A common security method used for online banking is to ask the user for three random characters from a passcode.
The file `keylog.txt` contains fifty successful login attempts, each consisting of three characters in the exact order they appear in the secret passcode.

Let $V = \{0, 1, 2, 3, 6, 7, 8, 9\}$ be the set of unique digits present in the logs.
Each 3-character entry $c_1 c_2 c_3$ specifies two directed precedence constraints:
$$c_1 \prec c_2 \quad \text{and} \quad c_2 \prec c_3$$

Assuming that each digit appears at most once, the objective is to find the **shortest possible secret passcode** by computing the topological ordering of the directed graph $G = (V, E)$.

---

## 2. The Naive Approach & Fundamental Bottlenecks

### Exhaustive Permutation Matching
A naive algorithm tests all permutations of digits $\{0, 1, \dots, 9\}$ against all 50 keylog entries:
```python
def naive_passcode_derivation():
    # checks 10! = 3.6 million permutations against 50 entries
    # ...
```

### Directed Acyclic Graph & Kahn's Algorithm
1. The precedence relations define a Directed Acyclic Graph (DAG) $G = (V, E)$.
2. By computing the in-degree of each vertex and applying **Kahn's Topological Sort Algorithm**, the unique valid passcode sequence is determined in $\mathcal{O}(|V| + |E|)$ time in $\approx 0.001$ seconds.

---

## 3. Core Intuition & Mathematical Structure

### Digits, In-Degrees, and Topological Sort Order

| Digit $v$ | In-Degree $d_{\text{in}}(v)$ | Directed Predecessors | Topological Step | Order Position |
| :---: | :---: | :---: | :---: | :---: |
| **$7$** | **$0$** | None (Leading digit) | Step 1 (dequeued first) | 1st |
| **$3$** | $1$ | $\{7\}$ | Step 2 (in-degree becomes 0) | 2nd |
| **$1$** | $2$ | $\{7, 3\}$ | Step 3 (in-degree becomes 0) | 3rd |
| **$6$** | $3$ | $\{7, 3, 1\}$ | Step 4 (in-degree becomes 0) | 4th |
| **$2$** | $4$ | $\{7, 3, 1, 6\}$ | Step 5 (in-degree becomes 0) | 5th |
| **$8$** | $5$ | $\{7, 3, 1, 6, 2\}$ | Step 6 (in-degree becomes 0) | 6th |
| **$9$** | $6$ | $\{7, 3, 1, 6, 2, 8\}$ | Step 7 (in-degree becomes 0) | 7th |
| **$0$** | $7$ | $\{7, 3, 1, 6, 2, 8, 9\}$ | Step 8 (dequeued last) | 8th |

---

## 4. Rigorous Mathematical Breakthrough & Derivations

### Kahn's Topological Sort Pipeline
1. Parse the 50 lines from `keylog.txt`.
2. For each attempt $c_1 c_2 c_3$:
   - Add directed edges $c_1 \to c_2$ and $c_2 \to c_3$.
   - Update in-degrees for $c_2$ and $c_3$.
3. Enqueue all vertices with $\text{in\_degree} = 0$ (initially just vertex `7`).
4. While queue is not empty:
   - Pop vertex $u$, append to `passcode`.
   - For each neighbor $v$ of $u$:
     - Decrement $\text{in\_degree}[v]$.
     - If $\text{in\_degree}[v] == 0$, enqueue $v$.
5. Convert ordered character array to integer.

---

## 5. Concrete Step-by-Step Example Walkthrough

### Example 1: Sample Constraints
- Given entries like `319`, `680`, `180`, `690`, `129`, `620`, `762`:
  - `7` appears before `6`, `3` appears before `1`, `1` appears before `6`, etc.
- Unique digits present: $\{0, 1, 2, 3, 6, 7, 8, 9\}$ ($|V| = 8$, digits 4 and 5 never appear).

### Example 2: Target Passcode Resolution
- Topological Sort sequence:
  $$7 \to 3 \to 1 \to 6 \to 2 \to 8 \to 9 \to 0$$
- Shortest Secret Passcode:
  $$\mathbf{73162890}$$

---

## 6. Implementation Architecture & Algorithmic Blueprint

### Algorithmic Execution Pipeline

| Stage | Operation | Code / Formula Action | Complexity |
| :---: | :--- | :--- | :---: |
| **Stage 1** | **File Loading** | Read `keylog.txt` lines | $\mathcal{O}(M)$ |
| **Stage 2** | **Graph Construction** | Add edges $c_1 \to c_2 \to c_3$, record in-degrees | $\mathcal{O}(M)$ |
| **Stage 3** | **Queue Init** | `deque([n for n in nodes if in_degree[n] == 0])` | $\mathcal{O}(|V|)$ |
| **Stage 4** | **Kahn's Sort Loop** | Pop $u$, decrement neighbors, enqueue 0 in-degree | $\mathcal{O}(|V| + |E|)$ |
| **Stage 5** | **Return Value** | Return scalar integer $73162890$ | $\mathcal{O}(1)$ |

---

## 7. Mathematical Complexity & Edge Case Invariants

| Dimension | Complexity | Performance / Resource Bounds |
| :--- | :--- | :--- |
| **Time Complexity** | $\mathcal{O}(|V| + |E|)$ where $|V| \le 10, |E| \le 50$ | $\approx 0.001$ seconds |
| **Space Complexity** | $\mathcal{O}(|V| + |E|)$ | Graph dictionary $\approx 1$ KB |
| **Dynamic Execution** | $100\%$ Inline | Topological sort precedence resolution |

### Critical Invariants & Edge Cases Handled:
1. **Dynamic Path Resolution**: Resolves `keylog.txt` relative to package location without relying on external working directories.
2. **Strict Acyclicity**: The underlying DAG contains zero cycles, guaranteeing a complete and unique topological ordering of all 8 digits.
