# Guided Example: Find the Score of All Prefixes of an Array

## 1. Two derived arrays, one shared running maximum

The task is built from two definitions that compose. The **conversion array** of an array `arr` replaces every element by itself plus the largest element seen so far in that same array: $\text{conver}[i] = \text{arr}[i] + \max(\text{arr}[0..i])$. The **score** of an array is then the sum of its conversion array. Given a **0-indexed** array `nums` of length $n$, we must report, for every $i$, the score of the prefix `nums[0..i]`.

Each answer therefore involves a prefix sum *of* a prefix maximum. The danger is the obvious reading of that sentence: computing each prefix's score independently costs $O(i)$ per prefix and $O(n^{2})$ overall. The lesson derives the two scalar quantities that make every prefix score available in constant additional work.

## 2. The representative input

Official Example 1 is the ideal teaching instance, because its running maximum both rises and stands still:

| Index $i$ | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| `nums[i]` | 2 | 3 | 7 | 5 | 10 |

The required output is `[4, 10, 24, 36, 56]`. The element `5` at index 3 is the informative one: it is smaller than every element before it, so it cannot become the new maximum, yet it still contributes to the score through `conver[3]`, where it is paired with the prefix maximum `7`. That `7` happens to sit immediately to its left, which makes the row look like a neighbour sum when it is nothing of the kind; a small element is always added to the *largest value of the whole prefix*, itself included.

The five prefixes and their conversion arrays, computed straight from the definition:

| Prefix $i$ | Sub-array | Conversion array | Score |
|---|---|---|---|
| 0 | `[2]` | `[4]` | 4 |
| 1 | `[2, 3]` | `[4, 6]` | 10 |
| 2 | `[2, 3, 7]` | `[4, 6, 14]` | 24 |
| 3 | `[2, 3, 7, 5]` | `[4, 6, 14, 12]` | 36 |
| 4 | `[2, 3, 7, 5, 10]` | `[4, 6, 14, 12, 20]` | 56 |

## 3. The structural observation: each conversion array extends the previous one

Read the middle column of the table downwards. The conversion array of prefix $i$ is the conversion array of prefix $i-1$ followed by one new term. This is not a coincidence specific to the example; it follows from the definition of the inner maximum.

The term $\text{conver}[j]$ inside the prefix `nums[0..i]` is $\text{nums}[j] + \max(\text{nums}[0..j])$. The index bound of that maximum is $j$, never $i$, so the value of $\text{conver}[j]$ is identical whether it is computed inside the prefix of length $i$ or inside any longer prefix. Old conversion terms are therefore immutable once the prefix has passed them, and the only new work for prefix $i$ is the single term

$$
\text{conver}[i] = \text{nums}[i] + M_i, \qquad M_i = \max(\text{nums}[0..i]).
$$

Writing $S_i$ for the score of the prefix `nums[0..i]` and $S_{-1} = 0$ for the empty prefix, immutability gives the one-line recurrence that solves the problem:

$$
S_i = S_{i-1} + \text{conver}[i] = S_{i-1} + \text{nums}[i] + M_i .
$$

The two scalars the sweep must carry are therefore the running maximum $M$ and the running score $S$. The running maximum itself needs no history either:

$$
M_i = \max(M_{i-1}, \text{nums}[i]), \qquad M_{-1} = -\infty .
$$

```mermaid
accTitle: Data flow of the running maximum and the running score
accDescr: The current element and the previous running maximum combine into the new running maximum, the element plus that maximum forms the new conversion term, and adding that term to the previous score produces the current answer entry.
flowchart LR
    A["nums[i]"] --> B["M[i] = max(M[i-1], nums[i])"]
    B --> C["conver[i] = nums[i] + M[i]"]
    A --> C
    C --> D["S[i] = S[i-1] + conver[i]"]
    E["S[i-1]"] --> D
    D --> F["ans[i] = S[i]"]
```

## 4. The sweep, one index at a time

Both scalars are read, updated, and written in a single left-to-right pass. `none` in the $M_{i-1}$ column marks the state before any element has been examined:

| $i$ | `nums[i]` | $M_{i-1}$ | $M_i$ | $\text{conver}[i]$ | $S_{i-1}$ | $S_i$ |
|---|---|---|---|---|---|---|
| 0 | 2 | none | 2 | $2 + 2 = 4$ | 0 | $0 + 4 = 4$ |
| 1 | 3 | 2 | 3 | $3 + 3 = 6$ | 4 | $4 + 6 = 10$ |
| 2 | 7 | 3 | 7 | $7 + 7 = 14$ | 10 | $10 + 14 = 24$ |
| 3 | 5 | 7 | 7 | $5 + 7 = 12$ | 24 | $24 + 12 = 36$ |
| 4 | 10 | 7 | 10 | $10 + 10 = 20$ | 36 | $36 + 20 = 56$ |

Three steps deserve comment.

- At $i = 2$ the new element `7` exceeds the old maximum `3`, so $M_2 = 7$ and the conversion term jumps to `14`. Had the term been formed with $M_1 = 3$ instead, the result would be `10`, and every later score would be too small by 4. The maximum must absorb the current element *before* the conversion term is formed.
- At $i = 3$ the maximum is unchanged: `5` cannot beat `7`. The conversion term still adds the full `7`, so the score keeps growing even though the maximum has stalled.
- The final row shows the maximum moving again, to `10`. Scores are the only quantity that is required in the answer; $M$ and $\text{conver}$ are internal scaffolding.

