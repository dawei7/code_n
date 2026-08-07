## Description

You are given an integer array `nums` that is **sorted in non-decreasing order**.

Determine if it is possible to split `nums` into **one or more subsequences** such that **both** of the following conditions are true:

- Each subsequence is a **consecutive increasing sequence** (i.e. each integer is **exactly one** more than the previous integer).

- All subsequences have a length of `3`** or more**.

Return `true`* if you can split *`nums`* according to the above conditions, or *`false`* otherwise*.

A **subsequence** of an array is a new array that is formed from the original array by deleting some (can be none) of the elements without disturbing the relative positions of the remaining elements. (i.e., `[1,3,5]` is a subsequence of `[<u>1</u>,2,<u>3</u>,4,<u>5</u>]` while `[1,3,2]` is not).
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples

#### Example 1

- **Input:** `nums = [1,2,3,3,4,5]`
- **Output:** `true`
- **Explanation:** nums can be split into the following subsequences:
[**<u>1</u>**,**<u>2</u>**,**<u>3</u>**,3,4,5] --> 1, 2, 3
[1,2,3,**<u>3</u>**,**<u>4</u>**,**<u>5</u>**] --> 3, 4, 5
#### Example 2

- **Input:** `nums = [1,2,3,3,4,4,5,5]`
- **Output:** `true`
- **Explanation:** nums can be split into the following subsequences:
[**<u>1</u>**,**<u>2</u>**,**<u>3</u>**,3,**<u>4</u>**,4,**<u>5</u>**,5] --> 1, 2, 3, 4, 5
[1,2,3,**<u>3</u>**,4,**<u>4</u>**,5,**<u>5</u>**] --> 3, 4, 5
#### Example 3

- **Input:** `nums = [1,2,3,4,4,5]`
- **Output:** `false`
- **Explanation:** It is impossible to split nums into consecutive increasing subsequences of length 3 or more.
### Constraints

- $1 \le \text{nums.length} \le 10^{4}$

- $-1000 \le \text{nums}[i] \le 1000$

- `nums` is sorted in **non-decreasing** order.