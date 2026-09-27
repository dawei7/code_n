# Guided Example: Boats to Save People

We trace the step-by-step weight sorting, two-pointer boundary pairing, greedy heaviest-passenger accommodation, capacity limit constraints ($2\text{ people per boat}$), and minimum boat count derivation on representative passenger weight lists:

- **Input:**
  $$
  people = [3, 2, 2, 1], \quad limit = 3
  $$
- **Required output:** `3`
  - Rescue boat rules & constraints:
    - We have an array $people$ where $people[k]$ is the weight of the $k$-th person.
    - Each rescue boat has a maximum weight capacity $limit = 3$.
    - **Crucial capacity constraint:** Each boat can carry **at most 2 people** at the same time, provided the sum of their weights is $\le limit$.
    - Objective: Find the minimum number of boats required to rescue all people.
    - For $people = [3, 2, 2, 1]$ with $limit = 3$:
      - Person with weight $3$ must ride alone (weight $3 \le 3$, no capacity left for anyone else) $\implies \mathbf{Boat\ 1}$.
      - Person with weight $2$ can pair with person of weight $1$ ($2 + 1 = 3 \le 3$) $\implies \mathbf{Boat\ 2}$.
      - Remaining person with weight $2$ rides alone $\implies \mathbf{Boat\ 3}$.
      - Total boats needed: **`3`**.
- **The Heaviest-Passenger Greedy Invariant:**
  - **The Heaviest Bottleneck:**
    - Consider the heaviest person currently unrescued, $people[j]$.
    - This person must board some boat.
    - Who can share a boat with $people[j]$?
    - If anyone can share with $people[j]$, the **lightest person** $people[i]$ is the easiest candidate to fit ($people[i] \le people[k]$ for all other $k$).
  - **Two-Pointer Decision Rule:**
    - Sort $people$ in ascending order.
    - Let $i = 0$ (lightest) and $j = n - 1$ (heaviest).
    - **Case 1 ($people[i] + people[j] \le limit$):**
      - The lightest person and heaviest person fit together in one boat.
      - Both board: $i \leftarrow i + 1, \; j \leftarrow j - 1$.
      - Increment boat count: $ans \leftarrow ans + 1$.
    - **Case 2 ($people[i] + people[j] > limit$):**
      - If even the lightest available person cannot fit with $people[j]$, then **no one** can fit with $people[j]$.
      - Person $j$ is forced to ride alone in their own boat: $j \leftarrow j - 1$.
      - Increment boat count: $ans \leftarrow ans + 1$.
    - This greedy exchange guarantees the minimum total number of boats.

---

## 1. Instance & Teaching Goal

Given $people = [3, 2, 2, 1]$ and $limit = 3$, demonstrate how the two-pointer sweep pairs passengers.

```text
Sorted People: [1,  2,  2,  3], limit = 3
Indices:        0   1   2   3
               (i)         (j)

Step 1: Check people[i] + people[j] = 1 + 3 = 4 > 3.
        Heaviest (3) cannot pair with anyone.
        Boat 1 carries [3] alone. j moves to 2.

Step 2: Check people[i] + people[j] = 1 + 2 = 3 <= 3.
        Pair found!
        Boat 2 carries [1, 2]. i moves to 1, j moves to 1.

Step 3: i == j (index 1, weight 2).
        Single person remaining.
        Boat 3 carries [2]. i moves to 2, j moves to 0.

Total Boats = 3
```

The teaching goal is to justify why pairing the heaviest with the lightest maximizes boat sharing capacity.

---

## 2. Conceptual Foundation & Invariants

