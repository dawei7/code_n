### 1. Description

Given a **1-indexed** array of integers `numbers` that is already ***sorted in non-decreasing order***, find two numbers such that they add up to a specific `target` number. Let these two numbers be $numbers[\text{index}_{1}]$ and $numbers[\text{index}_{2}]$ where $1 \le \text{index}_{1} < \text{index}_{2} \le \text{numbers.length}$.

Return* the indices of the two numbers *$\text{index}_{1}$* and *$\text{index}_{2}$*, **each incremented by one,** as an integer array *`[index_1, index_2]`* of length 2.*

The tests are generated such that there is **exactly one solution**. You **may not** use the same element twice.

Your solution must use only constant extra space.

### 2. Function Contract

**Inputs**

- `numbers`: An integer array sorted in non-decreasing order.
- `target`: The required sum of the two selected elements.

**Return value**

Return the unique pair of 1-based indices `[index1, index2]`, with `index1 < index2`.

### 3. Examples

#### Example 1

- **Input:** $numbers = [<u>2</u>,<u>7</u>,11,15], target = 9$
- **Output:** `[1,2]`
- **Explanation:** The sum of 2 and 7 is 9. Therefore, index_1 = 1, index_2 = 2. We return [1, 2].

#### Example 2

- **Input:** $numbers = [<u>2</u>,3,<u>4</u>], target = 6$
- **Output:** `[1,3]`
- **Explanation:** The sum of 2 and 4 is 6. Therefore index_1 = 1, index_2 = 3. We return [1, 3].

#### Example 3

- **Input:** $numbers = [<u>-1</u>,<u>0</u>], target = -1$
- **Output:** `[1,2]`
- **Explanation:** The sum of -1 and 0 is -1. Therefore index_1 = 1, index_2 = 2. We return [1, 2].

### 4. Constraints

- $2 \le \text{numbers.length} \le 3 * 10^{4}$

- $-1000 \le \text{numbers}[i] \le 1000$

- `numbers` is sorted in **non-decreasing order**.

- $-1000 \le target \le 1000$

- The tests are generated such that there is **exactly one solution**.
