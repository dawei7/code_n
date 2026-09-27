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

---

## 5. Algorithmic Correctness

**Soundness.** Let $M$ be the majority element, with frequency $f(M) > n/2$. The total frequency of all non-majority elements is $n - f(M) < n/2$. Since each cancellation step pairs one occurrence of a candidate with one occurrence of a non-candidate, at most $n - f(M)$ occurrences of $M$ can be cancelled. Since $f(M) > n - f(M)$, at least $f(M) - (n - f(M)) = 2f(M) - n \ge 1$ occurrences of $M$ must remain uncancelled. Therefore, $M$ cannot be eliminated.

**Completeness.** A single linear pass evaluates every element exactly once. Because the problem statement guarantees that a majority element always exists, the candidate remaining at the end of the array is unconditionally the majority element.

---

## 6. Traps This Instance Exposes

- **Count Is Not Total Frequency:** The variable `count` is a *net surplus counter*, NOT the total number of times `candidate` appeared in the array! For instance, in Step 3 above, `count` dropped from 2 to 1 even though 2 appeared twice.
- **Assuming Candidate Never Changes:** Temporary candidates can and do change (as seen in Step 5 where candidate briefly switched to 1). The algorithm guarantees only that the **final** candidate is correct.
- **Arrays Without a Majority Element:** If an array has no element with frequency $> n/2$ (e.g. $[1, 2, 3]$), Boyer–Moore will still return some arbitrary candidate. In problems where existence is not guaranteed, a second $O(N)$ verification pass is required to confirm frequency $> n/2$.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N$ is the number of elements in `nums`. The array is scanned once, performing $O(1)$ operations per element.
- **Auxiliary Space Complexity:** $O(1)$ constant memory, requiring only two scalar variables (`candidate` and `count`).
