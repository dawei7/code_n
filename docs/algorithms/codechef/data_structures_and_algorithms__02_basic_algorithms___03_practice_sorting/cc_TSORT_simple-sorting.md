# Simple Sorting

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | TSORT |
| Difficulty Rating | 667 |
| Difficulty Band | Practice Sorting |
| Path | Data Structures and Algorithms |
| Lesson | Sorting |
| Official Link | [TSORT](https://www.codechef.com/practice/course/sorting/SORTING/problems/TSORT) |

---

## Problem Statement

Given a list of numbers, you have to sort them in non decreasing order.

---

## Input Format

- The first line contains a single integer, $N$, denoting the number of integers in the list.
- The next $N$ lines contain a single integer each, denoting the elements of the list.

---

## Output Format

Output $N$ lines, containing one integer each, in non-decreasing order.

---

## Constraints

- $1 \leq N \leq 10^6$
- $0 \leq$ elements of the list $\leq 10^6$

---

## Examples

**Example 1**

**Input**

```text
5
5
3
6
7
1
```

**Output**

```text
1
3
5
6
7
```

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
3
```

**Output for this case**

```text
3
```



#### Test case 3

**Input for this case**

```text
6
```

**Output for this case**

```text
5
```



#### Test case 4

**Input for this case**

```text
7
```

**Output for this case**

```text
6
```



#### Test case 5

**Input for this case**

```text
1
```

**Output for this case**

```text
7
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [Simple Sorting Practice Problem in Sorting](https://www.codechef.com/practice/course/sorting/SORTING/problems/TSORT?tab=solution)

### [](#problem-statement-1)Problem Statement:

Given a list of numbers, you have to sort them in non decreasing order.

### [](#approach-2)Approach:

You need to sort these integers in non-decreasing order. Sorting algorithms with time complexity better than `O(N^2)` are necessary because `N` can be as large as 10^6, so using efficient sorting algorithms like **QuickSort** - [Quick Sort in Searching and Sorting Algorithms](https://www.codechef.com/learn/course/searching-sorting/SORTSEARCH8/problems/SESO28), **MergeSort** - [Merge sort algorithm in Design and Analysis of Algorithms](https://www.codechef.com/learn/course/college-design-analysis-algorithms/CPDAA03/problems/DAA012), or **HeapSort** - [Heap Sort in Heaps](https://www.codechef.com/learn/course/heaps/LIHP02/problems/HEAP08) `(O(N log N))` is essential. Preferably the in-built **sort** functions which are optimized for such tasks.

### [](#complexity-3)Complexity:

- **Time Complexity:** `O(N log N)` Using inbuilt sort function or any other sorting algorithms which has time complexity of `O(N log N)` as N<=10^6.

- **Space Complexity:** `O(N)` using vector to store the numbers.

</details>
