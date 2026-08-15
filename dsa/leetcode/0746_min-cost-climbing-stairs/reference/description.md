### 1. Description

You are given an integer array `cost` where $\text{cost}[i]$ is the cost of $$i^{\text{th}}$$ step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index `0`, or the step with index `1`.

Return *the minimum cost to reach the top of the floor*.

### 2. Function Contract

**Inputs**

- `cost`: Input parameter (`List[int]`).

**Return value**

- Returns `int`.

### 3. Examples

#### Example 1

- **Input:** $cost = [10,<u>15</u>,20]$
- **Output:** `15`
- **Explanation:** You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.

#### Example 2

- **Input:** $cost = [<u>1</u>,100,<u>1</u>,1,<u>1</u>,100,<u>1</u>,<u>1</u>,100,<u>1</u>]$
- **Output:** `6`
- **Explanation:** You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6.

### 4. Constraints

- $2 \le \text{cost.length} \le 1000$

- $0 \le \text{cost}[i] \le 999$
