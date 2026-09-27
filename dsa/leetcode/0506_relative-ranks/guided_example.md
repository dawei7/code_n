# Guided Example: Relative Ranks

We trace the step-by-step indirect index sorting by descending score, podium medal assignment (`"Gold Medal"`, `"Silver Medal"`, `"Bronze Medal"`), numerical rank string formatting for remaining athletes (`str(rank)`), and original order restoration on representative competition scores:

- **Input:** $score = [10, 3, 8, 9, 4]$
- **Required output:** `["Gold Medal", "5", "Bronze Medal", "Silver Medal", "4"]`
  - Number of athletes: $n = 5$
  - Scoring rules: Highest score gets Rank 1, second highest Rank 2, etc.
  - Podium titles:
    - 1st Place: `"Gold Medal"`
    - 2nd Place: `"Silver Medal"`
    - 3rd Place: `"Bronze Medal"`
    - 4th Place onwards: `"4"`, `"5"`, $\dots$
- **Indirect sorting execution trace:**
  - Original athlete indices: $[0, 1, 2, 3, 4]$
  - Sort indices descending by score value ($score[j]$):
    - Score $10$ (Index $0$) $\to$ Rank 1
    - Score $9$ (Index $3$) $\to$ Rank 2
    - Score $8$ (Index $2$) $\to$ Rank 3
    - Score $4$ (Index $4$) $\to$ Rank 4
    - Score $3$ (Index $1$) $\to$ Rank 5
    - Sorted index permutation:
      $$
      idx = [0, \; 3, \; 2, \; 4, \; 1]
      $$
  - **Assign Ranks to Original Positions:**
    - **Rank 1 ($i = 0$, Athlete $idx[0] = 0$):**
      - Top 1 $\implies ans[0] = \mathbf{\text{"Gold Medal"}}$
    - **Rank 2 ($i = 1$, Athlete $idx[1] = 3$):**
      - Top 2 $\implies ans[3] = \mathbf{\text{"Silver Medal"}}$
    - **Rank 3 ($i = 2$, Athlete $idx[2] = 2$):**
      - Top 3 $\implies ans[2] = \mathbf{\text{"Bronze Medal"}}$
    - **Rank 4 ($i = 3$, Athlete $idx[3] = 4$):**
      - $i \ge 3 \implies ans[4] = \text{str}(3 + 1) = \mathbf{\text{"4"}}$
    - **Rank 5 ($i = 4$, Athlete $idx[4] = 1$):**
      - $i \ge 3 \implies ans[1] = \text{str}(4 + 1) = \mathbf{\text{"5"}}$
  - Assembled answer array in original order:
    $$
    ans = [\mathbf{\text{"Gold Medal"}}, \; \mathbf{\text{"5"}}, \; \mathbf{\text{"Bronze Medal"}}, \; \mathbf{\text{"Silver Medal"}}, \; \mathbf{\text{"4"}}]
    $$
- **Already Sorted Descending Instance ($score = [5, 4, 3, 2, 1]$):**
  - Indices are unchanged $\implies \mathbf{[\text{"Gold Medal"}, \text{"Silver Medal"}, \text{"Bronze Medal"}, \text{"4"}, \text{"5"}]}$
- **Small Podium Input ($n = 2, score = [1, 2]$):**
  - Score 2 at index 1 gets Gold, Score 1 at index 0 gets Silver $\implies \mathbf{[\text{"Silver Medal"}, \text{"Gold Medal"}]}$
- **Single Athlete ($score = [100]$):** Returns $\mathbf{[\text{"Gold Medal"}]}$.

This instance demonstrates indirect permutation sorting, mathematically proves why sorting indices preserves original input positions while evaluating order statistics, and derives $O(N \log N)$ runtime and $O(N)$ space bounds.

---

## 1. Instance & Teaching Goal

Given an integer array $score$ of size $n$ where $score[i]$ is the score of the $i$-th athlete:
All scores are guaranteed to be unique.
Assign ranks based on scores:
- 1st place (highest score): `"Gold Medal"`
- 2nd place: `"Silver Medal"`
- 3rd place: `"Bronze Medal"`
- 4th place and below: their placement number as a string (e.g. `"4"`, `"5"`).
Return the rank array in the **original input order** of athletes.

```text
Input Scores: [ 10,   3,   8,   9,   4 ]
Athletes:       A0   A1   A2   A3   A4

Rank by Score:
  1st: A0 (Score 10) -> "Gold Medal"
  2nd: A3 (Score  9) -> "Silver Medal"
  3rd: A2 (Score  8) -> "Bronze Medal"
  4th: A4 (Score  4) -> "4"
  5th: A1 (Score  3) -> "5"

Restore to original index order [A0, A1, A2, A3, A4]:
  ["Gold Medal", "5", "Bronze Medal", "Silver Medal", "4"]
```

### The Indirect Sorting Pattern
- Sorting the array $score$ directly loses the original mapping of which athlete had which score.
- Instead of sorting the values, **we sort the array of indices** $[0, 1, \dots, n-1]$ using the score values as the comparison key:
  $$
  idx.\text{sort}(\text{key} = -score)
  $$
- The resulting list $idx$ tells us:
  - $idx[0]$ is the index of the athlete who earned 1st place.
  - $idx[1]$ is the index of the athlete who earned 2nd place.
  - And so forth.
