## Description

Given three integer arrays `arr1`, `arr2` and `arr3` **sorted** in **strictly increasing** order, return a sorted array of **only** the integers that appeared in **all** three arrays.
### Function Contract

**Inputs**

- `arr1`: A strictly increasing integer array.
- `arr2`: A strictly increasing integer array.
- `arr3`: A strictly increasing integer array.

Let $n_1$, $n_2$, and $n_3$ be the respective array lengths.

**Return value**

Return every value present in `arr1`, `arr2`, and `arr3`, in increasing order. If no integer belongs to all three arrays, return `[]`.

### Examples
#### Example 1

- **Input:** $arr1 = [1,2,3,4,5], arr2 = [1,2,5,7,9], arr3 = [1,3,4,5,8]$
- **Output:** `[1,5]`
- **Explanation:** Only 1 and 5 appeared in the three arrays.
#### Example 2

- **Input:** $arr1 = [197,418,523,876,1356], arr2 = [501,880,1593,1710,1870], arr3 = [521,682,1337,1395,1764]$
- **Output:** `[]`
### Constraints

- $1 \le \text{arr1.length}, \text{arr2.length}, \text{arr3.length} \le 1000$

- $1 \le \text{arr1}[i], \text{arr2}[i], \text{arr3}[i] \le 2000$