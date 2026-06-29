# Graph on an Array

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | ARRGRAPH |
| Difficulty Band | Rise from 3* to 4* |
| Path | Become 5 star |
| Lesson | Basic Graph Theory II - Shortest Paths |
| Official Link | [ARRGRAPH](https://www.codechef.com/practice/course/3to4stars/LP3TO402/problems/ARRGRAPH) |

---

## Problem Statement

You are given a sequence of integers $A_1, A_2, \dots, A_N$. You may change any number of its elements (possibly zero), obtaining a new sequence of positive integers $B_1, B_2, \dots, B_N$. Each element of $B$ must be an integer between $2$ and $50$ (both inclusive).

Let's define an undirected graph $G$ with $N$ vertices (numbered $1$ through $N$). For each pair of different vertices $i$ and $j$, there is an edge between $i$ and $j$ if and only if $B_i$ and $B_j$ are coprime.

You should choose the sequence $B$ in such a way that $G$ is a connected graph. The number of elements which need to be changed to obtain $B$ from $A$ should be minimum possible. Find one such sequence $B$ and the minimum required number of changes.

It can be proven that a solution always exists — it is always possible to modify sequence $A$ in such a way that $G$ is connected.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains a single integer $N$.
- The second line contains $N$ space-separated integers $A_1, A_2, \dots, A_N$.

### Output
For each test case, print two lines. The first line should contain a single integer — the minimum required number of changes. The second line should contain $N$ space-separated integers $B_1, B_2, \dots, B_N$ — the modified sequence.

If there are multiple solutions, you may print any one.

### Constraints
- $1 \le T \le 3 \cdot 10^4$
- $1 \le N \le 50$
- $2 \le A_i \le 50$ for each valid $i$

### Subtasks

**Subtask #1 (100 points):** original constraints

### Example Input
```
2
2
2 3
2
2 4
```

### Example Output
```
0
2 3
1
2 3
```

### Explanation
**Example 1**: There is an edge in $G$ between vertices $1$ and $2$. This graph is connected, so there is no need to change any elements.

**Example 2**: There is no edge between vertices $1$ and $2$ since $\mathrm{gcd}(2, 4) \neq 1$. This graph is not connected. We can change element $A_2=4$ to $3$ and make this graph connected.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](http://www.codechef.com/problems/ARRGRAPH)

[Contest](https://www.codechef.com/SNCK1A19/problems/ARRGRAPH)

**Setter:** [Praveen Dhinwa](https://www.codechef.com/users/dpraveen)

**Tester:** [Misha Chorniy](https://www.codechef.com/users/mgch)

**Editorialist:** [Taranpreet Singh](http://www.codechef.com/users/taran_1407)

### DIFFICULTY:

Easy

### PREREQUISITES:

[Union-Disjoint Sets](https://www.geeksforgeeks.org/union-find/) and Number theory (Knowledge of graphs and Connected components will be helpful).

### PROBLEM:

Given an array A of length N, We create graph consisting of N vertices, each corresponding to an element in array A. Undirected edge (a,b) is added if and only if gcd(A_a, A_b) is one. That is, A[a] and A[b] are co-prime.

We need to check whether this graph is connected or not, and if it isn’t connected, Change the minimum number of elements in the array to make the graph connected, if the graph is always constructed in similar fashion.

Note, 2 \leq A[i] \leq 50 should hold at all times even after modifications.

### SUPER QUICK EXPLANATION

- Use union disjoint sets to check whether the graph is already connected. Union operations can be performed naively in O(N^2).

- If the graph is connected, print the array. Otherwise, It can be proved that changing exactly one element in the array can make the graph connected.

- Choose one position in the array, replace it with a prime not used in the array. (Prime not used can be found by the sieve, and are guaranteed to exist since the graph is connected.)

### EXPLANATION

So, another problem with primes.

This editorial has two parts, one focusing on checking whether the graph is connected, and other making the graph connected if it is not yet connected.

Initially discussing problem from graph view.

First of all, Iterate over every pair of number, and check if there are co-prime, if yes, add an edge between two vertices. This way, we have added all edges in O(N^2). Now, using DFS, we can see the number of connected components in this resultant graph. If it is already connected (Number of connected components is 1), our graph is already valid, so we can just print the given array as output. (We can also use Union-Disjoint sets for checking if the graph is connected.)

Now, Let’s consider that the graph is not connected. Think about a number which will be co-prime to all numbers (So that we will connect this vertex to all other vertices in the graph, getting connected graph irrespective of all other values in the array, in just one step.

I know you all are good enough to guess I’m talking about 1, but problem setter intentionally choose to keep 2 \leq A[i] \leq 50 to make this task a bit harder

Let’s us suppose we choose a prime since it will not be co-prime only to its multiples. Choose a prime above N/2+1 makes sure that only multiple of this number in the array is the element itself.

So, just choose a prime and replace any element in array with this prime. I choose 47.

Suppose evil setter already knows of this solution and set all values in the array as 47. Isn’t our solution trapped?

So, how do we handle this, Simple!!

Just take another prime. It can be proven that the problem will be solved in one step since we can choose one element in the array, replace it with any such prime number in the array.

But, we shall make his effort useless, by noticing that we can always make the graph connected, in just one step. For proof, see primes above or equal to N/2+1. Let’s call them good primes.

We can prove that if the graph has at least two good primes, then the graph is connected.

**Reason: ** Suppose we have two good primes in the array, so, It’s guaranteed that all other elements in the array will be connected to at least one of the good prime. Thus, Graph is divided into at most two components, one containing first good prime while other containing the second good prime. These two good primes will also be connected to each other since two distinct primes are always Co-prime to each other, Resulting in the graph being connected.

So, I took primes 41 and 47 for this purpose, If the array doesn’t consist of all 47, replace the first element with 47 and that’s it. Otherwise, replace the first element with 41.

The reason of not choosing a prime smaller than or equal to N/2 is that we will need to be careful about choosing which element to replace, and also handle multiples of this prime present in the array. It can be done easily, but choosing a good prime makes things simple enough.

**To Problem setter, Thanks a lot for proofreading editorial as well as suggesting important points to be kept in the editorial.**

### Related problem

I guess those all those who participated in October long challenge already know about one such problem. For those who didn’t, [Coprime Components](https://www.codechef.com/OCT18A/problems/CPCOMP). Please suggest more such problems.

### Time Complexity

O(N^2) for initial graph construction dominate overall time complexity. Apart from that, all other operations take time of order O(N).

### AUTHOR’S AND TESTER’S SOLUTIONS:

[Setter’s solution](http://www.codechef.com/download/Solutions/SNCK1A19/setter/ARRGRAPH.cpp)

[Tester’s solution](http://www.codechef.com/download/Solutions/SNCK1A19/tester/ARRGRAPH.cpp)

[Editorialist’s solution](http://www.codechef.com/download/Solutions/SNCK1A19/editorialist/ARRGRAPH.java)

Feel free to Share your approach, If it differs. Suggestions are always welcomed.

</details>
