# Petersen Graph

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PETERSEN |
| Difficulty Rating | 1894 |
| Difficulty Band | Rise from 3* to 4* |
| Path | Become 5 star |
| Lesson | Graphs |
| Official Link | [PETERSEN](https://www.codechef.com/practice/course/3to4stars/LP3TO403/problems/PETERSEN) |

---

## Problem Statement

The following graph **G** is called a [Petersen graph](http://en.wikipedia.org/wiki/Petersen_graph) and its vertices have been numbered from **0** to **9**. Some letters have also been assigned to vertices of **G**, as can be seen from the following picture:

	Let's consider a walk **W** in graph **G**, which consists of **L** vertices **W1**, **W2**, ..., **WL**, such that **Wi** is connected with **Wi + 1** for 1 ≤ **i** < **L**. A string **S** of **L** letters **'A'-'E'** is realized by walk **W** if the sequence of letters written along **W** is equal to **S**. Vertices can be visited multiple times while walking along **W**.

For example, **S** = **'ABBECCD'** is realized by **W** = (0, 1, 6, 9, 7, 2, 3).

Your task is to determine whether there is a walk **W** which realizes a given string **S** in graph **G**, and if so, find the lexicographically least such walk.

### Input

	The first line of the input contains one integer **T** denoting the number of testcases to process.

	The only line of each testcase contains one string **S**. It is guaranteed that **S** only consists of symbols **'A'-'E'**.

### Output

	The output should contain exactly **T** lines, one line per each testcase in the order of their appearance. For each testcase, if there is no walk **W** which realizes **S**, then output **-1**. Otherwise, you should output the least lexicographical walk **W** which realizes **S**. Since all of the vertices are numbered from **0** to **9**, then it can be encoded as a string consisting of symbols **'0'-'9'** (see the "Examples" section for more details).

### Constraints

1 ≤ **T** ≤ 8;

1 ≤ **|S|** ≤ 100000(105).

---

## Examples

**Example 1**

**Input**

```text
2
AAB
AABE
```

**Output**

```text
501
-1
```

**Separated test cases**

#### Test case 1

**Input for this case**

```text
AAB
```

**Output for this case**

```text
501
```



#### Test case 2

**Input for this case**

```text
AABE
```

**Output for this case**

```text
-1
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

**Problem Link:** [contest](http://www.codechef.com/COOK52/problems/PETERSEN), [practice](http://www.codechef.com/problems/PETERSEN)

**Difficulty:** Simple

**Pre-requisites:** DFS, BFS, Graph traversal

**Problem:**

Given a graph **G**, its vertices have been numbered from **0** to **9**. Some letters have also been assigned to vertices of **G**, as can be seen from the following picture:

Given a string **S**. Your task is to determine whether there is a walk **W** which realizes a given string **S** in graph **G**, and if so, find the lexicographically least such walk.

**Explanation:**

Let’s consider the picture from the statement carefully. The key observation is that there’s no vertex **V** in **G** such that it’s connected with two other vertices with the same letter written on them.

In other words, if we are looking for a way to continue the current walk from a vertex **V** and the next letter in **S** is **C** then two options are possible:

-
**V** is not connected with vertices labled with **C**, so it’s impossible to continue the current walk;

-
**V** is connected with exactly one vertex **U** labled with **C**, so there’s only one way to continue the current walk.

The next observation is that there are only two possible vertices to start our walk. After that observation we are ready to compose the whole solution:

- Choosing the starting vertex of the walk;

- Trying to complete the walk by moving to the corresponding vertices(if possible);

- Finding the lexicographically least valid walk. It’s sufficient to compare paths only by their starting vertices.

There is an interesting fact that the only situation when there are two valid paths is when **S** consists of one symbol concatenated several times with itself. For example, there are two valid paths **3838** and **8383** for **S** = **DDDD**.

Complexity is **O(N)** per a testcase.

</details>
