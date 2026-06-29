# Count Distinct Values

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CNTDIST |
| Difficulty Band | Jump from 2* to 3* |
| Path | Become 5 star |
| Lesson | Sorting |
| Official Link | [CNTDIST](https://www.codechef.com/practice/course/2to3stars/LP2TO302/problems/CNTDIST) |

---

## Problem Statement

##

Given an array of size $n$, find the number of distinct elements in the array.

Chef already tried an attempt to solve the above problem and he came up with this [code](https://pastebin.com/tSrY8yD3).

The approach is simple, for each new number that is obtained, iterate over the previously obtained numbers and if a match is found then add one to the count of distinct numbers obtained so far, otherwise leave it as is (add zero).

However when Chef submitted the above code he got Time Limit Exceeded.

Determine the worst case time complexity of Chef's code.

It can be shown that the worst case time complexity is $\mathcal{\Theta}(n^a)$ where $a$ is an integer.

First find the value of $a$, and then optimise Chef's code using the data structures that you have learnt.

(Hint: Think about sets/ dictionary and how it could be used to solve this problem.)

### Input
- First line contains an integer $n$, the size of the array
- Next $n$ lines each contain a single integer, the elements of the array.

### Output
Print two lines. In the first line print the value of $a$ where the worst case time complexity of Chef's code is $\Theta(n^a)$.
In the second line, print a single integer, the number of distinct values in the given array.

### Constraints
- $1 \leq n \leq 10^5$
- $0 \leq A_i \leq 10^9$
- The elements of the array are generated uniformly randomly among the given constraints.

---

## Examples

**Example 1**

**Input**

```text
3
1
2
1
```

**Output**

```text
*
2
```

**Explanation**

In order to not give away the answer, the first line is given as "*". Note that this is not the correct answer but just a placeholder to explain the output format.

The given array contains the values $1$ and $2$ ($1$ repeated twice), hence the number of distinct values is $2$, and is printed in the second line.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [Count Distinct Values Practice Problem in Jump from 2* to 3*](https://www.codechef.com/practice/course/2to3stars/LP2TO302/problems/CNTDIST)

### [](#problem-statement-1)Problem Statement:

In this problem, you are asked to determine two things:

- The worst-case time complexity of Chef’s naive solution for finding the number of distinct elements in an array.

- The actual number of distinct values in the array.

### [](#approach-2)Approach:

-

Chef’s naive approach involves checking each element in the array against all previously encountered elements to determine if it has already been counted as distinct. For each element, this requires iterating through the entire list of previous elements, resulting in a nested loop structure. This leads to a time complexity of Θ(n^2) in the worst case because, for each of the `n` elements, up to `n−1` comparisons are made.

-

To optimize Chef’s solution, we can use a **set** or **hash set** to keep track of distinct elements. Inserting an element into a set has an average time complexity of `O(1)` due to the underlying hash table data structure. This means the entire process of counting distinct elements can be done in **linear time**, `O(n)`, by simply inserting each element into the set and then determining the size of the set.

### [](#complexity-3)Complexity:

- **Time Complexity:** using a set has a time complexity of `O(n)`.

- **Space Complexity:** `O(n)`, because in the worst case, the set stores all distinct elements, which can be up to `n` elements.

</details>
