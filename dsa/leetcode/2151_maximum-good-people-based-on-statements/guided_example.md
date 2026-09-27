# Guided Example: Maximum Good People Based on Statements

We analyze and execute the exhaustive bitmask consistency validation algorithm on a representative problem instance, demonstrating how treating truth-telling as a one-way implication model enables complete state space pruning.

- **Input:** `statements = [[2, 1, 2], [1, 2, 2], [2, 0, 2]]`
- **Output:** `2`

This instance illustrates binary state encoding, truth-teller assertion verification, contradiction short-circuiting, and popcount maximization.

---

## 1. Problem Overview & Representative Instance

A group of $n$ people contains two types of individuals:
- **Good people:** Always tell the truth. Every statement made by a good person must be factually accurate under the chosen classification.
- **Bad people:** May tell the truth or lie. Their statements are completely unconstrained and carry no predictive validity.

We are given an $n \times n$ matrix `statements`, where `statements[i][j]` records person $i$'s assertion regarding person $j$:
- `0`: Person $i$ claims person $j$ is bad.
- `1`: Person $i$ claims person $j$ is good.
- `2`: Person $i$ makes no statement about person $j$.

No person makes statements about themselves (`statements[i][i] = 2`).

The goal is to find the maximum possible number of people who can be classified as good in a consistent assignment, where no good person's statement is contradicted.

In our representative instance:
- Group size: $n = 3$.
- `statements = [[2, 1, 2], [1, 2, 2], [2, 0, 2]]`.
  - Person 0 states: Person 1 is good (`statements[0][1] = 1`).
  - Person 1 states: Person 0 is good (`statements[1][0] = 1`).
  - Person 2 states: Person 1 is bad (`statements[2][1] = 0`).

We must determine the largest subset of individuals who can simultaneously be good without logical conflict.

---

## 2. Mathematical & Algorithmic Principles

### Unilateral Implication Model

Let $T_i \in \{0, 1\}$ denote the assigned type of person $i$:
$$T_i = \begin{cases} 1 & \text{person } i \text{ is good} \\ 0 & \text{person } i \text{ is bad} \end{cases}$$

The problem semantics follow standard propositional implication:
$$T_i = 1 \implies \Big(\forall j: \text{statements}[i][j] \ne 2 \implies T_j = \text{statements}[i][j]\Big)$$

Notice the asymmetry:
- If $T_i = 1$, any mismatch ($T_j \ne \text{statements}[i][j]$) renders the configuration **invalid**.
- If $T_i = 0$, the implication $0 \implies \dots$ is vacuously true. The assertions made by bad individuals are ignored.

### Bitmask Space Enumeration

Because $n \le 15$, the entire universe of possible assignments contains:
$$2^n \le 2^{15} = 32768 \text{ states}$$

Each configuration can be represented as an integer bitmask $M \in [0, 2^n - 1]$, where bit $i$ of $M$ represents $T_i$:
$$T_i = (M \gg i) \ \& \ 1$$

For each mask $M$:
1. Check whether all active good persons ($T_i = 1$) make statements consistent with $M$.
2. If consistent, calculate the number of good people via Hamming weight (population count):
$$\text{count}(M) = \sum_{i=0}^{n-1} T_i$$
3. Maintain the global maximum over all consistent masks:
$$\text{MaxGood} = \max_{M \text{ is valid}} \text{popcount}(M)$$

| Concept / Variable | Formal Encoding | Role in Algorithmic Execution |
|---|---|---|
| Assignment Mask $M$ | Integer in $[0, 2^n - 1]$ | Encodes candidate binary partition of good/bad individuals |
| Type Extraction $T_i$ | $(M \gg i) \ \& \ 1$ | Tests if person $i$ is hypothesized to be good |
| Statement Compatibility | $\text{statements}[i][j] == T_j$ | Required for all good persons $i$ whenever statement is not $2$ |
| Contradiction Condition | $T_i = 1 \land \text{statements}[i][j] \ne 2 \land \text{statements}[i][j] \ne T_j$ | Immediately disqualifies mask $M$ |
| Objective Function | $\max \text{popcount}(M)$ | Identifies largest valid truth-telling coalition |

