# Chefland and Electricity

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CHEFELEC |
| Difficulty Rating | 1767 |
| Difficulty Band | 1600 to 1800 difficulty problems |
| Path | Become 5 star |
| Lesson | 1700 to 1800 difficulty problems |
| Official Link | [CHEFELEC](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1800/problems/CHEFELEC) |

---

## Problem Statement

There are **n** villages in a Chefland. Some of the villages have electricity facilities, other doesn't. You can consider the villages arranged in line in the order **1** to **n** from left to right. i-th of village can be considered at **xi** coordinates.

Chef decided that electricity should be provided to all the villages. So, he decides to buy some amount of electric wires to connect the villeges without electricity to some villages with electricity. As Chef does not want to spend too much amount of money on wires, can you find out minimum amount of length of wire Chef should buy.

### Input

First line of the input contains an integer **T** denoting the number of test cases. **T** test cases follow.

First line of each test case contains an integer **n** denoting number of villages in Chefland.

Second line will contain a string of length **n** containing '0' or '1's only. If i-th character of the string is '1', then it denotes that i-th village has electricity.

Next line contains **n** space separated integers denoting the **x** coordinates of the villages in the order from village **1** to **n

### Output

For each test case, output a single line containing a integer corresponding to the minimum length of wire Chef needs to buy.

### Constraints

- **1 ≤ T ≤ 10**

- It is guaranteed that there will be at least one village which will have electricity.

- **1 ≤ x1 <  x2 <  ... < xn ≤ 109**

### Subtasks

**Subtask #1 : 30 points**

- **1 ≤ N ≤ 1000**

**Subtask #2 : 70 points**

- **1 ≤ N ≤ 105**

---

## Examples

**Example 1**

**Input**

```text
2
2
01
1 2
3
100
1 5 6
```

**Output**

```text
1
5
```

**Explanation**

**In the first example**, first village does not have electricity. If we put a wire between village 1 and 2 of length 1, then both the villages will have electricity.

**In the second example**,
We can a draw a wire from first village to third village, passing through second village. Its total length will be 5. Now all the villages will have electricity. This is the minimum length of wire you will require.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2
01
1 2
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
3
100
1 5 6
```

**Output for this case**

```text
5
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](http://www.codechef.com/problems/CHEFELEC)

[Contest](http://www.codechef.com/JULY16/problems/CHEFELEC)

**Author:** [Praveen Dhinwa](https://www.codechef.com/users/dpraveen)

**Tester:** [Mugurel Ionut Andreica](http://www.codechef.com/users/mugurelionut)

**Editorialist:** [Praveen Dhinwa](http://www.codechef.com/users/dpraveen)

### DIFFICULTY:

Simple

### PREREQUISITES:

greedy

### PROBLEM:

There are n villages in a city. The positions of the villages are given to you in the sorted order of their x coordinates. Note that all the villages are in a single line. Also you can assume that a village will be denoted by a single point on the x axis. Recently some of the villages have been electrified. You are given this information by a string s, where s_i = '1' denotes that i-th village has been electrified. You want to electrify all the villages by a connecting un-electrified villages by connecting with some already electrified village by establishing a electricity line between the villages. Find out the minimum length of electric wire required.

### EXPLANATION:

One very simple observation is that if you connect some un-electrified village i to some electrified village j > i, then all the villages k (between i and j, i.e. i \leq k < j) will be electrified too.

**Observation**

It does not make any sense to not connect to some un-electrified village k to some village other than its left electrified village i, or its right electrified village j.

This observation allows us to split the villages on a line into segments such that end points of each segment are electrified (except the boundary villages, in that case, you might have zero or one of its end points being electrified.).  We can solve the problem individually for each segment greedily and their total will be amount of wire required.

Let us consider a segment of the villages between village i to j, such that villages i and j are electrified and no intermediate village i < k  j is electrified. What should be the minimum length of write needed to electrify all the intermediate villages. Note that we can electrify the intermediate villages by connecting them to some nearby electrified village. Note that each village will either be connected (via an electric wire passing through intermediate villages) to electrified village i on the left or to village j on the right.

In the optimal solution, we will be putting electric wire in the following way. An electric wire from i to some village k, and from village j to village k + 1.

i ------>k \quad  (k + 1)<---- j

Note that length of this wire will be total distance between village i and j minus the distance between village k and k + 1.

i.e. \text{length of wire} = (x_j - x_i) - (x_{k + 1} - x_k)

Note that we want to minimize value of length of wire. So, our aim is to maximize the value of x_{k + 1} - x_k for some k from i < k < j. We can easily find this value by iterating over the segment i to j once.

**Pseudo Code**

``ans = 0;
ans = 0;
for (int i = 0; i < n; )
        int j = n - 1;
        for (int k = i + 1; k < n; k++)
            if (lights[k] == '1')
                j = k;
                break;
        maxDiff = 0
        for (int k = i + 1; k < j; k++)
            maxDiff = max(maxDiff, x[k + 1] - x[k]);
        ans += x[j] - x[i] - maxDiff;
        i = j;
``

Note that the we are looping over the villages only once. If you look naively, you might think that complexity of the algorithm is \mathcal{O}(n^2). But, the complexity of the algorithm is \mathcal{O}(n), because the number of times, the inner loop over k runs, the value of outer loop variable i gets increased by that value (**check carefully that the last line is i = j**), making sure that overall the loop runs in total \mathcal{O}(n). You can see that none of the indices of the villages will be encountered more than once in the inner for loop and in the outer for loop too. So, time complexity of this algorithm is \mathcal{O}(n).

### Tester’s Solutions:

[Tester’s solution](http://www.codechef.com/download/Solutions/JULY16/Tester/CHEFELEC.cpp)

</details>
