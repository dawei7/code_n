### 1. Description

You are given a **0-indexed** array `arr` consisting of `n` positive integers, and a positive integer `k`.

The array `arr` is called **K-increasing** if $arr[i-k] \le \text{arr}[i]$ holds for every index `i`, where $k \le i \le n-1$.

- For example, `arr = [4, 1, 5, 2, 6, 2]` is K-increasing for $k = 2$ because:

		<li>$\text{arr}[0] \le \text{arr}[2] (4 \le 5)$

- $\text{arr}[1] \le \text{arr}[3] (1 \le 2)$

- $\text{arr}[2] \le \text{arr}[4] (5 \le 6)$

- $\text{arr}[3] \le \text{arr}[5] (2 \le 2)$

	</li>
- However, the same `arr` is not K-increasing for $k = 1$ (because $\text{arr}[0] > \text{arr}[1]$) or $k = 3$ (because $\text{arr}[0] > \text{arr}[3]$).

In one **operation**, you can choose an index `i` and **change** $\text{arr}[i]$ into **any** positive integer.

Return *the **minimum number of operations** required to make the array K-increasing for the given *`k`.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

- **Input:** `arr = [5,4,3,2,1], k = 1`
- **Output:** `4`
- **Explanation:**
**For k = 1, the resultant array has to be non-decreasing.
Some of the K-increasing arrays that can be formed are [5,<u>**6**</u>,<u>**7**</u>,<u>**8**</u>,<u>**9**</u>], [<u>**1**</u>,<u>**1**</u>,<u>**1**</u>,<u>**1**</u>,1], [<u>**2**</u>,<u>**2**</u>,3,<u>**4**</u>,<u>**4**</u>]. All of them require 4 operations.
It is suboptimal to change the array to, for example, [<u>**6**</u>,<u>**7**</u>,<u>**8**</u>,<u>**9**</u>,<u>**10**</u>] because it would take 5 operations.
It can be shown that we cannot make the array K-increasing in less than 4 operations.
#### Example 2

- **Input:** `arr = [4,1,5,2,6,2], k = 2`
- **Output:** `0`
- **Explanation:**
This is the same example as the one in the problem description.
Here, for every index i where 2 <= i <= 5, arr[i-2] <=** **arr[i].
Since the given array is already K-increasing, we do not need to perform any operations.
#### Example 3

- **Input:** `arr = [4,1,5,2,6,2], k = 3`
- **Output:** `2`
- **Explanation:**
Indices 3 and 5 are the only ones not satisfying arr[i-3] <= arr[i] for 3 <= i <= 5.
One of the ways we can make the array K-increasing is by changing arr[3] to 4 and arr[5] to 5.
The array will now be [4,1,5,<u>**4**</u>,6,<u>**5**</u>].
Note that there can be other ways to make the array K-increasing, but none of them require less than 2 operations.

### 4. Constraints

- $1 \le \text{arr.length} \le 10^{5}$

- $1 \le \text{arr}[i], k \le \text{arr.length}$