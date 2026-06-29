# Intersecting arrays

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | DSCPPAS261 |
| Difficulty Band | Practice Arrays |
| Path | Data Structures and Algorithms |
| Lesson | Arrays |
| Official Link | [DSCPPAS261](https://www.codechef.com/practice/course/arrays/ARRAYSPRO/problems/DSCPPAS261) |

---

## Problem Statement

Given two integer arrays $nums1$ and $nums2$, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and return the result in **sorted order**.

Intersection is defined as the common element in both arrays. For example -

$nums1$ - [1, 2] and $nums2$ - [2, 1, 3]

Therefore, only 1 and 2 are common in both arrays. On sorting the resultant array would be [1, 2].

---

## Input Format

- The first line contains two integers $n$ , $m$— the size of $nums1$ and $nums2$.
- The second line contains n integers $a1,a2,…,an$ — the number of $nums1$.
- The third line contains m integers $b1,b2,…,bm$ — the number of $nums2$.

---

## Output Format

Print all the elements that are appearing in both the arrays in sorted order.

---

## Constraints

- $ 1 \leq n,m \leq 100 $
- $ 0 \leq ai \leq 100 $
- $ 0 \leq bi \leq 100 $

---

## Examples

**Example 1**

**Input**

```text
2 3
1 2
2 1 3
```

**Output**

```text
1 2
```

**Explanation**

The common elements in both arrays are 1,2. so their intersection is 1,2.

**Example 2**

**Input**

```text
3 3
1 2 3
3 4 6
```

**Output**

```text
3
```

**Explanation**

Only 3 is present as the common element in both arrays.

**Example 3**

**Input**

```text
3 3
1 1 2
1 3 1
```

**Output**

```text
1 1
```

**Explanation**

There are 2 1's present in both of the arrays so the answer is `1 1`.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#### [](#problem-statement-1)Problem Statement

Given two integer arrays, `nums1` and `nums2`, find their intersection and return it. Each element in the result should appear as many times as it shows in both arrays. You can assume the values in `nums1` and `nums2` are limited to integers ranging from `0` to `100`.

#### [](#approach-2)Approach

This problem can be solved efficiently using a counting method due to the constraint on the values of the elements (ranging from `0` to `100`). Here’s how we can approach the problem:

-

**Fixed-Size Arrays for Counting:** Since the values in both input arrays are between `0` and `100`, we can use two fixed-size arrays (`v` and `c`) of length `101` to count the occurrences of each integer in both arrays.

-

**Counting Occurrences:**

- First, iterate through `nums1` and populate the `v` array, where `v[i]` stores the count of the number `i` in `nums1`.

- Next, iterate through `nums2` and populate the `c` array, where `c[i]` stores the count of the number `i` in `nums2`.

-

**Finding the Intersection:**

- For each possible integer value `i` from `0` to `100`, find the minimum count of `i` in both arrays (`v[i]` and `c[i]`). This represents how many times `i` should appear in the intersection.

- Add this minimum count of `i` to the result array.

-

**Output the Result:**

- The result array is filled with the elements representing the intersection of `nums1` and `nums2`.

- The `intersect` function modifies the `returnSize` to indicate the number of elements in the result and returns the array.

#### [](#code-explanation-3)Code Explanation

Here’s the breakdown of the provided code:

-

**Counting Occurrences:**

- The function `intersect` takes five parameters: two arrays (`nums1`, `nums2`), their respective sizes, a pointer to store the result size, and an array to store the intersection result.

- The `v` and `c` arrays of size `101` are initialized to zero. These arrays store the counts of each element in `nums1` and `nums2`.

-

**Populating the Count Arrays:**

- The first `for` loop populates the `v` array by counting occurrences of each element in `nums1`.

- The second `for` loop populates the `c` array by counting occurrences of each element in `nums2`.

-

**Finding the Intersection:**

- The third `for` loop iterates over the possible values (`0` to `100`), determines the minimum count of each number present in both `nums1` and `nums2`, and adds that many occurrences to the result array.

-

**Main Function:**

- The main function reads the sizes of the input arrays and their elements.

- It then calls the `intersect` function to find the intersection and store the result in the `ans` array.

- Finally, it prints the elements of the intersection.

#### [](#complexity-analysis-4)Complexity Analysis

- **Time Complexity:** O(n + m), where `n` is the size of `nums1` and `m` is the size of `nums2`. Counting the elements in each array takes O(n) and O(m) respectively, and finding the intersection involves a fixed iteration of 101 steps (from 0 to 100), which is constant.

- **Space Complexity:** O(1) auxiliary space, not considering the input and output arrays. The use of fixed-size arrays (`v`, `c`, and `ans`) makes the space usage constant.

</details>
