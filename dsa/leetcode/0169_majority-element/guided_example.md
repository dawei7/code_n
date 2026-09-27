# Guided Example: Majority Element

We trace the step-by-step Boyer–Moore Voting Algorithm and pairwise cancellation dynamics on representative integer arrays:

- **Input:** $\text{nums} = [2, 2, 1, 1, 1, 2, 2]$
- **Required output:** $2$ ($2$ appears $4$ times, exceeding $\lfloor 7/2 \rfloor = 3$)
- **Alternating Sequence Instance:** $\text{nums} = [3, 2, 3] \implies 3$
- **Singleton Array Instance:** $\text{nums} = [1] \implies 1$

This instance demonstrates Boyer–Moore single-pass voting, proves why the majority element ($> \lfloor n/2 \rfloor$) strictly survives pairwise cancellation against all non-majority elements combined, and operates in $O(N)$ time with strictly $O(1)$ auxiliary space.

---

## 1. Instance & Teaching Goal

Given an integer array $\text{nums} = [2, 2, 1, 1, 1, 2, 2]$ of length $n = 7$:
Find the majority element that appears strictly more than $\lfloor n / 2 \rfloor = 3$ times.
Counting occurrences:
- Count of $1$: $3$ occurrences.
- Count of $2$: $4$ occurrences.
Since $4 > 3$, the majority element is $2$.

A hash map tracks frequencies in $O(N)$ time but requires $O(N)$ auxiliary space.
Sorting the array takes $O(N \log N)$ time (where the element at index $\lfloor n / 2 \rfloor$ is guaranteed to be the majority).
The **Boyer–Moore Voting Algorithm** achieves both $O(N)$ time and $O(1)$ space using the **Principle of Pairwise Cancellation**:
- Pair up distinct elements $(a, b)$ with $a \ne b$ and cancel them out.
- Because the true majority element constitutes strictly more than half the array ($> 50\%$), it has more occurrences than all other elements combined.
- Even if every non-majority element cancels one copy of the majority element, the majority element cannot be exhausted. The final surviving candidate must be the majority element.

---

## 2. Conceptual Foundation & Invariants

### Boyer–Moore Voting Protocol
Maintain two scalar variables:
- `candidate`: the currently leading value (initialized to $\emptyset$).
- `count`: the net surplus balance of `candidate` (initialized to $0$).

For each element $x \in \text{nums}$:
1. **Elect Candidate on Zero Balance:**
   If $\text{count} == 0$:
   $$
   \text{candidate} \leftarrow x
   $$
   $$
   \text{count} \leftarrow 1
   $$
2. **Reinforce or Cancel:**
   Else if $x == \text{candidate}$:
   $$
   \text{count} \leftarrow \text{count} + 1
   $$
   Else ($x \ne \text{candidate}$):
   $$
   \text{count} \leftarrow \text{count} - 1
   $$

Return `candidate`.

> **Invariant.** At any point where `count` drops to $0$, the evaluated prefix consists of equal numbers of candidate and non-candidate elements that cancel each other out. Discarding this balanced prefix leaves the relative majority in the remaining suffix unchanged.

---

## 3. Step-by-Step Worked Execution

We trace the algorithm on $\text{nums} = [2, 2, 1, 1, 1, 2, 2]$:

### Initialization
- `candidate = null, count = 0`.

---

### Step 1: Element $x = 2$ (Index 0)
- `count == 0` $\implies$ Elect new candidate:
  $$
  \text{candidate} = 2, \quad \text{count} = 1
  $$

---

### Step 2: Element $x = 2$ (Index 1)
- $x == \text{candidate}$ ($2 == 2$). Reinforce:
  $$
  \text{count} \leftarrow 1 + 1 = \mathbf{2}
  $$

---

### Step 3: Element $x = 1$ (Index 2)
- $x \ne \text{candidate}$ ($1 \ne 2$). Cancel one pair:
  $$
  \text{count} \leftarrow 2 - 1 = \mathbf{1}
  $$

---

### Step 4: Element $x = 1$ (Index 3)
- $x \ne \text{candidate}$ ($1 \ne 2$). Cancel one pair:
  $$
  \text{count} \leftarrow 1 - 1 = \mathbf{0}
  $$
- Prefix $[2, 2, 1, 1]$ is completely balanced (two $2$s cancelled two $1$s).
- Balance is zero.

---

