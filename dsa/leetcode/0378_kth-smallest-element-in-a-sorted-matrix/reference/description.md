## Description

Given an `n x n` `matrix` where each of the rows and columns is sorted in ascending order, return *the* $$k^{\text{th}}$$ *smallest element in the matrix*.

Note that it is the $$k^{\text{th}}$$ smallest element **in the sorted order**, not the $$k^{\text{th}}$$ **distinct** element.

You must find a solution with a memory complexity better than $O(n^{2})$.
### Function Contract

**Inputs**

- `matrix`: A nonempty square integer matrix whose rows and columns are each sorted in non-decreasing order.
- `k`: A valid one-based rank among all matrix cells.

**Return value**

Return the value at rank `k` in the sorted multiset of all entries.

### Examples

#### Example 1

- **Input:** $matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8$
- **Output:** `13`
- **Explanation:** The elements in the matrix are [1,5,9,10,11,12,13,<u>**13**</u>,15], and the 8^th smallest number is 13
#### Example 2

- **Input:** $matrix = [[-5]], k = 1$
- **Output:** `-5`
### Constraints

- $n = \text{matrix.length} = \text{matrix}[i].length$

- $1 \le n \le 300$

- $-10^{9} \le \text{matrix}[i][j] \le 10^{9}$

- All the rows and columns of `matrix` are **guaranteed** to be sorted in **non-decreasing order**.

- $1 \le k \le n^{2}$

**Follow up:**

- Could you solve the problem with a constant memory (i.e., `O(1)` memory complexity)?

- Could you solve the problem in `O(n)` time complexity? The solution may be too advanced for an interview but you may find reading <a href="http://www.cse.yorku.ca/~andy/pubs/X+Y.pdf" target="_blank">this paper</a> fun.