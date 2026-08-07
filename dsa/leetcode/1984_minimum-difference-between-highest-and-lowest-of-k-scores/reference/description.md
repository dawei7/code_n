## Description

You are given a **0-indexed** integer array `nums`, where $\text{nums}[i]$ represents the score of the $$i^{\text{th}}$$ student. You are also given an integer `k`.

Pick the scores of any `k` students from the array so that the **difference** between the **highest** and the **lowest** of the `k` scores is **minimized**.

Return *the **minimum** possible difference*.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples

#### Example 1

- **Input:** `nums = [90], k = 1`
- **Output:** `0`
- **Explanation:** There is one way to pick score(s) of one student:
- [**<u>90</u>**]. The difference between the highest and lowest score is 90 - 90 = 0.
The minimum possible difference is 0.
#### Example 2

- **Input:** `nums = [9,4,1,7], k = 2`
- **Output:** `2`
- **Explanation:** There are six ways to pick score(s) of two students:
- [**<u>9</u>**,**<u>4</u>**,1,7]. The difference between the highest and lowest score is 9 - 4 = 5.
- [**<u>9</u>**,4,**<u>1</u>**,7]. The difference between the highest and lowest score is 9 - 1 = 8.
- [**<u>9</u>**,4,1,**<u>7</u>**]. The difference between the highest and lowest score is 9 - 7 = 2.
- [9,**<u>4</u>**,**<u>1</u>**,7]. The difference between the highest and lowest score is 4 - 1 = 3.
- [9,**<u>4</u>**,1,**<u>7</u>**]. The difference between the highest and lowest score is 7 - 4 = 3.
- [9,4,**<u>1</u>**,**<u>7</u>**]. The difference between the highest and lowest score is 7 - 1 = 6.
The minimum possible difference is 2.
### Constraints

- $1 \le k \le \text{nums.length} \le 1000$

- $0 \le \text{nums}[i] \le 10^{5}$