### 1. Description

You have some apples and a basket that can carry up to `5000` units of weight.

Given an integer array `weight` where $\text{weight}[i]$ is the weight of the $$i^{\text{th}}$$ apple, return *the maximum number of apples you can put in the basket*.

### 2. Function Contract

**Input**

- `weight`: An integer array containing one positive weight for each apple.

Each array occurrence represents a distinct apple, including repeated values. Any subset may be selected, and a combined weight of exactly `5000` is allowed.

Let $n$ be the number of elements in `weight`.

**Return value**

Return the greatest possible number of selected apples whose combined weight is at most `5000`.

### 3. Examples

#### Example 1

- **Input:** $weight = [100,200,150,1000]$
- **Output:** `4`
- **Explanation:** All 4 apples can be carried by the basket since their sum of weights is 1450.
#### Example 2

- **Input:** $weight = [900,950,800,1000,700,800]$
- **Output:** `5`
- **Explanation:** The sum of weights of the 6 apples exceeds 5000 so we choose any 5 of them.

### 4. Constraints

- $1 \le \text{weight.length} \le 10^{3}$

- $1 \le \text{weight}[i] \le 10^{3}$