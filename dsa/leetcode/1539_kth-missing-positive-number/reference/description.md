## Description

Given an array `arr` of positive integers sorted in a **strictly increasing order**, and an integer `k`.

Return *the* $$k^{\text{th}}$$ ***positive** integer that is **missing** from this array.*
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples
#### Example 1

- **Input:** `arr = [2,3,4,7,11], k = 5`
- **Output:** `9`
- **Explanation:** The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5^th missing positive integer is 9.
#### Example 2

- **Input:** `arr = [1,2,3,4], k = 2`
- **Output:** `6`
- **Explanation:** The missing positive integers are [5,6,7,...]. The 2^nd missing positive integer is 6.
### Constraints

- $1 \le \text{arr.length} \le 1000$

- $1 \le \text{arr}[i] \le 1000$

- $1 \le k \le 1000$

- $\text{arr}[i] < \text{arr}[j]$ for $1 \le i < j \le \text{arr.length}$

**Follow up:**

Could you solve this problem in less than $\mathcal{O}(n)$ complexity?