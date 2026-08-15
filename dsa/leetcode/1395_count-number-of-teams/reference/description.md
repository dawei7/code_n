### 1. Description

There are `n` soldiers standing in a line. Each soldier is assigned a **unique** `rating` value.

You have to form a team of 3 soldiers amongst them under the following rules:

- Choose 3 soldiers with index (`i`, `j`, `k`) with rating ($\text{rating}[i]$, $\text{rating}[j]$, $\text{rating}[k]$).

- A team is valid if: ($\text{rating}[i] < \text{rating}[j] < \text{rating}[k]$) or ($\text{rating}[i] > \text{rating}[j] > \text{rating}[k]$) where ($0 \le i < j < k < n$).

Return the number of teams you can form given the conditions. (soldiers can be part of multiple teams).

### 2. Function Contract

**Inputs**

- `rating`: Input parameter (`List[int]`).

**Return value**

- Returns `int`.

### 3. Examples

#### Example 1

- **Input:** $rating = [2,5,3,4,1]$
- **Output:** `3`
- **Explanation:** We can form three teams given the conditions. (2,3,4), (5,4,1), (5,3,1).

#### Example 2

- **Input:** $rating = [2,1,3]$
- **Output:** `0`
- **Explanation:** We can't form any team given the conditions.

#### Example 3

- **Input:** $rating = [1,2,3,4]$
- **Output:** `4`

### 4. Constraints

- $n = \text{rating.length}$

- $3 \le n \le 1000$

- $1 \le \text{rating}[i] \le 10^{5}$

- All the integers in `rating` are **unique**.