### 1. Dual-End Pointer Allocation:
With sorted weights $w_0 \le w_1 \le \dots \le w_{n-1}$:
$$
(i, j) = (0, n - 1)
$$
In every iteration, exactly one boat is allocated, and the remaining subproblem is on $[i', j - 1]$:
$$
i' = \begin{cases}
i + 1 & \text{if } w_i + w_j \le limit \\
i & \text{if } w_i + w_j > limit
\end{cases}
$$

---

## 3. Step-by-Step Worked Execution

Sort $people$ ascending:
$$
people = [1, 2, 2, 3]
$$
Parameters: $limit = 3, n = 4$.
Initialize: $i = 0, j = 3, ans = 0$.

---

### Step 1: Iteration 1 ($i = 0, j = 3$)
- Lightest weight: $people[0] = 1$.
- Heaviest weight: $people[3] = 3$.
- Combined weight:
  $$
  1 + 3 = 4 > limit = 3
  $$
- The heaviest person cannot pair with the lightest person.
- Person $3$ rides alone.
- Pointers update: $j \leftarrow 3 - 1 = 2$. ($i$ remains $0$).
- Boats used: $ans \leftarrow 0 + 1 = \mathbf{1}$.

---

### Step 2: Iteration 2 ($i = 0, j = 2$)
- Lightest weight: $people[0] = 1$.
- Heaviest weight: $people[2] = 2$.
- Combined weight:
  $$
  1 + 2 = 3 \le limit = 3
  $$
- Pair fits within limit!
- Both person $0$ and person $2$ board together.
- Pointers update: $i \leftarrow 0 + 1 = 1, \; j \leftarrow 2 - 1 = 1$.
- Boats used: $ans \leftarrow 1 + 1 = \mathbf{2}$.

---

### Step 3: Iteration 3 ($i = 1, j = 1$)
- Single person left: $people[1] = 2$.
- Because $i == j$, this person occupies the final boat alone.
- Pointers update: $i \leftarrow 1 + 1 = 2, \; j \leftarrow 1 - 1 = 0$.
- Boats used: $ans \leftarrow 2 + 1 = \mathbf{3}$.

---

### Termination:
$i = 2 > j = 0$. Loop terminates.
- **Minimum boats required:** **`3`**.

---

## 4. Complete Execution Trace

| Iteration | Lightest ($i$, Weight) | Heaviest ($j$, Weight) | Combined Weight | Condition ($\le limit$) | Passengers on Board | Pointer Updates | Total Boats $ans$ |
|:---:|:---:|:---:|:---:|:---:|:---|:---:|:---:|
| $1$ | $(0, 1)$ | $(3, 3)$ | $4$ | $4 > 3$ (Over limit) | $[3]$ (Solo) | $j: 3 \to 2$ | $1$ |
| $2$ | $(0, 1)$ | $(2, 2)$ | $3$ | $3 \le 3$ (Valid Pair) | $[1, 2]$ (Pair) | $i: 0 \to 1, \; j: 2 \to 1$ | $2$ |
| **$3$** | **$(1, 2)$** | **$(1, 2)$** | **$2$** | **Single person** | **$[2]$ (Solo)** | **$i: 1 \to 2, \; j: 1 \to 0$** | **`3`** |

---

## 5. Boundary Cases & Failure Modes

- **Everyone Can Pair Up ($[1, 2], limit = 3$):** $1 + 2 = 3 \le 3 \implies 1$ boat.
- **Everyone Must Ride Alone ($[3, 3, 3], limit = 3$):** Each pair $> limit \implies 3$ boats.
- **Single Person ($[2], limit = 3$):** $i == j$ on first step $\implies 1$ boat.
- **All People Have Identical Weight (e.g. four people of weight 2, limit 4):** Pairs $(2, 2)$ form 2 boats cleanly.

---

## 6. Traps & Common Anti-Patterns

- **Attempting to Put 3+ People in One Boat:** Even if three people have weights $1 + 1 + 1 = 3 \le limit$, each boat has a strict capacity of **at most 2 people**. Packing 3 people into a boat violates the problem specification.
- **Greedy Pairing of Lightest with Lightest:** Pairing the two lightest people leaves heavy people with no lightweight partners to absorb their deficit, forcing more boats overall.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Sorting array of $N$ weights: $\mathcal{O}(N \log N)$.
  - Two-pointer linear scan: $\mathcal{O}(N)$.
  - Total Time: $\mathcal{O}(N \log N)$, completing in $< 15$ ms for $N = 5 \times 10^4$.
- **Auxiliary Space Complexity:**
  - In-place sorting takes $\mathcal{O}(1)$ or $\mathcal{O}(\log N)$ depending on sorting implementation.