---

## 3. Step-by-Step Walkthrough with Intermediate State

We trace candidate bitmasks for $n = 3$, evaluating from highest population count downward.

```
People: {0, 1, 2}
statements:
[0]: calls 1 good
[1]: calls 0 good
[2]: calls 1 bad

Mask 111 (count 3): Person 2 is good, says 1 is bad. But 1 is good => CONTRADICTION
Mask 110 (count 2): People 0, 1 good; 2 bad.
  - 0 says 1 is good => True
  - 1 says 0 is good => True
  - 2's statement ignored
  => VALID!
```

### Step 1: Evaluate Mask $M = 7$ (`111` in binary)
- Candidate assignment: $T_0 = 1, T_1 = 1, T_2 = 1$.
- Popcount: $3$.
- Verify assertions of good individuals:
  - Person 0 ($T_0 = 1$): `statements[0][1] = 1`, matches $T_1 = 1$. (Valid)
  - Person 1 ($T_1 = 1$): `statements[1][0] = 1`, matches $T_0 = 1$. (Valid)
  - Person 2 ($T_2 = 1$): `statements[2][1] = 0`, but $T_1 = 1$! (Contradiction!)
- Conclusion: Person 2 claims Person 1 is bad, but Person 1 is good. Mask `111` is invalid.

### Step 2: Evaluate Mask $M = 6$ (`110` in binary)
- Bit mapping: bit 0 is $0$, bit 1 is $1$, bit 2 is $1$ (People 1 and 2 good; 0 bad).
- Candidate assignment: $T_0 = 0, T_1 = 1, T_2 = 1$.
- Popcount: $2$.
- Verify assertions:
  - Person 1 ($T_1 = 1$): `statements[1][0] = 1`, but $T_0 = 0$! (Contradiction!)
- Conclusion: Person 1 claims Person 0 is good, but Person 0 is bad. Mask `110` is invalid.

### Step 3: Evaluate Mask $M = 5$ (`101` in binary)
- Candidate assignment: $T_0 = 1, T_1 = 0, T_2 = 1$ (People 0 and 2 good; 1 bad).
- Popcount: $2$.
- Verify assertions:
  - Person 0 ($T_0 = 1$): `statements[0][1] = 1`, but $T_1 = 0$! (Contradiction!)
- Conclusion: Person 0 claims Person 1 is good, but Person 1 is bad. Mask `101` is invalid.

### Step 4: Evaluate Mask $M = 3$ (`011` in binary)
- Note: Bit 0 is $1$, bit 1 is $1$, bit 2 is $0$.
- Candidate assignment: $T_0 = 1, T_1 = 1, T_2 = 0$ (People 0 and 1 good; Person 2 bad).
- Popcount: $2$.
- Verify assertions:
  - Person 0 ($T_0 = 1$):
    - `statements[0][1] = 1`: matches $T_1 = 1$. (Valid)
    - `statements[0][2] = 2`: no statement. (Valid)
  - Person 1 ($T_1 = 1$):
    - `statements[1][0] = 1`: matches $T_0 = 1$. (Valid)
    - `statements[1][2] = 2`: no statement. (Valid)
  - Person 2 ($T_2 = 0$): Person 2 is bad. Statements ignored!
- Conclusion: No statement made by any good person is contradicted. Mask `011` is **valid**.
- Active maximum: $\max(0, 2) = 2$.

### Step 5: Remaining Subsets
- Any remaining mask has $\text{popcount} \le 1$.
- Since an assignment with $2$ good people is already proven consistent, no smaller subset can exceed $2$.
- Maximum good people achievable: $2$.

---

## 4. Comprehensive State Trace

The table below catalogs all $8$ potential assignments for the group:

