# Guided Example: Increasing Triplet Subsequence

We trace the step-by-step greedy patience sorting / LIS-2 tail tracking, dual sentinel maintenance (`mi = inf`, `mid = inf`), historical pair validity preservation across minimum updates, and third element completion verification on representative integer sequences:

- **Input:** $\text{nums} = [2, 1, 5, 0, 4, 6]$
- **Required output:** `true`
  - Valid increasing index triplet: $i = 3, j = 4, k = 5$
  - Values: $\text{nums}[3] = 0 < \text{nums}[4] = 4 < \text{nums}[5] = 6$ (also $1 < 5 < 6$)
  - Sequential state evolution:
    - $num = 2 \implies mi = 2$
    - $num = 1 \implies mi = 1$
    - $num = 5 \implies mid = 5$ (pair $(1, 5)$ established)
    - $num = 0 \implies mi = 0$ (new minimum, $mid = 5$ remains valid!)
    - $num = 4 \implies mid = 4$ (tighter pair $(0, 4)$ established)
    - $num = 6 \implies 6 > mid = 4 \implies$ triplet completed!
- **Strictly Decreasing Sequence:** $\text{nums} = [5, 4, 3, 2, 1] \implies \text{false}$ (no increasing pair exists)
- **Monotonically Increasing Array:** $\text{nums} = [1, 2, 3, 4, 5] \implies \text{true}$ (completes at third element)
- **Identical Numbers:** $\text{nums} = [1, 1, 1, 1] \implies \text{false}$ (strict inequality requires $<$ rather than $\le$)

This instance demonstrates two-variable Longest Increasing Subsequence (LIS) tracking, mathematically proves why updating $mi$ does not invalidate a previously established $mid$, contrasts $O(N)$ linear scanning with $O(N^3)$ brute force, and operates in strictly $O(1)$ auxiliary space.

---

## 1. Instance & Teaching Goal

Given array $\text{nums} = [2, 1, 5, 0, 4, 6]$ ($N = 6$):
Determine if there exists a triple of indices $(i, j, k)$ such that:
$$
i < j < k \quad \text{and} \quad \text{nums}[i] < \text{nums}[j] < \text{nums}[k]
$$
Return `true` if such a triplet exists, or `false` otherwise.

```text
Array: [2, 1, 5, 0, 4, 6]
Indices:0  1  2  3  4  5

Possible Increasing Triplets:
- (1, 2, 5): nums[1]=1 < nums[2]=5 < nums[5]=6
- (3, 4, 5): nums[3]=0 < nums[4]=4 < nums[5]=6

Output: True
```

### The Invariant of the Two Thresholds
Instead of storing every possible subsequence, we only track the **best possible tails** for subsequences of length 1 and length 2:
- $mi$: The smallest element seen so far (the best tail for a length-1 increasing sequence).
- $mid$: The smallest second element of any valid increasing pair $(\text{nums}[i], \text{nums}[j])$ with $i < j$ seen so far.
- If we ever encounter any number strictly greater than $mid$ ($num > mid$), we have instantly proven that an increasing triplet exists!

---

## 2. Conceptual Foundation & Invariants

### State Variables:
Initialize:
$$
mi = \infty, \quad mid = \infty
$$

### Transition Logic per Element $num \in nums$:
1. **Triplet Check:**
   $$
   \text{if } num > mid: \quad \text{return True}
   $$
   *(If $num > mid$, because $mid$ was formed by some earlier number smaller than $mid$, $(first, mid, num)$ is a guaranteed valid triplet).*
2. **First Element Update:**
   $$
   \text{if } num \le mi: \quad mi = num
   $$
   *(A smaller first element expands the opportunity for future pairs to form).*
3. **Second Element Update (Else Branch):**
   $$
   mid = num
   $$
   *(Here $mi < num \le mid$. Therefore $num$ forms a valid pair with $mi$, and replaces $mid$ with a tighter, smaller threshold).*

> **Key Invariant: Why Updating $mi$ is Safe.**
> Suppose $mi$ was $1$, $mid$ was set to $5$ (from pair $(1, 5)$), and later $num = 0$ arrives, resetting $mi = 0$.
> Even though $mi = 0$ appeared *after* $mid = 5$, $mid = 5$ remains a valid pair tail because the historical value $1$ that justified $mid = 5$ appeared before $5$!
> If a later number is $> 5$ (e.g. $6$), the triplet $(1, 5, 6)$ is valid. If a later number is between $0$ and $5$ (e.g. $4$), it pairs with $0$ to form $(0, 4)$, tightening $mid$ to $4$. In all cases, correctness is maintained!

---

## 3. Step-by-Step Worked Execution

We trace the state evolution on $\text{nums} = [2, 1, 5, 0, 4, 6]$:
Initialized: $mi = \infty, mid = \infty$.

---

### Step 1: $num = 2$
- $num > mid \iff 2 > \infty$ (**False**).
- $num \le mi \iff 2 \le \infty$ (**True**).
  $$
  mi \leftarrow 2
  $$
