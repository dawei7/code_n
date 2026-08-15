### 1. Description

You are given a binary array `nums`.

You can do the following operation on the array **any** number of times (possibly zero):

- Choose **any** index `i` from the array and **flip** **all** the elements from index `i` to the end of the array.

**Flipping** an element means changing its value from 0 to 1, and from 1 to 0.

Return the **minimum** number of operations required to make all elements in `nums` equal to 1.

### 2. Function Contract

**Inputs**

- `nums`: Input parameter (`List[int]`).

**Return value**

- Returns `int`.

### 3. Examples

#### Example 1

- **Input:** nums = [0,1,1,0,1]

- **Output:** 4

- **Explanation:** We can do the following operations:

- Choose the index $i = 1$. The resulting array will be `nums = [0,<u>**0**</u>,<u>**0**</u>,<u>**1**</u>,<u>**0**</u>]`.

- Choose the index $i = 0$. The resulting array will be `nums = [<u>**1**</u>,<u>**1**</u>,<u>**1**</u>,<u>**0**</u>,<u>**1**</u>]`.

- Choose the index $i = 4$. The resulting array will be `nums = [1,1,1,0,<u>**0**</u>]`.

- Choose the index $i = 3$. The resulting array will be `nums = [1,1,1,<u>**1**</u>,<u>**1**</u>]`.

#### Example 2

- **Input:** nums = [1,0,0,0]

- **Output:** 1

- **Explanation:** We can do the following operation:

- Choose the index $i = 1$. The resulting array will be `nums = [1,<u>**1**</u>,<u>**1**</u>,<u>**1**</u>]`.

### 4. Constraints

- $1 \le \text{nums.length} \le 10^{5}$

- $0 \le \text{nums}[i] \le 1$
