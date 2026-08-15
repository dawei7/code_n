### 1. Description

You are given an array of **distinct** integers `arr` and an array of integer arrays `pieces`, where the integers in `pieces` are **distinct**. Your goal is to form `arr` by concatenating the arrays in `pieces` **in any order**. However, you are **not** allowed to reorder the integers in each array $\text{pieces}[i]$.

Return `true` *if it is possible **to form the array *`arr`* from *`pieces`. Otherwise, return `false`.

### 2. Function Contract

**Inputs**

- `arr`: Input parameter (`List[int]`).
- `pieces`: Input parameter (`List[List[int]]`).

**Return value**

- Returns `bool`.

### 3. Examples

#### Example 1

- **Input:** `arr = [15,88], pieces = [[88],[15]]`
- **Output:** `true`
- **Explanation:** Concatenate [15] then [88]

#### Example 2

- **Input:** `arr = [49,18,16], pieces = [[16,18,49]]`
- **Output:** `false`
- **Explanation:** Even though the numbers match, we cannot reorder pieces[0].

#### Example 3

- **Input:** `arr = [91,4,64,78], pieces = [[78],[4,64],[91]]`
- **Output:** `true`
- **Explanation:** Concatenate [91] then [4,64] then [78]

### 4. Constraints

- $1 \le \text{pieces.length} \le \text{arr.length} \le 100$

- $sum(\text{pieces}[i].length) = \text{arr.length}$

- $1 \le \text{pieces}[i].length \le \text{arr.length}$

- $1 \le \text{arr}[i], \text{pieces}[i][j] \le 100$

- The integers in `arr` are **distinct**.

- The integers in `pieces` are **distinct** (i.e., If we flatten pieces in a 1D array, all the integers in this array are distinct).
