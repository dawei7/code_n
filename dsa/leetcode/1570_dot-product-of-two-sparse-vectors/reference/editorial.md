[TOC]

## Solution

A sparse vector is a vector that has mostly zero values, while a dense vector is a vector where most of the elements are non-zero. It is inefficient to store a sparse vector as a one-dimensional array (Approach 1). Instead, we can store the non-zero values and their corresponding indices in a dictionary, with the index being the key (Approach 2). Alternatively, we can represent elements of a sparse vector as an array of pairs for each non-zero value. Each pair has an integer index and a numerical value (Approach 3).

A related question is [LeetCode 311. Sparse Matrix Multiplication](https://leetcode.com/problems/sparse-matrix-multiplication/).

---

### Approach 1: Non-efficient Array Approach

#### Intuition

We ignore the sparsity of the array and store the original array.

#### Algorithm

```python
class SparseVector:
    def __init__(self, nums):
        self.array = nums

    def dotProduct(self, vec):
        result = 0
        for num1, num2 in zip(self.array, vec.array):
            result += num1 * num2
        return result
```

#### Complexity Analysis

Let $n$ be the length of the input array.

* Time complexity: $O(n)$ for both constructing the sparse vector and calculating the dot product.

* Space complexity: $O(1)$ for constructing the sparse vector as we simply save a reference to the input array and $O(1)$ for calculating the dot product.

---

### Approach 2: Hash Table

#### Intuition

Store the non-zero values and their corresponding indices in a dictionary, with the index being the key. Any index that is not present corresponds to a value 0 in the input array.

#### Algorithm

```python
class SparseVector:
    def __init__(self, nums: List[int]):
        self.nonzeros = {}
        for i, n in enumerate(nums):
            if n != 0:
                self.nonzeros[i] = n

    def dotProduct(self, vec: 'SparseVector') -> int:
        result = 0
        # iterate through each non-zero element in this sparse vector
        # update the dot product if the corresponding index has a non-zero value in the other vector
        for i, n in self.nonzeros.items():
            if i in vec.nonzeros:
                result += n * vec.nonzeros[i]
        return result
```

#### Complexity Analysis

Let $n$ be the length of the input array and $L$ be the number of non-zero elements.

* Time complexity: $O(n)$ for creating the Hash Map; $O(L)$ for calculating the dot product.

* Space complexity: $O(L)$ for creating the Hash Map, as we only store elements that are non-zero. $O(1)$ for calculating the dot product.

---

### Approach 3: Index-Value Pairs

#### Intuition

We can also represent elements of a sparse vector as a list of <index, value> pairs. We use two pointers to iterate through the two vectors to calculate the dot product.

#### Algorithm

```python
class SparseVector:
    def __init__(self, nums: List[int]):
        self.pairs = []
        for index, value in enumerate(nums):
            if value != 0:
                self.pairs.append([index, value])

    def dotProduct(self, vec: 'SparseVector') -> int:
        result = 0
        p, q = 0, 0

        while p < len(self.pairs) and q < len(vec.pairs):
            if self.pairs[p][0] == vec.pairs[q][0]:
                result += self.pairs[p][1] * vec.pairs[q][1]
                p += 1
                q += 1
            elif self.pairs[p][0] < vec.pairs[q][0]:
                p += 1
            else:
                q += 1

        return result

```

#### Complexity Analysis

Let $n$ be the length of the input array and $L$ and $L_{2}$ be the number of non-zero elements for the two vectors.

* Time complexity: $O(n)$ for creating the <index, value> pair for non-zero values; $O(L+L_{2})$ for calculating the dot product.

* Space complexity: $O(L)$ for creating the <index, value> pairs for non-zero values. $O(1)$ for calculating the dot product.