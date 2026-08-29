### 1. Description

Given an array of integers `temperatures` represents the daily temperatures, return *an array* `answer` *such that* $\text{answer}[i]$ *is the number of days you have to wait after the* $i^{\text{th}}$ *day to get a warmer temperature*. If there is no future day for which this is possible, keep $\text{answer}[i] = 0$ instead.

### 2. Function Contract

**Inputs**

- `temperatures`: Input parameter (`List[int]`).

**Return value**

- Returns `List[int]`.

### 3. Examples

#### Example 1

- **Input:** $temperatures = [73,74,75,71,69,72,76,73]$
- **Output:** `[1,1,4,2,1,1,0,0]`

#### Example 2

- **Input:** $temperatures = [30,40,50,60]$
- **Output:** `[1,1,1,0]`

#### Example 3

- **Input:** $temperatures = [30,60,90]$
- **Output:** `[1,1,0]`

### 4. Constraints

- $1 \le \text{temperatures.length} \le 10^{5}$

- $30 \le \text{temperatures}[i] \le 100$
