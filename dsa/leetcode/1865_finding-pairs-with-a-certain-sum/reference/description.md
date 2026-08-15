### 1. Description

You are given two integer arrays `nums1` and `nums2`. You are tasked to implement a data structure that supports queries of two types:

- **Add** a positive integer to an element of a given index in the array `nums2`.

- **Count** the number of pairs `(i, j)` such that $\text{nums1}[i] + \text{nums2}[j]$ equals a given value ($0 \le i < \text{nums1.length}$ and $0 \le j < \text{nums2.length}$).

Implement the `FindSumPairs` class:

- `FindSumPairs(int[] nums1, int[] nums2)` Initializes the `FindSumPairs` object with two integer arrays `nums1` and `nums2`.

- `void add(int index, int val)` Adds `val` to $\text{nums2}[index]$, i.e., apply $\text{nums2}[index] += val$.

- `int count(int tot)` Returns the number of pairs `(i, j)` such that $\text{nums1}[i] + \text{nums2}[j] = tot$.

### 2. Function Contract

**Methods**

- `FindSumPairs(nums1: List[int], nums2: List[int])`: Initializes the data structure.
- `add(index: int, val: int)`: Executes operation.
- `count(tot: int) -> `int``: Executes operation.

### 3. Examples

#### Example 1

```
**Input**
["FindSumPairs", "count", "add", "count", "count", "add", "add", "count"]
[[[1, 1, 2, 2, 2, 3], [1, 4, 5, 2, 5, 4]], [7], [3, 2], [8], [4], [0, 1], [1, 1], [7]]
**Output**
[null, 8, null, 2, 1, null, null, 11]

**Explanation**
FindSumPairs findSumPairs = new FindSumPairs([1, 1, 2, 2, 2, 3], [1, 4, 5, 2, 5, 4]);
findSumPairs.count(7);  // return 8; pairs (2,2), (3,2), (4,2), (2,4), (3,4), (4,4) make 2 + 5 and pairs (5,1), (5,5) make 3 + 4
findSumPairs.add(3, 2); // now nums2 = [1,4,5,**<u>4</u>**,5,4]
findSumPairs.count(8);  // return 2; pairs (5,2), (5,4) make 3 + 5
findSumPairs.count(4);  // return 1; pair (5,0) makes 3 + 1
findSumPairs.add(0, 1); // now nums2 = [**<u>2</u>**,4,5,4,5,4]
findSumPairs.add(1, 1); // now nums2 = [2,**<u>5</u>**,5,4,5,4]
findSumPairs.count(7);  // return 11; pairs (2,1), (2,2), (2,4), (3,1), (3,2), (3,4), (4,1), (4,2), (4,4) make 2 + 5 and pairs (5,3), (5,5) make 3 + 4
```

### 4. Constraints

- $1 \le \text{nums1.length} \le 1000$

- $1 \le \text{nums2.length} \le 10^{5}$

- $1 \le \text{nums1}[i] \le 10^{9}$

- $1 \le \text{nums2}[i] \le 10^{5}$

- $0 \le index < \text{nums2.length}$

- $1 \le val \le 10^{5}$

- $1 \le tot \le 10^{9}$

- At most `1000` calls are made to `add` and `count` **each**.
