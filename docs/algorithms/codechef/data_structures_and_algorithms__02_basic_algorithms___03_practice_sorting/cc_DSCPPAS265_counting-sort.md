# Counting sort

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | DSCPPAS265 |
| Difficulty Rating | 1650 |
| Difficulty Band | Practice Sorting |
| Path | Data Structures and Algorithms |
| Lesson | Sorting |
| Official Link | [DSCPPAS265](https://www.codechef.com/practice/course/sorting/SORTINGPRO/problems/DSCPPAS265) |

---

## Problem Statement

You are given a list of integers. Your task is to sort the list based on the frequency of each integer in ascending order. If two integers have the same frequency, the one with the smaller value should come first.

---

## Input Format

- The first line contains a single integer $n$, the number of integers in the list.
- The second line contains $n$ space separated integers $a1,a2,…,an$.

---

## Output Format

Print the sorted list based on the frequency of each integer.

---

## Constraints

- $1 \leq n \leq 100$.
- $1 \leq a_i \leq 100$.

---

## Examples

**Example 1**

**Input**

```text
4
1 2 3 2
```

**Output**

```text
1 3 2 2
```

**Explanation**

The frequencies are: 1 appears once, 2 appears twice, and 3 appears once.

Sorting primarily by frequency, integers 1 and 3 (each appearing once) come before 2 (appearing twice). Since 1 and 3 have the same frequency, they are sorted by their value, resulting in 1 before 3.

The final sorted list is: 1, 3, 2, 2.

**Example 2**

**Input**

```text
4
2 1 1 1
```

**Output**

```text
2 1 1 1
```

**Explanation**

The frequencies are: 1 appears thrice and 2 appears once.

Sorting by frequency, the integer 2 (appearing once) comes before 1 (appearing three times).

The final sorted list is: 2,1,1,1.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#### [](#problem-statement-1)Problem Statement:

You are given a list of integers. The task is to sort the list based on the frequency of each integer in ascending order. If two integers have the same frequency, the integer with the smaller value should come first.

#### [](#approach-2)Approach:

To solve this problem, we need to accomplish two main tasks:

- Count the frequency of each integer in the list.

- Sort the integers based on their frequency in ascending order. If two integers have the same frequency, the one with the smaller value should appear first.

Here’s a step-by-step explanation of the approach:

#### [](#step-1-counting-the-frequencies-3)Step 1: Counting the Frequencies

- We initialize an array `count` where `count[i]` stores the frequency of integer `i`.

- We iterate over the input list and increment the count of each integer in the `count` array.

#### [](#step-2-creating-a-list-of-pairs-4)Step 2: Creating a List of Pairs

- After counting the frequencies, we create a list of pairs where each pair consists of an integer and its corresponding frequency.

- For example, if the frequency of integer `3` is `2`, we create a pair `(3, 2)`.

#### [](#step-3-sorting-the-list-of-pairs-5)Step 3: Sorting the List of Pairs

- We then sort this list of pairs based on two criteria:

- **Primary Criterion:** Sort by frequency in ascending order.

- **Secondary Criterion:** If two integers have the same frequency, sort by the integer’s value in ascending order.

#### [](#step-4-generating-the-sorted-list-6)Step 4: Generating the Sorted List

- Finally, we construct the sorted list by appending each integer in the order determined by the sorted list of pairs.

#### [](#example-7)Example:

Let’s consider an example where the input list is:

``[4, 5, 6, 5, 4, 3]
``

-

The frequency count will be:

- `4` occurs `2` times.

- `5` occurs `2` times.

- `6` occurs `1` time.

- `3` occurs `1` time.

-

The list of pairs based on frequency would be:

``[(6, 1), (3, 1), (4, 2), (5, 2)]
``

-

After sorting based on frequency and value, the list becomes:

``[(3, 1), (6, 1), (4, 2), (5, 2)]
``

-

The final sorted output list would be:

``[3, 6, 4, 4, 5, 5]
``

#### [](#time-complexity-8)Time Complexity:

The time complexity is `O(n + k log k)` where `n` is the number of elements and `k` is the number of unique elements in the list.

#### [](#space-complexity-9)Space Complexity:

The space complexity is `O(k)` for storing the frequency list, where `k` is the number of unique elements.

</details>