- State: $mi = 2, mid = \infty$.

---

### Step 2: $num = 1$
- $num > mid \iff 1 > \infty$ (**False**).
- $num \le mi \iff 1 \le 2$ (**True**).
  $$
  mi \leftarrow 1
  $$
- State: $mi = 1, mid = \infty$.

---

### Step 3: $num = 5$
- $num > mid \iff 5 > \infty$ (**False**).
- $num \le mi \iff 5 \le 1$ (**False**).
- Else: $mi < num \le mid$ ($1 < 5 \le \infty$).
  $$
  mid \leftarrow 5
  $$
  *(First valid increasing pair established: $(1, 5)$).*
- State: $mi = 1, mid = 5$.

---

### Step 4: $num = 0$
- $num > mid \iff 0 > 5$ (**False**).
- $num \le mi \iff 0 \le 1$ (**True**).
  $$
  mi \leftarrow 0
  $$
  *(Minimum updated to $0$. Historical pair tail $mid = 5$ is preserved!).*
- State: $mi = 0, mid = 5$.

---

### Step 5: $num = 4$
- $num > mid \iff 4 > 5$ (**False**).
- $num \le mi \iff 4 \le 0$ (**False**).
- Else: $mi < num \le mid$ ($0 < 4 \le 5$).
  $$
  mid \leftarrow 4
  $$
  *(New tighter pair established: $(0, 4)$).*
- State: $mi = 0, mid = 4$.

---

### Step 6: $num = 6$
- $num > mid \iff 6 > 4$ (**True!**).
- Condition satisfied!
- Triplet confirmed: $\text{nums}[3] = 0 < \text{nums}[4] = 4 < \text{nums}[5] = 6$.
- Immediately return:
  $$
  \mathbf{\text{True}}
  $$

---

## 4. Complete Execution Trace

```text
nums = [2, 1, 5, 0, 4, 6]
Initial: mi = inf, mid = inf

num = 2: 2 <= mi  -> mi = 2
num = 1: 1 <= mi  -> mi = 1
num = 5: 5 > mi   -> mid = 5 (pair (1, 5) active)
num = 0: 0 <= mi  -> mi = 0  (pair (1, 5) still active, mi reset to 0)
num = 4: 4 > mi   -> mid = 4 (pair (0, 4) active)
num = 6: 6 > mid  -> TRIPLET FOUND! -> return True
```

| Step | Element $num$ | Check $num > mid$? | Check $num \le mi$? | Action Taken | $mi$ (Best 1-Tail) | $mid$ (Best 2-Tail) | Active Pair Representation |
|:---:|:---:|:---:|:---:|:---|:---:|:---:|:---|
| Init | - | - | - | - | $\infty$ | $\infty$ | None |
| 1 | 2 | No | Yes | Set $mi = 2$ | 2 | $\infty$ | None |
| 2 | 1 | No | Yes | Set $mi = 1$ | 1 | $\infty$ | None |
| 3 | 5 | No | No | Set $mid = 5$ | 1 | 5 | $(1, 5)$ |
| 4 | 0 | No | Yes | Set $mi = 0$ | 0 | 5 | $(1, 5)$ active, $(0, \cdot)$ candidate |
| 5 | 4 | No | No | Set $mid = 4$ | 0 | 4 | $(0, 4)$ |
| **6** | **6** | **Yes ($6 > 4$)** | - | **Return True** | 0 | 4 | **Triplet $(0, 4, 6)$ Complete!** |

---

## 5. Algorithmic Correctness

**Soundness.** A value of $mid < \infty$ is set only when an earlier number $a$ was strictly smaller than $mid$ ($a < mid$). If a later number $num$ satisfies $num > mid$, then $a < mid < num$ is an existing increasing triplet with valid index ordering. Even if $mi$ was subsequently replaced by a value appearing after $mid$, the existence of $a$ prior to $mid$ is an immutable mathematical fact.

**Completeness.** By greedily maintaining the smallest possible $mi$ and the smallest possible $mid$, the algorithm maximizes the likelihood that any subsequent number will exceed $mid$. If any valid increasing triplet exists in the array, the greedy update rules guarantee that some element will be recognized as greater than $mid$.

---

## 6. Traps This Instance Exposes

- **Index Desynchronization Illusion:** When $mi$ becomes $0$ while $mid$ is $5$, $0$ occurs after $5$ in the array. This does not invalidate $mid = 5$ because $5$ was paired with $1$, which occurred before $5$.
- **Strict Inequality Requirement:** If the problem required non-decreasing ($\le$), equality would be permitted. For strictly increasing ($<$), checking $num \le mi$ prevents duplicate numbers from falsely triggering pair creation.
- **Premature Return on Length 2:** Only three elements complete the triplet; two elements merely set $mid$.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N$ is the number of elements in `nums`. We perform a single linear scan, executing at most 2 comparison checks per element in $O(1)$ time.
- **Auxiliary Space Complexity:** $O(1)$ strictly constant memory, using only two scalar floating-point variables ($mi, mid$).
