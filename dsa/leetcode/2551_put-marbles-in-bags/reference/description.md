### 1. Description

You have `k` bags. You are given a **0-indexed** integer array `weights` where $\text{weights}[i]$ is the weight of the $$i^{\text{th}}$$ marble. You are also given the integer `k.`

Divide the marbles into the `k` bags according to the following rules:

- No bag is empty.

- If the $$i^{\text{th}}$$ marble and $$j^{\text{th}}$$ marble are in a bag, then all marbles with an index between the $$i^{\text{th}}$$ and $$j^{\text{th}}$$ indices should also be in that same bag.

- If a bag consists of all the marbles with an index from `i` to `j` inclusively, then the cost of the bag is $\text{weights}[i] + \text{weights}[j]$.

The **score** after distributing the marbles is the sum of the costs of all the `k` bags.

Return *the **difference** between the **maximum** and **minimum** scores among marble distributions*.

### 2. Function Contract

**Inputs**

- `weights`: Input parameter (`List[int]`).
- `k`: Input parameter (`int`).

**Return value**

- Returns `int`.

### 3. Examples

#### Example 1

- **Input:** $weights = [1,3,5,1], k = 2$
- **Output:** `4`
- **Explanation:** The distribution [1],[3,5,1] results in the minimal score of (1+1) + (3+1) = 6.
The distribution [1,3],[5,1], results in the maximal score of (1+3) + (5+1) = 10.
Thus, we return their difference 10 - 6 = 4.

#### Example 2

- **Input:** $weights = [1, 3], k = 2$
- **Output:** `0`
- **Explanation:** The only distribution possible is [1],[3].
Since both the maximal and minimal score are the same, we return 0.

### 4. Constraints

- $1 \le k \le \text{weights.length} \le 10^{5}$

- $1 \le \text{weights}[i] \le 10^{9}$
