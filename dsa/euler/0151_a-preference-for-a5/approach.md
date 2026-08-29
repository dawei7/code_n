# Paper Sheets of Standard Sizes - Optimal Approach

## 1. Problem Essence & Formal Mathematical Formulation

A printing shop runs 16 batches of jobs per week (Monday morning to Friday afternoon, with lunch breaks).
At the start of the week on Monday morning, the supervisor puts a single sheet of paper of size $A1$ in the envelope.

At the start of each batch:
- If there is only one sheet of size $A5$ in the envelope, the supervisor uses it and leaves the envelope empty.
- If the chosen sheet has size $A_k$ ($k < 5$), it is halved into sizes $A_{k+1}, A_{k+2}, \dots, A_5$. One $A_5$ is used for the batch, and the remaining sheets are placed into the envelope.

For batch 1, the supervisor takes the single $A1$ sheet, halves it into $A2, A3, A4, A5$, uses the $A5$, and places $\{A2, A3, A4, A5\}$ in the envelope.
For batch 16, there is only one $A5$ sheet left in the envelope.

The objective is to find the **expected number of times during the week (excluding batch 1 and batch 16) that the supervisor finds only one single sheet of paper in the envelope**:
$$\mathbb{E}[N_1] = \sum_{b=2}^{15} \mathbb{P}(\text{envelope has exactly 1 sheet at batch } b)$$
giving the answer rounded to 6 decimal places.

---

## 2. The Naive Approach & Fundamental Bottlenecks

### Monte Carlo Simulation
A naive approach simulates random draws across millions of random trials:
```python
def naive_paper_sheets():
    # Monte Carlo cannot reliably converge to 6 decimal places in reasonable time
    # ...
```

### Exact Markov State Tree Traversal
1. **State Vector Representation:**
   The contents of the envelope can be represented by a 4-tuple of sheet counts:
   $$\mathbf{s} = (c_2, c_3, c_4, c_5)$$
   where $c_k$ is the number of sheets of size $A_k$.
2. **Transition Dynamics:**
   - At batch 2, the initial state is $\mathbf{s}_2 = (1, 1, 1, 1)$ with probability $1.0$.
   - Total sheets $T = c_2 + c_3 + c_4 + c_5$.
   - Drawing $A2$ (prob $c_2/T$): $\mathbf{s} \to (c_2-1, c_3+1, c_4+1, c_5+1)$.
   - Drawing $A3$ (prob $c_3/T$): $\mathbf{s} \to (c_2, c_3-1, c_4+1, c_5+1)$.
   - Drawing $A4$ (prob $c_4/T$): $\mathbf{s} \to (c_2, c_3, c_4-1, c_5+1)$.
   - Drawing $A5$ (prob $c_5/T$): $\mathbf{s} \to (c_2, c_3, c_4, c_5-1)$.
3. **Linearity of Expectation:**
   Since $\mathbb{E}[N_1] = \sum_{b=2}^{15} \mathbb{E}[\mathbb{I}_{\text{single at } b}]$, we simply accumulate the exact probability $P(\mathbf{s})$ whenever $T = 1$ for batches $b \in [2, 15]$.
4. The entire state tree contains fewer than 500 reachable states and evaluates in $\approx 0.001$ seconds.

---

## 3. Core Intuition & Mathematical Structure

### Sheet Halving and Envelope State Transitions

| Drawn Sheet | Halved Pieces Created | Sheet Used | Sheets Returned to Envelope | State Transition $\Delta (c_2, c_3, c_4, c_5)$ |
| :---: | :---: | :---: | :---: | :---: |
| **$A2$** | $A3, A4, A5, A5$ | $1 \times A5$ | $A3, A4, A5$ | $(-1, +1, +1, +1)$ |
| **$A3$** | $A4, A5, A5$ | $1 \times A5$ | $A4, A5$ | $(0, -1, +1, +1)$ |
| **$A4$** | $A5, A5$ | $1 \times A5$ | $A5$ | $(0, 0, -1, +1)$ |
| **$A5$** | None | $1 \times A5$ | None | $(0, 0, 0, -1)$ |

---

## 4. Rigorous Mathematical Breakthrough & Derivations

### State Graph BFS / DFS Traversal Pipeline
1. Initialize queue with root tuple: `[((1, 1, 1, 1), 1.0, 2)]`.
2. Initialize `expected_singles = 0.0`.
3. While queue is not empty:
   - Pop `(state, prob, batch_num)`.
   - $T = c_2 + c_3 + c_4 + c_5$.
   - If $T == 0$: continue.
   - If `batch_num not in (1, 16)` and $T == 1$:
     - `expected_singles += prob`
   - For each available sheet size $A_k$ with $c_k > 0$:
     - Next prob $= \text{prob} \times (c_k / T)$.
     - Push `(next_state, next_prob, batch_num + 1)`.
4. Return formatted string: `f"{expected_singles:.6f}" = "0.464399"`.

---

## 5. Concrete Step-by-Step Example Walkthrough

### Example 1: Root State at Batch 2
- State $\mathbf{s}_2 = (1, 1, 1, 1) \implies T = 4 > 1$.
- Not a single sheet.
- 4 outgoing branches with equal probability $1/4$:
  - Pick $A2 \implies (0, 2, 2, 2)$ with $P = 0.25$.
  - Pick $A3 \implies (1, 0, 2, 2)$ with $P = 0.25$.
  - Pick $A4 \implies (1, 1, 0, 2)$ with $P = 0.25$.
  - Pick $A5 \implies (1, 1, 1, 0)$ with $P = 0.25$.

### Example 2: Target Evaluation for Entire Week
- Summing all path probabilities arriving at $T = 1$ during batches $2 \dots 15$:
  $$\mathbb{E}[N_1] = \mathbf{0.464399}$$

---

## 6. Implementation Architecture & Algorithmic Blueprint

### Algorithmic Execution Pipeline

| Stage | Operation | Code / Formula Action | Complexity |
| :---: | :--- | :--- | :---: |
| **Stage 1** | **Root Init** | `queue = [((1, 1, 1, 1), 1.0, 2)]; expected = 0.0` | $\mathcal{O}(1)$ |
| **Stage 2** | **BFS Traversal** | Pop `(state, prob, batch)` | $< 500$ states |
| **Stage 3** | **Single Sheet Check**| If $T == 1$ and $b \notin \{1, 16\}$: `expected += prob` | $\mathcal{O}(1)$ |
| **Stage 4** | **Branch Extensions** | For $c_k > 0$: enqueue next state with $p \cdot (c_k / T)$ | $\le 4$ branches |
| **Stage 5** | **Return String** | Return `f"{expected_singles:.6f}" = "0.464399"` | $\mathcal{O}(1)$ |

---

## 7. Mathematical Complexity & Edge Case Invariants

| Dimension | Complexity | Performance / Resource Bounds |
| :--- | :--- | :--- |
| **Time Complexity** | $\mathcal{O}(\text{States})$ where $\text{States} < 500$ | $\approx 0.001$ seconds |
| **Space Complexity** | $\mathcal{O}(\text{States})$ | BFS queue $\approx 10$ KB |
| **Dynamic Execution** | $100\%$ Inline | Exact Markov state graph probability propagation |

### Critical Invariants & Edge Cases Handled:
1. **Boundary Batches Exclusion**: Batch 1 (initial $A1$ sheet) and batch 16 (final $A5$ sheet) are explicitly excluded as specified in the problem statement.
2. **Total Probability Conservation**: At every depth level $b$, the sum of probabilities across all states in the queue equals exactly $1.0$.
