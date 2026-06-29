# Collisions

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | LCOLLIS |
| Difficulty Rating | 1352 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1200 to 1400 difficulty problems |
| Official Link | [LCOLLIS](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1400/problems/LCOLLIS) |

---

## Problem Statement

Once **N** boys and **M** girls attended a party. You are given a matrix **A** of **N** rows and **M** columns where **Aij** is **1** if the **i-th** boy likes the **j-th** girl, otherwise it will be 0. Note that it is not necessary that if a boy **x** likes girl **y**, then girl **y** should like boy **x**.

You know that if there are two different boys **x** and **y**, who both like girl **z**, then there will be a collision.
Can you calculate the number of different collisions at this party? Note that order of boys in the collision doesn't matter.

### Input

The first line contains a single integer **T** denoting the number of test cases. Then **T** test cases follow.

The first line of each test case contains two space separated integers **N**, **M** denoting the number of boys and girls, respectively.

Each of the following **N** lines contain **M** characters, each of them is either **'0'** or **'1'**.

### Output

For each test case output a single line containing an integer corresponding to the number of collisions at the party.

### Constraints

- **1** ≤ **T** ≤ **100**

- **1** ≤ **N, M** ≤ **10**

---

## Examples

**Example 1**

**Input**

```text
2
4 3
111
100
110
000
2 2
10
01
```

**Output**

```text
4
0
```

**Explanation**

**Example Case 1.** All three boys like the first girl, so there are **(1, 2, 1), (1, 3, 1), (2, 3, 1)** collisions with her. Boys **1** and **3** both like the second girl so this is one more collision. Only one boy likes the third girl, so there are no collisions with her and thus we have **4** collisions total.

**Example Case 2.** For each girl there is only one boy who likes her, so there are no collisions at all.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4 3
111
100
110
```

**Output for this case**

```text
4
```



#### Test case 2

**Input for this case**

```text
000
2 2
10
01
```

**Output for this case**

```text
0
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice][111]

[Contest][222]

**Author:** [Pavel Sheftelevich](http://www.codechef.com/users/pavel1996)

**Tester:** [Karan Aggarwal](http://www.codechef.com/users/karanaggarwal)

**Editorialist:** [Praveen Dhinwa](http://www.codechef.com/users/dpraveen)

### DIFFICULTY:

Cakewalk

### PREREQUISITES:

basic implementation

### PROBLEM:

There are n boys and m girls in a class. You are given a matrix of size n \times m whose i, j-th entry denotes whether i-th boy likes j-th girl or not. There will be a collision if two boys i, j likes a girl k. You have to find number of collisions that can possibly happen in the class. Note that collision i, j liking k and j, i liking k is the same collision and should not be counted more than once.

### QUICK EXPLANATION

We can just iterate over all possible pairs of boys and girls and check whether the corresponding triplets causes a collision or not.

### EXPLANATION:

There will be a collisions if two boys i, j likes girl k. Let a[n][m] denote the matrix given in the input, whose a_{i, j} entry denotes whether i-th boy likes j-th girl or not. Then we can check whether their a collision formed by triplets i, j, k by checking whether a_{i, k} and a_{j, k} both are equal to 1 or not.

We should notice one important thing is the order of boys in the collision does not matter, i.e. if order of i, j in the collision should not be counted twice. (i, j, k) and (j, i, k) collisions are essentially the same. So, for ease of counting, we can count a collision of pairs (i, j, k) if i < j.

For finding total number of collisions, we can notice that dimensions of the matrix dimensions are very small, n, m \leq 10. So, we can counting the collisions by just checking all triplets (i, j, k).

See the following pseudo code.

``
collisions = 0
for i from 1 to n:
	for j from i + 1 to n:
		for k from 1 to m:
			if (a[i][k] == 1 and a[j][k] == 1):
				collisions += 1
print collisions

``

### TIME COMPLEXITY

As we iterate over pairs i, j, k, where i and j can take values upto n and k can take values up to m. So, the overall time complexity will be \mathcal{O}(n * n * m) = \mathcal{O}(n^2 m). In the worst case, for a single test case, our program will take around \mathcal{O}(10^3) operations. There are total 100 test cases. So, total number of operations our program will take will be around \mathcal{O}(10^5) which will run very comfortably in 1 secs. Usually C, C++, Java can perform roughly 10^8 simple arithmetic operations in a second.

### AUTHOR’S AND TESTER’S SOLUTIONS:

[Author’s solution](http://www.codechef.com/download/Solutions/LTIME37/Setter/LCOLLIS.cpp)

[Tester’s solution](http://www.codechef.com/download/Solutions/LTIME37/Tester/LCOLLIS.cpp)

[111]: [http://www.codechef.com/problems/LCOLLIS](http://www.codechef.com/problems/LCOLLIS)

[222]: [http://www.codechef.com/LTIME37/problems/LCOLLIS](http://www.codechef.com/LTIME37/problems/LCOLLIS)

</details>
