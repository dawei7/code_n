# Poor Pigs

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 458 |
| Difficulty | Hard |
| Topics | Math, Dynamic Programming, Combinatorics |
| Official Link | [LeetCode](https://leetcode.com/problems/poor-pigs/) |

## Problem Description
### Goal
Exactly one of `buckets` buckets is poisoned. A pig that drinks poison dies after `minutesToDie`, and the experiment has `minutesToTest` total minutes. You may arrange several simultaneous testing rounds and let each pig drink mixtures from selected buckets in each round.

Return the minimum number of pigs needed to identify the poisoned bucket with certainty. Each pig has one observable state for every completed death interval plus a final surviving state, so combined pig outcomes must distinguish all buckets. Testing schedules may encode buckets through those states; simply assigning one pig per bucket is not required. The answer depends on the number of full rounds available.

### Function Contract
**Inputs**

- `buckets`: the number of buckets, exactly one of which is poisoned
- `minutesToDie`: minutes between consuming poison and the observable outcome
- `minutesToTest`: total minutes available for the experiment

**Return value**

- The minimum number of pigs sufficient to identify the poisoned bucket with certainty

### Examples
**Example 1**

- Input: `buckets = 1000, minutesToDie = 15, minutesToTest = 60`
- Output: `5`

**Example 2**

- Input: `buckets = 4, minutesToDie = 15, minutesToTest = 15`
- Output: `2`

**Example 3**

- Input: `buckets = 4, minutesToDie = 15, minutesToTest = 30`
- Output: `2`

### Required Complexity

- **Time:** $O(\log buckets)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Count distinguishable outcomes for one pig**

There are `rounds = minutesToTest // minutesToDie` complete opportunities to observe a death. A pig can die after any one of those rounds or remain alive through the test, giving `rounds + 1` distinguishable final states.

**Combine pigs as independent state digits**

With `p` pigs, the vector of their final states has `(rounds + 1) ** p` possibilities. Label each bucket with a different base-`rounds + 1` code and let pig `q` drink from a bucket in the round encoded by digit `q`; the observed state vector identifies that code. Thus this capacity is achievable, not merely an upper bound.

**Find the smallest sufficient exponent**

Start with capacity one and multiply by the per-pig state count until capacity reaches `buckets`. The number of multiplications is the smallest `p` satisfying `states ** p >= buckets`. Using integer multiplication avoids floating-point rounding near exact powers.

**Why fewer pigs cannot work**

Any experiment ultimately observes only one of the possible final state vectors. With fewer pigs than the computed exponent, there are fewer vectors than buckets, so two poisoned-bucket scenarios must produce the same observation and cannot always be distinguished.

#### Complexity detail

Capacity grows by a factor of at least two per pig, so the loop runs $O(\log buckets)$ times. It stores only the state count, capacity, and pig count, using $O(1)$ space.

#### Alternatives and edge cases

- **Logarithm and ceiling:** directly computes the exponent but can round an exact power incorrectly in floating-point arithmetic.
- **Dynamic-programming capacity table:** generalizes to related testing variants but stores states unnecessary for this formula.
- **Explicitly generate outcome vectors:** demonstrates the coding construction but creates `Theta(buckets)` signatures instead of counting them.
- **One bucket:** needs no experiment and therefore zero pigs.
- **Only one testing round:** each pig has two states, so the answer is the smallest `p` with `2 ** p >= buckets`.
- **Unused partial interval:** only complete `minutesToDie` intervals produce an observable additional death state.
- **Exact capacity:** when `states ** p = buckets`, exactly `p` pigs suffice; do not add one more.

</details>
