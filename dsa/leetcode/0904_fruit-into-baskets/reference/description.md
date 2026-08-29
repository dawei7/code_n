### 1. Description

You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array `fruits` where $\text{fruits}[i]$ is the **type** of fruit the $i^{\text{th}}$ tree produces.

You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

- You only have **two** baskets, and each basket can only hold a **single type** of fruit. There is no limit on the amount of fruit each basket can hold.

- Starting from any tree of your choice, you must pick **exactly one fruit** from **every** tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.

- Once you reach a tree with fruit that cannot fit in your baskets, you must stop.

Given the integer array `fruits`, return *the **maximum** number of fruits you can pick*.

### 2. Function Contract

**Inputs**

- `fruits`: Input parameter (`List[int]`).

**Return value**

- Returns `int`.

### 3. Examples

#### Example 1

- **Input:** $fruits = [<u>1,2,1</u>]$
- **Output:** `3`
- **Explanation:** We can pick from all 3 trees.

#### Example 2

- **Input:** $fruits = [0,<u>1,2,2</u>]$
- **Output:** `3`
- **Explanation:** We can pick from trees [1,2,2].
If we had started at the first tree, we would only pick from trees [0,1].

#### Example 3

- **Input:** $fruits = [1,<u>2,3,2,2</u>]$
- **Output:** `4`
- **Explanation:** We can pick from trees [2,3,2,2].
If we had started at the first tree, we would only pick from trees [1,2].

### 4. Constraints

- $1 \le \text{fruits.length} \le 10^{5}$

- $0 \le \text{fruits}[i] < \text{fruits.length}$
