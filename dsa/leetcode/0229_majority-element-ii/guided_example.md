# Guided Example: Majority Element II

We trace the step-by-step Boyer-Moore generalized two-candidate voting algorithm, triplet cancellation, and second-pass frequency verification on representative integer arrays:

- **Input:** $\text{nums} = [3, 2, 3]$
- **Required output:** `[3]` (Appears 2 times, which is strictly greater than $\lfloor 3 / 3 \rfloor = 1$)
- **Two Majorities Instance:** $\text{nums} = [1, 1, 1, 3, 3, 2, 2, 2] \implies [1, 2]$ (Both $1$ and $2$ appear 3 times, exceeding $\lfloor 8 / 3 \rfloor = 2$)
- **No Majority Instance:** $\text{nums} = [1, 2, 3, 4] \implies []$ (Threshold is $\lfloor 4 / 3 \rfloor = 1$; no element appears $> 1$ times)
- **Single Element Instance:** $\text{nums} = [1] \implies [1]$ ($\lfloor 1 / 3 \rfloor = 0$, $1 > 0$)

This instance demonstrates the generalized Boyer-Moore voting mechanism ($k = 3$), mathematically proves why at most 2 elements can exceed $\lfloor N / 3 \rfloor$, explains triplet cancellation (discarding groups of 3 distinct values), avoids hash maps for $O(1)$ space, and completes in $O(N)$ time.

---

## 1. Instance & Teaching Goal

Given an integer array $\text{nums} = [3, 2, 3]$ of size $N = 3$:
Find all elements that appear **strictly more than $\lfloor N / 3 \rfloor$ times**.
Here, $\lfloor 3 / 3 \rfloor = 1$.
The required frequency threshold is strictly $> 1$ (at least 2 occurrences).
- Value $3$ appears 2 times ($2 > 1$). **Qualifies.**
- Value $2$ appears 1 time ($1 \not> 1$). Does not qualify.
Output: `[3]`.

### Mathematical Limit: At Most Two Majorities
Why can there be at most **two** majority elements exceeding $\lfloor N / 3 \rfloor$?
Suppose there were 3 distinct elements $e_1, e_2, e_3$, each appearing $> \lfloor N / 3 \rfloor$ times.
Then each element appears at least $\lfloor N / 3 \rfloor + 1$ times:
$$
\text{Total Occurrences} \ge 3 \times \left(\left\lfloor \frac{N}{3} \right\rfloor + 1\right) > 3 \times \frac{N}{3} = N
$$
The total count would strictly exceed the size of the array, which is impossible!
Therefore, the answer can contain **at most 2 candidates**.
Instead of tracking frequencies of all distinct numbers in a hash map ($O(N)$ space), we only need **two candidate slots** and **two counters** ($O(1)$ space).

---

## 2. Conceptual Foundation & Invariants

### The Boyer-Moore Triplet Cancellation Principle
In Boyer-Moore I (majority $> N/2$), identical pairs cancel different elements ($2$-element cancellation).
In Boyer-Moore II (majority $> N/3$), we cancel **triplets of three distinct elements**:
- Whenever three distinct values $\{a, b, c\}$ are encountered, dropping all three reduces the size of the array by 3 while reducing the count of each element by at most 1.
- Any element that truly appears $> N/3$ times cannot be eliminated by these cancellations and will survive in one of the two candidate slots!

### Pass 1: Candidate Election Protocol
Maintain candidates $c_1, c_2$ and counters $\text{cnt}_1, \text{cnt}_2$ initialized to $0$:
For each element $x \in \text{nums}$:
1. If $x == c_1$: increment $\text{cnt}_1 += 1$.
2. Else if $x == c_2$: increment $\text{cnt}_2 += 1$.
3. Else if $\text{cnt}_1 == 0$: assign $c_1 \leftarrow x, \, \text{cnt}_1 \leftarrow 1$.
4. Else if $\text{cnt}_2 == 0$: assign $c_2 \leftarrow x, \, \text{cnt}_2 \leftarrow 1$.
5. Else: **Triplet cancellation!**
   $$
   \text{cnt}_1 \leftarrow \text{cnt}_1 - 1, \quad \text{cnt}_2 \leftarrow \text{cnt}_2 - 1
   $$

*(Critical Invariant: Checks $x == c_1$ and $x == c_2$ must be evaluated before replacing a zero-count slot to prevent the same number from occupying both candidate registers)*.

### Pass 2: Exact Frequency Verification
Pass 1 guarantees that if a majority element exists, it must be in $\{c_1, c_2\}$. However, it does not guarantee that surviving candidates actually meet the threshold.
Count the actual occurrences of $c_1$ and $c_2$ across the original array:
- If $\text{count}(c_1) > \lfloor N / 3 \rfloor$: add $c_1$ to results.
- If $c_2 \ne c_1$ and $\text{count}(c_2) > \lfloor N / 3 \rfloor$: add $c_2$ to results.

> **Invariant.** If an element appears $> \lfloor N / 3 \rfloor$ times in $\text{nums}$, it will finish Pass 1 in either $c_1$ or $c_2$.

---

## 3. Step-by-Step Worked Execution

We trace the two passes on $\text{nums} = [3, 2, 3]$ ($N = 3, \lfloor 3/3 \rfloor = 1$):

### Pass 1: Candidate Election
Initialize $c_1 = \text{None}, \text{cnt}_1 = 0, \quad c_2 = \text{None}, \text{cnt}_2 = 0$.

