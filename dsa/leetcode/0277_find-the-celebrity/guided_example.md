# Guided Example: Find the Celebrity

We trace the step-by-step tournament elimination pass ($N - 1$ queries), transitive candidate survivor isolation, and dual bidirectional verification on representative party relationship matrices:

- **Input:** $n = 3, \quad \text{graph} = \begin{bmatrix} 1 & 1 & 0 \\ 0 & 1 & 0 \\ 1 & 1 & 1 \end{bmatrix}$ (where $\text{graph}[i][j] == 1$ represents $\text{knows}(i, j) == \text{True}$)
- **Required output:** $1$ (Person 1 is known by 0 and 2, but knows nobody else)
- **No Celebrity Cycle:** $n = 3, \quad \text{graph} = \begin{bmatrix} 1 & 0 & 1 \\ 1 & 1 & 0 \\ 0 & 1 & 1 \end{bmatrix} \implies -1$ (Cyclic dependencies: 0 knows 2, 2 knows 1, 1 knows 0; survivor fails verification)
- **Minimal Pair:** $n = 2, \quad \text{graph} = \begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix} \implies 1$ (Query $\text{knows}(0, 1) == \text{True}$ eliminates 0)

This instance demonstrates binary reduction via deductive elimination, proves why every call to `knows(a, b)` unconditionally eliminates at least one person from celebrity contention, details the necessity of the second verification pass to catch instances where no celebrity exists, and bounds total API calls strictly to $3N - 3$ in $O(1)$ auxiliary space.

---

## 1. Instance & Teaching Goal

Given $n = 3$ people labeled $0, 1, 2$ and an API `knows(a, b)`:
A **celebrity** is defined by two simultaneous conditions:
1. **Outgoing degree is 0:** The celebrity knows **nobody else** at the party.
2. **Incoming degree is $n - 1$:** **Everyone else** knows the celebrity.

Adjacency truth matrix:
$$
\text{knows}(i, j) = \begin{pmatrix}
(0,0)=1 & (0,1)=1 & (0,2)=0 \\
(1,0)=0 & (1,1)=1 & (1,2)=0 \\
(2,0)=1 & (2,1)=1 & (2,2)=1
\end{pmatrix}
$$
- Person 0 knows 1 (cannot be celebrity).
- Person 2 knows 0 and 1 (cannot be celebrity).
- Person 1 knows nobody other than self, and is known by both 0 and 2.
Output: $\mathbf{1}$.

### The $O(N^2)$ vs $O(N)$ API Call Bottleneck
A brute-force matrix check makes $N(N - 1) = O(N^2)$ queries.
However, **a single query `knows(a, b)` always eliminates one person:**
- If $\text{knows}(a, b) == \text{True}$: $a$ knows someone, so **$a$ is definitely not a celebrity**.
- If $\text{knows}(a, b) == \text{False}$: $b$ is unknown to $a$, so **$b$ is definitely not a celebrity**.
In exactly $N - 1$ queries, we can eliminate $N - 1$ candidates, leaving a single potential survivor.

---

## 2. Conceptual Foundation & Invariants

### Phase 1: Candidate Elimination Tournament ($N - 1$ queries)
Initialize `cand = 0`:
For each person $i$ from $1$ to $n - 1$:
- Query $\text{knows}(\text{cand}, i)$:
  - If $\text{True}$: $\text{cand}$ knows $i$, so $\text{cand}$ is disqualified. Person $i$ becomes the new candidate:
    $$
    \text{cand} \leftarrow i
    $$
  - If $\text{False}$: person $i$ is not known by $\text{cand}$, so person $i$ is disqualified. $\text{cand}$ remains unchanged.

### Phase 2: Candidate Verification ($\le 2(N - 1)$ queries)
Elimination only proves that *if* a celebrity exists, it must be `cand`. It does **not** prove that `cand` actually is a celebrity!
We must verify `cand` against all other $i \ne \text{cand}$:
1. **Outgoing check:** If $\text{knows}(\text{cand}, i) == \text{True} \implies \text{return } -1$.
2. **Incoming check:** If $\text{knows}(i, \text{cand}) == \text{False} \implies \text{return } -1$.
If `cand` passes all checks for all $i \ne \text{cand}$, return `cand`.

> **Invariant.** After the elimination loop, all persons other than `cand` are provably non-celebrities. If a real celebrity exists, it cannot have been eliminated and must be `cand`.

---

## 3. Step-by-Step Worked Execution

We trace the algorithm on $n = 3$ with relationship matrix:
- $\text{knows}(0, 1) = \text{True}$
- $\text{knows}(0, 2) = \text{False}$
- $\text{knows}(1, 0) = \text{False}, \quad \text{knows}(1, 2) = \text{False}$
- $\text{knows}(2, 0) = \text{True}, \quad \text{knows}(2, 1) = \text{True}$

---

### Phase 1: Elimination Pass

#### Step 1: Initialize Candidate
$$
\text{cand} = 0
$$