### Step 5: Element $x = 1$ (Index 4)
- `count == 0` $\implies$ Elect new candidate:
  $$
  \text{candidate} = 1, \quad \text{count} = 1
  $$

---

### Step 6: Element $x = 2$ (Index 5)
- $x \ne \text{candidate}$ ($2 \ne 1$). Cancel pair:
  $$
  \text{count} \leftarrow 1 - 1 = \mathbf{0}
  $$
- Prefix $[1, 2]$ cancelled out.

---

### Step 7: Element $x = 2$ (Index 6)
- `count == 0` $\implies$ Elect new candidate:
  $$
  \text{candidate} = 2, \quad \text{count} = 1
  $$

End of array reached.
Final elected candidate: $\mathbf{2}$.

---

## 4. Complete Execution Trace

```text
Array:         [ 2,    2,    1,    1,    1,    2,    2 ]
candidate:       2     2     2     2     1     1     2
count:           1  -> 2  -> 1  -> 0  -> 1  -> 0  -> 1
Cancellations:   [ 2, 2 ] vs [ 1, 1 ] cancel!
                 [ 1 ] vs [ 2 ] cancel!
                 Surviving element: 2
```

| Index $i$ | Value $x$ | Prior State (`cand, cnt`) | Condition Evaluated | Updated `candidate` | Updated `count` | Conceptual Net State |
|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| 0 | 2 | `(null, 0)` | `cnt == 0` | 2 | 1 | Surplus of one 2 |
| 1 | 2 | `(2, 1)` | $x == \text{cand}$ | 2 | 2 | Surplus of two 2s |
| 2 | 1 | `(2, 2)` | $x \ne \text{cand}$ | 2 | 1 | One 2 cancelled by 1 |
| 3 | 1 | `(2, 1)` | $x \ne \text{cand}$ | 2 | 0 | Two 2s cancelled by two 1s |
| 4 | 1 | `(2, 0)` | `cnt == 0` | 1 | 1 | Temporary surplus of one 1 |
| 5 | 2 | `(1, 1)` | $x \ne \text{cand}$ | 1 | 0 | 1 cancelled by 2 |
| **6** | **2** | **`(1, 0)`** | **`cnt == 0`** | **2** | **1** | **Surviving Majority: 2** |

### The Cancellation Ledger

The single `count` variable stands for several simultaneous pairings. Adding them up shows the counting argument behind the invariant, and shows exactly how much of the majority survives:

| Cancellation event | Pairs matched | Running surplus of the elected candidate | Elements consumed so far | What the prefix proves |
|:---|:---|:---:|:---:|:---|
| Indices 0-1 reinforce candidate $2$ | no cancellation | $+2$ for $2$ | 2 of 7 | The prefix holds two uncancelled copies of $2$ |
| Index 2 cancels | $(2, 1)$ | $+1$ for $2$ | 3 of 7 | One copy of $2$ is retired against a $1$; the remainder is untouched |
| Index 3 cancels | $(2, 1)$ | $0$ | 4 of 7 | The prefix $[2, 2, 1, 1]$ is perfectly balanced, so removing it cannot change which value dominates the suffix $[1, 2, 2]$ |
| Index 4 elects $1$ | no cancellation | $+1$ for $1$ | 5 of 7 | The new candidate is a temporary placeholder, not a claim about the whole array |
| Index 5 cancels | $(1, 2)$ | $0$ | 6 of 7 | The second balanced prefix $[1, 2]$ is discarded as well |
| Index 6 elects $2$ | no cancellation | $+1$ for $2$ | 7 of 7 | The suffix left after both balanced prefixes is the single element $2$ |

Two balanced prefixes were discarded ($4$ elements in the first, $2$ in the second), and the element that survived both discards is $2$. In total $3$ pairs were cancelled: two copies of $2$ against two $1$s, and one $1$ against one $2$. Since $2$ occurs $4$ times and every other value occurs $3$ times in total, at most $3$ copies of $2$ could ever be cancelled — one always remains.

### Boundary Scenarios This Instance Sits Next To