- We then place the rank strings directly into $ans[idx[i]]$.

---

## 2. Conceptual Foundation & Invariants

### 1. Index Permutation:
Let $idx$ be a permutation of $\{0, 1, \dots, n - 1\}$ such that:
$$
score[idx[0]] > score[idx[1]] > \dots > score[idx[n-1]]
$$

### 2. Podium and Number Assignment:
For each rank position $i \in [0, n - 1]$:
Let $j = idx[i]$ be the athlete's original index:
$$
ans[j] =
\begin{cases}
\text{"Gold Medal"} & \text{if } i == 0 \\
\text{"Silver Medal"} & \text{if } i == 1 \\
\text{"Bronze Medal"} & \text{if } i == 2 \\
\text{str}(i + 1) & \text{if } i \ge 3
\end{cases}
$$

> **Bijection Invariant.** Because each index $j \in [0, n-1]$ appears exactly once in $idx$, every athlete is assigned exactly one rank without gaps or collisions.

---

## 3. Step-by-Step Worked Execution

We trace $score = [10, 3, 8, 9, 4]$ ($n = 5$):

---

### Step 1: Initialize and Sort Index Array
- Initial indices: $idx = [0, 1, 2, 3, 4]$.
- Sort indices by descending score:
  - $score[0] = 10$ (Rank 1)
  - $score[3] = 9$ (Rank 2)
  - $score[2] = 8$ (Rank 3)
  - $score[4] = 4$ (Rank 4)
  - $score[1] = 3$ (Rank 5)
- Permuted indices:
  $$
  idx = [0, \; 3, \; 2, \; 4, \; 1]
  $$

---

### Step 2: Assign Labels to Output Array $ans$
Initialize $ans$ of size $5$:

1. **Rank 1 ($i = 0$, Athlete $j = idx[0] = 0$):**
   - $ans[0] = \mathbf{\text{"Gold Medal"}}$
2. **Rank 2 ($i = 1$, Athlete $j = idx[1] = 3$):**
   - $ans[3] = \mathbf{\text{"Silver Medal"}}$
3. **Rank 3 ($i = 2$, Athlete $j = idx[2] = 2$):**
   - $ans[2] = \mathbf{\text{"Bronze Medal"}}$
4. **Rank 4 ($i = 3$, Athlete $j = idx[3] = 4$):**
   - $ans[4] = \text{str}(3 + 1) = \mathbf{\text{"4"}}$
5. **Rank 5 ($i = 4$, Athlete $j = idx[4] = 1$):**
   - $ans[1] = \text{str}(4 + 1) = \mathbf{\text{"5"}}$

---

### Step 3: Final Output Array
$$
ans = [\mathbf{\text{"Gold Medal"}}, \; \mathbf{\text{"5"}}, \; \mathbf{\text{"Bronze Medal"}}, \; \mathbf{\text{"Silver Medal"}}, \; \mathbf{\text{"4"}}]
$$

---

## 4. Complete Execution Trace

| Rank Position $i + 1$ | Permuted Index $j = idx[i]$ | Athlete Score $score[j]$ | Assigned Label | Output Target $ans[j]$ |
|:---:|:---:|:---:|:---:|:---:|
| **1st** | $0$ | $10$ | `"Gold Medal"` | $ans[0]$ |
| **2nd** | $3$ | $9$ | `"Silver Medal"` | $ans[3]$ |
| **3rd** | $2$ | $8$ | `"Bronze Medal"` | $ans[2]$ |
| **4th** | $4$ | $4$ | `"4"` | $ans[4]$ |
| **5th** | $1$ | $3$ | `"5"` | $ans[1]$ |

---

## 5. Boundary Cases & Failure Modes

- **Single Athlete ($n = 1$):** Loop runs once for $i = 0 \implies \mathbf{[\text{"Gold Medal"}]}$.
- **Two Athletes ($n = 2$):** Only Gold and Silver awarded $\implies \mathbf{[\text{"Silver Medal"}, \text{"Gold Medal"}]}$.
- **Three Athletes ($n = 3$):** Exactly Gold, Silver, and Bronze awarded.
- **Large $n = 10^4$:** Standard $O(N \log N)$ index sorting finishes in $< 10$ ms.

---

## 6. Traps & Common Anti-Patterns

- **Using Nested Loops ($O(N^2)$ Rank Counting):** Counting how many numbers are greater than $score[i]$ by scanning the entire array for each athlete takes $O(N^2)$ time. Index sorting solves the problem in $O(N \log N)$.
- **1-Indexed vs 0-Indexed Placement Strings:** Placing athlete $i=3$ with string `str(i)` yields `"3"` instead of `"4"`. Ranks are 1-indexed, requiring `str(i + 1)`.
- **Modifying Scores In-Place:** Overwriting the score array with strings causes type-casting errors in statically typed languages and destroys the original input values.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Initializing the index array takes $O(N)$ time.
  - Sorting $N$ indices takes $O(N \log N)$ time.
  - Assigning strings to the output array takes $O(N)$ time.
  - Total Time: $\mathcal{O}(N \log N)$. For $N = 10^4$, finishes in $< 8$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(N)$ space for the index permutation array $idx$ and output string array $ans$.
