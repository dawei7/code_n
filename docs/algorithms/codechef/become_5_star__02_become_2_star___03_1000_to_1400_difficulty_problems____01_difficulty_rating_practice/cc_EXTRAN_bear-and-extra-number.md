# Bear and Extra Number

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | EXTRAN |
| Difficulty Rating | 1311 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1200 to 1400 difficulty problems |
| Official Link | [EXTRAN](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1400/problems/EXTRAN) |

---

## Problem Statement

A sequence is called nice if its elements are distinct consecutive numbers, possibly in changed order.
For example, both (6, 7, 8) and (15, 13, 16, 14) are nice, while (4, 6), (4, 5, 5, 6) and (15, 16, 15) are not.

Limak has a nice sequence.
While he was in school today, someone inserted one extra number in the sequence.
Limak has just returned and realized that the sequence isn't nice anymore!
He wants to remove the inserted number and make his sequence nice again.
Can you help him to find the number that he should remove?

Formally, in each test case you are given a sequence of **N** numbers **A**1, **A**2, ..., **AN**.
Your task is to find the value **X**, such that removing one occurrence of **X** would make the sequence nice.
It's guaranteed that exactly one solution exists.

### Input

The first line of the input contains an integer **T** denoting the number of test cases.
The description of **T** test cases follows.

The first line of each test case contains an integer **N** denoting the size of the new sequence.

The second line of a test case contains **N** integers **A**1, **A**2, ..., **AN** denoting the new sequence.

### Output

For each test case, output a single line containing one integer — a number that should be removed from the given sequence.

### Constraints

- **1** ≤ **T** ≤ **10**

- **3** ≤ **N** ≤ **105**

- **1** ≤ **A**i ≤ **109**

- The given sequence isn't nice.

- There is exactly one solution.

### Subtasks

- Subtask #1 (40 points) **3** ≤ **N** ≤ **1000**

- Subtask #2 (60 points) Original constraints

---

## Examples

**Example 1**

**Input**

```text
4
5
45 42 46 48 47
3
7 7 8
8
12 156 157 158 159 160 161 162
4
8 7 10 6
```

**Output**

```text
42
7
12
10
```

**Explanation**

**Test case 1.** The sequence **A** is (45, 42, 46, 48, 47). We should remove the number 42, and the remaining numbers will form a nice sequence (45, 46, 48, 47).

**Test case 2.** We should remove one of two 7's to get the sequence (7, 8), which is nice.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5
45 42 46 48 47
```

**Output for this case**

```text
42
```



#### Test case 2

**Input for this case**

```text
3
7 7 8
```

**Output for this case**

```text
7
```



#### Test case 3

**Input for this case**

```text
8
12 156 157 158 159 160 161 162
```

**Output for this case**

```text
12
```



#### Test case 4

**Input for this case**

```text
4
8 7 10 6
```

**Output for this case**

```text
10
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](https://www.codechef.com/problems/EXTRAN)

[Contest](https://www.codechef.com/MARCH17/problems/EXTRAN)

**Author:** [Kamil D?bowski](https://www.codechef.com/users/errichto)

**Testers:** [Sergey Kulik](https://www.codechef.com/users/xcwgf666)

**Editorialist:** [Pawel Kacprzak](https://www.codechef.com/users/pkacprzak)

### DIFFICULTY:

Simple

### PREREQUISITES:

Sorting, basic programming

### PROBLEM:

We call a sequence of integers **nice** if and only if they can be arranged into a sequence of distinct consecutive numbers.

The problem can be described as the following process: initially, there was a sequence B consisting of N-1 integers, which was a nice sequence. Then, number X was inserted somewhere into B to form a new sequence A. We know that A is not a nice sequence, i.e. integers in A cannot be arranged into a sequence of distinct consecutive numbers. The task is to for a given sequence B found the number X, which was inserted into B to form B. It is guaranteed that there exists one unique answer to the problem and N \geq 3.

### QUICK EXPLANATION:

Sort the given sequence and notice that there is sufficient to check 3 separated cases defining X.

### EXPLANATION:

### Subtask 1

In the first subtask we know that N is at most 1000, so one possible solution is to iterate over all numbers in A, and for each such number check if A without that number is a nice sequence.

Let’s assume that we want to check that A without its i-th element, i.e. A[i] is a nice sequence. If it is, then we know that the answer to the problem is A[i], because the answer is guaranteed to be unique. In order to check if A without A[i] is a nice sequence, we can build a new sequence C which have all elements from A except A[i], sort C in ascending order and check if all two consecutive elements of sorted C are consecutive integers. Notice that since it’s guaranteed that the answer exists and it’s unique, then there exists i such that A without A[i] is a good sequence and it will be found by the above process because it checks all i. The time complexity per a single test case is O(N \cdot N \cdot \log N), because for each of N choices of i we perform a sort of N-1 elements followed by a linear check over these elements, and it is enough to get accepted. This complexity can be slightly improved to O(N^2) by sorting the input sequence at the beginning.

### Subtask 2

In the second subtask, N can be at most 10^5, so the method used for the first subtask is too slow here.

Let’s consider a sequence B, i.e. the sequence into X was inserted to form A. The main observation is since we know that B was nice, then there are just 3 possible cases to check:

-
X + 1 is smaller than the minimum element of B

-
X - 1 is larger than the maximum element of B

-
X is equal to one of the elements of B

Notice that the above 3 cases indeed cover all possibilities. In order to prove that, let m be the smallest element of B and let M be the largest element of B. We know that X cannot be equal to m-1, because then A would be a nice sequence and we know it’s not. Similarly, X cannot be equal to M+1, because then A would also be a nice sequence. Now, each integer except m-1 and M+1 falls into one of the above 3 cases, so the only remaining thing to do is to check which of these cases is true. In order to do that, at the beginning we sort A. Then checking cases 1 and 2 is very easy - just compare two smallest elements and two largest elements of A. To check if the third case is true, we can just iterate over sorted sequence A and check if any two its consecutive elements are equal. The total time complexity of this method is O(N \cdot \log N) and it’s dominated by the sorting phase.

### AUTHOR’S AND TESTER’S SOLUTIONS:

Setter’s solution can be found [here](https://www.codechef.com/download/Solutions/MARCH17/Setter/EXTRAN.cpp).

Tester’s solution can be found [here](https://www.codechef.com/download/Solutions/MARCH17/Tester1/EXTRAN.cpp).

Editorialist’s solution can be found [here](https://www.codechef.com/download/Solutions/MARCH17/Editorialist/EXTRAN.cpp).

</details>