| Scenario | Input | Expected | Net cancellation / final `count` | Why this boundary matters |
|:---|:---|:---:|:---:|:---|
| Single element | $[7]$ | 7 | elected on an empty ballot, final `count` $= 1$ | A one-element prefix is trivially "more than half", and the very first comparison uses `count == 0` rather than `x == candidate` |
| Strict alternation | $[3, 2, 3]$ | 3 | $3 \to$ cancel $\to 0 \to$ re-elect $3$, final `count` $= 1$ | The majority does not have to lead from the start; it can be re-elected after the count returns to zero |
| Negative values | $[-1, 2, -1, -1]$ | $-1$ | $2$ is cancelled, then $-1$ survives, final `count` $= 2$ | Comparison is by equality only, so negating an array cannot break the algorithm; a sentinel such as $0$ would be wrong here |
| Majority arrives late | $[1, 2, 3, 9, 9, 9, 9, 9]$ | 9 | four early elements cancel to $0$, then $9$ accumulates `count` $= 5$ | The whole prefix is discarded, which is legal precisely because it was balanced |
| Balanced prefix, odd tail | $[2, 2, 1, 1, 1]$ | 1 | first four elements cancel to $0$, $1$ elected with `count` $= 1$ | A one-element residue is enough when a majority exists; the guarantee is what makes the last election trustworthy |
| No majority at all | $[1, 2, 3]$ | undefined by the contract | candidate becomes $3$ with `count` $= 1$ | The vote still returns a value, so a second counting pass is needed whenever existence is not guaranteed |

---

## 5. Algorithmic Correctness

**Soundness.** Let $M$ be the majority element, with frequency $f(M) > n/2$. The total frequency of all non-majority elements is $n - f(M) < n/2$. Since each cancellation step pairs one occurrence of a candidate with one occurrence of a non-candidate, at most $n - f(M)$ occurrences of $M$ can be cancelled. Since $f(M) > n - f(M)$, at least $f(M) - (n - f(M)) = 2f(M) - n \ge 1$ occurrences of $M$ must remain uncancelled. Therefore, $M$ cannot be eliminated.

**Completeness.** A single linear pass evaluates every element exactly once. Because the problem statement guarantees that a majority element always exists, the candidate remaining at the end of the array is unconditionally the majority element.

---

## 6. Traps This Instance Exposes

- **Count Is Not Total Frequency:** The variable `count` is a *net surplus counter*, NOT the total number of times `candidate` appeared in the array! For instance, in Step 3 above, `count` dropped from 2 to 1 even though 2 appeared twice.
- **Assuming Candidate Never Changes:** Temporary candidates can and do change (as seen in Step 5 where candidate briefly switched to 1). The algorithm guarantees only that the **final** candidate is correct.
- **Arrays Without a Majority Element:** If an array has no element with frequency $> n/2$ (e.g. $[1, 2, 3]$), Boyer–Moore will still return some arbitrary candidate. In problems where existence is not guaranteed, a second $O(N)$ verification pass is required to confirm frequency $> n/2$.

### Alternative Approaches on This Array

| Approach | How it decides $[2, 2, 1, 1, 1, 2, 2]$ | Time | Auxiliary space | Tradeoff for this contract |
|:---|:---|:---:|:---:|:---|
| Hash map of frequencies | Counts $1 \to 3$ and $2 \to 4$, then returns $2$ | $O(N)$ | $O(N)$ | Optimal time but the map grows with the number of distinct values, so it forfeits the constant-space requirement |
| Sort, then read the middle position | Sorts to $[1, 1, 1, 2, 2, 2, 2]$ and returns index $\lfloor 7/2 \rfloor = 3$, which holds $2$ | $O(N \log N)$ | $O(\log N)$ to $O(N)$ depending on the sort | Correct because a value occurring more than half the time must occupy the middle slot, but it pays a logarithmic factor and may mutate the input |
| Bit-by-bit majority reconstruction | Builds the answer bit by bit, each pass keeping only the elements whose bit matches the current majority bit | $O(32N)$ | $O(1)$ | Constant space and correct, yet it needs a fixed-width integer assumption and many passes over the data |
| Boyer–Moore voting | Cancels $2$ against $1$ four times and keeps a surplus copy of $2$ | $O(N)$ | $O(1)$ | Reaches both bounds; the price is that correctness depends on the existence guarantee, so a verification pass is required when that is absent |
| Random sampling | Picks a random index and checks its value's frequency | $O(N)$ per check | $O(1)$ | The majority occupies more than half the array, so a handful of samples usually finds it, but the method is probabilistic rather than certain |

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N$ is the number of elements in `nums`. The array is scanned once, performing $O(1)$ operations per element.
- **Auxiliary Space Complexity:** $O(1)$ constant memory, requiring only two scalar variables (`candidate` and `count`).
