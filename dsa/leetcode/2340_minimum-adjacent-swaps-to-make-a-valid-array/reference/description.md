### 1. Description

You are given a **0-indexed** integer array `nums`.

**Swaps** of **adjacent** elements are able to be performed on `nums`.

A **valid** array meets the following conditions:

- The largest element (any of the largest elements if there are multiple) is at the rightmost position in the array.

- The smallest element (any of the smallest elements if there are multiple) is at the leftmost position in the array.

Return *the **minimum** swaps required to make *`nums`* a valid array*.

### 2. Function Contract

**Inputs**

- `nums`: A list of $n$ positive integers ($1 \le n \le 10^5$).

**Return value**

Return an integer representing the minimum number of adjacent swaps required to move a smallest element to the first index and a largest element to the last index.

### 3. Examples

#### Example 1

- **Input:** `nums = [3,4,5,5,3,1]`
- **Output:** `6`
- **Explanation:** Perform the following swaps:
- Swap 1: Swap the 3^rd and 4^th elements, nums is then [3,4,5,<u>**3**</u>,<u>**5**</u>,1].
- Swap 2: Swap the 4^th and 5^th elements, nums is then [3,4,5,3,<u>**1**</u>,<u>**5**</u>].
- Swap 3: Swap the 3^rd and 4^th elements, nums is then [3,4,5,<u>**1**</u>,<u>**3**</u>,5].
- Swap 4: Swap the 2^nd and 3^rd elements, nums is then [3,4,<u>**1**</u>,<u>**5**</u>,3,5].
- Swap 5: Swap the 1^st and 2^nd elements, nums is then [3,<u>**1**</u>,<u>**4**</u>,5,3,5].
- Swap 6: Swap the 0^th and 1^st elements, nums is then [<u>**1**</u>,<u>**3**</u>,4,5,3,5].
It can be shown that 6 swaps is the minimum swaps required to make a valid array.
#### Example 2

- **Input:** `nums = [9]`
- **Output:** `0`
- **Explanation:** The array is already valid, so we return 0.

### 4. Constraints

- $1 \le \text{nums.length} \le 10^{5}$

- $1 \le \text{nums}[i] \le 10^{5}$