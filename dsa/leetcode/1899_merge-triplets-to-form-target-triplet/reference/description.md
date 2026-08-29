### 1. Description

A **triplet** is an array of three integers. You are given a 2D integer array `triplets`, where $\text{triplets}[i] = [a_{i}, b_{i}, c_{i}]$ describes the $i^{\text{th}}$ **triplet**. You are also given an integer array $target = [x, y, z]$ that describes the **triplet** you want to obtain.

To obtain `target`, you may apply the following operation on `triplets` **any number** of times (possibly **zero**):

- Choose two indices (**0-indexed**) `i` and `j` ($i \neq j$) and **update** $\text{triplets}[j]$ to become $[max(a_{i}, a_{j}), max(b_{i}, b_{j}), max(c_{i}, c_{j})]$.

		- For example, if $\text{triplets}[i] = [2, 5, 3]$ and $\text{triplets}[j] = [1, 7, 5]$, $\text{triplets}[j]$ will be updated to `[max(2, 1), max(5, 7), max(3, 5)] = [2, 7, 5]`.

Return `true` *if it is possible to obtain the *`target`* **triplet** *`[x, y, z]`* as an** element** of *`triplets`*, or *`false`* otherwise*.

### 2. Function Contract

**Inputs**

- `triplets`: Input parameter (`List[List[int]]`).
- `target`: Input parameter (`List[int]`).

**Return value**

- Returns `bool`.

### 3. Examples

#### Example 1

- **Input:** $triplets = [[2,5,3],[1,8,4],[1,7,5]], target = [2,7,5]$
- **Output:** `true`
- **Explanation:** Perform the following operations:
- Choose the first and last triplets [<u>[2,5,3]</u>,[1,8,4],<u>[1,7,5]</u>]. Update the last triplet to be [max(2,1), max(5,7), max(3,5)] = [2,7,5]. triplets = [[2,5,3],[1,8,4],<u>[2,7,5]</u>]
The target triplet [2,7,5] is now an element of triplets.

#### Example 2

- **Input:** $triplets = [[3,4,5],[4,5,6]], target = [3,2,5]$
- **Output:** `false`
- **Explanation:** It is impossible to have [3,2,5] as an element because there is no 2 in any of the triplets.

#### Example 3

- **Input:** $triplets = [[2,5,3],[2,3,4],[1,2,5],[5,2,3]], target = [5,5,5]$
- **Output:** `true`
- **Explanation:** Perform the following operations:
- Choose the first and third triplets [<u>[2,5,3]</u>,[2,3,4],<u>[1,2,5]</u>,[5,2,3]]. Update the third triplet to be [max(2,1), max(5,2), max(3,5)] = [2,5,5]. triplets = [[2,5,3],[2,3,4],<u>[2,5,5]</u>,[5,2,3]].
- Choose the third and fourth triplets [[2,5,3],[2,3,4],<u>[2,5,5]</u>,<u>[5,2,3]</u>]. Update the fourth triplet to be [max(2,5), max(5,2), max(5,3)] = [5,5,5]. triplets = [[2,5,3],[2,3,4],[2,5,5],<u>[5,5,5]</u>].
The target triplet [5,5,5] is now an element of triplets.

### 4. Constraints

- $1 \le \text{triplets.length} \le 10^{5}$

- $\text{triplets}[i].length = \text{target.length} = 3$

- $1 \le a_{i}, b_{i}, c_{i}, x, y, z \le 1000$
