# Stable Quick Sort

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | QCKSRT2 |
| Difficulty Band | Jump from 2* to 3* |
| Path | Become 5 star |
| Lesson | Sorting |
| Official Link | [QCKSRT2](https://www.codechef.com/practice/course/2to3stars/LP2TO302/problems/QCKSRT2) |

---

## Problem Statement

## Stable Quick Sort

Recall the meaning of stable sort

A sorting algorithm is stable, if the relative order of elements that are "equal" are maintained.

To demonstrate this, consider a list of pairs of integers, [(1, 2), (2, 3), (2, 1), (3, 2)]

If we want to sort this list such that tuples with lesser first elements occur first, but among tuples with the same first value, we are not bothered with the order of the second value, for example both (2, 3) and (2, 1) can occur in any order and are considered "equal" to each other.

If we run **any** stable sorting algorithm with the comparator defined as above, the relative order of the elements with the same first value will remain unchanged. For the above example, a stable sorting algorithm will not change the above array given, however an unstable sorting algorithm could print [(1, 2), (2, 1), (2, 3), (3, 2)] instead.

We know that the some implementations of quick sort are not stable, specifically the one given in the question [QCKSRT1](https://codechef.com/PEC2021F/problems/QCKSRT1) is not stable.

Here is an attempt at a modification of quick sort ([modified quick sort](https://pastebin.com/79VhLCXT)) that is intended to be stable.

Note that it is no longer "in-place", that is we create extra memory for copying the values of the array. (Not really relevant to this problem, just an interesting observation)

In the above code ([modified quick sort](https://pastebin.com/79VhLCXT)), the line for choosing the pivot is left blank. If we choose the pivot to be the first value of the array (i.e $arr[l]$), then the sorting algorithm will be stable, however if it is randomised, then it won't be.

You are to help fill the gap in the above algorithm while making it randomised.

Given an array $A$ (of size $n$), of pairs of integers, print (in increasing order) those indices (numbered from $0$ to $n-1$) that if chosen as a pivot for the above modified [quick sort](https://pastebin.com/79VhLCXT) algorithm, results in a stable sorting algorithm.

Note that the if the output of your program is a list of indices called $candidates$ then choosing the pivot as $arr[candidates[rand(0, len(candidates)-1)]]$ would result in a version of quick sort that is both randomised and stable.

You are given a [solution template](https://pastebin.com/mLg6vGmb), note that the input and output is taken care of in the template and you only need to correct the function $choose\_pivot$ in the above template.

### Input

Note that you can directly fill in the $choose\_pivot$ function given in the [solution template](https://pastebin.com/mLg6vGmb), so you do not have to worry about this section.

This is an explanation of how input is taken in the solution template.

There are two lines, the first line contains a single integer $n$, the size of the array.

The second line contains $2n$ space separated integers, the $2i^{th}$ and $(2i+1)^{th}$ numbers denote the $i^{th}$ tuple.

### Output

Note that you can directly fill in the $choose\_pivot$ function given in the [solution template](https://pastebin.com/mLg6vGmb), so you do not have to worry about this section.

This is an explanation of how output is done in the given solution template.

In the first line print $m$, the number of valid choices of indices for the pivot in the first iteration of quick sort of this array

In the second line print those indices (space separated) in increasing order.

### Constraints

$1 \leq n \leq 1000$

$-10^9 \leq $ every integer given $ \leq 10^9$

---

## Examples

**Example 1**

**Input**

```text
4
1 2 2 3 2 1 3 2
```

**Output**

```text
3
0 1 3
```

**Explanation**

The given array is $\{(1, 2), (2, 3), (2, 1), (3, 2)\}$

If we choose the index 2, then the partitioned array after the first iteration of quick sort becomes $\{(1, 2), (2, 1), (2, 3), (3, 2)\}$ which is affects the stability, since the order of $(2, 3)$ and $(2, 1)$ is changed.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [https://www.codechef.com/practice/course/2to3stars/LP2TO302/problems/QCKSRT2](https://www.codechef.com/practice/course/2to3stars/LP2TO302/problems/QCKSRT2)

### [](#problem-statement-1)Problem Statement:

You are given a collection of `n` pairs, where each pair contains two integers. The task is to write a function that selects the indices (0-based) of pairs based on the uniqueness of the first element of each pair. The output should be a list of indices such that the first element of each selected pair is unique, maintaining the original order of the pairs.

### [](#approach-2)Approach:

To solve this problem, we need to ensure that for each unique first element in the pairs, we only select the first occurrence of it and store the index. Here’s a step-by-step breakdown of the approach:

**Tracking Unique Elements**:

- **Initialize a `set`**: Create a set to store the first elements of the pairs as they are encountered. This ensures that only unique elements are tracked.

- **Create a `candidates` container**: Initialize a container (e.g., a list or array) to store the indices of the pairs whose first elements are unique.

- **Iterate through the array of pairs**:

- For each pair, check if the first element is not present in the set.

- If the element is unique (i.e., not found in the set):

- Append the current index of the pair to the `candidates` container.

- Insert the first element into the set to mark it as seen.

**Return the `candidates` container**: After the iteration, return the container holding the indices of the selected pairs.

### [](#complexity-3)Complexity:

- **Time Complexity:** `O(n)`, where `n` is the number of pairs. This is because we are iterating over the array once and performing insert and find operations on a set, which takes `O(1)` on average due to hash set operations.

- **Space Complexity:** `O(n)` in the worst case, due to storing unique elements and indices.

</details>
