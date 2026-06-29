# Chef and Three Dogs

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CHDOGS |
| Difficulty Rating | 1473 |
| Difficulty Band | 1400 to 1600 difficulty problems |
| Path | Become 5 star |
| Lesson | 1400 to 1500 difficulty problems |
| Official Link | [CHDOGS](https://www.codechef.com/practice/course/2-star-difficulty-problems/DIFF1500/problems/CHDOGS) |

---

## Problem Statement

Chef has three dogs sitting at the vertices of an equilateral triangle. The length of each side of the triangle equals to **s** meters. Chef gives the command "Start!" and each dog starts to run with constant speed **v** meters per second. At each moment, each dog is running towards the dog just right to him (in counter-clockwise direction). Therefore, their trajectories are forming some spirals that converging to one point as illustrated below.

How long does it takes dogs to meet each other after the command "Start!"?

### Input

The first line of the input contains an integer **T** denoting the number of test cases. The description of **T** test cases follows.

The only line of each test case contains two space-separated integers **s** and **v**.

### Output

For each test case, output a single line containing a real number corresponding to the answer of the problem. The answer will be considered correct if its absolute or relative error does not exceed 10-6.

### Constraints

- **1** ≤ **T** ≤ **10**

- **1** ≤ **s, v** ≤ **109**

### Subtasks

- Subtask #1 (40 points): **1** ≤ **s, v** ≤ **10**

- Subtask #2 (60 points): **original constraints**

---

## Examples

**Example 1**

**Input**

```text
2
2 5
1 1000000000
```

**Output**

```text
0.266667
0.0000001
```

**Explanation**

Due to the triangle being very small, but the dogs running extremely fast, they will meet after less than 1e-6 seconds. Thus, due to remark about absolute or relative error in the output section, any answer within [0, 1e-6] will be considered correct.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2 5
```

**Output for this case**

```text
0.266667
```



#### Test case 2

**Input for this case**

```text
1 1000000000
```

**Output for this case**

```text
0.0000001
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINKS

[Practice](http://www.codechef.com/problems/CHDOGS)

[Contest](http://www.codechef.com/OCT16/problems/CHDOGS)

### DIFFICULTY

simple

### PREREQUISITES

symmetry, rate of approach, trigonometry

### PROBLEM

There are three points on equilateral triangle of side s. Each point is moving constant velocity v towards the point on the right of it. You need to find the time at which these three points will meet.

### QUICK EXPLANATION

The answer is \frac{2}{3} \frac{s}{v}.

### EXPLANATION

This question can be solved in a lot of the ways. Actually, this problem was easily search-able on web. The intent of giving this problem was to familiarize the readers with various different ways of solving the problem.

#### Where will the points meet?

By symmetry, we can say that the points will meet at the centroid of the triangle. In fact, the triangle formed by the three points at any install during their journey will also stay equilateral.

### Velocity of approach based solutions.

Let us consider the points A, B, C, at some instant. The point A is moving towards B. B is moving towards C, and C towards A. Let us find our rate of approach of points A and B towards each other. A is moving towards B, so its velocity vector v will contribute completely in the rate of approach. Velocity vector of B is directed towards C, so its component v cos(60) towards A will only contribute in the rate of approach. So rate of approach of A and B towards each other will be v + v cos(60) = \frac{3 v}{2}.

By symmetry, we can say that rate of approach will be same for A, B, A, C and B, C all three pairs.

Initially the distance between A, B is s. So, total time taken in meeting will be

\frac{s}{\frac{3 v}{2}} = \frac{2 s}{3 v}

You can also see [this beautiful written answer on stackexchange](http://math.stackexchange.com/a/1081921) too.

### By solving the expression for separation vs time

You can solve this question by rigorously working out expressions of separation vs time. This solution can be found [here](http://math.stackexchange.com/a/1839577).

### Simulation based solution

You can say that the time will be proportional to side of equilateral triangle s, inversely proportional to speed.

t \propto \frac{s}{v}

The proportional relation should not depend on values of s and v, so it will be a constant.

t = c \cdot \frac{s}{v}

Finding the constant c can be done experimentally by a simulating the motion of points by taking dt (change in time) as low as possible. You will see that the constant will approach towards \frac{2}{3}.

### Interesting readings.

[This Stackexchange answer](http://math.stackexchange.com/a/44897) very beautifully explain finding the location of meeting of points without using the symmetry argument directly.

In the same context, [this answer](http://math.stackexchange.com/a/44903) is also worth reading.

This [Quora answer](https://www.quora.com/There-are-3-points-placed-on-the-vertices-of-an-equilateral-triangle-of-side-A-Each-point-travels-with-a-constant-speed-of-v-directly-to-the-next-point-How-much-time-does-it-take-for-the-three-points-to-meet/answer/Ajit-Athle?srid=3wWX) gives an idea of solving the problem for any general regular polygon.

Time complexity of all these solutions at the end are constant time (\mathcal{O}(1).

### EDITORIALIST’S SOLUTION

Can be found [here](http://www.codechef.com/download/Solutions/OCT16/Editorialist/CHDOGS.cpp).

### TESTER’S SOLUTION

Can be found [here](http://www.codechef.com/download/Solutions/OCT16/Tester/CHDOGS.cpp).

</details>
