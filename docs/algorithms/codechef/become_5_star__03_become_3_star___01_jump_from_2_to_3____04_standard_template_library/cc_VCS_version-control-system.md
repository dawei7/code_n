# Version Control System

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | VCS |
| Difficulty Rating | 1217 |
| Difficulty Band | Jump from 2* to 3* |
| Path | Become 5 star |
| Lesson | Standard Template Library |
| Official Link | [VCS](https://www.codechef.com/practice/course/2to3stars/LP2TO304/problems/VCS) |

---

## Problem Statement

A *version control system*(VCS) is a repository of files, often the files for the source code of computer programs, with monitored access. Every change made to the source is tracked, along with who made the change, why they made it, and references to problems fixed, or enhancements introduced, by the change.

	Version control systems are essential for any form of distributed, collaborative development. Whether it is the history of a wiki page or large software development project, the ability to track each change as it was made, and to reverse changes when necessary can make all the difference between a well managed and controlled process and an uncontrolled ‘first come, first served’ system. It can also serve as a mechanism for due diligence for software projects.

	In this problem we'll consider a simplified model of a development project. Let's suppose, that there are **N** source files in the project. All the source files are distinct and numbered from 1 to **N**.

	A VCS, that is used for maintaining the project, contains two sequences of source files. The first sequence contains the source files, that are ignored by the VCS. If a source file is not in the first sequence, then it's considered to be unignored. The second sequence contains the source files, that are tracked by the VCS. If a source file is not in the second sequence, then it's considered to be untracked. A source file can either be or not be in any of these two sequences.

	Your task is to calculate two values: the number of source files of the project, that are both tracked and ignored, and the number of source files of the project, that are both untracked and unignored.

### Input

The first line of the input contains an integer **T** denoting the number of test cases. The description of **T** test cases follows.

The first line of the test case description contains three integers **N**, **M** and **K** denoting the number of source files in the project, the number of ignored source files and the number of tracked source files.

The second line contains **M** distinct integers denoting the sequence **A** of ignored source files. The sequence is strictly increasing.

The third line contains **K** distinct integers denoting the sequence **B** of tracked source files. The sequence is strictly increasing.

### Output

For each test case, output a single line containing two integers: the number of the source files, that are both tracked and ignored, and the number of the source files, that are both untracked and unignored.

### Constraints

- 1 ≤ **T** ≤ 100

- 1 ≤ **M**, **K** ≤ **N** ≤ 100

- 1 ≤ **A1** < **A2** < ... < **AM** ≤ **N**

- 1 ≤ **B1** < **B2** < ... < **BK** ≤ **N**

---

## Examples

**Example 1**

**Input**

```text
2
7 4 6
1 4 6 7
1 2 3 4 6 7
4 2 2
1 4
3 4
```

**Output**

```text
4 1
1 1
```

**Explanation**

In the first test case, the source files {1, 4, 6, 7} are both tracked and ignored, the source file {5} is both untracked and unignored.

	In the second test case, the source file {4} is both tracked and ignored, the source file {2} is both untracked and unignored.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
7 4 6
1 4 6 7
1 2 3 4 6 7
```

**Output for this case**

```text
4 1
```



#### Test case 2

**Input for this case**

```text
4 2 2
1 4
3 4
```

**Output for this case**

```text
1 1
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](http://www.codechef.com/problems/VCS)

[Contest](http://www.codechef.com/COOK57/problems/VCS)

**Author:** [Konstantsin Sokol](http://www.codechef.com/users/kostya_by)

**Tester:** [Gedi Zheng](http://www.codechef.com/users/stzgd)

**Editorialist:** [Miguel Oliveira](http://www.codechef.com/users/mogers)

### DIFFICULTY:

Easy.

### PREREQUISITES:

Sets.

### PROBLEM

Given 2 sets of integers, count the number of integers that appear in both sets and the number of integers between 1 and N that do not appear in either set.

### QUICK EXPLANATION

The source files that are both tracked and ignored are the intersection of the two sets given in the input.

The source files that are both untracked and unignored are the numbers in the interval [1, N] that do not appear in either of the given lists.

### EXPLANATION

We are given 2 lists of unique integers. We can treat these lists as sets. A set is a collection of distinct items (integers in this case).

**Both ignored and tracked source files**

The source files that are both tracked and ignored are the integers in the intersection of the 2 given sets.

To calculate the set intersection, the simplest way is to search all integers of the first set in the second set. Since we have only 100 numbers, we could do this search naively with 2 nested loops and a time complexity of O(M*K).

A smarter way is to use a hash table. Note that the numbers are between 1 and 100. We can use an array with 100 positions and mark position *i* if number *i* is in the set. This way we can look-up if a number is in a set in O(1) time. Thus, the time complexity of the set intersection is O(M) to build set A, O(K) to build set B and O(M) to check if the items in set A appear in set B. The total time complexity of this set intersection is O(M+K).

Also, you can use set, map, unordered_map in C++ to make a look up table too.

Also, sometimes you can use bitwise operations with bit packing the sets in the integer to int or long data type. Then, you can use bitwise operations (e.g. and, or, xor) to check set intersection. Also, for two sorted arrays a, b, you can use set_intersection in C++ to find number of common elements in both the arrays in linear time.

**Both unignored and untracked source files**

The number of source files that are both untracked and unignored are the integers between 1 and N that do not appear in set A or B. We can use the same logic and search all numbers between 1 and N in sets A and B. This will take O(N) time if we use hashing or O(N * (M+K)) with the naive search.

**Time Complexity**

The total time complexities are O(N + M + K) using hashing and O(M * K + N * (M+K)). Both were perfectly fine as the size of the sets are up to 100.

### AUTHOR’S AND TESTER’S SOLUTIONS:

[Setter’s solution](http://www.codechef.com/download/Solutions/COOK57/Setter/VCS.cpp)

[Tester’s solution](http://www.codechef.com/download/Solutions/COOK57/Tester/VCS.cpp)

</details>