| Mask $M$ | Binary $[T_2, T_1, T_0]$ | Good Subset | Popcount | Evaluated Statements | First Contradiction Detected | Validity Status |
|---|---|---|---|---|---|---|
| $7$ | `111` | $\{0, 1, 2\}$ | $3$ | Person 2: $1$ is bad | Conflict with $T_1 = 1$ | Invalid |
| $6$ | `110` | $\{1, 2\}$ | $2$ | Person 1: $0$ is good | Conflict with $T_0 = 0$ | Invalid |
| $5$ | `101` | $\{0, 2\}$ | $2$ | Person 0: $1$ is good | Conflict with $T_1 = 0$ | Invalid |
| $4$ | `100` | $\{2\}$ | $1$ | Person 2: $1$ is bad | Matches $T_1 = 0$ | **Valid** |
| $3$ | `011` | $\{0, 1\}$ | $2$ | Person 0: $1$ good<br>Person 1: $0$ good | None (Matches $T_1=1, T_0=1$) | **Valid (Optimum)** |
| $2$ | `010` | $\{1\}$ | $1$ | Person 1: $0$ is good | Conflict with $T_0 = 0$ | Invalid |
| $1$ | `001` | $\{0\}$ | $1$ | Person 0: $1$ is good | Conflict with $T_1 = 0$ | Invalid |
| $0$ | `000` | $\emptyset$ | $0$ | None (no good people) | None | **Valid** |

Global maximum count of good people: $2$ (achieved by subset $\{0, 1\}$).

---

## 5. Algorithmic Correctness & Soundness

### Soundness
A mask $M$ is declared valid only if every pair $(i, j)$ where $T_i = 1$ and $\text{statements}[i][j] \ne 2$ satisfies $\text{statements}[i][j] == T_j$. This guarantees that under this assignment, no truth-telling person has uttered a false claim.

### Completeness
The loop over $M \in [0, 2^n - 1]$ iterates over every possible subset of $\{0, 1, \dots, n - 1\}$. Because every conceivable truth-value assignment is explicitly tested, the global maximum over valid configurations cannot miss any valid state.

---

## 6. Edge Cases & Anti-Patterns

### Edge Cases
1. **Mutual Accusation:** `statements = [[2, 0], [0, 2]]`. Two people each call the other bad. Mask `11` fails because good person 0 says 1 is bad, contradicting $T_1 = 1$. Masks `10` and `01` both succeed with count $1$.
2. **All Neutral Statements:** If all non-diagonal entries are `2`, no person makes any statements. The mask $M = 2^n - 1$ (everyone good) has zero constraints to violate, returning $n$.
3. **No Good People Possible:** If every individual makes statements that force global circular contradictions, the empty mask $M = 0$ (all bad) remains valid, returning $0$.
4. **Disjoint Components:** If individuals form disconnected statement clusters, each cluster resolves independently; bitmask search naturally finds the optimal product of choices across components.

### Common Anti-Patterns
- **Evaluating Statements from Bad People:** Checking if a bad person's statement is false is incorrect. Bad people *may* tell the truth or lie. Imposing constraints on bad individuals falsely prunes valid assignments.
- **2-SAT Misapplication:** 2-SAT requires symmetric implications ($A \implies B \iff \neg B \implies \neg A$). Here, if person $i$ is bad, person $i$'s statements provide no implication about other people, making the logical relation asymmetric and NP-complete on general graphs.
- **Greedy Selection:** Picking people with the fewest accusations fails because cascading mutual endorsements can validate large clusters that initially look conflicting.

---

## 7. Complexity Analysis

### Time Complexity
- There are $2^n$ candidate bitmasks.
- For each mask:
  - Checking consistency requires testing all pairs $(i, j)$ where $T_i = 1$.
  - There are at most $n$ good people, each making up to $n$ statement checks, taking $O(n^2)$ operations in the worst case (or $O(n)$ using bitwise word operations).
- Total time complexity is $O(2^n \cdot n^2)$.
- For $n \le 15$, $2^{15} \times 15^2 = 32768 \times 225 \approx 7.3 \times 10^6$ basic operations, which executes in under $30$ milliseconds.

### Auxiliary Space Complexity
- Bitmask enumeration requires only scalar integer loop variables.
- No dynamic memory allocation or recursive call frames are needed.
- Total auxiliary space complexity is $O(1)$.
