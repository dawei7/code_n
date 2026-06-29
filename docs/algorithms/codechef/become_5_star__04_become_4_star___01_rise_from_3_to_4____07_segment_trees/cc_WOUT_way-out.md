# Way Out

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | WOUT |
| Difficulty Rating | 1845 |
| Difficulty Band | Rise from 3* to 4* |
| Path | Become 5 star |
| Lesson | Segment Trees |
| Official Link | [WOUT](https://www.codechef.com/practice/course/3to4stars/LP3TO407/problems/WOUT) |

---

## Problem Statement

Oh, no! Chef’s in trouble. He’s got himself stuck in a cave (we don’t know how) and is looking for a way out. The bigger problem is that he needs to get his tractor out of the cave (don't ask why Chef owns a tractor!). He currently faces a large block of height **N** cells and length **N** cells, and needs to get his tractor across this block. The block is made up of vertical columns of soil, each of which is one cell long. Each column has a continuous vertical gap, with the **i**th column having its gap from the **li**th cell to the **hi**th cell (starting from the bottom, 0-indexing). That is, in the **i**th column, there is no soil from the **li**th cell to the **hi**th cell (both inclusive). Chef can build additional gaps by clearing some cells of soil. His tractor has height **H**, and therefore, he needs to build a horizontal corridor of height **H** passing through all the columns. That is, some consecutive **H** rows must have no soil. Please see the figures in the example and explanation sections for more details.

Chef is able to clear one cell of soil by spending one unit of energy. Chef is smart, and will figure out a way to build the horizontal corridor while spending the minimum possible amount of energy. To estimate how many of his tasty dishes he will still be able to cook for you tonight, find out what is the minimum possible energy he needs to spend.

### Input

First line of input contains one integer **T** - number of test cases. **T** test cases follow.

Each test case starts with two integers **N** and **H** – size of the cave and height of the tractor, respectively. In each of the next **N** lines are two integers **li** and **hi**, respectively indicating lowest and highest number of cell for the gap in the **i**th column.

### Output

One integer – minimum energy required.

### Constraints

- **1** ≤ **T** ≤ **103**

- **1** ≤ **N** ≤ **106**

- **1** ≤ sum of **N** over all test cases ≤ **106**

- **1** ≤ **H** ≤ **N**

- **0** ≤ **li** ≤ **hi** < **N**

### Subtasks

Subtask 1 (25 points): **T ≤ 100, N ≤ 100**

Subtask 2 (75 points): No additional constraints

---

## Examples

**Example 1**

**Input**

```text
2
4 3
1 2
1 2
1 2
1 2
5 2
2 3
1 2
2 3
1 2
2 3
```

**Output**

```text
4
2
```

**Explanation**

In the second case, the figure describes the initial map, where white cells denote empty cells and brown cells denote soil cells.

When we removed soil in two cells as the following figure, then we can make a corridor of height 2, adn this is the optimal way to make a corridor.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Contest](http://www.codechef.com/AUG15/problems/WOUT)

[Practice](http://www.codechef.com/AUG15/problems/WOUT)

**Author:** [Vitalij Kozhukhivskij](http://www.codechef.com/users//witalij_hq)

**Tester:** [Hiroto Sekido](http://www.codechef.com/users/laycurse)

**Editorialist:** [Kevin Atienza](http://www.codechef.com/users/kevinsogo)

### DIFFICULTY:

Easy

### PREREQUISITES:

Dynamic programming, subarray sums, prefix sums, segment trees

### PROBLEM:

There is a grid of N\times N cells. The N blocks of each column are made up of soil, except for a contiguous sequence of cells: from the $l_i$th cell to the $h_i$th cell (starting from the bottom, 0-indexing). Cells can be cleared of soil.

We need to create a subgrid of length N and height H containing no soil. What is the minimum number of cells needed to be cleared of soil?

### QUICK EXPLANATION:

There are only N-H+1 possible N\times H subgrids. The answer is the the minimum number of soil cells among all such subgrids. We can preprocess our grid so we can compute the sum of each subgrid in constant time.

To preprocess:

- We need to know the number of soil cells in each row (denoted by r_i for 0 \le i < N). r_i is equal to the number of j s such that 0 \le j < N and i < l_j or i > h_j. This is also equal to the following expression:

N - \#\{j : 0 \le j < N, i \le h_j\} +  \#\{j : 0 \le j < N, i < l_j\}

Thus the $r_i$s can be computed quickly by considering the $l_j$s and $h_j$s in sorted order.

- We also need to know the number of soil cells in each prefix of rows, i.e. let s_i be the sum r_0 + r_1 + \cdots + r_{i-1}.

Then the number of soil cells in each N\times H subgrid can be computed as s_i - s_{i-H} for H \le i \le N.

### EXPLANATION:

Clearly, we need to find the N\times H subgrid with the minimum number of soil cells in it. There are only N-H+1 such subgrids: the following illustrates the case N = 7 and H = 3 (there are N-H+1 = 5 subgrids):

``.......          #######   .......   .......   .......   .......
.......          #######   #######   .......   .......   .......
.......          #######   #######   #######   .......   .......
....... -------> .......   #######   #######   #######   .......
.......          .......   .......   #######   #######   #######
.......          .......   .......   .......   #######   #######
.......          .......   .......   .......   .......   #######
``

We can simply construct the N\times N grid, and compute the number of soil cells in these subgrids. Since there are N-H+1 subgrids and each one has NH cells to check, this algorithm runs in O((N-H+1)NH) time. The worst case is when H is around half of N (which makes the running time O(N^3)), so unfortunately this algorithm is only good for the first subtask. For the second subtask, you can’t even store the whole grid due to the memory requirements!

To answer the second subtask, we need a way to sum up these subgrids without constructing the whole grid. The first thing we notice is that the only information we need from its row is the number of soil cells in it, i.e. we don’t need to know their positions in the row. Let’s say the i th row (0 \le i < N) contains r_i soil cells. Then the number of soil cells in each of the N-H+1 subgrids are the following:

- r_0 + r_1 + r_2 + \cdots + r_{H-1}

- r_1 + r_2 + r_3 + \cdots + r_H

- r_2 + r_3 + r_4 + \cdots + r_{H+1}

- r_3 + r_4 + r_5 + \cdots + r_{H+2}

- \ldots

- r_{N-H} + r_{N-H+1} + r_{N-H+3} + \cdots + r_{N-1}

The smallest of these is the answer! Thus, it would be very helpful if we can compute the sequence r_0, r_1, \ldots, r_{N-1} quickly, without constructing the whole grid!

To do so, we use the following observation: r_i is equal to the number of j s such that 0 \le j < N and i < l_j or i > h_j. Now, counting all such j s this way is still not fast enough, so we do some manipulations first. For a statement \phi(j), let C_{\phi(j)} be the number of j s such that 0 \le j < N and \phi(j) is true. To familiarize yourself with this notation, we give a few basic facts (we invite you to verify each one):

- C_{\text{true}} = N

- C_{\text{false}} = 0

- C_{\phi(j)} + C_{\text{not }\phi(j)} = C_{\text{true}} = N

- C_{\phi(j)} = C_{\text{true}} - C_{\text{not }\phi(j)} = N - C_{\text{not }\phi(j)}

- C_{\phi_1(j) \text{ or } \phi_2(j)} = C_{\phi_1(j)} + C_{\phi_2(j)} - C_{\phi_1(j) \text{ and } \phi_2(j)}

-
C_{c < f(j)} + C_{c = f(j)} + C_{c > f(j)} = N (trichotomy)

- C_{c < f(j)} + C_{c = f(j)} = C_{c \le f(j)}

- If f_1(j) \le f_2(j) for all j, then C_{f_1(j) \le c \le f_2(j)} = C_{c \le f_2(j)} - C_{c < f_1(j)}

Now, back to r_i. We have the following (using some of the facts above:

\begin{aligned}
r_i
&= C_{i < l_j \text{ or } i > h_j} \\\
&= N - C_{\text{not } (i < l_j \text{ or } i > h_j)} \\\
&= N - C_{i \ge l_j \text{ and } i \le h_j} \\\
&= N - C_{l_j \le i \le h_j} \\\
&= N - (C_{i \le h_j} - C_{i < l_j})
\end{aligned}

The last one is true because l_j \le h_j. Now, we have:

r_i = N - C_{i \le h_j} + C_{i < l_j}

To compute the $r_i$s, we just need to compute the quantity - C_{i \le h_j} + C_{i < l_j} for all 0 \le i < N.

The key to this is to notice that r_i can be computed by a simple adjustment from r_{i-1}! In other words, we can just calculate the difference r_i - r_{i-1}, and if we have already computed r_{i-1}, then we can calculate r_i by adding this difference. In more detail, let’s try to compute r_i - r_{i-1}:

\begin{aligned}
r_i - r_{i-1}
&= (N - C_{i \le h_j} + C_{i < l_j}) - (N - C_{i-1 \le h_j} + C_{i-1 < l_j}) \\\
&= N - C_{i \le h_j} + C_{i \le l_j-1} - N + C_{i \le h_j+1} - C_{i \le l_j} \\\
&= C_{i \le h_j+1} - C_{i \le h_j} + C_{i \le l_j-1} - C_{i \le l_j} \\\
&= (C_{i \le h_j+1} - C_{i \le h_j}) + (C_{i \le l_j-1} - C_{i \le l_j}) \\\
&= C_{i = h_j+1} - C_{i = l_j}
\end{aligned}

But we can compute the values C_{i = h_j+1} and C_{i = l_j} for 0 \le i < N quickly, via a linear pass of all pairs (l_j,h_j) for 0 \le j < N! The following pseudocode does it:

``# arrays are initialized with zeroes
Ch[0...N]   # Ch[i] will contain C[i = h_j + 1]
Cl[0...N]   # Ch[i] will contain C[i = l_j]
for j = 0...N-1:
    Ch[h_j + 1] += 1
    Cl[l_j] += 1
``

Now that all the C_{i = h_j+1} and C_{i = l_j} are computed, we can now compute all the $r_i$s using the following recurrence:

r_{-1} = N

r_i = r_{i-1} + C_{i = h_j+1} - C_{i = l_j}

The following pseudocode does it:

``# array is initialized with zeroes
r[0...N]
curr = N
for i in 0...N-1:
    curr += Ch[i] - Cl[i]
    r[i] = curr
``

Clearly, these pseudocodes run in O(N) time!

Finally, to compute the answer, we need to know the following sums:

- r_0 + r_1 + r_2 + \cdots + r_{H-1}

- r_1 + r_2 + r_3 + \cdots + r_H

- r_2 + r_3 + r_4 + \cdots + r_{H+1}

- r_3 + r_4 + r_5 + \cdots + r_{H+2}

- \ldots

- r_{N-H} + r_{N-H+1} + r_{N-H+3} + \cdots + r_{N-1}

and then compute the minimum among them. But this is easy! Notice that r_i + r_{i+1} + \cdots + r_j is simply (r_0 + \cdots + r_j) - (r_0 + \cdots + r_{i-1}), so we can first try computing the **prefix sums**. Let s_i be the sum r_0 + r_1 + \cdots + r_{i-1}. Then r_i + r_{i+1} + \cdots + r_j is simply s_{j+1} - s_i. The $s_i$s can be computed in O(N) too, because s_i = s_{i-1} + r_{i-1}, with the base case s_0 = 0. Afterwards, the sums we need are simply:

- s_H - s_0

- s_{H+1} - s_1

- s_{H+2} - s_2

- \ldots

- s_N - s_{N-H}

Since all the steps of this algorithm runs is O(N), the answer can thus be computed in O(N) time in total!

The following is a sample implementation in Python:

``for cas in xrange(input()):
    n, h = map(int, raw_input().strip().split())
    row = [0]*(n+2)
    for i in xrange(n):
        a, b = map(int, raw_input().strip().split())
        row[a+1] -= 1
        row[b+2] += 1
    row[0] = n
    for i in xrange(n): row[i+1] += row[i]
    for i in xrange(n): row[i+1] += row[i]
    print min(row[i] - row[i-h] for i in xrange(h,n+1))
``

A few things to notice about this implementation:

- The pairs (l_j, h_j) are never stored in an array: they are obtained from the input on the fly, processed, and thrown away immediately.

- Instead of having two arrays for Ch[i] and Cl[i], we only use a single array containing Ch[i] - Cl[i].

- We reuse the same array `row` to contain the values Ch[i] - Cl[i], r_i and s_i. Furthermore, r_i is stored in index i+1 of `row`.

### Time Complexity:

O(N)

### AUTHOR’S AND TESTER’S SOLUTIONS:

[setter](http://www.codechef.com/download/Solutions/AUG15/Setter/WOUT.java)

[tester](http://www.codechef.com/download/Solutions/AUG15/Tester/WOUT.cpp)

</details>