#### Step 2: Compare $\text{cand} = 0$ with $i = 1$
- Query: $\text{knows}(0, 1)$.
- Result: $\text{True}$.
- Deduction: Person 0 knows person 1. Therefore, Person 0 cannot be the celebrity!
- Update candidate:
  $$
  \text{cand} \leftarrow 1
  $$
  *(Person 0 eliminated)*.

#### Step 3: Compare $\text{cand} = 1$ with $i = 2$
- Query: $\text{knows}(1, 2)$.
- Result: $\text{False}$.
- Deduction: Person 1 does not know person 2. If person 2 were the celebrity, person 1 would have known them. Therefore, Person 2 cannot be the celebrity!
- Update candidate:
  $$
  \text{cand} \text{ remains } 1
  $$
  *(Person 2 eliminated)*.

Tournament finished. Sole remaining survivor: $\text{cand} = \mathbf{1}$.

#### Eligibility Frontier After Each Query

The tournament is easier to audit when the candidate is tracked together with
the set of people who are still *possible* celebrities. Every probe evicts
exactly one person, so after query $k$ that frontier holds $n - k$ labels, and
the identity of the survivor never depends on the order in which the queries
were asked.

| Query # | Probe | Read | Evicted from eligibility | Why the eviction is forced | Eligible set after |
|:---:|:---|:---:|:---:|:---|:---|
| 0 (no probe yet) | — | — | — | No relationship information has been gathered | $\{0, 1, 2\}$ |
| 1 | $\text{knows}(0, 1)$ | $\text{True}$ | Person 0 | A celebrity has outdegree $0$, so knowing anyone excludes them | $\{1, 2\}$ |
| 2 | $\text{knows}(1, 2)$ | $\text{False}$ | Person 2 | A celebrity has indegree $n - 1$; person 1 does not know person 2, so 2 fails it | $\{1\}$ |

The frontier shrinks by exactly one entry per probe, which is what makes $n - 1$
probes sufficient to isolate a single candidate.

---

### Phase 2: Verification Pass on $\text{cand} = 1$

We check both relationship directions for all $i \ne 1$:

#### Check against Person $i = 0$:
1. Outgoing: $\text{knows}(1, 0) == \text{False}$ (**Pass**: Candidate knows nobody).
2. Incoming: $\text{knows}(0, 1) == \text{True}$ (**Pass**: Person 0 knows candidate).

#### Check against Person $i = 2$:
1. Outgoing: $\text{knows}(1, 2) == \text{False}$ (**Pass**: Candidate knows nobody).
2. Incoming: $\text{knows}(2, 1) == \text{True}$ (**Pass**: Person 2 knows candidate).

Candidate $1$ satisfies all $2(N - 1) = 4$ verification criteria.
**Return $1$!**

---

## 4. Complete Execution Trace

```text
n = 3
Phase 1: Elimination
  cand = 0
  i = 1: knows(0, 1) is True  -> 0 eliminated -> cand = 1
  i = 2: knows(1, 2) is False -> 2 eliminated -> cand = 1
  Survivor: 1

Phase 2: Verification
  i = 0: knows(1, 0) is False (OK), knows(0, 1) is True (OK)
  i = 2: knows(1, 2) is False (OK), knows(2, 1) is True (OK)
  All checks pass!

Result: 1
```

| Phase | Query Target $(a, b)$ | API Result | Deduction / Elimination | Current Candidate $\text{cand}$ |
|:---|:---:|:---:|:---|:---:|
| Elimination | $\text{knows}(0, 1)$ | $\text{True}$ | 0 knows 1 $\implies$ 0 disqualified | 1 |
| Elimination | $\text{knows}(1, 2)$ | $\text{False}$ | 1 doesn't know 2 $\implies$ 2 disqualified | **1 (Survivor)** |
| Verification | $\text{knows}(1, 0)$ | $\text{False}$ | Candidate 1 does not know 0 | 1 |
| Verification | $\text{knows}(0, 1)$ | $\text{True}$ | Person 0 knows candidate 1 | 1 |
| Verification | $\text{knows}(1, 2)$ | $\text{False}$ | Candidate 1 does not know 2 | 1 |
| Verification | $\text{knows}(2, 1)$ | $\text{True}$ | Person 2 knows candidate 1 | 1 |
| **Conclusion** | - | - | All conditions satisfied | **$\mathbf{1}$ (Celebrity)** |

### Contrast: When No Celebrity Exists (Cycle $[0 \to 2 \to 1 \to 0]$)
1. The elimination pass evicts person 1 ($\text{knows}(0, 1) == \text{False}$) and then person 0 ($\text{knows}(0, 2) == \text{True}$), so the survivor is person 2.
2. Verification against $i = 0$ passes both directions: $\text{knows}(2, 0) == \text{False}$ and $\text{knows}(0, 2) == \text{True}$.
3. Verification against $i = 1$ fails at the **outgoing** probe: $\text{knows}(2, 1) == \text{True}$, so the survivor does know someone after all.
4. The pass therefore returns $\mathbf{-1}$ without ever reaching the incoming probe $\text{knows}(1, 2)$.

