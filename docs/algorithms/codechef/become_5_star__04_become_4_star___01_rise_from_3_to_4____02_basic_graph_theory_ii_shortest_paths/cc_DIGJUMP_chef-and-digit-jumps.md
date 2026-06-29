# Chef and Digit Jumps

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | DIGJUMP |
| Difficulty Rating | 1886 |
| Difficulty Band | Rise from 3* to 4* |
| Path | Become 5 star |
| Lesson | Basic Graph Theory II - Shortest Paths |
| Official Link | [DIGJUMP](https://www.codechef.com/practice/course/3to4stars/LP3TO402/problems/DIGJUMP) |

---

## Problem Statement

Chef loves games! But he likes to invent his own. Now he plays game "Digit Jump". Chef has a sequence of digits $S_{1}, S_{2}, \ldots , S_{N}$. He is staying in the first digit $S_{1}$ and wants to reach the last digit $S_{N}$ in the minimal number of jumps.

While staying in some index $i$ Chef can jump into $i - 1$ and $i + 1$, but he can't jump out from sequence. Or he can jump into any digit with the same value $S_i$.

Help Chef to find the minimal number of jumps he need to reach digit $S_{N}$ from digit $S_1$.

### Input
Input contains a single line consist of string $S$ of length $N$ - the sequence of digits.

### Output
In a single line print single integer - the minimal number of jumps he needs.

### Constraints
- $1\leq N \leq 10^5$
- Each symbol of $S$ is a digit from $0$ to $9$.

---

## Examples

**Example 1**

**Input**

```text
01234567890
```

**Output**

```text
1
```

**Explanation**

***Test Case 1:*** Chef can directly jump from the first digit (it is $0$) to the last (as it is also $0$).

**Example 2**

**Input**

```text
012134444444443
```

**Output**

```text
4
```

**Explanation**

***Test Case 2:*** Chef should follow the following path: $1 - 2 - 4 - 5 - 15$.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](http://www.codechef.com/problems/DIGJUMP)

[Contest](http://www.codechef.com/JUNE14/problems/DIGJUMP)

**Tester:** [Shiplu Hawlader](http://www.codechef.com/users/shiplu)

**Editorialist:** [Praveen Dhinwa](http://www.codechef.com/users/dpraveen)

### DIFFICULTY:

Easy

### PREREQUISITES:

bfs, dijkstra

### PROBLEM:

Given a string s of N. You have to go from start of the string(index 0) to the end of the string (index N - 1).

From position i, you can go to next (i + 1) or previous (i - 1) position. You can also move from the current position to the indices where the

character is same as current character s[i].

### QUICK EXPLANATION

- Minimum number of operations can not be greater than 19.

- By your moves, you will never be visiting a single digit more than twice.

- You can solve this problem by a modified bfs.

- You can also make use of simple dijkstra’s algorithm.

### EXPLANATION

**Few observations**

-

Minimum number of operations can not be greater than 19.

**Proof:**

You can start from first position and go to rightmost index where you can directly go.

Then from that position go to next position and keep repeating the previous step.

Note that you will be visiting a single number at most twice. Hence you can at most make 19 moves because first digit will be visited once.

They will 19 in the cases of 001122334455667788999.

-

By your moves, you will never be visiting a single digit more than twice.

**Proof:**

If you are using more than 2 moves for going from a digit to another, you can simply reduce one of the move by simply going from

one of the position to other in just a single move. So you can simply keep the at most 2 moves for moving from a digit to another.

**Wrong greedy strategies**

Let us first discuss about some greedy strategies and figure out the reason why they are wrong.

From the current position, go to the rightmost index having same character/digit as the current character/digit.

If this number does not occur again in the right part of array, then go to next position (ie. i + 1).

Please see the following recursive implementation of this strategy.

**Pseudo Code**

``def greedy(int cur):
	// cur = N denotes end/ target position.
	if (cur = N) return 0;
	last = cur + 1;
	for i = cur + 1 to N:
		if (s[i] == s[pos]):
			last = i;
	return 1 + greedy(cur);
``

The above strategy will fail in these kind of cases:

010000561

According to greedy strategy, From 0, you will go to rightmost 0, then from that position to 5, then to 6 and finally you will go to 1.

Total number of operations required are 4.

But you can do it in simply 2 operations. Go from 0 to 1 and then go to rightmost 1 (target position).

**Wrong dp algorithm**

Some contestants have used wrong dp algorithm. Let dp[i] denote the minimum number of moves needed to reach position i from position 0.

Some wre considering the transition from (i - 1)  th   position to i or

from some position j < i (such that digit at j is same as digit at i.) to i.

Note that this kind of dp solutions are wrong because they don’t consider the moves going backwards (from position i to i - 1), they are only

considering the forward moves.

A simple test case where they will fail.

In the case: 02356401237894, dp program will give answer 6, but we can go from position 0 to 6 and then to 4 on the left side of

second 0 (backward move) and then directly go to 4.

So total number of operations required are 3.

**Bfs Solution**

Now consider the movement operations from one position to other to be edges of the graph and indices of the string as nodes of the graphs.

Finding minimum number of operations to reach from 0 to N - 1 is equivalent to finding shortest path in the graph above mentioned. As

the weights in the give graph are unit weights, we can use bfs instead of using dijkstra’s algorithm.

So we can simply do a bfs from our start node(index 0) to end node(index n - 1).

Number of nodes in the graph are n, but the number of edges could

potentially go up to N  2  (Consider the case of all 0’s, entire graph is a complete graph.).

**Optimized bfs Solution**

Now we will make use of the 2 observations that we have made in the starting and we will update the bfs solution accordingly.

Whenever you visit a vertex i such that then you should also visit all the the indices j such that s[j] = s[i] (this follows directly

from observation 2). Now you can make sure to not to push any of the indices having digit same as current digit because according to observation 2,

we are never going to make more than 2 moves from a position to another position with same digit, So after adding that the current character, you should make sure that you are never going to visit any vertex with same value as s[i].

For a reference implementation, see Vivek’s [solution](http://www.codechef.com/viewplaintext/4109825).

**Another Easy solution**

Credit for the solution goes to Sergey Nagin(Sereja).

Let dp[i] denote the number of steps required to go from position 0 to position i.

From the previous observations, we know that we wont need more than 20 steps.

So lets make 20 iterations.

Before starting all the iterations, we will set dp[1] = 0 and dp[i] = infinity for all other i > 1.

On each iteration, we will calculate Q[k] where Q[k] is the minimum value of dp[i] such that s[i] = k.

ie. Q[k] denotes the minimum value of dp over the positions where the digit is equal to k.

We can update the dp by following method.

dp[i] = min(dp[i], dp[i - 1] + 1, dp[i + 1] + 1, Q[s[i]] + 1);

Here the term dp[i - 1] + 1 denotes that we have come from previous position ie (i - 1).

Here the term dp[i + 1] + 1 denotes that we have come from next position ie (i + 1).

The term Q[s[i]] + 1 denotes the minimum number of operations needed to come from a position with same digit as the current i  th  digit.

**Pseudo code:**

``// initialization phase.
dp[1] = 0;
for (int i = 2; i <= N; i++) dp[i] = inf;
for (int it = 0; it < 20; i++) {
	// Compute Q[k]
	for (int k = 0; k < 10; k++)
		Q[k] = inf;
	for (int i = 1; i <= n; i++) {
		Q[s[i] - '0'] = min(Q[s[i] - '0'], dp[i]);
	}
	// Update the current iteration.
	for (int i = 1; i <= n; i++) {
		dp[i] = min(dp[i], dp[i - 1] + 1, dp[i + 1] + 1, Q[s[i] - '0'] + 1);
	}
}
// dp[n] will be our answer.
``

**Proof**

If you done proof of dijkstra’s algorithm, you can simply found equivalence between the two proofs.

**Complexity**:

Complexity is O(20 * N). Here 20 is max number of iterations.

### AUTHOR’S AND TESTER’S SOLUTIONS:

[Tester’s solution](http://www.codechef.com/download/Solutions/2014/June/Tester/DIGJUMP.cpp)

</details>