The final value $S_4 = 56$ matches the required output, and the accumulated values `[4, 10, 24, 36, 56]` are the answer array itself: each prefix score is written the moment it is produced, and never revised.

## 5. Invariant and Correctness of the incremental update

> **Invariant $I(i)$.** Immediately after the element at index $i$ has been processed, the running maximum equals $\max(\text{nums}[0..i])$ and the running score equals $\sum_{j=0}^{i} \bigl(\text{nums}[j] + \max(\text{nums}[0..j])\bigr)$, which is the score of the prefix `nums[0..i]`.

*Base case.* At $i = 0$ the update sets $M_0 = \max(-\infty, \text{nums}[0]) = \text{nums}[0]$, and the single-element prefix's maximum is indeed $\text{nums}[0]$. The score becomes $0 + \text{nums}[0] + M_0 = 2\,\text{nums}[0]$, which is the sum of the one-term conversion array `[nums[0] + nums[0]]`. So $I(0)$ holds.

*Inductive step.* Assume $I(i-1)$, so the running score equals the score of `nums[0..i-1]`. The first update is $M_i = \max(M_{i-1}, \text{nums}[i])$, which by the hypothesis is $\max\bigl(\max(\text{nums}[0..i-1]), \text{nums}[i]\bigr) = \max(\text{nums}[0..i])$. The second update adds $\text{nums}[i] + M_i$, which is exactly $\text{conver}[i]$ for the prefix of length $i+1$. Adding one immutable term to the previous prefix's score yields the score of the longer prefix, because Section 3 established that the earlier terms do not change. Hence $I(i)$.

*Termination.* After the last index the invariant states that the running score equals the score of the full array `nums[0..n-1]`, and every intermediate value was written to the output when its own index was processed.

The crucial step in that argument is the immutability claim, and it is what separates this problem from a trap: an author who believes the conversion array can be precomputed once for the whole array and then reused verbatim would be right, and an author who believes the conversion of the prefix must be recomputed because "the maximum could change later" would be wrong for the *earlier* terms but right for the newest one. Both intuitions agree on this instance, which is why the append-only table in Section 2 repays a second look.

A fully independent cross-check is available and worth doing once by hand: the score is also

$$
S_i = \underbrace{\sum_{j=0}^{i} \text{nums}[j]}_{P_i} + \underbrace{\sum_{j=0}^{i} M_j}_{Q_i},
$$

the prefix sum of the array plus the prefix sum of the running maximum sequence. Computing both sums directly:

| $i$ | $P_i$ | $Q_i$ | $P_i + Q_i$ | Score from the sweep | Agree |
|---|---|---|---|---|---|
| 0 | 2 | 2 | 4 | 4 | yes |
| 1 | 5 | 5 | 10 | 10 | yes |
| 2 | 12 | 12 | 24 | 24 | yes |
| 3 | 17 | 19 | 36 | 36 | yes |
| 4 | 27 | 29 | 56 | 56 | yes |

The two derivations agree at every index, which confirms that the incremental update loses no contribution and double-counts none.

## 6. Traps this instance exposes

| Situation | Tempting shortcut | Why it fails | Correct treatment |
|---|---|---|---|
| A new element larger than the previous maximum, as at $i = 2$ | Form the conversion term with the maximum carried in from the previous step | `7` is compared against `3`, giving the term `10` instead of `14`, and every later score is short by 4 | Update the running maximum first, then add it |
| An element smaller than the maximum, as at $i = 3$ | Assume an element below the maximum contributes only itself | The conversion term is `5 + 7 = 12`, not `5 + 5 = 10`; the score still grows by the full maximum | Every element is paired with the prefix maximum, itself included |
| A repeated maximum | Skip the score update when the maximum does not move | The maximum standing still does not make the conversion term zero; `conver[i]` is still `nums[i] + M` | Add the conversion term at every index, unconditionally |
| Recomputing each prefix from its definition | Sum the conversion array for every $i$ separately | That is $O(n^{2})$ work; with $n$ up to $10^{5}$ it is on the order of $10^{10}$ additions | Carry one score scalar forward |
| Large values and long arrays | Use a 32-bit accumulator | With $1 \le \text{nums}[i] \le 10^{9}$ and $n \le 10^{5}$, a score can reach $2 \cdot 10^{14}$, far beyond the 32-bit signed maximum near $2.1 \cdot 10^{9}$ | Use a 64-bit accumulator |
| The unseen "empty prefix" | Emit a score of 0 for the empty prefix | The output has length $n$, one entry per nonempty prefix | Start the score at 0 internally and write the first answer only after index 0 is processed |

The fourth row is the one that decides whether the submission is accepted. The interpretation is easy and the recurrence is short, so the only real risk in this problem is an implementation whose asymptotics are a class too slow, and the difference between the two classes is exactly the sentence "old conversion terms never change".

## 7. Time and auxiliary space complexity

**Time.** The sweep performs a constant number of operations per index: one comparison to refresh the running maximum, one addition for the conversion term, and one addition for the score. With $n$ indices the running time is $O(n)$. Recomputing each prefix independently would instead be $\sum_{i=0}^{n-1} (i+1) = \frac{n(n+1)}{2}$, which is $\Theta(n^{2})$.

**Auxiliary space.** Only two scalars are carried between iterations, the running maximum and the running score, so the working memory beyond the output is $O(1)$. The output array of $n$ scores is required by the contract and is not auxiliary. The alternative in Section 5 that stores the full running-maximum sequence and both prefix-sum arrays would use $O(n)$ extra space for the same answers, which is why the scalar formulation is preferred.
