# Bear and Ladder

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | BRLADDER |
| Difficulty Rating | 999 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 800 to 1000 difficulty rating problems |
| Official Link | [BRLADDER](https://www.codechef.com/practice/course/logical-problems/DIFF1000/problems/BRLADDER) |

---

## Problem Statement

Bearland has infinitely many cities, numbered starting from 1.
Some pairs of cities are connected with bidirectional roads:

- There are roads 1-2, 3-4, 5-6, 7-8, and so on (there is a road between cities 2*i+1 and 2*i+2 for every non-negative integer i).

- There are roads 1-3, 3-5, 5-7, 7-9, ... (between every two consecutive odd numbers).

- There are roads 2-4, 4-6, 6-8, 8-10, ... (between every two consecutive even numbers).

This is how the first few cities and roads between them look like:

You are given **Q** queries.
In each query, for the given pair of different cities **a** and **b**, you should check if there is a road between them.
For each query, print "YES" or "NO" accordingly.

### Input

The first line of the input contains an integer **Q**, denoting the number of queries.

Each of the following **Q** lines contains two distinct integers **a** and **b**, denoting two cities in one query.

### Output

For each query, output a single line containing the answer — "YES" if there is a road between the given cities **a** and **b**, and "NO" otherwise (without the quotes).

### Constraints

- 1 ≤ **Q** ≤ 1000

- 1 ≤ **a**, **b** ≤ 109

- **a** ≠ **b**

---

## Examples

**Example 1**

**Input**

```text
7
1 4
4 3
5 4
10 12
1 3
999999999 1000000000
17 2384823
```

**Output**

```text
NO
YES
NO
YES
YES
YES
NO
```

**Explanation**

In the example test, the answer is "YES" for pairs (4, 3), (10, 12), (1, 3) and (999999999, 1000000000).
Roads 3-4 and 1-3 you can see on the drawing in the statement.

The answer is "NO" for example for a pair (1, 4), because there is no road between cities 1 and 4.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1 4
```

**Output for this case**

```text
NO
```



#### Test case 2

**Input for this case**

```text
4 3
```

**Output for this case**

```text
YES
```



#### Test case 3

**Input for this case**

```text
5 4
```

**Output for this case**

```text
NO
```



#### Test case 4

**Input for this case**

```text
10 12
```

**Output for this case**

```text
YES
```



#### Test case 5

**Input for this case**

```text
1 3
```

**Output for this case**

```text
YES
```



#### Test case 6

**Input for this case**

```text
999999999 1000000000
```

**Output for this case**

```text
YES
```



#### Test case 7

**Input for this case**

```text
17 2384823
```

**Output for this case**

```text
NO
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](https://www.codechef.com/problems/BRLADDER)

[Contest](https://www.codechef.com/LTIME46/problems/BRLADDER)

**Author:** [Kamil D?bowski](https://www.codechef.com/users/errichto)

**Testers:** [Hasan Jaddouh](https://www.codechef.com/users/kingofnumbers),  [Sergey Kulik](https://www.codechef.com/users/xcwgf666)

**Editorialist:** [Pawel Kacprzak](https://www.codechef.com/users/pkacprzak)

### DIFFICULTY:

Cakewalk

### PREREQUISITES:

Elementary math

### PROBLEM:

For a given **infinite** [ladder graph](https://en.wikipedia.org/wiki/Ladder_graph) G with vertices numbered from 1, and integer Q, the goal is to answer Q queries. Each query contains two integers a and b and asks if there is an edge between vertices a and b in G.

There are 3 types of edges between vertices of G:

-

There is an edge between vertices labeled with two consecutive numbers if and only if the smaller label is odd

-

There is an edge between vertices labeled with two consecutive odd numbers

-

There is an edge between vertices labeled with two consecutive even numbers

### EXPLANATION:

In order to solve the problem, we are going to answer queries one after another. For a fixed query (a, b), we simply check if a, b can form an edge within any of the classes defined above. Notice that performing such a check for each class is easy:

**Class 1:** Checking if a, b forms an edge of the first class can be done by just checking if the smaller label is odd and the difference between the larger and the smaller label is exactly 1.

**Classes 2 and 3:** Checking if a, b forms an edge of either the second or the third class can be done by just checking if the difference between the larger and the smaller label is exactly 2.

Since performing each of the above checks takes a constant time, the total complexity of the solution is O(Q).

### AUTHOR’S AND TESTER’S SOLUTIONS:

Setter’s solution can be found [here](https://www.codechef.com/download/Solutions/LTIME46/Setter/BRLADDER.cpp).

First tester’s solution can be found [here](https://www.codechef.com/download/Solutions/LTIME46/Tester1/BRLADDER.cpp).

Second tester’s solution can be found [here](https://www.codechef.com/download/Solutions/LTIME46/Tester2/BRLADDER.cpp).

</details>
