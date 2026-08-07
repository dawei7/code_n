### 1. Description

Alice and Bob have a different total number of candies. You are given two integer arrays `aliceSizes` and `bobSizes` where $\text{aliceSizes}[i]$ is the number of candies of the $$i^{\text{th}}$$ box of candy that Alice has and $\text{bobSizes}[j]$ is the number of candies of the $$j^{\text{th}}$$ box of candy that Bob has.

Since they are friends, they would like to exchange one candy box each so that after the exchange, they both have the same total amount of candy. The total amount of candy a person has is the sum of the number of candies in each box they have.

Return a*n integer array *`answer`* where *$\text{answer}[0]$* is the number of candies in the box that Alice must exchange, and *$\text{answer}[1]$* is the number of candies in the box that Bob must exchange*. If there are multiple answers, you may **return any** one of them. It is guaranteed that at least one answer exists.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

- **Input:** $aliceSizes = [1,1], bobSizes = [2,2]$
- **Output:** `[1,2]`
#### Example 2

- **Input:** $aliceSizes = [1,2], bobSizes = [2,3]$
- **Output:** `[1,2]`
#### Example 3

- **Input:** $aliceSizes = [2], bobSizes = [1,3]$
- **Output:** `[2,3]`

### 4. Constraints

- $1 \le \text{aliceSizes.length}, \text{bobSizes.length} \le 10^{4}$

- $1 \le \text{aliceSizes}[i], \text{bobSizes}[j] \le 10^{5}$

- Alice and Bob have a different total number of candies.

- There will be at least one valid answer for the given input.