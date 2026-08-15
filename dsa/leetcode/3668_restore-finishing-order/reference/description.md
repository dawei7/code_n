### 1. Description

You are given an integer array `order` of length `n` and an integer array `friends`.

- `order` contains every integer from 1 to `n` **exactly once**, representing the IDs of the participants of a race in their **finishing** order.

- `friends` contains the IDs of your friends in the race **sorted** in strictly increasing order. Each ID in friends is guaranteed to appear in the `order` array.

Return an array containing your friends' IDs in their **finishing** order.

### 2. Function Contract

**Inputs**

- `order`: Input parameter (`List[int]`).
- `friends`: Input parameter (`List[int]`).

**Return value**

- Returns `List[int]`.

### 3. Examples

#### Example 1

- **Input:** order = [3,1,2,5,4], friends = [1,3,4]

- **Output:** [3,1,4]

- **Explanation:** The finishing order is `[<u>**3**</u>, <u>**1**</u>, 2, 5, <u>**4**</u>]`. Therefore, the finishing order of your friends is `[3, 1, 4]`.

#### Example 2

- **Input:** order = [1,4,5,3,2], friends = [2,5]

- **Output:** [5,2]

- **Explanation:** The finishing order is `[1, 4, <u>**5**</u>, 3, <u>**2**</u>]`. Therefore, the finishing order of your friends is `[5, 2]`.

### 4. Constraints

- $1 \le n = \text{order.length} \le 100$

- `order` contains every integer from 1 to `n` exactly once

- $1 \le \text{friends.length} \le min(8, n)$

- $1 \le \text{friends}[i] \le n$

- `friends` is strictly increasing
