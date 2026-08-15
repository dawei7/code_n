### 1. Description

You are given a binary array `nums`.

You can do the following operation on the array **any** number of times (possibly zero):

- Choose **any** 3 **consecutive** elements from the array and **flip** **all** of them.

**Flipping** an element means changing its value from 0 to 1, and from 1 to 0.

Return the **minimum** number of operations required to make all elements in `nums` equal to 1. If it is impossible, return -1.

### 2. Function Contract

**Inputs**

- `nums`: Input parameter (`List[int]`).

**Return value**

- Returns `int`.

### 3. Examples

#### Example 1

- **Input:** nums = [0,1,1,1,0,0]

- **Output:** 3

- **Explanation:** We can do the following operations:

- Choose the elements at indices 0, 1 and 2. The resulting array is `nums = [<u>**1**</u>,<u>**0**</u>,<u>**0**</u>,1,0,0]`.

- Choose the elements at indices 1, 2 and 3. The resulting array is `nums = [1,<u>**1**</u>,<u>**1**</u>,**<u>0</u>**,0,0]`.

- Choose the elements at indices 3, 4 and 5. The resulting array is `nums = [1,1,1,**<u>1</u>**,<u>**1**</u>,<u>**1**</u>]`.

#### Example 2

- **Input:** nums = [0,1,1,1]

- **Output:** -1

- **Explanation:** It is impossible to make all elements equal to 1.

### 4. Constraints

- $3 \le \text{nums.length} \le 10^{5}$

- $0 \le \text{nums}[i] \le 1$
