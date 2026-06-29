# Sticks

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | STICKS |
| Difficulty Rating | 1261 |
| Difficulty Band | Level up from 1* to 2* |
| Path | Become 5 star |
| Lesson | Sorting |
| Official Link | [STICKS](https://www.codechef.com/practice/course/1to2stars/LP1TO204/problems/STICKS) |

---

## Problem Statement

Chef and his little brother are playing with sticks. They have total **N** sticks. Length of **i**-th stick is **Ai**.
Chef asks his brother to choose any four sticks and to make a rectangle with those sticks its sides. Chef warns his brother to not to break any of the sticks, he has to use sticks as a whole. Also, he wants that the rectangle formed should have the maximum possible area among all the rectangles that Chef's brother can make.

Chef's little brother takes this challenge up and overcomes it. Can you also do so? That is, you have to tell whether it is even possible to create a rectangle? If yes, then you have to tell the maximum possible area of rectangle.

### Input

The first line contains a single integer **T** denoting the number of test-cases. **T** test cases follow.

The first line of each test case contains a single integer **N** denoting the number of sticks.

The second line of each test case contains **N** space-separated integers **A1**, **A2**, ..., **AN** denoting the lengths of sticks.

### Output

For each test case, output a single line containing an integer representing the maximum possible area for rectangle or -1 if it's impossible to form any rectangle using the available sticks.

### Constraints

- **1** ≤ **T** ≤ **100**

- **1** ≤ **N** ≤ **103**

- **1** ≤ sum of **N**'s over all test-cases in a single test file ≤ **103**

- **1** ≤ **Ai** ≤ **103**

---

## Examples

**Example 1**

**Input**

```text
2
5
1 2 3 1 2
4
1 2 2 3
```

**Output**

```text
2
-1
```

**Explanation**

**Example case 1.** Chef's brother can choose sticks of lengths 1, 2, 1, 2. He can create a rectangle with area 1 * 2 = 2.

**Example case 2.** It's impossible to choose 4 sticks so that they form a rectangle.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5
1 2 3 1 2
```

**Output for this case**

```text
2
```



#### Test case 2

**Input for this case**

```text
4
1 2 2 3
```

**Output for this case**

```text
-1
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](http://www.codechef.com/problems/STICKS)

[Contest](http://www.codechef.com/COOK71/problems/STICKS)

[Video Editorial](https://youtu.be/i7FElgi-5QI)

**Author:** [Hasan Jaddouh](https://www.codechef.com/users/kingofnumbers)

**Tester:** [Misha Chorniy](https://www.codechef.com/users/mgch)

**Editorialist:** [Pushkar Mishra](https://www.codechef.com/users/pushkarmishra)

### DIFFICULTY:

Simple

### PREREQUISITES:

Greedy

### PROBLEM:

Given an array of A of N integers which represent stick lengths, we have to report the maximal area over all the rectangles that we can form with the given sticks without breaking any.

### EXPLANATION:

The problem is a simple one based on a very basic property of all rectangles: the opposite sides of a rectangle are parallel, and hence, equal in length. The area of a rectangle is given by base B multiplied by height H. Now, to maximise the area, we simply need to maximise the length of sticks we choose as our B and H. This is pretty intuitive but we can also invoke the [exchange argument method](http://web.stanford.edu/class/archive/cs/cs161/cs161.1138/handouts/120%20Guide%20to%20Greedy%20Algorithms.pdf) (page 3 of link) to give a more formal argument as proof of why this works (left to reader as a simple learning exercise).

Now we come to the implementation detail of the above mentioned algorithm. Note that N and A_{max} both range between 1 and 10^3. So, one way is that we simply keep an array Count of length 10^3 wherein Count[i] is the number of sticks of length i that we have. Once we have populated this structure, we can simply scan from 10^3 down to 1. If while scanning, we can find one field which has more than 3 sticks, then that i can be our height and base both; at this point we terminate our scan. If we find a field that has more than 1 stick, we can make it either our height or base and continue our scan to find a value for the other one. If at the end of scan we don’t find at least two i for which the count is more than 1, then we output -1 since no rectangle can be formed.

The other implementation can be by using a map instead of an array. In that case, if the N is much smaller than A_{max}, we can get a better performance. Both of the implementations easily pass for the given constraints.

Please see editorialist’s/setter’s program for implementation details.

### COMPLEXITY:

\mathcal{O}(N\log N) or \mathcal{O}(A_{max}) per test case.

### SAMPLE SOLUTIONS:

[Author](http://www.codechef.com/download/Solutions/COOK71/Setter/STICKS.cpp)

[Tester](http://www.codechef.com/download/Solutions/COOK71/Tester/STICKS.cpp)

[Editorialist](http://www.codechef.com/download/Solutions/COOK71/Editorialist/STICKS.cpp)

### Video Editorial

</details>