### Boundary Census Across the Visited Instances

The same two-phase procedure produces all four outcomes below. Read the fourth
column as the single probe that decides the verdict: a pass means verification
completed, and any other entry names the first probe that contradicted one of the
two celebrity conditions.

| Instance | $n$ | Survivor after elimination | Decisive probe from Phase 2 | Probe value | Returned |
|:---|:---:|:---:|:---|:---:|:---:|
| Celebrity in the middle | 3 | Person 1 | none: all $2(n - 1) = 4$ probes pass | — | $1$ |
| Cycle $0 \to 2 \to 1 \to 0$ | 3 | Person 2 | $\text{knows}(2, 1)$ (outgoing) | $\text{True}$ | $-1$ |
| Minimal pair, celebrity last | 2 | Person 1 | none: both probes pass | — | $1$ |
| Minimal pair, mutual acquaintance | 2 | Person 1 | $\text{knows}(1, 0)$ (outgoing) | $\text{True}$ | $-1$ |
| Minimal pair, mutual strangers | 2 | Person 0 | $\text{knows}(1, 0)$ (incoming) | $\text{False}$ | $-1$ |
| Maximum party, everyone knows everyone | 100 | Person 99 | $\text{knows}(99, 0)$ (outgoing) | $\text{True}$ | $-1$ |

Two rows deserve emphasis. The mutual-stranger pair is the only shape where the
first survivor fails the *incoming* condition, because each person is unknown to
the other; and at $n = 2$ the elimination pass spends its single probe and the
verification pass spends exactly two, so the smallest legal party already uses
the full $3n - 3 = 3$ budget.

---

## 5. Algorithmic Correctness

**Soundness.** A returned index `cand` has been explicitly verified in Phase 2: $\text{knows}(\text{cand}, i) == \text{False}$ and $\text{knows}(i, \text{cand}) == \text{True}$ for all $i \ne \text{cand}$. This satisfies the exact mathematical definition of a celebrity.

**Completeness.** Suppose person $C$ is the celebrity. In Phase 1, whenever $C$ is compared against another person $X$:
- If $\text{cand} == C$ and $i == X$: $\text{knows}(C, X)$ is $\text{False}$, so $X$ is eliminated and $\text{cand}$ remains $C$.
- If $\text{cand} == X$ and $i == C$: $\text{knows}(X, C)$ is $\text{True}$, so $X$ is eliminated and $\text{cand}$ becomes $C$.
Thus, a true celebrity can **never be eliminated**. The survivor must be $C$.

---

## 6. Traps This Instance Exposes

- **Skipping Verification (Phase 2):** Returning the elimination survivor directly fails whenever no celebrity exists. The tournament guarantees only that everyone else is disqualified, not that the survivor is valid.
- **Self-Query Trap:** Querying $\text{knows}(i, i)$ provides no information because people know themselves. The loops must strictly test $i \ne \text{cand}$.
- **API Call Budget:** Total calls in Phase 1 is $N - 1$. Total calls in Phase 2 is at most $2(N - 1)$. Total queries $\le 3N - 3$, satisfying the minimum call constraint.

### Alternative Strategies and What Each One Costs

| Strategy | Query pattern | Query bound | Probes at $n = 100$ | Auxiliary space | Tradeoff or failure mode |
|:---|:---|:---:|:---:|:---:|:---|
| Tournament then verify (this lesson) | One probe per challenger, then two probes per opponent of the survivor | $3n - 3$ | $\le 297$ | $O(1)$ | None beyond the constant: the elimination probe count is fixed at $n - 1$ and cannot be reduced |
| Exhaustive tally | Ask every ordered pair once and count indegree and outdegree per person | $n(n - 1)$ | $9900$ | $O(n)$ | Correct but $O(n^2)$ probes; it blows the $3n$ call budget and learns nothing the tournament misses |
| Stack pairing | Push every label, repeatedly pop two, keep the one that survives the pair, push it back | $3n - 3$ | $\le 297$ | $O(n)$ | Same probe count, but the stack holds up to $n$ labels, so it trades the constant-space guarantee for no benefit |
| Two-pointer convergence | Start at persons $0$ and $n - 1$; advance the left index when $\text{knows}(\text{left}, \text{right})$ is $\text{True}$, otherwise retreat the right index | $3n - 3$ | $\le 297$ | $O(1)$ | Equally cheap, but each step discards an endpoint on faith; skipping either verification direction silently accepts the cycle instance |

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N$ is the number of people. Phase 1 performs $N - 1$ API calls. Phase 2 performs at most $2(N - 1)$ API calls. The maximum number of API calls is $3N - 3$, which is strictly linear.
- **Auxiliary Space Complexity:** $O(1)$ auxiliary space. Only a single candidate tracker `cand` is stored.
