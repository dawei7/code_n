# Check if the array is sorted

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | ARRAYSORTED |
| Difficulty Band | Practice Arrays |
| Path | Data Structures and Algorithms |
| Lesson | Arrays |
| Official Link | [ARRAYSORTED](https://www.codechef.com/practice/course/arrays/ARRAYSPRO/problems/ARRAYSORTED) |

---

## Problem Statement

Given an array $nums$ which is rotated. You have to find out if the given array is sorted and rotated.

An array is considered **sorted and rotated** if:
- There exists a non-decreasing sorted array $A$.
- After rotating $A$ by some $k$ positions (possibly $k = 0$), we obtain the given array $nums$.
- Rotation means some suffix of $A$ is moved to the front, keeping the relative order of elements.

Duplicates are allowed in the array.

**Note:**
If $A$ is the original sorted array and it is rotated **right** by $k$ positions, the resulting array $B$ satisfies:

$$
B[(i+k) \bmod A.length] = A[i]
$$

for every valid index $i$. \
`1 2 3 4 5` is a sorted array and `2 3 4 5 1` is also a sorted array but after 4 rotations.

## Function Declaration

### Function Name
$check$ – This function checks whether a given array $nums$ is a non-decreasing sorted array that has been rotated any number of times (including zero rotations).

### Parameters

* $nums$ : A reference to a vector of integers representing the array.

### Return Value

* Returns $true$ if the array $nums$ can be obtained by rotating a non-decreasing sorted array.
* Returns $false$ otherwise.

## Constraints

- $1 \leq \text{nums.length} \leq 10^5$
- $1 \leq \text{nums}[i] \leq 100$

---

## Input Format

* The first line contains an integer $N$ — the size of the array.
* The second line contains $N$ space-separated integers — the elements of the array $nums$.

---

## Output Format

* $true$ if the array is sorted in non-decreasing order and then rotated any number of times (including zero).
  * $false$ otherwise.

---

## Constraints

$$ 1 \leq \text{nums.length} \leq 100 $$ \
$$ 1 \leq \text{nums}[i] \leq 100 $$

---

## Examples

**Example 1**

**Input**

```text
7
6 7 1 2 3 4 5
```

**Output**

```text
true
```

**Explanation**

The original sorted array was `[1,2,3,4,5,6,7]`.
Rotating by `k = 2` positions gives `[6,7,1,2,3,4,5]`.

**Example 2**

**Input**

```text
5
68 97 10 21 45
```

**Output**

```text
true
```

**Explanation**

The original sorted array `[10 ,21 ,45 ,68 ,97]` rotated by `k = 2` results in `[68 ,97 ,10 ,21 ,45]`.

**Example 3**

**Input**

```text
5
4 5 2 3 1
```

**Output**

```text
false
```

**Explanation**

No rotation of a sorted array can produce this order.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

## Problem Restatement

You are given an array of integers. You need to determine whether the array is **sorted in non-decreasing order** (ascending order with duplicates allowed).

If the array is sorted, return **true**, otherwise return **false**.

---

## Key Observations

1. **Sorted in non-decreasing order** means every element must be **less than or equal to the next element**:

   $$
   nums[i] \leq nums[i+1] \quad \text{for all valid } i
   $$

2. If at least one violation exists (i.e., `nums[i] > nums[i+1]`), the array is not sorted.

3. We don’t need to modify the array or use extra space; we can simply check adjacent pairs.

---

## Approach

1. Traverse the array from index `0` to `n-2`.
2. For each index `i`, compare `nums[i]` with `nums[i+1]`.
3. If `nums[i] > nums[i+1]`, immediately return **false** (not sorted).
4. If no violation is found, return **true** at the end.

---

## Complexity Analysis

* **Time Complexity:**
  We only check each pair once, so the complexity is **O(n)**, where `n` is the length of the array.

* **Space Complexity:**
  No extra space is used apart from a variable to track comparisons → **O(1)**.

---

</details>