1. **Element $x = 3$:**
   - Matches $c_1$ or $c_2$? No.
   - $\text{cnt}_1 == 0 \implies c_1 \leftarrow 3, \, \text{cnt}_1 \leftarrow 1$.
   - State: $c_1 = 3 (\text{cnt}_1 = 1), \quad c_2 = \text{None} (\text{cnt}_2 = 0)$.
2. **Element $x = 2$:**
   - Matches $c_1 (3)$? No.
   - Matches $c_2$? No.
   - $\text{cnt}_1 == 0$? No.
   - $\text{cnt}_2 == 0 \implies c_2 \leftarrow 2, \, \text{cnt}_2 \leftarrow 1$.
   - State: $c_1 = 3 (\text{cnt}_1 = 1), \quad c_2 = 2 (\text{cnt}_2 = 1)$.
3. **Element $x = 3$:**
   - Matches $c_1 (3)$? **Yes!**
   - Increment $\text{cnt}_1 \leftarrow 1 + 1 = 2$.
   - State: $c_1 = 3 (\text{cnt}_1 = 2), \quad c_2 = 2 (\text{cnt}_2 = 1)$.

Pass 1 completes with candidates $c_1 = 3$ and $c_2 = 2$.

---

### Pass 2: Frequency Verification
Count actual occurrences of candidates in $\text{nums} = [3, 2, 3]$:
- For candidate $c_1 = 3$:
  $$
  \text{actual\_count} = 2
  $$
  Compare with threshold: $2 > \lfloor 3 / 3 \rfloor = 1$ $\implies \mathbf{3 \text{ qualifies!}}$
- For candidate $c_2 = 2$:
  $$
  \text{actual\_count} = 1
  $$
  Compare with threshold: $1 \not> 1$ $\implies 2$ fails.

Final output: $\mathbf{[3]}$.

---

## 4. Complete Execution Trace

```text
nums = [3, 2, 3], N = 3, threshold = floor(3/3) = 1

Pass 1 (Voting):
i = 0, x = 3: cnt1=0 -> c1 = 3, cnt1 = 1
i = 1, x = 2: cnt2=0 -> c2 = 2, cnt2 = 1
i = 2, x = 3: x == c1 -> cnt1 = 2

Candidates: c1 = 3, c2 = 2

Pass 2 (Verification):
count(3) = 2 > 1 -> KEEP 3
count(2) = 1 <= 1 -> REJECT 2

Result: [3]
```

| Step | Element $x$ | Candidate 1 ($c_1, \text{cnt}_1$) | Candidate 2 ($c_2, \text{cnt}_2$) | Action Rule Applied | Status |
|:---:|:---:|:---:|:---:|:---|:---|
| Init | - | $(\text{None}, 0)$ | $(\text{None}, 0)$ | Initialize | - |
| 1 | 3 | $(3, 1)$ | $(\text{None}, 0)$ | Fill empty slot 1 | Elected $c_1 = 3$ |
| 2 | 2 | $(3, 1)$ | $(2, 1)$ | Fill empty slot 2 | Elected $c_2 = 2$ |
| **3** | **3** | **$(3, 2)$** | **$(2, 1)$** | **Increment $c_1$ vote** | **Pass 1 Complete** |
| Verify | 3 | Count in array $= 2$ | Threshold $= 1$ | $2 > 1 \implies$ Valid | **`[3]`** |
| Verify | 2 | Count in array $= 1$ | Threshold $= 1$ | $1 \not> 1 \implies$ Invalid | Discarded |

---

## 5. Algorithmic Correctness

**Soundness.** Pass 2 counts the exact frequency of both candidates across the entire array. An element is added to the result if and only if its true frequency strictly exceeds $\lfloor N / 3 \rfloor$.

**Completeness.** Suppose an element $M$ appears $C > \lfloor N / 3 \rfloor$ times. Each triplet cancellation decrements $\text{cnt}_M$ by at most 1, while simultaneously discarding 2 other distinct elements not equal to $M$. Since there are only $N - C$ elements other than $M$, at most $\frac{N - C}{2}$ triplet cancellations can ever occur. Since $C > N/3$, $C - \frac{N - C}{2} = \frac{3C - N}{2} > 0$. Therefore, $M$'s count can never be driven to zero by non-$M$ elements, ensuring $M$ survives Pass 1.

---

## 6. Traps This Instance Exposes

- **Missing Verification Pass:** In Boyer-Moore, surviving candidates are not guaranteed to exceed the threshold (e.g. on `[1, 2, 3, 4]`, two numbers will survive Pass 1 with count 1, but neither exceeds $\lfloor 4/3 \rfloor = 1$). Pass 2 is mandatory.
- **Equal Candidates Trap:** If `x == c1` is not checked before `cnt2 == 0`, a duplicate of $c_1$ could be placed into $c_2$, leaving both slots holding the same value.
- **Strict Inequality:** The condition is strictly greater than $\lfloor N / 3 \rfloor$, not greater than or equal to. If $N = 6$, threshold is $2$; an element with 2 occurrences does not qualify.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N$ is the length of `nums`. Pass 1 performs $N$ constant-time iterations. Pass 2 performs $N$ comparisons to verify counts. Total runtime is $2N = O(N)$.
- **Auxiliary Space Complexity:** $O(1)$ constant memory, storing only the scalar variables $c_1, c_2, \text{cnt}_1, \text{cnt}_2$.
